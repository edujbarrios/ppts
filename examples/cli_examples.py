"""
Example CLI: How to use PromptSmith from the command line.
"""

print("""
=====================================================================
   PromptSmith ⚡ - CLI Usage Guide
=====================================================================

1. CREATE A PARAMETERS FILE
   -------------------------
   
   Interactive:
   $ python -m promptsmith init my_params.yaml
   
   You'll be prompted to enter basic information.


2. VIEW PARAMETERS
   ---------------
   
   $ python -m promptsmith show my_params.yaml
   
   Shows all parameters and their values.


3. ADD PARAMETERS
   --------------
   
   $ python -m promptsmith add my_params.yaml --key department --value Engineering
   $ python -m promptsmith add my_params.yaml -k city -v "San Francisco"
   
   Adds or updates a parameter.


4. REMOVE PARAMETERS
   -----------------
   
   $ python -m promptsmith remove my_params.yaml old_param
   
   Removes a parameter from the file.


5. GET A PARAMETER
   ---------------
   
   $ python -m promptsmith get my_params.yaml name
   
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
   $ python -m promptsmith render email.txt my_params.yaml
   
   With extra parameters:
   $ python -m promptsmith render email.txt my_params.yaml -p sender_name="Maria" -p project="AI Platform"
   
   Save output:
   $ python -m promptsmith render email.txt my_params.yaml -o output.txt


7. MERGE YAML FILES
   ----------------
   
   $ python -m promptsmith merge target.yaml source.yaml
   
   Merges parameters from source.yaml into target.yaml


PRACTICAL EXAMPLES:
===================

# Create work parameters
$ python -m promptsmith init work.yaml

# Add project information
$ python -m promptsmith add work.yaml -k project -v "E-Commerce Platform"
$ python -m promptsmith add work.yaml -k status -v "In Progress"

# View all parameters
$ python -m promptsmith show work.yaml

# Use in a prompt
$ echo "Project: {{project}} - Status: {{status}}" > status.txt
$ python -m promptsmith render status.txt work.yaml

# Save output
$ python -m promptsmith render status.txt work.yaml -o report.txt

=====================================================================
Tip: You can edit YAML files directly with any text editor.
     They're just text files!
====================================================================
""")
