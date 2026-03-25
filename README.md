# protocollab-specs

[![Validate Specs](https://github.com/cherninkiy/protocollab-specs/actions/workflows/validate.yml/badge.svg)](https://github.com/cherninkiy/protocollab-specs/actions/workflows/validate.yml)

**Community-driven protocol specifications for [protocollab](https://github.com/cherninkiy/protocollab).**

This repository is the central, curated collection of YAML protocol definitions compatible with protocollab. Every spec can be validated, versioned, and used to generate parsers, Wireshark dissectors, and test suites.

## 🚀 Quick start

1. Clone and install protocollab from source:
   ```bash
   git clone https://github.com/cherninkiy/protocollab.git
   cd protocollab
   pip install -e .
   cd ..

2. Validate a spec:
   ```bash
   protocollab validate protocols/examples/ping_protocol.yaml --strict
   ```

3. Generate Python parser:
   ```bash
   protocollab generate python protocols/examples/ping_protocol.yaml --output ./output
   ```

## 📁 Repository structure

- `protocols/` – specifications organised by domain
  - `examples/` – simple, documented specs for learning
  - `industrial/`, `iot/`, `telecom/` – production‑ready specs
- `tests/` – automated validation of all specs (run via `pytest`)
- `scripts/` – helper tools

    Note: This repository **requires the protocollab tool to be installed**. Since it is not yet available on PyPI, please install it from source as described above.

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a spec.  
All contributions are welcome and must be licensed under Apache 2.0.

## 🔒 License

Apache 2.0 – see [LICENSE](LICENSE) for details.
