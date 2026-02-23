# 📦 Guía para Publicar PPTS en PyPI

## Prerrequisitos

### 1. Crear cuenta en PyPI
- **PyPI (producción)**: https://pypi.org/account/register/
- **TestPyPI (pruebas)**: https://test.pypi.org/account/register/

### 2. Generar API Token
1. Ve a tu cuenta en PyPI: https://pypi.org/manage/account/
2. Scroll hasta "API tokens"
3. Click en "Add API token"
4. Nombre: "PPTS Upload Token"
5. Scope: "Entire account" (o específico para el proyecto después de la primera subida)
6. **Copia el token** (empieza con `pypi-`), lo necesitarás después

### 3. Instalar herramientas necesarias
```bash
pip install --upgrade build twine
```

## Preparación del Paquete

### 1. Actualizar información del proyecto

**Editar `setup.py` y `pyproject.toml`:**
- Cambiar la URL del repositorio GitHub (actualmente: `yourusername/ppts`)
- Verificar versión: `1.0.0`
- Verificar autor: `Eduardo J. Barrios`

### 2. Verificar archivos necesarios
- ✅ `README.md` - Descripción del proyecto
- ✅ `LICENSE` - Licencia MIT
- ✅ `requirements.txt` - Dependencias
- ✅ `setup.py` - Configuración del paquete
- ✅ `pyproject.toml` - Configuración moderna
- ✅ `MANIFEST.in` - Archivos a incluir

### 3. Limpiar builds anteriores
```bash
# Eliminar carpetas de build anteriores
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue
```

## Proceso de Publicación

### Opción A: Publicar directamente a PyPI (Producción)

#### Paso 1: Construir el paquete
```bash
python -m build
```

Esto creará:
- `dist/ppts-1.0.0-py3-none-any.whl`
- `dist/ppts-1.0.0.tar.gz`

#### Paso 2: Verificar el paquete
```bash
twine check dist/*
```

#### Paso 3: Subir a PyPI
```bash
twine upload dist/*
```

Te pedirá:
- **Username**: `__token__`
- **Password**: Tu API token (empieza con `pypi-`)

### Opción B: Probar primero en TestPyPI (Recomendado)

#### Paso 1: Construir
```bash
python -m build
```

#### Paso 2: Subir a TestPyPI
```bash
twine upload --repository testpypi dist/*
```

Credenciales TestPyPI:
- **Username**: `__token__`
- **Password**: Tu token de TestPyPI

#### Paso 3: Probar instalación desde TestPyPI
```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps ppts
```

#### Paso 4: Si funciona, subir a PyPI real
```bash
twine upload dist/*
```

## Configurar .pypirc (Opcional - Para no escribir credenciales)

### Windows:
Crea `%USERPROFILE%\.pypirc`:
```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_API_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TEST_API_TOKEN_HERE
```

### Linux/Mac:
Crea `~/.pypirc` con el mismo contenido.

**⚠️ IMPORTANTE**: Agrega `.pypirc` a `.gitignore` para no subir tus tokens.

## Verificación Post-Publicación

### 1. Verificar en PyPI
- Visita: https://pypi.org/project/ppts/
- Verifica que la descripción se vea correctamente
- Revisa los metadatos

### 2. Probar instalación
```bash
# Crear entorno virtual nuevo
python -m venv test_env
test_env\Scripts\activate  # Windows
# source test_env/bin/activate  # Linux/Mac

# Instalar desde PyPI
pip install ppts

# Probar
ppts --help
python -c "from ppts import PPTS; print('OK')"
```

## Actualizar Versión (Futuras releases)

1. **Actualizar versión** en:
   - `setup.py`: `version="1.0.1"`
   - `pyproject.toml`: `version = "1.0.1"`
   - `ppts/__init__.py`: `__version__ = "1.0.1"`

2. **Commit cambios**:
   ```bash
   git add .
   git commit -m "Bump version to 1.0.1"
   git tag v1.0.1
   git push origin master --tags
   ```

3. **Reconstruir y subir**:
   ```bash
   Remove-Item -Recurse -Force dist, build, *.egg-info
   python -m build
   twine check dist/*
   twine upload dist/*
   ```

## Comandos Rápidos (Resumen)

```bash
# 1. Limpiar
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue

# 2. Construir
python -m build

# 3. Verificar
twine check dist/*

# 4. Subir a PyPI
twine upload dist/*
```

## Troubleshooting

### Error: "File already exists"
- Ya subiste esta versión. Incrementa el número de versión.

### Error: "Invalid distribution"
- Ejecuta: `twine check dist/*`
- Revisa el README.md (debe ser Markdown válido)

### Error: "403 Forbidden"
- Verifica tu API token
- Asegúrate de usar `__token__` como username
- El token debe empezar con `pypi-`

### El README no se ve bien en PyPI
- Asegúrate de que `long_description_content_type="text/markdown"` en setup.py
- Verifica que README.md sea Markdown válido
- Prueba renderizar localmente: `python -m readme_renderer README.md`

## Recursos

- **PyPI**: https://pypi.org/
- **TestPyPI**: https://test.pypi.org/
- **Documentación**: https://packaging.python.org/
- **Twine**: https://twine.readthedocs.io/

---

¡Listo! Después de publicar, tu paquete estará disponible con:
```bash
pip install ppts
```
