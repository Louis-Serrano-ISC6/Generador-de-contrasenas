
import re

def validar_contrasena(contrasena):
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){5,14}$"
    
    if re.match(regex, contrasena):
        return True
    else:
        return False

