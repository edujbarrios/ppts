"""
Example CLI: How to use PPTS from the command line.
"""

print("""
=====================================================================
   PPTS ⚡ - CLI Usage Guide
=====================================================================

1. CREATE A PARAMETERS FILE
   -------------------------
   
   Interactive:
   $ python -m ppts init yaml_params/my_params.yaml
   
   You'll be prompted to enter basic information.


2. VIEW PARAMETERS
   ---------------
   
   $ python -m ppts show yaml_params/my_params.yaml
   
   Shows all parameters and their values.


3. ADD PARAMETERS
   --------------
   
   $ python -m ppts add yaml_params/my_params.yaml --key department --value Engineering
   $ python -m ppts add yaml_params/my_params.yaml -k city -v "San Francisco"
   
   Adds or updates a parameter.


4. REMOVE PARAMETERS
   -----------------
   
   $ python -m ppts remove yaml_params/my_params.yaml old_param
   
   Removes a parameter from the file.


5. GET A PARAMETER
   ---------------
   
   $ python -m ppts get yaml_params/my_params.yaml name
   
   Shows the value of a specific parameter.


6. RENDER A PROMPT
   ---------------
   
   Create a prompt file (e.g., email.txt):
   
   Subject: Meeting Request
   
   Hello {{name}},
   
   I'm {{sender_name}} from {{company}}.
   I'd like to discuss {{project}}.
   
   Best regards,
   {{sender_name}}
   
   
   Then render:
   $ python -m ppts render email.txt yaml_params/my_params.yaml
   
   With extra parameters:
   $ python -m ppts render email.txt yaml_params/my_params.yaml -p sender_name="Maria" -p project="AI Platform"
   
   Save output:
   $ python -m ppts render email.txt yaml_params/my_params.yaml -o output.txt


7. MERGE YAML FILES
   ----------------
   
   
   $ ppts merge yaml_params/target.yaml yaml_params/source.yaml
   
   Merges parameters from source.yaml into target.yaml


PRACTICAL EXAMPLES:
===================

# Create work parameters
$ python -m ppts init yaml_params/work.yaml

# Add project information
$ python -m ppts add yaml_params/work.yaml -k project -v "E-Commerce Platform"
$ python -m ppts add yaml_params/work.yaml -k status -v "In Progress"

# View all parameters
$ python -m ppts show yaml_params/work.yaml

# Use in a prompt
$ echo "Project: {{project}} - Status: {{status}}" > status.txt
$ python -m ppts render status.txt yaml_params/work.yaml

# Save output
$ python -m ppts render status.txt yaml_params/work.yaml -o report.txt

=====================================================================
Tip: You can edit YAML files directly with any text editor.
     They're just text files stored in yaml_params/ folder!
====================================================================
""")
