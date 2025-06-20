# Support
- **Issues**: Report bugs and feature requests via GitHub Issues

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

### Debug Mode
```bash
python main.py --debug
```

Enable detailed logging:

```bash
# Set log level to DEBUG
export PYTHONPATH=.
python -c "
import logging
logging.basicConfig(level=logging.DEBUG)
from server import main
import asyncio
asyncio.run(main())
"
```