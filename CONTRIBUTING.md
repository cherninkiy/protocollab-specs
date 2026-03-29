# Contributing to protocollab-specs

Thank you for considering contributing! This repository follows the same Code of Conduct as the main [protocollab project](https://github.com/cherninkiy/protocollab/blob/main/CODE_OF_CONDUCT.md).

## Adding or updating a specification

1. Fork the repository and create a branch from `main`.

2. Make sure you have protocollab installed from source:
   ```bash
   git clone https://github.com/cherninkiy/protocollab.git
   cd protocollab
   pip install -e .
   cd ..
   ```

2. Place your spec in the appropriate subdirectory under `protocols/`.  
   - If it’s a new domain, add a new folder with a clear name.

3. Ensure the spec passes **strict validation**:
   ```bash
   protocollab validate path/to/your/spec.yaml --strict
   ```

4. Add or update tests in `tests/` if your spec includes new features.

5. Run the full test suite locally:
   ```bash
   pip install pytest
   pytest tests/
   ```
   
6. Submit a Pull Request. Use the provided template and fill in all sections.

## Specification requirements

- The file must be valid YAML and follow the protocollab specification schema (`base.schema.json` by default, but `strict` is encouraged).
- Must include at least:
  ```yaml
  meta:
    id: <unique_snake_case_name>
    title: "Human-readable title"
    description: "Purpose of the protocol"
    endian: le|be
    version: "1.0.0" # optional but recommended

  seq:
    - id: field_name
      type: u1   # e.g. u1, u2, u4, uint8, uint16, bytes …
      doc: "Field description"
  ```
- Avoid including any confidential or proprietary information. All specs become public under Apache 2.0.

## Review process

- Automated CI will validate all specs and run tests.
- At least one maintainer will review for:
  - Correctness against the referenced standard (if any)
  - Compliance with the schema
  - Clarity and documentation
- Once approved, a maintainer will merge your PR.

## Questions?

Open an issue or discuss in the [protocollab Discussions](https://github.com/cherninkiy/protocollab/discussions).