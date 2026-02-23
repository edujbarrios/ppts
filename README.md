# ParamForge ⚡

Transforma tus prompts en plantillas reutilizables con YAML simple.

## ¿Qué es ParamForge?

ParamForge es una herramienta minimalista que te permite definir variables en archivos YAML y usarlas en cualquier prompt. Sin plantillas predefinidas, sin complejidad innecesaria. Solo tus parámetros, tus prompts.

## Características

- 📝 **YAML Simple**: Define parámetros en archivos YAML fáciles de editar
- 🔄 **Totalmente Personalizable**: Agrega, modifica o elimina parámetros según necesites
- 🎯 **Reutilizable**: Usa los mismos parámetros en múltiples prompts
- 🛠️ **CLI Intuitivo**: Interfaz de línea de comandos simple
- 💾 **Múltiples Contextos**: Crea diferentes archivos YAML para diferentes proyectos o contextos

## Instalación

```bash
pip install -r requirements.txt
```

## Inicio Rápido

### 1. Crea tu archivo de parámetros YAML

```yaml
# params.yaml
name: Alice
role: Senior Developer
company: TechCorp
email: alice@example.com
language: Python
experience_years: 5
```

### 2. Usa los parámetros en tu prompt

```python
from paramforge import ParamForge

# Cargar parámetros
forge = ParamForge.from_yaml("params.yaml")

# Crear un prompt usando los parámetros
prompt = """
Hello {{name}}!
You work as a {{role}} at {{company}}.
Contact: {{email}}
You have {{experience_years}} years of experience in {{language}}.
"""

# Renderizar
result = forge.render(prompt)
print(result)
```

### 3. Editar parámetros

Simplemente edita el archivo YAML:

```yaml
# params.yaml - ¡Agrega más parámetros cuando quieras!
name: Bob
address: "456 Oak Avenue"
role: Tech Lead
company: InnovateCo
email: bob@example.com
phone: "+1-555-9876"
language: JavaScript
experience_years: 8

# Nuevos parámetros personalizados
project: AI Platform
timezone: EST
availability: Full-time
skills:
  - Python
  - JavaScript
  - Docker
```

### Usando el CLI

```bash
# Renderizar un prompt con parámetros YAML
python -m paramforge render my_prompt.txt params.yaml

# Ver parámetros disponibles
python -m paramforge show params.yaml

# Agregar nuevos parámetros
python -m paramforge add params.yaml -k department -v Engineering

# Crear un nuevo archivo de parámetros
python -m paramforge init my_params.yaml
```

## Ejemplos de Uso

### Ejemplo 1: Email Profesional

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

### Ejemplo 2: Perfil Profesional

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

## Estructura del Proyecto

```
paramforge/
├── paramforge/           # Paquete principal
│   ├── __init__.py
│   ├── core.py          # Motor de parámetros
│   └── cli.py           # CLI
├── examples/
│   ├── *.yaml           # Ejemplos de parámetros
│   └── *.py             # Ejemplos de código
├── README.md
├── requirements.txt
└── setup.py
```

## API

### ParamForge Class

```python
from paramforge import ParamForge

# Crear desde YAML
forge = ParamForge.from_yaml("params.yaml")

# Renderizar prompt
result = forge.render("Hello {{name}}!")

# Agregar parámetro
forge.add("new_key", "new_value")

# Obtener parámetro
value = forge.get("name")

# Listar todos los parámetros
params = forge.list_params()

# Guardar cambios
forge.save("params.yaml")
```

## Mejores Prácticas

1. **Nombres Descriptivos**: Usa nombres claros para tus parámetros (ej: `user_email` en lugar de `e`)
2. **Organización**: Crea múltiples archivos YAML para diferentes contextos (trabajo, personal, proyectos)
3. **Comentarios**: Documenta tus archivos YAML con comentarios
4. **Versionado**: Mantén tus archivos YAML en control de versiones
5. **Backup**: Haz copias de seguridad de tus parámetros importantes

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

## ¿Por qué ParamForge?

- ✅ **Minimalista**: Solo YAML y tus prompts
- ✅ **Flexible**: Define los parámetros que necesites
- ✅ **Reutilizable**: Un YAML, múltiples prompts
- ✅ **Portable**: Comparte archivos YAML fácilmente
- ✅ **Sin Complejidad**: Sin plantillas predefinidas, sin configuración compleja

## Licencia

MIT License - Haz lo que quieras con esto.

---

**ParamForge** - Hecho con ⚡ para workflows de prompt engineering simples y poderosos.
