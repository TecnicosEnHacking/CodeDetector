import os
import re

def disclaimer():
    print("\n*******************")
    print("   Herramienta creada por Técnicos en Hacking")
    print("   Uso exclusivo para análisis de seguridad en entornos controlados")
    print("   Precaución: No nos hacemos responsables del mal uso.")
    print("*******************\n")

# Lista de patrones de código malicioso y nivel de riesgo
patterns = {
    "Bash": [
        (r"rm\s+-rf\s+/\w*", "Eliminar archivos del sistema", "Alto"),
        (r"dd\s+if=/dev/zero", "Sobreescribir disco", "Alto"),
        (r"curl\s+.+\|\s+bash", "Descarga y ejecución de script remoto", "Alto"),
        (r"wget\s+.+\|\s+bash", "Descarga y ejecución de script remoto", "Alto"),
        (r"nc\s+-e", "Shell reversa usando netcat", "Alto"),
        (r"bash\s+-i\s+>&", "Shell reversa usando bash", "Alto"),
        (r"chmod\s+777\s+.+", "Cambio de permisos en archivos", "Medio"),
        (r"chown\s+.+\s+/etc/passwd", "Cambio de propietario en archivo crítico", "Alto"),
        (r"echo\s+.+>\s+/etc/hosts", "Modificación de archivo hosts", "Alto"),
        (r"iptables\s+.+", "Modificación de reglas de firewall", "Medio"),
    ],
    "Python": [
        (r"os\.system\(.+rm\s+-rf\s+/\w*", "Eliminar archivos del sistema", "Alto"),
        (r"subprocess\.call\(.+rm\s+-rf\s+/\w*", "Eliminar archivos del sistema", "Alto"),
        (r"os\.system\(.+nc\s+-e", "Shell reversa usando netcat", "Alto"),
        (r"subprocess\.Popen\(.+nc\s+-e", "Shell reversa usando netcat", "Alto"),
        (r"socket\.socket\(.+\)\.connect", "Intento de conexión externa", "Medio"),
        (r"eval\(.*\)", "Ejecución dinámica de código", "Alto"),
        (r"os\.remove\(.+\)", "Eliminación de archivos específicos", "Medio"),
        (r"os\.rmdir\(.+\)", "Eliminación de directorios", "Medio"),
        (r"exec\(.*\)", "Ejecución de código sin validación", "Alto"),
        (r"pickle\.loads\(.+\)", "Deserialización de objetos con riesgos", "Medio"),
    ]
}

def analyze_code(file_path, lang):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        print(f"\n[Escaneando archivo: {file_path}]")
        for line_no, line in enumerate(lines, start=1):
            for pattern, description, risk_level in patterns[lang]:
                if re.search(pattern, line):
                    print(f"\n[⚠️  Posible Código Malicioso Detectado]")
                    print(f"Archivo: {file_path}")
                    print(f"Línea: {line_no}")
                    print(f"Descripción: {description}")
                    print(f"Nivel de Riesgo: {risk_level}")
                    print(f"Código sospechoso: {line.strip()}")
    print("\n[Escaneo completado para este archivo]\n")

def analyze_directory(directory_path, lang):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py') and lang == "Python":
                analyze_code(os.path.join(root, file), lang)
            elif file.endswith('.sh') and lang == "Bash":
                analyze_code(os.path.join(root, file), lang)

def main():
    disclaimer()
    print("Bienvenido al detector de código malicioso en herramientas.\n")
    option = input("¿Desea analizar un archivo específico (1) o un directorio completo (2)? ")

    if option == '1':
        file_path = input("Ingrese la ruta completa del archivo a analizar: ")
        if file_path.endswith('.py'):
            lang = "Python"
        elif file_path.endswith('.sh'):
            lang = "Bash"
        else:
            print("Archivo no compatible. Solo se admiten archivos .py o .sh.")
            return
        analyze_code(file_path, lang)
    
    elif option == '2':
        directory_path = input("Ingrese la ruta completa del directorio a analizar: ")
        lang = input("Seleccione el lenguaje de programación (Python/Bash): ").capitalize()
        if lang in patterns:
            analyze_directory(directory_path, lang)
        else:
            print("Lenguaje no compatible. Solo se admiten Python o Bash.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
