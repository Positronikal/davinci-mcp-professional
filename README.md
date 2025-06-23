# DaVinci MCP Professional v2.1.0
A modern, professional implementation of a Model Context Protocol server for DaVinci Resolve integration. This project is a hard/project fork from the excellent work done by @samuelgursky at https://github.com/samuelgursky/davinci-resolve-mcp. It's an independent project now due to major overhaul and restructuring making it incompatible with the original repo. DaVinci MCP Professional is a fully enterprise-grade implementation of an MCP specifically designed expose the full range of functionality either DaVinci Resolve or DaVinci Resolve Studio to an MCP client. Supported clients include both Claude Desktop (preferred) or Cursor.

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