"""
Basic usage examples of PPTS for AI prompt parametrization.
"""

from ppts import PPTS

print("=" * 70)
print("PPTS ⚡ - AI Prompt Parametrization Examples")
print("=" * 70)
print()

# Example 1: Simple AI Role Configuration
print("Example 1: Basic AI Prompt")
print("-" * 70)

params = PPTS({
    'role': 'helpful AI assistant',
    'task': 'answer questions',
    'language': 'English'
})

prompt = """You are a {{role}}.
Your task: {{task}}
Language: {{language}}"""

result = params.render(prompt)
print(result)
print()

# Example 2: Load from YAML file
print("Example 2: Load AI Config from YAML")
print("-" * 70)

try:
    params = PPTS.from_yaml("examples/yaml_params/params.yaml")
    
    prompt = """You are a {{role}}.

Task: {{task}}
Input: {{input_type}}
Output: {{output_format}}
Language: {{language}}

Focus areas:
{% for area in focus_areas %}
- {{area}}
{% endfor %}"""
    
    result = params.render(prompt)
    print(result)
    print()
except FileNotFoundError:
    print("params.yaml file not found. Run from project root.")
    print()

# Example 3: Code Analysis Prompt
print("Example 3: Code Analysis Configuration")
print("-" * 70)

params = PPTS({
    'role': 'senior code reviewer',
    'code_language': 'Python',
    'analysis_depth': 'comprehensive',
    'check_items': ['security', 'performance', 'best practices']
})

prompt = """You are a {{role}}.

Analyze the following {{code_language}} code.
Depth: {{analysis_depth}}

Check for:
{% for item in check_items %}
- {{item}}
{% endfor %}"""

result = params.render(prompt)
print(result)
print()

# Example 4: Content Conditionals
print("Example 4: Conditional Prompt Sections")
print("-" * 70)

params = PPTS({
    'role': 'technical writer',
    'include_examples': True,
    'include_diagrams': False,
    'max_length': 1000
})

prompt = """You are a {{role}}.

Write documentation with max {{max_length}} words.

{% if include_examples %}
Include code examples.
{% endif %}
{% if include_diagrams %}
Include diagrams.
{% endif %}"""

result = params.render(prompt)
print(result)
print()

# Example 5: Add Parameters Dynamically
print("Example 5: Dynamic Parameter Addition")
print("-" * 70)

params = PPTS({'role': 'data analyst'})
print(f"Initial: {params.list_params()}")

params.add('output_format', 'JSON')
params.add('max_results', 10)
params.add('sort_by', 'relevance')

print(f"After adding: {params.list_params()}")
print()

# Example 6: Override with Extra Parameters
print("Example 6: Runtime Parameter Override")
print("-" * 70)

params = PPTS({
    'role': 'translator',
    'source_lang': 'English'
})

# Override target_lang at runtime
result = params.render(
    "You are a {{role}}. Translate from {{source_lang}} to {{target_lang}}.",
    target_lang="Spanish"
)
print(result)
print()

# Example 7: Save Configuration
print("Example 7: Save AI Configuration")
print("-" * 70)

params = PPTS({
    'role': 'AI code generator',
    'language': 'Python',
    'style': 'object-oriented',
    'include_tests': True,
    'include_docs': True,
    'frameworks': ['FastAPI', 'SQLAlchemy']
})

params.save('yaml_params/code_generator_config.yaml')
print("✓ Configuration saved to yaml_params/code_generator_config.yaml")
print()

print("=" * 70)
print("Examples completed!")
print("=" * 70)
