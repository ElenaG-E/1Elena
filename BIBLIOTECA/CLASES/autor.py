from datetime import datetime
import paises

class Autor(paises):
    def __init__(self, id_autor, nombre_autor, seudonimo_autor, codigo_pais, fecha_ac, biografia_autor):
        super().__init__(codigo_pais)
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.seudonimo_autor = seudonimo_autor
        self.fecha_nac = fecha_nac
        self. gi


from github import Github

# Autenticación con tu token de acceso personal
token = 'tu_token_de_acceso_personal'
g = Github(token)

# Obtener tu perfil
user = g.get_user()

# Imprimir información del usuario
print(f"Hola, {user.login}! Tu nombre es {user.name}.")
