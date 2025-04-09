
import re

class ValidarContrasena:

    def validar_contrasena_regex(self,contrasena):
        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){5,14}$"

        if re.match(regex, contrasena):
            return True
        else:
            return False


    def validar_contrasena(self, cadena: str) -> bool:

        """
        Valida una contraseña según los siguientes criterios:
        1. Longitud entre 5 y 14 caracteres.  (funcion lista)
        2. Comienza con una letra (mayúscula o minúscula). (funcion lista)
        3. Contiene al menos una letra mayúscula. (funcion lista)
        4. Contiene al menos una letra minúscula. (funcion lista)
        5. Contiene al menos un número.  (funcion lista)
        6. Contiene al menos un carácter especial (@, *, ?, -). (funcion lista)

        :param cadena: La contraseña a validar.
        :return: True si la contraseña es válida, False de lo contrario.
        """

        return (

            self.validar_longitud(cadena) and
            self.primer_caracter_es_letra(cadena) and
            self.contiene_letra_mayuscula(cadena) and
            self.contiene_letra_minuscula(cadena) and
            self.contiene_numero(cadena) and
            self.contiene_caracter_especial(cadena)

        )


    def validar_longitud(self,cadena: str) -> bool:
        """
        Valida la longitud de la cadena que se encuentre entre 5 a 14 caracteres como maximo.
        :param cadena:
        :return: True si la longitud es válida, False de lo contrario.
        """
        return 5 <= len(cadena) <= 14

    def primer_caracter_es_letra(self,cadena: str) -> bool:
        """
        Verifica si el primer caracter de la cadena es una letra
        :param cadena:
        :return: True: si es una letra, False de lo contrario.
        """
        return self.es_letra(cadena[0])

    def es_letra(self,caracter: str) -> bool:
        """
        Verifica si el carácter es una letra (mayúscula o minúscula).
        :param caracter: El carácter a verificar.
        :return: True si es una letra, False de lo contrario.
        """
        return ("A" <= caracter <= "Z") or ("a" <= caracter <= "z")

    def contiene_letra_mayuscula(self,cadena: str) -> bool:
        """
        Verifica si la cadena contiene al menos una letra mayúscula.
        :param cadena:
        :return: True si contiene una letra mayúscula, False de lo contrario.
        """

        for caracter in cadena:
            if 'A' <= caracter <= 'Z':
                return True
        return False

    def contiene_letra_minuscula(self,cadena: str) -> bool:
        """
        Verifica si la cadena contiene al menos una letra minúscula.
        :param cadena:
        :return: True si contiene una letra minúscula, False de lo contrario.
        """

        for caracter in cadena:
            if 'a' <= caracter <= 'z':
                return True
        return False

    def contiene_numero(self,cadena: str) -> bool:

        for caracter in cadena:

            if '0' <= caracter <= '9':
                return True
        return False

    def contiene_caracter_especial(self,cadena: str) -> bool:

        for caracter in cadena:

            if caracter in {'@', '-', '?', '*'}:
                return True

        return False





