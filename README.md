# PPTS ⚡

**Prompt Parametrizer and Template Structurer**

Craft reusable prompts with simple YAML parameters.

## What is PPTS?

PPTS (Prompt Parametrizer and Template Structurer) is a minimalist tool that lets you define variables in YAML files and use them in any prompt. No predefined templates, no unnecessary complexity. Just your parameters, your prompts.

Structure your prompts with reusable parameters - you provide the YAML configuration, and PPTS helps you generate consistent, customizable prompts.

## Features

- 📝 **Simple YAML**: Define parameters in easy-to-edit YAML files
- 🔄 **Fully Customizable**: Add, modify or remove parameters as you need
- 🎯 **Reusable**: Use the same parameters in multiple prompts
- 🛠️ **Intuitive CLI**: Simple command-line interface
- 💾 **Multiple Contexts**: Create different YAML files for different projects or contexts

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ppts.git
cd ppts

# Install dependencies
pip install -r requirements.txt

# Install the tool (development mode)
pip install -e .
```

Now you can use `ppts` command anywhere:
```bash
ppts --help
```

## Quick Start

### 1. Create your YAML parameters file

```yaml
# yaml_params/params.yaml
role: expert software architect
task: analyze and suggest improvements
input_type: Python code
output_format: markdown with code examples
language: English
tone: professional and helpful
focus_areas:
  - Performance
  - Security
  - Best practices
```

### 2. Use the parameters in your prompt

```python
from ppts import PPTS

# Load parameters
params = PPTS.from_yaml("yaml_params/params.yaml")

# Create a prompt for an LLM
prompt = """
You are a {{role}}.

Task: {{task}}
Input: {{input_type}}
Output format: {{output_format}}
Language: {{language}}
Tone: {{tone}}

Focus on these areas:
{% for area in focus_areas %}
- {{area}}
{% endfor %}

Please analyze the following code and provide your feedback.
"""

# Render
result = params.render(prompt)
print(result)
```

### 3. Edit parameters for different use cases

Simply edit the YAML file to change the prompt behavior:

```yaml
# yaml_params/params.yaml - Code Review Configuration
role: senior code reviewer
task: identify bugs and security issues
input_type: JavaScript code
output_format: structured JSON
language: Spanish
tone: constructive and educational
focus_areas:
  - Security vulnerabilities
  - Memory leaks
  - Error handling
  - Code duplication

# Or for Content Creation
role: creative content writer
task: generate blog post ideas
output_format: bullet points
language: English
tone: engaging and casual
topic: artificial intelligence
target_audience: tech enthusiasts
max_ideas: 10
```

### Using the CLI

```bash
# Render a prompt with YAML parameters
python -m ppts render my_prompt.txt yaml_params/params.yaml

# View available parameters
python -m ppts show yaml_params/params.yaml

# Add new parameters
python -m ppts add yaml_params/params.yaml -k department -v Engineering

# Create a new parameters file
python -m ppts init yaml_params/my_params.yaml
```

## Usage Examples

### Example 1: Code Analysis Prompt

```yaml
# yaml_params/params.yaml
role: expert Python developer
task: code review
code_type: REST API endpoint
focus: security and performance
output_sections:
  - Security Issues
  - Performance Bottlenecks
  - Best Practice Violations
  - Suggested Improvements
```

```python
from ppts import PPTS

params = PPTS.from_yaml("yaml_params/params.yaml")

prompt_template = """
You are a {{role}}.

Analyze this {{code_type}} focusing on {{focus}}.

Provide your analysis in these sections:
{% for section in output_sections %}
## {{section}}
{% endfor %}
"""

result = params.render(prompt_template)
# Send to your LLM API
```

### Example 2: Content Generation Prompt

```yaml
# modify yaml_params/params.yaml with:
role: technical writer
task: create tutorial
topic: Docker containerization
audience: beginner developers
style: step-by-step with examples
max_length: 1500 words
include:
  - Prerequisites
  - Code examples
  - Common pitfalls
  - Best practices
```

```python
params = PPTS.from_yaml("yaml_params/params.yaml")

prompt = """
As a {{role}}, {{task}} about {{topic}} for {{audience}}.

Style: {{style}}
Max length: {{max_length}}

Include:
{% for item in include %}
- {{item}}
{% endfor %}
"""

result = params.render(prompt)
```

## API

### PPTS Class

```python
from ppts import PPTS

# Create from YAML
params = PPTS.from_yaml("yaml_params/params.yaml")

# Render prompt
result = params.render("You are a {{role}}. Task: {{task}}")

# Add parameter
params.add("temperature", 0.7)
params.add("max_tokens", 1000)

# Get parameter
value = params.get("role")

# List all parameters
all_params = params.list_params()

# Save changes
params.save("yaml_params/params.yaml")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Why PPTS?

- ✅ **Minimalist**: Just YAML and your prompts
- ✅ **Flexible**: Define the parameters you need
- ✅ **Reusable**: One YAML, multiple prompts
- ✅ **Portable**: Share YAML files easily
- ✅ **No Complexity**: No predefined templates, no complex configuration
- ✅ **Structured Approach**: Parametrized prompts with template structuring

## License

MIT License - Do whatever you want with this.

## Citation

If you find this repository and tool useful in your research or project, feel free to cite it as:

```bibtex
@software{barrios2026ppts,
  author = {Barrios, Eduardo J.},
  title = {PPTS: Prompt Parametrized and Template Structurer},
  year = {2026},
  url = {https://github.com/yourusername/ppts},
  note = {A minimalist tool for parametrizing AI prompts with YAML}
}
```

**APA Format:**
```
Barrios, Eduardo J. (2026). PPTS: Prompt Parametrized and Template Structurer. 
GitHub repository. https://github.com/yourusername/ppts
```

---

## Author

[Eduardo J. Barrios](https://edujbarrios.com)
