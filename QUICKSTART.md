# Quick Start Guide

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd paramforge

# Install dependencies
pip install -r requirements.txt

# Or install in development mode
pip install -e .
```

## First Steps

1. **Create a parameters file:**
```bash
python -m paramforge init my_params.yaml
```

2. **View your parameters:**
```bash
python -m paramforge show my_params.yaml
```

3. **Create a prompt file** (e.g., `email.txt`):
```
Hello {{name}},

This is {{sender_name}} from {{company}}.

Best regards,
{{sender_name}}
```

4. **Render it:**
```bash
python -m paramforge render email.txt my_params.yaml
```

## Python Usage

```python
from paramforge import ParamForge

# Load parameters
forge = ParamForge.from_yaml("my_params.yaml")

# Use in your code
prompt = "Hello {{name}}! You are a {{role}}."
result = forge.render(prompt)
print(result)
```

## Example

```bash
# Run the examples
python examples/basic_usage.py
python examples/advanced_usage.py
```

That's it! Check README.md for full documentation.
