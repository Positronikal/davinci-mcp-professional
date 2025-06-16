# DaVinci MCP Professional v2.1.0

A modern, professional implementation of a Model Context Protocol server for DaVinci Resolve integration.

## What Makes This Professional

This is a complete architectural rewrite and cleanup of existing DaVinci Resolve MCP implementations:

- **Clean Architecture**: Proper separation of concerns between MCP protocol and DaVinci Resolve API
- **Modern Python**: Uses current best practices with type hints, async/await, and comprehensive error handling
- **Simplified Setup**: Single command installation with automatic dependency management
- **Windows Compatible**: Proper encoding handling and console output for Windows environments
- **Standardized Dependencies**: Uses `uv` for fast, reliable dependency management
- **Comprehensive Testing**: Built-in test suite to verify functionality
- **Production Ready**: Clean codebase suitable for professional environments

## Quick Start

### Prerequisites

- DaVinci Resolve installed (Free or Studio)
- Python 3.9+ 
- DaVinci Resolve running

### Installation

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

### Usage with AI Assistants

#### With Claude Desktop
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

#### With Cursor
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

## Available Tools

### System Tools
- `get_version` - Get DaVinci Resolve version
- `get_current_page` - Get current page (Edit, Color, etc.)
- `switch_page` - Switch to a specific page

### Project Tools
- `list_projects` - List available projects
- `get_current_project` - Get current project name
- `open_project` - Open a project by name
- `create_project` - Create a new project

### Timeline Tools
- `list_timelines` - List timelines in current project
- `get_current_timeline` - Get current timeline name
- `create_timeline` - Create a new timeline
- `switch_timeline` - Switch to a timeline

### Media Tools
- `list_media_clips` - List clips in media pool
- `import_media` - Import media files

## Available Resources

- `resolve://version` - DaVinci Resolve version
- `resolve://current-page` - Current page
- `resolve://projects` - Available projects
- `resolve://current-project` - Current project name
- `resolve://timelines` - Available timelines
- `resolve://current-timeline` - Current timeline name
- `resolve://media-clips` - Media pool clips

## Development

### Adding New Tools

1. Add tool definition to `tools/__init__.py`
2. Add tool implementation to `server.py` in `_call_tool()` method

### Adding New Resources

1. Add resource definition to `resources/__init__.py`
2. Add resource implementation to `server.py` in `_read_resource()` method

### Running Tests

```bash
python test.py
```

### Debug Mode

```bash
python main.py --debug
```

## Troubleshooting

### DaVinci Resolve Not Found

If you get errors about DaVinci Resolve not being found:

1. Make sure DaVinci Resolve is installed in the default location
2. Check that all required files exist by running the test suite
3. On Windows, ensure DaVinci Resolve is in Program Files, not Program Files (x86)

### DaVinci Resolve Not Running

The server requires DaVinci Resolve to be running before starting:

1. Start DaVinci Resolve
2. Wait for it to fully load
3. Then start the MCP server

### Import Errors

If you get Python import errors:

1. Make sure you ran `python setup.py` first
2. Check that the virtual environment was created (`.venv` directory should exist)
3. Try running `uv pip install -e .` manually

## Architecture Highlights

This implementation emphasizes:

- **Reliability**: Comprehensive error handling and graceful failure modes
- **Maintainability**: Clean separation of concerns and modular design
- **Performance**: Efficient async/await patterns and minimal overhead
- **Compatibility**: Cross-platform support with Windows-specific optimizations
- **Professional Standards**: Proper logging, testing, and documentation

## License

MIT License - see LICENSE file for details.

## About

DaVinci MCP Professional represents a complete architectural transformation from experimental MCP implementations to production-ready professional software suitable for critical workflows.
