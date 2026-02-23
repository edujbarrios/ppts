# PromptSmith ⚡

Craft reusable prompts with simple YAML parameters.

## What is PromptSmith?

PromptSmith is a minimalist tool that lets you define variables in YAML files and use them in any prompt. No predefined templates, no unnecessary complexity. Just your parameters, your prompts.

Think of it as a **forge for your prompts** - you provide the raw materials (YAML parameters), and PromptSmith helps you craft the final product (rendered prompts).

## Features

- 📝 **Simple YAML**: Define parameters in easy-to-edit YAML files
- 🔄 **Fully Customizable**: Add, modify or remove parameters as you need
- 🎯 **Reusable**: Use the same parameters in multiple prompts
- 🛠️ **Intuitive CLI**: Simple command-line interface
- 💾 **Multiple Contexts**: Create different YAML files for different projects or contexts

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### 1. Create your YAML parameters file

```yaml
# params.yaml
name: Alice
role: Senior Developer
company: TechCorp
email: alice@example.com
language: Python
experience_years: 5
```

### 2. Use the parameters in your prompt

```python
from promptsmith import PromptSmith

# Load parameters
smith = PromptSmith.from_yaml("params.yaml")

# Create a prompt using the parameters
prompt = """
Hello {{name}}!
You work as a {{role}} at {{company}}.
Contact: {{email}}
You have {{experience_years}} years of experience in {{language}}.
"""

# Render
result = smith.render(prompt)
print(result)
```

### 3. Edit parameters

Simply edit the YAML file:

```yaml
# params.yaml - Add more parameters whenever you want!
name: Bob
address: "456 Oak Avenue"
role: Tech Lead
company: InnovateCo
email: bob@example.com
phone: "+1-555-9876"
language: JavaScript
experience_years: 8

# New custom parameters
project: AI Platform
timezone: EST
availability: Full-time
skills:
  - Python
  - JavaScript
  - Docker
```

### Using the CLI

```bash
# Render a prompt with YAML parameters
python -m promptsmith render my_prompt.txt params.yaml

# View available parameters
python -m promptsmith show params.yaml

# Add new parameters
python -m promptsmith add params.yaml -k department -v Engineering

# Create a new parameters file
python -m promptsmith init my_params.yaml
```

## Usage Examples

### Example 1: Professional Email

```yaml
# params.yaml
name: María García
role: Product Manager
company: TechStart
email: maria@techstart.com
recipient_name: John Doe
project: Mobile App Redesign
```

```text
Hello {{recipient_name}},

I'm {{name}}, {{role}} at {{company}}.

I'd like to discuss the {{project}} project with you.

Best regards,
{{name}}
{{email}}
```

### Example 2: Professional Profile

```yaml
# profile_params.yaml
name: Alex Johnson
profession: Full Stack Developer
years: 7
city: San Francisco
specialties:
  - React
  - Node.js
  - AWS
```

## Project Structure

```
promptsmith/
├── promptsmith/          # Main package
│   ├── __init__.py
│   ├── core.py          # Parameter engine
│   └── cli.py           # CLI
├── examples/
│   ├── *.yaml           # Parameter examples
│   └── *.py             # Code examples
├── README.md
├── requirements.txt
└── setup.py
```

## API

### PromptSmith Class

```python
from promptsmith import PromptSmith

# Create from YAML
smith = PromptSmith.from_yaml("params.yaml")

# Render prompt
result = smith.render("Hello {{name}}!")

# Add parameter
smith.add("new_key", "new_value")

# Get parameter
value = smith.get("name")

# List all parameters
params = smith.list_params()

# Save changes
smith.save("params.yaml")
```

## Best Practices

1. **Descriptive Names**: Use clear names for your parameters (e.g., `user_email` instead of `e`)
2. **Organization**: Create multiple YAML files for different contexts (work, personal, projects)
3. **Comments**: Document your YAML files with comments
4. **Version Control**: Keep your YAML files in version control
5. **Backup**: Make backups of your important parameters

```yaml
# params.yaml - Personal Information
# Last updated: 2026-02-23

# Basic Info
name: Your Name
email: your.email@example.com

# Work Info  
role: Your Role
company: Your Company
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Why PromptSmith?

- ✅ **Minimalist**: Just YAML and your prompts
- ✅ **Flexible**: Define the parameters you need
- ✅ **Reusable**: One YAML, multiple prompts
- ✅ **Portable**: Share YAML files easily
- ✅ **No Complexity**: No predefined templates, no complex configuration
- ✅ **Artisan Approach**: Craft your prompts with precision

## License

MIT License - Do whatever you want with this.

---

**PromptSmith** ⚡ - Forging better prompts through simplicity.
