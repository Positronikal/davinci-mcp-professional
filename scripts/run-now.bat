@echo off
REM Quick Start Script for DaVinci Resolve MCP Server (Windows). This
REM script sets up the environment and starts the MCP server. Ctrl-C
REM to shutdown MCP server.

echo ==============================================
echo   DaVinci Resolve MCP Server - Quick Start
echo ==============================================
echo.

REM Set script, root, and venv path vars:
set SCRIPT_DIR=D:\bin\DaVinci\davinci-resolve-mcp\scripts
set ROOT_DIR=D:\bin\DaVinci\davinci-resolve-mcp
echo Project root: %ROOT_DIR%
echo.
set RESOLVE_MCP_SERVER=%ROOT_DIR%\src\resolve_mcp_server.py

REM User launch DaVinci Resolve:
echo Launch DaVinci Resolve if it isn't already running before continuing
echo the MCP server launch.
echo.
pause

REM Simple check for Resolve process:
tasklist /FI "IMAGENAME eq Resolve.exe" 2>nul | find /i "Resolve.exe" >nul
if %ERRORLEVEL% NEQ 0 goto :resolve_not_running

echo DaVinci Resolve is running, continuing...
echo.
goto :resolve_running

:resolve_not_running
echo ERROR: DaVinci Resolve is not running...
echo MCP launch will terminate.
pause
exit /b 1

:resolve_running
REM Set envars for the session:
echo Setting environment variables...
echo.
set RESOLVE_SCRIPT_API="C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting"
set RESOLVE_SCRIPT_LIB="C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll"
set PYTHONPATH=%PYTHONPATH%;%RESOLVE_SCRIPT_API%\Modules

REM Uncomment to permanently save envars:
::setx RESOLVE_SCRIPT_API "%RESOLVE_SCRIPT_API%" >nul
::setx RESOLVE_SCRIPT_LIB "%RESOLVE_SCRIPT_LIB%" >nul
::setx PYTHONPATH "%RESOLVE_SCRIPT_API%\Modules" >nul

REM Check if server script exists:
echo Checking for MCP server script...
echo.
if not exist "%RESOLVE_MCP_SERVER%" (
    echo ERROR: Server script not found at %RESOLVE_MCP_SERVER%!
    echo MCP launch will terminate.
    pause
    exit /b 1
)

REM Check if %ROOT_DIR% is uv initialized and install mcp[cli]:
echo Checking uv initialization...
echo.
if not exist "%ROOT_DIR%" (
    echo ERROR: Root directory %ROOT_DIR% does not exist!
    echo MCP launch will terminate.
    pause
    exit /b 1
)
cd %ROOT_DIR%
if not exist "pyproject.toml" (
    echo uv project not initialized. Initializing...
    uv init
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: uv environment did not initialize properly!
        pause
        exit /b 1
) else (
    echo uv project is initialized.
    echo.
)

echo Checking for mcp[cli] installation...
echo.
uv list | findstr /i "mcp" >nul
if %ERRORLEVEL% NEQ 0 (
    echo mcp[cli] not found. Installing...
    echo.
    uv add "mcp[cli]"
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Failed to install mcp[cli]...
        echo MCP launch will terminate.
        exit /b 1
    )
) else (
    echo mcp[cli] is already installed.
    echo.
)

REM Start the server
echo Starting DaVinci Resolve MCP Server. Ctrl-C to quit.
echo.
uv run mcp
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to launch MCP server.
    pause
    exit /b 1
)