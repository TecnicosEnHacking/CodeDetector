# CodeDetector #

**CodeDetector** es una herramienta avanzada diseñada por Técnicos en Hacking para escanear archivos y directorios en busca de comandos maliciosos en scripts de Python y Bash, esta herramienta identifica patrones de código que podrían representar un riesgo de seguridad y clasifica cada hallazgo con un nivel de riesgo (Bajo, Medio, Alto) para facilitar el análisis.

## Características
- **Soporte para Python y Bash**: Detecta patrones en archivos `.py` y `.sh`.
- **Clasificación de Nivel de Riesgo**: Asigna niveles de riesgo para ayudar a evaluar la peligrosidad de cada comando.
- **Análisis de Directorios Completos**: Permite escanear múltiples archivos en una carpeta.
- **Compatibilidad con Kali Linux**: Diseñada para entornos de seguridad y pruebas de auditoría.

## Disclaimer
**Nota**: Esta herramienta debe utilizarse exclusivamente en entornos controlados y con propósitos de auditoría y análisis de seguridad, **no nos hacemos responsables** del uso indebido de esta herramienta, Técnicos en Hacking no se responsabiliza por cualquier daño o actividad ilícita realizada con este software.

## Requisitos
La herramienta requiere Python 3 y las siguientes librerías:
- `re`
- `os`

## Clonamos el repositorio
```bash
git clone https://github.com/TecnicosEnHacking/CodeDetector
cd CodeDetector
```
## Instalar dependencias
```bash
pip install -r requirements.txt
```
## Ejecucion de la herramienta
```bash
python CodeDetector.py
```
