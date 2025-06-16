"""
MCP resources for DaVinci Resolve integration.
"""

from typing import List
import mcp.types as types


def get_all_resources() -> List[types.Resource]:
    """Get all available MCP resources."""
    return [
        # System resources
        types.Resource(
            uri="resolve://version",
            name="DaVinci Resolve Version",
            description="Current version of DaVinci Resolve",
            mimeType="text/plain"
        ),
        
        types.Resource(
            uri="resolve://current-page",
            name="Current Page",
            description="The currently active page in DaVinci Resolve",
            mimeType="text/plain"
        ),
        
        # Project resources
        types.Resource(
            uri="resolve://projects",
            name="Available Projects",
            description="List of all available projects in the current database",
            mimeType="application/json"
        ),
        
        types.Resource(
            uri="resolve://current-project",
            name="Current Project",
            description="Name of the currently open project",
            mimeType="text/plain"
        ),
        
        # Timeline resources
        types.Resource(
            uri="resolve://timelines",
            name="Available Timelines",
            description="List of all timelines in the current project",
            mimeType="application/json"
        ),
        
        types.Resource(
            uri="resolve://current-timeline",
            name="Current Timeline",
            description="Name of the current timeline",
            mimeType="text/plain"
        ),
        
        # Media resources
        types.Resource(
            uri="resolve://media-clips",
            name="Media Pool Clips",
            description="List of all clips in the media pool",
            mimeType="application/json"
        ),
    ]
