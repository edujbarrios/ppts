"""
Core engine for PPTS - Prompt Parametrized and Template Structurer
Simple YAML-based parameter management for prompts.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional, List
from jinja2 import Environment, Template, exceptions
import yaml


class PPTS:
    """
    Manage parameters from YAML files and render prompts with them.
    
    Simple concept: Load parameters from YAML, use them in any prompt.
    """
    
    def __init__(self, params: Optional[Dict[str, Any]] = None):
        """
        Initialize PPTS with parameters.
        
        Args:
            params: Dictionary of parameters (default: empty dict)
        """
        self.params = params or {}
        self._env = Environment(
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True
        )
    
    @classmethod
    def from_yaml(cls, filepath: str) -> 'PPTS':
        """
        Load parameters from a YAML file.
        
        Args:
            filepath: Path to YAML file
            
        Returns:
            PPTS instance with loaded parameters
            
        Example:
            smith = PPTS.from_yaml("params.yaml")
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            params = yaml.safe_load(f) or {}
        return cls(params)
    
    @classmethod
    def create_default(cls, filepath: str) -> 'PPTS':
        """
        Create a default YAML parameter file with common fields.
        
        Args:
            filepath: Path where to create the YAML file
            
        Returns:
            PPTS instance
            
        Example:
            smith = PPTS.create_default("my_params.yaml")
        """
        default_params = {
            'name': 'Your Name',
            'email': 'your.email@example.com',
            'role': 'Your Role',
            'company': 'Your Company',
            'address': 'Your Address',
        }
        
        # Save to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("# PPTS Parameters\n")
            f.write(f"# Created: {filepath}\n")
            f.write("# Edit this file to add your own parameters\n\n")
            yaml.dump(default_params, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        return cls(default_params)
    
    def render(self, prompt: str, **extra_params) -> str:
        """
        Render a prompt using the loaded parameters.
        
        Args:
            prompt: The prompt string with {{variable}} placeholders
            **extra_params: Additional parameters to merge with loaded params
            
        Returns:
            Rendered prompt string
            
        Example:
            result = smith.render("Hello {{name}}!")
        """
        # Merge loaded params with any extra params
        final_params = {**self.params, **extra_params}
        
        try:
            template = self._env.from_string(prompt)
            return template.render(**final_params)
        except exceptions.UndefinedError as e:
            raise ValueError(f"Missing parameter in prompt: {e}")
    
    def render_file(self, prompt_file: str, **extra_params) -> str:
        """
        Render a prompt from a file.
        
        Args:
            prompt_file: Path to file containing the prompt
            **extra_params: Additional parameters
            
        Returns:
            Rendered prompt string
            
        Example:
            result = smith.render_file("my_prompt.txt")
        """
        with open(prompt_file, 'r', encoding='utf-8') as f:
            prompt = f.read()
        return self.render(prompt, **extra_params)
    
    def add(self, key: str, value: Any) -> None:
        """
        Add or update a parameter.
        
        Args:
            key: Parameter name
            value: Parameter value
            
        Example:
            smith.add("department", "Engineering")
        """
        self.params[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a parameter value.
        
        Args:
            key: Parameter name
            default: Default value if key doesn't exist
            
        Returns:
            Parameter value or default
            
        Example:
            name = smith.get("name")
        """
        return self.params.get(key, default)
    
    def remove(self, key: str) -> None:
        """
        Remove a parameter.
        
        Args:
            key: Parameter name
            
        Example:
            smith.remove("old_param")
        """
        if key in self.params:
            del self.params[key]
    
    def list_params(self) -> Dict[str, Any]:
        """
        Get all parameters.
        
        Returns:
            Dictionary of all parameters
            
        Example:
            all_params = smith.list_params()
        """
        return self.params.copy()
    
    def save(self, filepath: str, include_comments: bool = True) -> None:
        """
        Save parameters to a YAML file.
        
        Args:
            filepath: Path to save YAML file
            include_comments: Whether to include header comments
            
        Example:
            smith.save("updated_params.yaml")
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            if include_comments:
                f.write("# PPTS Parameters\n")
                f.write(f"# File: {filepath}\n\n")
            yaml.dump(self.params, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    def merge_yaml(self, filepath: str) -> None:
        """
        Merge parameters from another YAML file.
        
        Args:
            filepath: Path to YAML file to merge
            
        Example:
            smith.merge_yaml("additional_params.yaml")
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            new_params = yaml.safe_load(f) or {}
        self.params.update(new_params)
    
    def __len__(self) -> int:
        """Get number of parameters."""
        return len(self.params)
    
    def __contains__(self, key: str) -> bool:
        """Check if parameter exists."""
        return key in self.params
    
    def __repr__(self) -> str:
        """String representation."""
        return f"PPTS(parameters={len(self.params)})"
    
    def __str__(self) -> str:
        """User-friendly string representation."""
        param_list = ", ".join(self.params.keys())
        return f"PPTS with {len(self.params)} parameters: {param_list}"
