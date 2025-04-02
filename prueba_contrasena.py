
import re

def validar_contrasena(contrasena):
    # Expresión regular corregida
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$"
    
    # Validar la contraseña
    if re.match(regex, contrasena):
        return True
    else:
        return False

