"""
Advanced examples of PromptSmith for real use cases.
"""

from promptsmith import PromptSmith

print("=" * 70)
print("PromptSmith ⚡ - Advanced Examples")
print("=" * 70)
print()

# Example 1: Professional Email
print("Example 1: Professional Email Generator")
print("-" * 70)

email_params = PromptSmith({
    'sender_name': 'María García',
    'sender_role': 'Product Manager',
    'sender_email': 'maria@techstart.com',
    'recipient_name': 'John Doe',
    'project_name': 'Mobile App Redesign',
    'meeting_date': 'March 15, 2026',
    'meeting_time': '2:00 PM'
})

email_template = """
Subject: {{project_name}} - Meeting Request

Dear {{recipient_name}},

I hope this email finds you well.

I'm {{sender_name}}, {{sender_role}} at TechStart. I'd like to schedule 
a meeting to discuss the {{project_name}} project with you.

Proposed Date: {{meeting_date}} at {{meeting_time}}

Please let me know if this time works for you.

Best regards,
{{sender_name}}
{{sender_email}}
""".strip()

result = email_params.render(email_template)
print(result)
print("\n")

# Example 2: Professional Profile
print("Example 2: Professional Profile Generator")
print("-" * 70)

profile_params = PromptSmith({
    'name': 'Alex Johnson',
    'title': 'Full Stack Developer',
    'experience_years': 7,
    'location': 'San Francisco, CA',
    'specialties': ['React', 'Node.js', 'AWS', 'Docker'],
    'github': 'github.com/alexj',
    'linkedin': 'linkedin.com/in/alexjohnson'
})

profile_template = """
{{name}}
{{title}} | {{experience_years}}+ years of experience
📍 {{location}}

💼 Specialties:
{% for specialty in specialties %}
• {{specialty}}
{% endfor %}

🔗 Connect:
GitHub: {{github}}
LinkedIn: {{linkedin}}
""".strip()

result = profile_params.render(profile_template)
print(result)
print("\n")

# Example 3: Project Report
print("Example 3: Project Status Report")
print("-" * 70)

project_params = PromptSmith({
    'project': 'E-Commerce Platform',
    'sprint': 'Sprint 12',
    'manager': 'Sarah Chen',
    'completed_tasks': [
        'User authentication system',
        'Product catalog API',
        'Shopping cart functionality'
    ],
    'in_progress_tasks': [
        'Payment integration',
        'Order management'
    ],
    'blockers': [
        'Waiting for payment gateway API keys'
    ],
    'completion_percentage': 75
})

report_template = """
📊 PROJECT STATUS REPORT

Project: {{project}}
Sprint: {{sprint}}
Project Manager: {{manager}}

{% if completion_percentage >= 80 %}
🟢 Status: On track ({{completion_percentage}}% complete)
{% elif completion_percentage >= 50 %}
🟡 Status: In progress ({{completion_percentage}}% complete)
{% else %}
🔴 Status: Needs attention ({{completion_percentage}}% complete)
{% endif %}

✅ Completed Tasks:
{% for task in completed_tasks %}
• {{task}}
{% endfor %}

🔄 In Progress:
{% for task in in_progress_tasks %}
• {{task}}
{% endfor %}

{% if blockers %}
⚠️  Blockers:
{% for blocker in blockers %}
• {{blocker}}
{% endfor %}
{% endif %}
""".strip()

result = project_params.render(report_template)
print(result)
print("\n")

# Example 4: Code Review Request
print("Example 4: Code Review Request")
print("-" * 70)

review_params = PromptSmith({
    'developer': 'Carlos Ruiz',
    'reviewer': 'Tech Lead',
    'feature': 'User Authentication',
    'pr_number': '142',
    'files_changed': 8,
    'lines_added': 245,
    'lines_removed': 67,
    'testing': 'Unit tests included',
    'documentation': 'API docs updated'
})

review_template = """
Code Review Request - PR #{{pr_number}}

Developer: {{developer}}
Feature: {{feature}}

📝 Changes:
• Files changed: {{files_changed}}
• Lines added: {{lines_added}}
• Lines removed: {{lines_removed}}

✓ {{testing}}
✓ {{documentation}}

@{{reviewer}} - Please review when you have a chance.
""".strip()

result = review_params.render(review_template)
print(result)
print("\n")

# Example 5: Data Analysis
print("Example 5: Data Analysis Template")
print("-" * 70)

analysis_params = PromptSmith({
    'analyst': 'Dr. Lisa Wang',
    'dataset': 'Customer Behavior Q1 2026',
    'records': 150000,
    'date_range': 'Jan 1 - Mar 31, 2026',
    'metrics': [
        'Customer acquisition cost',
        'Conversion rate',
        'Average order value',
        'Customer lifetime value'
    ],
    'tools': ['Python', 'Pandas', 'Matplotlib']
})

analysis_template = """
DATA ANALYSIS REPORT

Analyst: {{analyst}}
Dataset: {{dataset}}
Period: {{date_range}}
Total Records: {{records:,}}

Key Metrics to Analyze:
{% for metric in metrics %}
{{loop.index}}. {{metric}}
{% endfor %}

Tools Used: {{tools|join(", ")}}

Please provide:
- Statistical summary
- Trend analysis
- Key insights and recommendations
""".strip()

result = analysis_params.render(analysis_template)
print(result)
print("\n")

# Example 6: Merge multiple contexts
print("Example 6: Combine Contexts")
print("-" * 70)

try:
    # Load personal parameters
    personal = PromptSmith.from_yaml("examples/params.yaml")
    
    # Merge with work parameters
    personal.merge_yaml("examples/work_params.yaml")
    
    combined_template = """
Professional Profile

Name: {{name}}
Role: {{role}} at {{company}}
Team: {{team}}
Current Project: {{current_project}}

Contact: {{email}}
Location: {{work_location}}
    """.strip()
    
    result = personal.render(combined_template)
    print(result)
    
except FileNotFoundError:
    print("YAML files not found. Run from project root.")

print("\n")
print("=" * 70)
print("Advanced examples completed!")
print("=" * 70)
