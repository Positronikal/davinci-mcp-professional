"""
Pytest configuration for DaVinci MCP Professional test suite.
"""

import pytest
import sys
from pathlib import Path

# Add the src directory to Python path for imports
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture(scope="session")
def project_root():
    """Provide the project root directory path."""
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def src_directory():
    """Provide the source code directory path."""
    return Path(__file__).parent.parent / "src"


@pytest.fixture
def temp_config_file(tmp_path):
    """Create a temporary configuration file for testing."""
    config_content = """
    {
        "test_setting": "test_value",
        "debug": true
    }
    """
    config_file = tmp_path / "test_config.json"
    config_file.write_text(config_content)
    return config_file


# Configure pytest markers
def pytest_configure(config):
    """Configure custom pytest markers."""
    config.addinivalue_line(
        "markers", "security: mark test as security-related"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


# Skip tests that require external dependencies if not available
def pytest_collection_modifyitems(config, items):
    """Modify test collection to handle conditional skipping."""
    try:
        import safety
    except ImportError:
        safety_skip = pytest.mark.skip(reason="safety not installed")
        for item in items:
            if "safety" in item.name:
                item.add_marker(safety_skip)
    
    try:
        import bandit
    except ImportError:
        bandit_skip = pytest.mark.skip(reason="bandit not installed")
        for item in items:
            if "bandit" in item.name:
                item.add_marker(bandit_skip)
