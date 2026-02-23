"""
Basic usage examples of PromptSmith.
"""

from promptsmith import PromptSmith

print("=" * 70)
print("PromptSmith ⚡ - Usage Examples")
print("=" * 70)
print()

# Example 1: Create and use basic parameters
print("Example 1: Basic Parameters")
print("-" * 70)

smith = PromptSmith({
    'name': 'Alice',
    'role': 'Developer',
    'company': 'TechCorp'
})

prompt = "Hello {{name}}! You work as a {{role}} at {{company}}."
result = smith.render(prompt)
print(result)
print()

# Example 2: Load from YAML file
print("Example 2: Load from YAML")
print("-" * 70)

try:
    forge = ParamForge.from_yaml("examples/params.yaml")
    
    prompt = """
Dear {{name}},

Thank you for your interest in the {{role}} position.
We received your application at {{email}}.

Best regards,
HR Team
    """.strip()
    
    result = smith.render(prompt)
    print(result)
    print()
except FileNotFoundError:
    print("params.yaml file not found. Run from project root.")
    print()

# Example 3: Add parameters dynamically
print("Example 3: Add Parameters")
print("-" * 70)

smith = PromptSmith({'name': 'Bob'})
print(f"Initial parameters: {smith.list_params()}")

smith.add('email', 'bob@example.com')
smith.add('city', 'New York')

print(f"After adding: {smith.list_params()}")
print()

# Example 4: Prompts with lists
print("Example 4: Using Lists")
print("-" * 70)

smith = PromptSmith({
    'name': 'Carol',
    'skills': ['Python', 'JavaScript', 'Docker', 'Kubernetes']
})

prompt = """
Developer: {{name}}

Technical Skills:
{% for skill in skills %}
- {{skill}}
{% endfor %}
""".strip()

result = forge.render(prompt)
print(result)
print()

# Example 5: Prompts with conditionals
print("Example 5: Conditionals")
print("-" * 70)

smith = PromptSmith({
    'name': 'David',
    'experience_years': 8,
    'language': 'Python'
})

prompt = """
Candidate: {{name}}
Language: {{language}}

{% if experience_years >= 5 %}
✓ Senior level candidate with {{experience_years}} years of experience
{% else %}
✓ Junior/Mid level candidate with {{experience_years}} years of experience
{% endif %}
""".strip()

result = forge.render(prompt)
print(result)
print()

# Example 6: Extra parameters in render
print("Example 6: Extra Parameters")
print("-" * 70)

smith = PromptSmith({'name': 'Elena'})

# YAML parameters + extra parameters
result = smith.render(
    "Hello {{name}} from {{city}}!",
    city="Paris"  # Extra parameter
)
print(result)
print()

# Example 7: Save parameters
print("Example 7: Save to YAML")
print("-" * 70)

smith = PromptSmith({
    'name': 'Frank',
    'email': 'frank@example.com',
    'role': 'Data Scientist',
    'tools': ['Python', 'TensorFlow', 'PyTorch']
})

smith.save('my_params.yaml')
print("✓ Parameters saved to my_params.yaml")
print()

# Example 8: Forge information
print("Example 8: Information")
print("-" * 70)

smith = PromptSmith({
    'param1': 'value1',
    'param2': 'value2',
    'param3': 'value3'
})

print(f"Representation: {repr(smith)}")
print(f"String: {str(smith)}")
print(f"Number of parameters: {len(smith)}")
print(f"Contains 'param1'? {'param1' in smith}")
print(f"Contains 'param99'? {'param99' in smith}")
print()

print("=" * 70)
print("Examples completed!")
print("=" * 70)
