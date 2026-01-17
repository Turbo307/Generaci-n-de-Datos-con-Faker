import random
from faker import Faker

TOTAL_REGISTROS = 50

fake = Faker("es_MX")
registros = []

for i in range(TOTAL_REGISTROS):
    usuario = {
        "id": i + 1,
        "nombre": fake.name(),
        "correo": fake.email(),
        "direccion": fake.address().replace("\n", ", "),
        "perfil": random.choice(
            ["Administrador", "Usuario", "Invitado"]
        ),
    }
    registros.append(usuario)

for usuario in registros:
    print(f"ID: {usuario['id']}")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Correo: {usuario['correo']}")
    print(f"Direccion: {usuario['direccion']}")
    print(f"Perfil: {usuario['perfil']}")
    print("-" * 50)
