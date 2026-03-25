#!/usr/bin/env python3
"""Run validation on all YAML files in protocols/."""
import subprocess
import sys
from pathlib import Path

def main():
    protocols_dir = Path(__file__).parent.parent / "protocols"
    failed = []
    for yaml_file in protocols_dir.glob("**/*.yaml"):
        print(f"Validating {yaml_file}...")
        result = subprocess.run(
            ["protocollab", "validate", str(yaml_file), "--strict"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(result.stderr)
            failed.append(yaml_file)
    if failed:
        print(f"\n❌ Validation failed for {len(failed)} files:")
        for f in failed:
            print(f"  {f}")
        sys.exit(1)
    else:
        print("\n✅ All specs are valid.")

if __name__ == "__main__":
    main()