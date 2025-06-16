#!/usr/bin/env python3
"""
Setup script for the new DaVinci Resolve MCP Server implementation.
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from typing import Dict, Any

def run_command(cmd: list, check: bool = True) -> subprocess.CompletedProcess:
    """Run a command and return the result."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=False, capture_output=True, text=True)
    
    if result.returncode != 0 and check:
        print(f"Command failed with exit code {result.returncode}")
        if result.stdout:
            print(f"STDOUT: {result.stdout}")
        if result.stderr:
            print(f"STDERR: {result.stderr}")
        raise subprocess.CalledProcessError(result.returncode, cmd)
    
    return result

def check_uv_installed() -> bool:
    """Check if uv is installed."""
    try:
        result = run_command(["uv", "--version"], check=False)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def install_uv() -> bool:
    """Install uv package manager."""
    print("Installing uv package manager...")
    try:
        # Try to install via pip first
        run_command([sys.executable, "-m", "pip", "install", "uv"])
        return True
    except subprocess.CalledProcessError:
        print("Failed to install uv via pip. Please install uv manually:")
        print("Visit: https://docs.astral.sh/uv/getting-started/installation/")
        return False

def setup_project(project_dir: Path) -> bool:
    """Set up the uv project."""
    os.chdir(project_dir)
    
    # Copy the new pyproject.toml over the old one
    pyproject_new = project_dir / "pyproject_new.toml"
    pyproject_old = project_dir / "pyproject.toml"
    
    if pyproject_new.exists():
        print("Updating pyproject.toml with new configuration...")
        # Remove the old file first if it exists
        if pyproject_old.exists():
            pyproject_old.unlink()
        pyproject_new.rename(pyproject_old)
    
    # Initialize uv project if not already done
    if not (project_dir / ".venv").exists():
        print("Initializing uv virtual environment...")
        run_command(["uv", "venv"])
    
    # Install dependencies
    print("Installing dependencies...")
    run_command(["uv", "pip", "install", "-e", "."])
    
    return True

def create_mcp_config(project_dir: Path) -> Dict[str, Any]:
    """Create MCP configuration for Cursor."""
    
    # Get the absolute path to the Python interpreter and main script
    if os.name == "nt":  # Windows
        python_path = project_dir / ".venv" / "Scripts" / "python.exe"
    else:  # macOS/Linux
        python_path = project_dir / ".venv" / "bin" / "python"
    
    main_script = project_dir / "main_new.py"
    
    config = {
        "mcpServers": {
            "davinci-resolve": {
                "name": "DaVinci Resolve MCP v2.0",
                "command": str(python_path),
                "args": [str(main_script)]
            }
        }
    }
    
    return config

def save_mcp_config(config: Dict[str, Any], project_dir: Path) -> None:
    """Save MCP configuration files."""
    
    # Save project-level config
    project_config_dir = project_dir / ".cursor"
    project_config_dir.mkdir(exist_ok=True)
    
    project_config_file = project_config_dir / "mcp.json"
    with open(project_config_file, "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"Created project MCP config: {project_config_file}")
    
    # Also save system-level config
    if os.name == "nt":  # Windows
        system_config_dir = Path(os.environ["APPDATA"]) / "Cursor"
    else:  # macOS/Linux
        system_config_dir = Path.home() / ".cursor"
    
    system_config_dir.mkdir(exist_ok=True)
    system_config_file = system_config_dir / "mcp.json"
    
    # Load existing config if it exists, otherwise create new
    if system_config_file.exists():
        with open(system_config_file, "r") as f:
            existing_config = json.load(f)
        
        # Update with our server config
        if "mcpServers" not in existing_config:
            existing_config["mcpServers"] = {}
        
        existing_config["mcpServers"]["davinci-resolve"] = config["mcpServers"]["davinci-resolve"]
        
        with open(system_config_file, "w") as f:
            json.dump(existing_config, f, indent=2)
    else:
        with open(system_config_file, "w") as f:
            json.dump(config, f, indent=2)
    
    print(f"Updated system MCP config: {system_config_file}")

def main() -> int:
    """Main setup function."""
    print("="*60)
    print("  DaVinci Resolve MCP Server v2.0 Setup")
    print("="*60)
    
    project_dir = Path(__file__).parent
    print(f"Project directory: {project_dir}")
    
    # Check if uv is installed
    if not check_uv_installed():
        print("uv package manager not found.")
        if not install_uv():
            return 1
    
    print("✓ uv package manager is available")
    
    # Set up the project
    try:
        setup_project(project_dir)
        print("✓ Project setup complete")
    except subprocess.CalledProcessError as e:
        print(f"✗ Project setup failed: {e}")
        return 1
    
    # Create MCP configuration
    try:
        config = create_mcp_config(project_dir)
        save_mcp_config(config, project_dir)
        print("✓ MCP configuration created")
    except Exception as e:
        print(f"✗ MCP configuration failed: {e}")
        return 1
    
    # Final instructions
    print("\n" + "="*60)
    print("Setup complete! Next steps:")
    print("="*60)
    print("1. Start DaVinci Resolve")
    print("2. Test the server:")
    print(f"   cd {project_dir}")
    print("   python main_new.py")
    print("3. Use with Cursor - the MCP server should now be available")
    print("\nThe new implementation is in src_new/ directory")
    print("Original implementation remains in src/ for comparison")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
