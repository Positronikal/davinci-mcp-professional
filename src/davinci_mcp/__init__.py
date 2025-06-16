"""
DaVinci Resolve MCP Server

A modern, clean implementation of a Model Context Protocol server
for DaVinci Resolve integration.
"""

__version__ = "2.1.0"
__author__ = "Samuel Gursky, Hoyt"

from .server import DaVinciMCPServer
from .resolve_client import DaVinciResolveClient

__all__ = ["DaVinciMCPServer", "DaVinciResolveClient"]
