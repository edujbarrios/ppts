"""
Ejemplos básicos de uso de ParamForge.
"""

from paramforge import ParamForge

print("=" * 70)
print("ParamForge ⚡ - Ejemplos de Uso")
print("=" * 70)
print()

# Ejemplo 1: Crear y usar parámetros básicos
print("Ejemplo 1: Parámetros Básicos")
print("-" * 70)

forge = ParamForge({
    'name': 'Alice',
    'role': 'Developer',
    'company': 'TechCorp'
})

prompt = "Hello {{name}}! You work as a {{role}} at {{company}}."
result = forge.render(prompt)
print(result)
print()

# Ejemplo 2: Cargar desde archivo YAML
print("Ejemplo 2: Cargar desde YAML")
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
    
    result = forge.render(prompt)
    print(result)
    print()
except FileNotFoundError:
    print("Archivo params.yaml no encontrado. Ejecuta desde la raíz del proyecto.")
    print()

# Ejemplo 3: Agregar parámetros dinámicamente
print("Ejemplo 3: Agregar Parámetros")
print("-" * 70)

forge = ParamForge({'name': 'Bob'})
print(f"Parámetros iniciales: {forge.list_params()}")

forge.add('email', 'bob@example.com')
forge.add('city', 'New York')

print(f"Después de agregar: {forge.list_params()}")
print()

# Ejemplo 4: Prompts con listas
print("Ejemplo 4: Usando Listas")
print("-" * 70)

forge = ParamForge({
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

# Ejemplo 5: Prompts con condicionales
print("Ejemplo 5: Condicionales")
print("-" * 70)

forge = ParamForge({
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

# Ejemplo 6: Parámetros extra en render
print("Ejemplo 6: Parámetros Extra")
print("-" * 70)

forge = ParamForge({'name': 'Elena'})

# Parámetros del YAML + parámetros extra
result = forge.render(
    "Hello {{name}} from {{city}}!",
    city="Paris"  # Parámetro extra
)
print(result)
print()

# Ejemplo 7: Guardar parámetros
print("Ejemplo 7: Guardar a YAML")
print("-" * 70)

forge = ParamForge({
    'name': 'Frank',
    'email': 'frank@example.com',
    'role': 'Data Scientist',
    'tools': ['Python', 'TensorFlow', 'PyTorch']
})

forge.save('my_params.yaml')
print("✓ Parámetros guardados en my_params.yaml")
print()

# Ejemplo 8: Información del forge
print("Ejemplo 8: Información")
print("-" * 70)

forge = ParamForge({
    'param1': 'value1',
    'param2': 'value2',
    'param3': 'value3'
})

print(f"Representación: {repr(forge)}")
print(f"String: {str(forge)}")
print(f"Número de parámetros: {len(forge)}")
print(f"¿Contiene 'param1'? {'param1' in forge}")
print(f"¿Contiene 'param99'? {'param99' in forge}")
print()

print("=" * 70)
print("¡Ejemplos completados!")
print("=" * 70)
