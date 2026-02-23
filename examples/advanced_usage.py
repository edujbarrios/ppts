"""
Ejemplos avanzados de ParamForge para casos de uso reales.
"""

from paramforge import ParamForge

print("=" * 70)
print("ParamForge ⚡ - Ejemplos Avanzados")
print("=" * 70)
print()

# Ejemplo 1: Email Profesional
print("Ejemplo 1: Generador de Emails Profesionales")
print("-" * 70)

email_params = ParamForge({
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

# Ejemplo 2: Perfil Profesional
print("Ejemplo 2: Generador de Perfil Profesional")
print("-" * 70)

profile_params = ParamForge({
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

# Ejemplo 3: Reporte de Proyecto
print("Ejemplo 3: Reporte de Estado de Proyecto")
print("-" * 70)

project_params = ParamForge({
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

# Ejemplo 4: Code Review Request
print("Ejemplo 4: Solicitud de Code Review")
print("-" * 70)

review_params = ParamForge({
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

# Ejemplo 5: Análisis de Datos
print("Ejemplo 5: Template de Análisis de Datos")
print("-" * 70)

analysis_params = ParamForge({
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

# Ejemplo 6: Merge de múltiples contextos
print("Ejemplo 6: Combinar Contextos")
print("-" * 70)

try:
    # Cargar parámetros personales
    personal = ParamForge.from_yaml("examples/params.yaml")
    
    # Combinar con parámetros de trabajo
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
    print("Archivos YAML no encontrados. Ejecuta desde la raíz del proyecto.")

print("\n")
print("=" * 70)
print("¡Ejemplos avanzados completados!")
print("=" * 70)
