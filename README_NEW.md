# DaVinci Resolve MCP Server v2.0

A modern, clean implementation of a Model Context Protocol server for DaVinci Resolve integration.

## What's New in v2.0

This is a complete rewrite of the original DaVinci Resolve MCP server with:

- **Clean Architecture**: Proper separation of concerns between MCP protocol and DaVinci Resolve API
- **Modern Python**: Uses current best practices with type hints, async/await, and proper error handling
- **Simplified Setup**: Single command installation with automatic dependency management
- **Better Error Handling**: Clear error messages and graceful failure handling
- **Standardized Dependencies**: Uses `uv` for fast, reliable dependency management
- **Comprehensive Testing**: Built-in test suite to verify functionality

## Quick Start

### Prerequisites

- DaVinci Resolve installed (Free or Studio)
- Python 3.9+ 
- DaVinci Resolve running

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd /path/to/davinci-resolve-mcp
   ```

2. **Run the setup script**
   ```bash
   python setup_new.py
   ```
   
   This will:
   - Install the `uv` package manager if needed
   - Set up a virtual environment
   - Install all dependencies
   - Create MCP configuration files for Cursor

3. **Test the installation**
   ```bash
   python test_new.py
   ```

4. **Start the server**
   ```bash
   python main_new.py
   ```

### Usage with Cursor

The setup script automatically configures Cursor to use the new MCP server. After setup:

1. Start DaVinci Resolve
2. Start the MCP server (`python main_new.py`)
3. Open Cursor - the DaVinci Resolve MCP should be available

You can then use commands like:
- "What version of DaVinci Resolve is running?"
- "List all projects"
- "Create a new timeline called 'My Edit'"
- "Switch to the Color page"

## Project Structure

```
src_new/davinci_mcp/
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
python test_new.py
```

### Debug Mode

```bash
python main_new.py --debug
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

1. Make sure you ran `python setup_new.py` first
2. Check that the virtual environment was created (`.venv` directory should exist)
3. Try running `uv pip install -e .` manually

## Comparison with v1.x

| Feature | v1.x | v2.0 |
|---------|------|------|
| Architecture | Monolithic | Modular |
| Error Handling | Basic | Comprehensive |
| Setup | Complex scripts | Single command |
| Dependencies | Mixed (pip/uv/conda) | Standardized (uv) |
| Testing | None | Built-in test suite |
| Code Quality | Mixed | Modern Python practices |
| Documentation | Scattered | Centralized |

## Migration from v1.x

The new v2.0 implementation is installed alongside the original in the `src_new/` directory. This allows you to:

1. Test the new implementation without affecting the old one
2. Compare functionality between versions
3. Gradually migrate custom features

To switch permanently to v2.0:
1. Verify everything works with `python test_new.py`
2. Update any custom scripts to use `main_new.py`
3. Optionally remove the old `src/` directory when satisfied

## License

MIT License - see LICENSE file for details.
