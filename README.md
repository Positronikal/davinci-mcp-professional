# DaVinci MCP Professional
A modern, professional implementation of a Model Context Protocol server for DaVinci Resolve integration. This project is a hard/project fork from the excellent work done by @samuelgursky at https://github.com/samuelgursky/davinci-resolve-mcp. It's an independent project now due to major overhaul and restructuring making it incompatible with the original repo. DaVinci MCP Professional is a fully enterprise-grade implementation of an MCP specifically designed to expose the full range of functionality of either DaVinci Resolve or DaVinci Resolve Studio to MCP clients. Supported clients include both Claude Desktop (preferred) or Cursor.

## Installation Options

### 🚀 One-Click Installation (Recommended)
DaVinci MCP Professional is available as a Desktop Extension (DXT) for easy installation:

1. **Download** the latest `.dxt` file from [Releases](https://github.com/Positronikal/davinci-mcp-professional/releases)
2. **Open Claude Desktop** and go to Settings > Extensions
3. **Drag and drop** the `.dxt` file to install
4. **Configure** any optional settings (DaVinci Resolve path, debug mode)
5. **Start DaVinci Resolve** and begin using AI-assisted video editing!

### ⚙️ Manual Installation
For developers and advanced users who prefer manual setup:

1. **Clone the repository**
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Configure Claude Desktop**: Add server configuration to `claude_desktop_config.json`
4. **See USING.md** for detailed manual setup instructions

## What Makes This Professional
This is a complete architectural rewrite and cleanup of existing DaVinci Resolve MCP implementations:

- **Clean Architecture**: Proper separation of concerns between MCP protocol and DaVinci Resolve API
- **Modern Python**: Uses current best practices with type hints, async/await, and comprehensive error handling
- **Simplified Setup**: Single command installation with automatic dependency management
- **Windows Compatible**: Proper encoding handling and console output for Windows environments
- **Standardized Dependencies**: Uses `uv` for fast, reliable dependency management
- **Comprehensive Testing**: Built-in test suite to verify functionality
- **Production Ready**: Clean codebase suitable for professional environments

## Architecture Highlights
This implementation emphasizes:

- **Reliability**: Comprehensive error handling and graceful failure modes
- **Maintainability**: Clean separation of concerns and modular design
- **Performance**: Efficient async/await patterns and minimal overhead
- **Compatibility**: Cross-platform support with Windows-specific optimizations
- **Professional Standards**: Proper logging, testing, and documentation

## Usage
See `USING` located elsewhere in this repo.

## Getting Help
See `BUGS` located elsewhere in this repo.

## License
See `COPYING` located elsewhere in this repo.

## Contributing
See `CONTRIBUTING` located elsewhere in this repo.