# Quick Start

## Prerequisites
- DaVinci Resolve installed (Free or Studio)
- Python 3.9+ 
- DaVinci Resolve running

## Installation
1. **Clone or navigate to the project directory**
   ```bash
   cd /path/to/davinci-mcp-professional
   ```

2. **Run the setup script**
   ```bash
   python setup.py
   ```
   
   This will:
   - Install the `uv` package manager if needed
   - Set up a virtual environment
   - Install all dependencies
   - Create MCP configuration files for Cursor and Claude Desktop

3. **Test the installation**
   ```bash
   python test.py
   ```

4. **Start the server interactively**
   ```bash
   python main.py
   ```

## Usage with AI Assistants

### With Claude Desktop
Update your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "davinci-resolve": {
      "name": "DaVinci MCP Professional",
      "command": "/path/to/davinci-mcp-professional/.venv/Scripts/python.exe",
      "args": ["/path/to/davinci-mcp-professional/mcp_server.py"]
    }
  }
}
```

### With Cursor
The setup script automatically configures Cursor. After setup:

1. Start DaVinci Resolve
2. Open Cursor - the DaVinci Resolve MCP should be available

You can then use commands like:
- "What version of DaVinci Resolve is running?"
- "List all projects"
- "Create a new timeline called 'My Edit'"
- "Switch to the Color page"

## Project Structure
```
src/davinci_mcp/
├── __init__.py          # Package initialization
├── cli.py               # Command line interface
├── server.py            # Main MCP server implementation
├── resolve_client.py    # DaVinci Resolve API client
├── tools/               # MCP tool definitions
│   └── __init__.py
├── resources/           # MCP resource definitions
│   └── __init__.py
└── utils/               # Utility functions
    ├── __init__.py
    └── platform.py      # Platform detection and setup
```

# Available Tools

## System Tools
- `get_version` - Get DaVinci Resolve version
- `get_current_page` - Get current page (Edit, Color, etc.)
- `switch_page` - Switch to a specific page

## Project Tools
- `list_projects` - List available projects
- `get_current_project` - Get current project name
- `open_project` - Open a project by name
- `create_project` - Create a new project

## Timeline Tools
- `list_timelines` - List timelines in current project
- `get_current_timeline` - Get current timeline name
- `create_timeline` - Create a new timeline
- `switch_timeline` - Switch to a timeline

## Media Tools
- `list_media_clips` - List clips in media pool
- `import_media` - Import media files

# Available Resources
- `resolve://version` - DaVinci Resolve version
- `resolve://current-page` - Current page
- `resolve://projects` - Available projects
- `resolve://current-project` - Current project name
- `resolve://timelines` - Available timelines
- `resolve://current-timeline` - Current timeline name
- `resolve://media-clips` - Media pool clips

# Development

## Adding New Tools
1. Add tool definition to `tools/__init__.py`
2. Add tool implementation to `server.py` in `_call_tool()` method

## Adding New Resources
1. Add resource definition to `resources/__init__.py`
2. Add resource implementation to `server.py` in `_read_resource()` method

## Running Tests
```bash
python test.py
```

# Troubleshooting
See `BUGS` elsewhere in this repo.