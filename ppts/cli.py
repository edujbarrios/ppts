"""
Command-line interface for PPTS (Prompt Parametrized and Template Structurer).
"""

import sys
import json
from pathlib import Path
import click
from colorama import init, Fore, Style
import yaml

from .core import PPTS

# Initialize colorama
init(autoreset=True)


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """
    PPTS ⚡ - Prompt Parametrized and Template Structurer
    
    Create, edit and use YAML parameters in your prompts simply.
    """
    pass


@cli.command()
@click.argument('filepath', default='params.yaml')
@click.option('--name', prompt='Your name', help='Your name')
@click.option('--email', prompt='Your email', help='Your email')
@click.option('--role', prompt='Your role', default='', help='Your role')
@click.option('--company', prompt='Your company', default='', help='Your company')
def init(filepath, name, email, role, company):
    """
    Create a new YAML parameters file.
    
    Example:
        ppts init my_params.yaml
    """
    params = {
        'name': name,
        'email': email,
    }
    
    if role:
        params['role'] = role
    if company:
        params['company'] = company
    
    smith = PPTS(params)
    smith.save(filepath)
    
    click.echo(f"{Fore.GREEN}✓ Parameters file created: {filepath}")
    click.echo(f"{Fore.CYAN}You can edit it manually to add more parameters.")


@cli.command()
@click.argument('params_file', type=click.Path(exists=True))
def show(params_file):
    """
    Show all parameters from a YAML file.
    
    Example:
        ppts show params.yaml
    """
    try:
        smith = PPTS.from_yaml(params_file)
        params = smith.list_params()
        
        click.echo(f"{Fore.CYAN}📄 Parameters in {params_file}:")
        click.echo()
        
        if not params:
            click.echo(f"{Fore.YELLOW}  (empty)")
            return
        
        # Find max key length for alignment
        max_len = max(len(str(k)) for k in params.keys())
        
        for key, value in params.items():
            # Format value
            if isinstance(value, (list, dict)):
                value_str = json.dumps(value, ensure_ascii=False)
            else:
                value_str = str(value)
            
            # Truncate long values
            if len(value_str) > 60:
                value_str = value_str[:57] + "..."
            
            click.echo(f"  {Fore.YELLOW}{key:<{max_len}} {Fore.WHITE}→ {Style.DIM}{value_str}")
        
        click.echo()
        click.echo(f"{Fore.GREEN}Total: {len(params)} parameters")
        
    except Exception as e:
        click.echo(f"{Fore.RED}Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('prompt_file', type=click.Path(exists=True))
@click.argument('params_file', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), help='Archivo de salida')
@click.option('--param', '-p', multiple=True, help='Parámetro adicional: key=value')
def render(prompt_file, params_file, output, param):
    """
    Render a prompt using YAML parameters.
    
    Examples:
        ppts render my_prompt.txt params.yaml
        ppts render my_prompt.txt params.yaml -o output.txt
        ppts render my_prompt.txt params.yaml -p extra_key=value
    """
    try:
        # Load parameters
        smith = PPTS.from_yaml(params_file)
        
        # Add extra inline parameters
        extra_params = {}
        for p in param:
            if '=' not in p:
                click.echo(f"{Fore.RED}Error: Parameter must be key=value format: {p}", err=True)
                sys.exit(1)
            key, value = p.split('=', 1)
            extra_params[key] = value
        
        # Render
        result = smith.render_file(prompt_file, **extra_params)
        
        # Output
        if output:
            with open(output, 'w', encoding='utf-8') as f:
                f.write(result)
            click.echo(f"{Fore.GREEN}✓ Output saved to: {output}")
        else:
            click.echo(result)
            
    except Exception as e:
        click.echo(f"{Fore.RED}Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('params_file', type=click.Path(exists=True))
@click.option('--key', '-k', required=True, help='Nombre del parámetro')
@click.option('--value', '-v', required=True, help='Valor del parámetro')
def add(params_file, key, value):
    """
    Add or update a parameter in the YAML file.
    
    Example:
        ppts add params.yaml --key department --value Engineering
    """
    try:
        smith = PPTS.from_yaml(params_file)
        
        # Try to parse value as JSON for complex types
        try:
            parsed_value = json.loads(value)
        except json.JSONDecodeError:
            parsed_value = value
        
        smith.add(key, parsed_value)
        smith.save(params_file)
        
        click.echo(f"{Fore.GREEN}✓ Parameter added: {Fore.YELLOW}{key} {Fore.WHITE}= {parsed_value}")
        
    except Exception as e:
        click.echo(f"{Fore.RED}Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('params_file', type=click.Path(exists=True))
@click.argument('key')
def remove(params_file, key):
    """
    Remove a parameter from the YAML file.
    
    Example:
        ppts remove params.yaml old_param
    """
    try:
        smith = PPTS.from_yaml(params_file)
        
        if key not in smith:
            click.echo(f"{Fore.YELLOW}⚠ Parameter '{key}' does not exist")
            return
        
        smith.remove(key)
        smith.save(params_file)
        
        click.echo(f"{Fore.GREEN}✓ Parameter removed: {key}")
        
    except Exception as e:
        click.echo(f"{Fore.RED}Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('params_file', type=click.Path(exists=True))
@click.argument('key')
def get(params_file, key):
    """
    Get the value of a specific parameter.
    
    Example:
        ppts get params.yaml name
    """
    try:
        smith = PPTS.from_yaml(params_file)
        value = smith.get(key)
        
        if value is None:
            click.echo(f"{Fore.YELLOW}⚠ Parameter '{key}' not found")
        else:
            click.echo(f"{Fore.YELLOW}{key}: {Fore.WHITE}{value}")
            
    except Exception as e:
        click.echo(f"{Fore.RED}Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('target_file', type=click.Path(exists=True))
@click.argument('source_file', type=click.Path(exists=True))
def merge(target_file, source_file):
    """
    Merge parameters from two YAML files.
    
    Example:
        ppts merge params.yaml additional_params.yaml
    """
    try:
        smith = PPTS.from_yaml(target_file)
        initial_count = len(smith)
        
        smith.merge_yaml(source_file)
        smith.save(target_file)
        
        new_count = len(smith) - initial_count
        click.echo(f"{Fore.GREEN}✓ Files merged")
        click.echo(f"{Fore.CYAN}New parameters added: {new_count}")
        
    except Exception as e:
        click.echo(f"{Fore.RED}Error: {str(e)}", err=True)
        sys.exit(1)


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == '__main__':
    main()
