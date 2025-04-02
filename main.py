from prueba_contrasena import validar_contrasena


if __name__ == "__main__":
    if validar_contrasena("Contraseña123!"):
        print("Contraseña válida")
    else:
        print("Contraseña inválida")


