"""
Command-line interface for ParamForge.
"""

import sys
import json
from pathlib import Path
import click
from colorama import init, Fore, Style
import yaml

from .core import ParamForge

# Initialize colorama
init(autoreset=True)


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """
    ParamForge ⚡ - Parametriza prompts con archivos YAML editables.
    
    Crea, edita y usa parámetros YAML en tus prompts de forma simple.
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
    Crear un nuevo archivo de parámetros YAML.
    
    Ejemplo:
        prompt-forge init my_params.yaml
    """
    params = {
        'name': name,
        'email': email,
    }
    
    if role:
        params['role'] = role
    if company:
        params['company'] = company
    
    forge = ParamForge(params)
    forge.save(filepath)
    
    click.echo(f"{Fore.GREEN}✓ Archivo de parámetros creado: {filepath}")
    click.echo(f"{Fore.CYAN}Puedes editarlo manualmente para agregar más parámetros.")


@cli.command()
@click.argument('params_file', type=click.Path(exists=True))
def show(params_file):
    """
    Mostrar todos los parámetros de un archivo YAML.
    
    Ejemplo:
        prompt-forge show params.yaml
    """
    try:
        forge = ParamForge.from_yaml(params_file)
        params = forge.list_params()
        
        click.echo(f"{Fore.CYAN}📄 Parámetros en {params_file}:")
        click.echo()
        
        if not params:
            click.echo(f"{Fore.YELLOW}  (vacío)")
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
        click.echo(f"{Fore.GREEN}Total: {len(params)} parámetros")
        
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
    Renderizar un prompt usando parámetros YAML.
    
    Ejemplos:
        prompt-forge render my_prompt.txt params.yaml
        prompt-forge render my_prompt.txt params.yaml -o output.txt
        prompt-forge render my_prompt.txt params.yaml -p extra_key=value
    """
    try:
        # Load parameters
        forge = ParamForge.from_yaml(params_file)
        
        # Add extra inline parameters
        extra_params = {}
        for p in param:
            if '=' not in p:
                click.echo(f"{Fore.RED}Error: Parámetro debe ser key=value: {p}", err=True)
                sys.exit(1)
            key, value = p.split('=', 1)
            extra_params[key] = value
        
        # Render
        result = forge.render_file(prompt_file, **extra_params)
        
        # Output
        if output:
            with open(output, 'w', encoding='utf-8') as f:
                f.write(result)
            click.echo(f"{Fore.GREEN}✓ Resultado guardado en: {output}")
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
    Agregar o actualizar un parámetro en el archivo YAML.
    
    Ejemplo:
        prompt-forge add params.yaml --key department --value Engineering
    """
    try:
        forge = PromptForge.from_yaml(params_file)
        
        # Try to parse value as JSON for complex types
        try:
            parsed_value = json.loads(value)
        except json.JSONDecodeError:
            parsed_value = value
        
        forge.add(key, parsed_value)
        forge.save(params_file)
        
        click.echo(f"{Fore.GREEN}✓ Parámetro agregado: {Fore.YELLOW}{key} {Fore.WHITE}= {parsed_value}")
        
    except Exception as e:
        click.echo(f"{Fore.RED}Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('params_file', type=click.Path(exists=True))
@click.argument('key')
def remove(params_file, key):
    """
    Eliminar un parámetro del archivo YAML.
    
    Ejemplo:
        prompt-forge remove params.yaml old_param
    """
    try:
        forge = PromptForge.from_yaml(params_file)
        
        if key not in forge:
            click.echo(f"{Fore.YELLOW}⚠ Parámetro '{key}' no existe")
            return
        
        forge.remove(key)
        forge.save(params_file)
        
        click.echo(f"{Fore.GREEN}✓ Parámetro eliminado: {key}")
        
    except Exception as e:
        click.echo(f"{Fore.RED}Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.argument('params_file', type=click.Path(exists=True))
@click.argument('key')
def get(params_file, key):
    """
    Obtener el valor de un parámetro específico.
    
    Ejemplo:
        prompt-forge get params.yaml name
    """
    try:
        forge = PromptForge.from_yaml(params_file)
        value = forge.get(key)
        
        if value is None:
            click.echo(f"{Fore.YELLOW}⚠ Parámetro '{key}' no encontrado")
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
    Combinar parámetros de dos archivos YAML.
    
    Ejemplo:
        prompt-forge merge params.yaml additional_params.yaml
    """
    try:
        forge = ParamForge.from_yaml(target_file)
        initial_count = len(forge)
        
        forge.merge_yaml(source_file)
        forge.save(target_file)
        
        new_count = len(forge) - initial_count
        click.echo(f"{Fore.GREEN}✓ Archivos combinados")
        click.echo(f"{Fore.CYAN}Nuevos parámetros agregados: {new_count}")
        
    except Exception as e:
        click.echo(f"{Fore.RED}Error: {str(e)}", err=True)
        sys.exit(1)


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == '__main__':
    main()
