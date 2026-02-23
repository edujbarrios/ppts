"""
Ejemplo CLI: Cómo usar PromptForge desde la línea de comandos.
"""

print("""
=====================================================================
   ParamForge ⚡ - Guía de Uso del CLI
=====================================================================

1. CREAR UN ARCHIVO DE PARÁMETROS
   --------------------------------
   
   Interactivo:
   $ python -m paramforge init my_params.yaml
   
   Se te pedirá ingresar información básica.


2. VER PARÁMETROS
   --------------
   
   $ python -m paramforge show my_params.yaml
   
   Muestra todos los parámetros y sus valores.


3. AGREGAR PARÁMETROS
   ------------------
   
   $ python -m paramforge add my_params.yaml --key department --value Engineering
   $ python -m paramforge add my_params.yaml -k city -v "San Francisco"
   
   Agrega o actualiza un parámetro.


4. ELIMINAR PARÁMETROS
   -------------------
   
   $ python -m paramforge remove my_params.yaml old_param
   
   Elimina un parámetro del archivo.


5. OBTENER UN PARÁMETRO
   --------------------
   
   $ python -m paramforge get my_params.yaml name
   
   Muestra el valor de un parámetro específico.


6. RENDERIZAR UN PROMPT
   --------------------
   
   Crea un archivo de prompt (ej: email.txt):
   
   Subject: Meeting Request
   
   Hello {{name}},
   
   I'm {{sender_name}} from {{company}}.
   I'd like to discuss {{project}}.
   
   Best regards,
   {{sender_name}}
   
   
   Luego renderiza:
   $ python -m paramforge render email.txt my_params.yaml
   
   Con parámetros extra:
   $ python -m paramforge render email.txt my_params.yaml -p sender_name="Maria" -p project="AI Platform"
   
   Guardar resultado:
   $ python -m paramforge render email.txt my_params.yaml -o output.txt


7. COMBIMAR ARCHIVOS YAML
   -----------------------
   
   $ python -m paramforge merge target.yaml source.yaml
   
   Combina los parámetros de source.yaml en target.yaml


EJEMPLOS PRÁCTICOS:
===================

# Crear parámetros de trabajo
$ python -m paramforge init work.yaml

# Agregar información del proyecto
$ python -m paramforge add work.yaml -k project -v "E-Commerce Platform"
$ python -m paramforge add work.yaml -k status -v "In Progress"

# Ver todos los parámetros
$ python -m paramforge show work.yaml

# Usar en un prompt
$ echo "Project: {{project}} - Status: {{status}}" > status.txt
$ python -m paramforge render status.txt work.yaml

# Guardar resultado
$ python -m paramforge render status.txt work.yaml -o report.txt

=====================================================================
Tip: Puedes editar los archivos YAML directamente con cualquier
     editor de texto. ¡Son solo archivos de texto!
====================================================================
""")
