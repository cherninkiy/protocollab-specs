import pytest
import subprocess
import os
from pathlib import Path

PROTOCOLS_DIR = Path(__file__).parent.parent / "protocols"

@pytest.mark.parametrize("spec_path", PROTOCOLS_DIR.glob("**/*.yaml"))
def test_validate_spec(spec_path):
    """Run protocollab validate --strict on every YAML file."""
    result = subprocess.run(
        ["protocollab", "validate", str(spec_path), "--strict"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Validation failed for {spec_path}\n{result.stderr}"