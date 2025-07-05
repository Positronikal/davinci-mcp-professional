"""
Type definitions for DaVinci Resolve API.

This module provides Protocol definitions for the DaVinci Resolve API
to improve type safety while working with the external scripting interface.
"""

from typing import Any, Dict, List, Optional, Protocol, runtime_checkable


@runtime_checkable
class DaVinciProject(Protocol):
    """Protocol for DaVinci Resolve Project objects."""

    def GetName(self) -> str:
        """Get the project name."""
        ...

    def GetTimelines(self) -> List[Any]:
        """Get all timelines in the project."""
        ...

    def GetCurrentTimeline(self) -> Optional[Any]:
        """Get the currently active timeline."""
        ...

    def AddTimeline(self, name: str) -> Optional[Any]:
        """Add a new timeline with the given name."""
        ...

    def GetMediaPool(self) -> Any:
        """Get the media pool for this project."""
        ...


@runtime_checkable
class DaVinciTimeline(Protocol):
    """Protocol for DaVinci Resolve Timeline objects."""

    def GetName(self) -> str:
        """Get the timeline name."""
        ...

    def GetTrackCount(self, track_type: str) -> int:
        """Get the number of tracks of the specified type."""
        ...


@runtime_checkable
class DaVinciMediaPool(Protocol):
    """Protocol for DaVinci Resolve MediaPool objects."""

    def GetClips(self) -> List[Any]:
        """Get all clips in the media pool."""
        ...

    def ImportMedia(self, file_path: str) -> bool:
        """Import media from the specified file path."""
        ...


@runtime_checkable
class DaVinciProjectManager(Protocol):
    """Protocol for DaVinci Resolve ProjectManager objects."""

    def GetCurrentProject(self) -> Optional[DaVinciProject]:
        """Get the currently open project."""
        ...

    def GetProjectsInDatabase(self) -> List[Dict[str, Any]]:
        """Get all projects in the current database."""
        ...

    def GetProjectListInCurrentFolder(self) -> List[str]:
        """Get project list in current folder."""
        ...

    def CreateProject(self, name: str) -> Optional[DaVinciProject]:
        """Create a new project with the given name."""
        ...

    def LoadProject(self, name: str) -> Optional[DaVinciProject]:
        """Load an existing project by name."""
        ...


@runtime_checkable
class DaVinciResolveApp(Protocol):
    """Protocol for the main DaVinci Resolve application object."""

    def GetVersion(self) -> List[str]:
        """Get the DaVinci Resolve version information."""
        ...

    def GetProductName(self) -> str:
        """Get the product name."""
        ...

    def GetVersionString(self) -> str:
        """Get the version as a string."""
        ...

    def GetProjectManager(self) -> DaVinciProjectManager:
        """Get the project manager."""
        ...

    def GetCurrentPage(self) -> str:
        """Get the currently active page."""
        ...

    def OpenPage(self, page: str) -> bool:
        """Open a specific page."""
        ...

    def GetCurrentProject(self) -> Optional[DaVinciProject]:
        """Get the currently active project."""
        ...


# Type aliases for common return types
ResolveVersion = List[str]
ProjectName = str
TimelineName = str
PageName = str
MediaClipInfo = Dict[str, Any]
