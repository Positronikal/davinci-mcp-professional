"""
Security-focused test suite for DaVinci MCP Professional.

This module contains tests specifically designed to verify security aspects
of the application, including dependency security, file permissions, and
potential vulnerability detection.
"""

import pytest
import subprocess
import json
import os
import stat
from pathlib import Path
from typing import Generator


class TestSecurity:
    """Security-focused test cases."""
    
    def test_no_hardcoded_secrets_in_git_history(self):
        """Ensure no hardcoded secrets in git history."""
        try:
            # Search for potential secrets in git log
            result = subprocess.run([
                'git', 'log', '--all', '--grep=password', '--grep=token', 
                '--grep=secret', '--grep=key', '--grep=api_key', '--oneline'
            ], capture_output=True, text=True, cwd=Path(__file__).parent.parent)
            
            # If there are matches, they might indicate secrets in commit messages
            if result.stdout.strip():
                pytest.fail(f"Potential secrets found in git history: {result.stdout}")
                
        except subprocess.CalledProcessError:
            # Git might not be available or repo might not be initialized
            pytest.skip("Git not available or not in a git repository")
    
    def test_no_secrets_in_codebase(self):
        """Check for potential hardcoded secrets in source code."""
        project_root = Path(__file__).parent.parent
        python_files = list(project_root.rglob("*.py"))
        
        # Patterns that might indicate hardcoded secrets
        secret_patterns = [
            "password=",
            "api_key=", 
            "secret=",
            "token=",
            "aws_access_key",
            "private_key=",
        ]
        
        violations = []
        
        for py_file in python_files:
            # Skip test files and virtual environment
            if any(skip in str(py_file) for skip in ['test_', 'tests/', '.venv/', 'lib/']):
                continue
                
            try:
                content = py_file.read_text(encoding='utf-8').lower()
                for pattern in secret_patterns:
                    if pattern in content:
                        # Check if it's in a comment or a test
                        lines = content.split('\n')
                        for i, line in enumerate(lines):
                            if pattern in line and not line.strip().startswith('#'):
                                violations.append(f"{py_file}:{i+1} - {line.strip()}")
            except UnicodeDecodeError:
                # Skip binary files
                continue
        
        if violations:
            pytest.fail(f"Potential hardcoded secrets found:\n" + "\n".join(violations))
    
    def test_dependencies_security(self):
        """Check for known vulnerabilities in dependencies using safety."""
        try:
            result = subprocess.run([
                'safety', 'check', '--json'
            ], capture_output=True, text=True, cwd=Path(__file__).parent.parent)
            
            if result.returncode != 0:
                try:
                    vulnerabilities = json.loads(result.stdout)
                    if vulnerabilities:
                        vuln_summary = []
                        for vuln in vulnerabilities:
                            vuln_summary.append(
                                f"Package: {vuln.get('package', 'Unknown')} "
                                f"Version: {vuln.get('installed_version', 'Unknown')} "
                                f"Vulnerability: {vuln.get('vulnerability_id', 'Unknown')}"
                            )
                        pytest.fail(
                            f"Security vulnerabilities found:\n" + "\n".join(vuln_summary)
                        )
                except json.JSONDecodeError:
                    # If we can't parse JSON, check if there's an error message
                    if "vulnerabilities found" in result.stdout.lower():
                        pytest.fail(f"Security vulnerabilities detected: {result.stdout}")
                        
        except FileNotFoundError:
            pytest.skip("Safety tool not installed. Run: pip install safety")
    
    def test_file_permissions(self):
        """Ensure sensitive files have appropriate permissions."""
        project_root = Path(__file__).parent.parent
        
        # Files that should not be world-readable
        sensitive_patterns = [
            '.env*',
            '*config*.json',
            '*secret*',
            '*.key',
            '*.pem',
            'credentials*',
        ]
        
        violations = []
        
        for pattern in sensitive_patterns:
            for file_path in project_root.rglob(pattern):
                if file_path.is_file():
                    file_stat = file_path.stat()
                    # Check if file is readable by others (octal 004)
                    if file_stat.st_mode & stat.S_IROTH:
                        violations.append(f"{file_path} is world-readable")
        
        if violations:
            pytest.fail("Insecure file permissions found:\n" + "\n".join(violations))
    
    def test_import_security(self):
        """Check for potentially dangerous imports."""
        project_root = Path(__file__).parent.parent
        python_files = list(project_root.rglob("*.py"))
        
        # Potentially dangerous imports that should be reviewed
        dangerous_imports = [
            "eval(",
            "exec(",
            "compile(",
            "__import__(",
            "subprocess.call(",
            "os.system(",
            "pickle.loads(",
            "marshal.loads(",
        ]
        
        violations = []
        
        for py_file in python_files:
            # Skip test files and virtual environment
            if any(skip in str(py_file) for skip in ['.venv/', 'lib/', 'test_']):
                continue
                
            try:
                content = py_file.read_text(encoding='utf-8')
                lines = content.split('\n')
                
                for i, line in enumerate(lines):
                    for dangerous in dangerous_imports:
                        if dangerous in line and not line.strip().startswith('#'):
                            violations.append(
                                f"{py_file}:{i+1} - Potentially dangerous: {line.strip()}"
                            )
                            
            except UnicodeDecodeError:
                continue
        
        # This is a warning rather than a failure since some uses might be legitimate
        if violations:
            print("⚠️  Potentially dangerous imports found (review required):")
            for violation in violations:
                print(f"   {violation}")
    
    def test_environment_variables(self):
        """Check for insecure environment variable handling."""
        # Check if any sensitive environment variables are set
        sensitive_env_vars = [
            'AWS_SECRET_ACCESS_KEY',
            'DATABASE_PASSWORD',
            'API_SECRET',
            'PRIVATE_KEY',
            'TOKEN',
        ]
        
        exposed_vars = []
        for var in sensitive_env_vars:
            if os.getenv(var):
                exposed_vars.append(var)
        
        if exposed_vars:
            print(f"⚠️  Sensitive environment variables detected: {', '.join(exposed_vars)}")
            print("Ensure these are properly secured in production.")
    
    def test_configuration_security(self):
        """Check configuration files for security issues."""
        project_root = Path(__file__).parent.parent
        config_files = []
        
        # Find configuration files
        for pattern in ['*.json', '*.yaml', '*.yml', '*.toml', '*.ini', '*.conf']:
            config_files.extend(project_root.rglob(pattern))
        
        violations = []
        
        for config_file in config_files:
            # Skip files in virtual environment
            if '.venv' in str(config_file) or 'lib' in str(config_file):
                continue
                
            try:
                content = config_file.read_text(encoding='utf-8').lower()
                
                # Check for potential secrets in config files
                if any(secret in content for secret in [
                    'password', 'secret', 'token', 'key', 'credential'
                ]):
                    # Check if it's just a field name or an actual value
                    lines = content.split('\n')
                    for i, line in enumerate(lines):
                        if '=' in line or ':' in line:
                            if any(secret in line for secret in [
                                'password', 'secret', 'token', 'key'
                            ]):
                                # Check if there's an actual value (not just field name)
                                if any(char in line for char in ['=', ':']):
                                    parts = line.split('=' if '=' in line else ':')
                                    if len(parts) > 1 and parts[1].strip():
                                        violations.append(
                                            f"{config_file}:{i+1} - Potential secret: {line.strip()}"
                                        )
                                        
            except UnicodeDecodeError:
                continue
        
        if violations:
            print("⚠️  Potential secrets in configuration files:")
            for violation in violations:
                print(f"   {violation}")


class TestInputValidation:
    """Test input validation and sanitization."""
    
    def test_path_traversal_protection(self) -> None:
        """Test protection against path traversal attacks."""
        # This test would be specific to your application's file handling
        # For now, it's a placeholder that demonstrates the concept
        
        # Example malicious paths that should be blocked
        # These would be tested against your actual file handling logic
        print("📝 Path traversal protection tests should be implemented based on your file handling logic")
    
    def test_command_injection_protection(self) -> None:
        """Test protection against command injection."""
        # If your application executes system commands, test with malicious input
        # Example malicious commands that should be blocked
        print("📝 Command injection protection tests should be implemented if executing system commands")


if __name__ == "__main__":
    # Run the security tests
    pytest.main([__file__, "-v"])
