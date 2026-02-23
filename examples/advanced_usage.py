"""
Advanced examples of PPTS for AI/LLM prompt engineering.
"""

from ppts import PPTS

print("=" * 70)
print("PPTS ⚡ - Advanced AI Prompt Examples")
print("=" * 70)
print()

# Example 1: Multi-Step AI Agent Prompt
print("Example 1: Multi-Step Agent Configuration")
print("-" * 70)

agent_params = PPTS({
    'role': 'AI research assistant',
    'task': 'literature review',
    'steps': [
        'Search for relevant papers',
        'Summarize key findings',
        'Identify research gaps',
        'Suggest future directions'
    ],
    'output_format': 'structured report',
    'citation_style': 'APA',
    'max_papers': 10
})

agent_template = """You are a {{role}}.

Task: {{task}}

Follow these steps:
{% for step in steps %}
{{loop.index}}. {{step}}
{% endfor %}

Output format: {{output_format}}
Citation style: {{citation_style}}
Maximum papers to review: {{max_papers}}"""

result = agent_params.render(agent_template)
print(result)
print("\n")

# Example 2: Chain-of-Thought Reasoning
print("Example 2: Chain-of-Thought Prompt")
print("-" * 70)

cot_params = PPTS({
    'role': 'logical reasoning expert',
    'problem_type': 'mathematical word problem',
    'reasoning_steps': [
        'Identify given information',
        'Define what needs to be found',
        'Choose appropriate method',
        'Show step-by-step calculation',
        'Verify the answer'
    ],
    'include_explanation': True
})

cot_template = """You are a {{role}}.

Problem type: {{problem_type}}

Reasoning process:
{% for step in reasoning_steps %}
Step {{loop.index}}: {{step}}
{% endfor %}

{% if include_explanation %}
Provide detailed explanations for each step.
{% endif %}"""

result = cot_params.render(cot_template)
print(result)
print("\n")

# Example 3: Few-Shot Learning Prompt
print("Example 3: Few-Shot Learning Configuration")
print("-" * 70)

fewshot_params = PPTS({
    'task': 'sentiment analysis',
    'examples': [
        {'input': 'This product is amazing!', 'output': 'positive'},
        {'input': 'Terrible experience, very disappointed.', 'output': 'negative'},
        {'input': 'It works as expected.', 'output': 'neutral'}
    ],
    'input_label': 'Text',
    'output_label': 'Sentiment'
})

fewshot_template = """Task: {{task}}

Examples:
{% for example in examples %}
{{input_label}}: {{example.input}}
{{output_label}}: {{example.output}}

{% endfor %}
Now analyze the following:"""

result = fewshot_params.render(fewshot_template)
print(result)
print("\n")

# Example 4: Structured Output Generation
print("Example 4: Structured JSON Output")
print("-" * 70)

structured_params = PPTS({
    'role': 'API response generator',
    'output_schema': {
        'user_id': 'integer',
        'username': 'string',
        'email': 'string',
        'created_at': 'ISO 8601 datetime',
        'is_active': 'boolean'
    },
    'required_fields': ['user_id', 'username', 'email'],
    'format': 'JSON'
})

structured_template = """You are a {{role}}.

Generate output in {{format}} format with this schema:
{% for field, type in output_schema.items() %}
- {{field}}: {{type}}{% if field in required_fields %} (required){% endif %}
{% endfor %}"""

result = structured_params.render(structured_template)
print(result)
print("\n")

# Example 5: Code Generation with Constraints
print("Example 5: Code Generation Prompt")
print("-" * 70)

codegen_params = PPTS({
    'role': 'expert Python developer',
    'task': 'implement REST API endpoint',
    'language': 'Python',
    'framework': 'FastAPI',
    'requirements': [
        'Include input validation',
        'Add error handling',
        'Write docstrings',
        'Include type hints'
    ],
    'style_guide': 'PEP 8',
    'include_tests': True
})

codegen_template = """You are a {{role}}.

Task: {{task}}
Language: {{language}}
Framework: {{framework}}

Requirements:
{% for req in requirements %}
✓ {{req}}
{% endfor %}

Follow {{style_guide}} style guide.
{% if include_tests %}
Include unit tests.
{% endif %}"""

result = codegen_params.render(codegen_template)
print(result)
print("\n")

# Example 6: Context-Aware Document Analysis
print("Example 6: Document Analysis with Context")
print("-" * 70)

analysis_params = PPTS({
    'role': 'technical document analyst',
    'document_type': 'API documentation',
    'analysis_aspects': [
        {'aspect': 'Completeness', 'weight': 'high'},
        {'aspect': 'Clarity', 'weight': 'high'},
        {'aspect': 'Examples', 'weight': 'medium'},
        {'aspect': 'Error cases', 'weight': 'medium'}
    ],
    'output_format': 'detailed report with scores',
    'include_suggestions': True
})

analysis_template = """You are a {{role}}.

Analyze this {{document_type}}.

Evaluation criteria:
{% for item in analysis_aspects %}
- {{item.aspect}} (priority: {{item.weight}})
{% endfor %}

Output: {{output_format}}
{% if include_suggestions %}
Include actionable improvement suggestions.
{% endif %}"""

result = analysis_params.render(analysis_template)
print(result)
print("\n")

# Example 7: Merge Multiple Configurations
print("Example 7: Merge Configurations")
print("-" * 70)

try:
    # Load base configuration
    base_config = PPTS({
        'role': 'AI assistant',
        'language': 'English',
        'tone': 'professional'
    })
    
    # Simulate loading additional config from YAML
    # In real use: base_config.merge_yaml("examples/yaml_params/additional_config.yaml")
    
    base_config.add('specialized_task', 'code review')
    base_config.add('output_format', 'markdown')
    
    combined_template = """You are a {{role}}.
Task: {{specialized_task}}
Language: {{language}}
Tone: {{tone}}
Format: {{output_format}}"""
    
    result = base_config.render(combined_template)
    print(result)
    
except Exception as e:
    print(f"Note: {e}")

print("\n")
print("=" * 70)
print("Advanced examples completed!")
print("=" * 70)
