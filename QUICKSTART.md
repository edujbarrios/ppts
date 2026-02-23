# Quick Start Guide

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd ppts

# Install dependencies
pip install -r requirements.txt

# Or install in development mode
pip install -e .
```

## First Steps

1. **Create a parameters file:**
```bash
python -m ppts init yaml_params/my_prompt.yaml
```

2. **View your parameters:**
```bash
python -m ppts show yaml_params/my_prompt.yaml
```

3. **Create a prompt template** (e.g., `ai_prompt.txt`):
```
You are a {{role}}.

Task: {{task}}
Input type: {{input_type}}
Output format: {{output_format}}

Focus on:
{% for area in focus_areas %}
- {{area}}
{% endfor %}

Provide your analysis below.
```

4. **Render it:**
```bash
python -m ppts render ai_prompt.txt yaml_params/my_prompt.yaml
```

## Python Usage

```python
from ppts import PPTS

# Load parameters
params = PPTS.from_yaml("yaml_params/my_prompt.yaml")

# Use in your code
prompt = "You are a {{role}}. Task: {{task}}"
result = params.render(prompt)
print(result)
```

# Use in your code
prompt = "Hello {{name}}! You are a {{role}}."
result = smith.render(prompt)
print(result)
```

## Examples

```bash
# Run the examples
python examples/basic_usage.py
python examples/advanced_usage.py
```

That's it! Check README.md for full documentation.
