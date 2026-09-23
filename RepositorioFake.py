class RepositorioFake:
    def __init__(self):
        self.compras = []
    
    def guardar(self, usuario, cantidad):
        self.compras.append({
            'usuario': usuario,
            'cantidad': cantidad
        })

"""       
repo = RepositorioFake()
repo.guardar('Juan', 3)
repo.guardar('Camila', 5)
print(repo.compras)
"""