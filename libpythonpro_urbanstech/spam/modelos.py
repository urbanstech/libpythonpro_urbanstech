class Usuario:
    """
    Esta classe representa um usuário no sistema.
    This class represents a user in the system.
    """

    def __init__(self, nome):
        """
        Inicializa um novo usuário com um nome e um ID indefinido (None).
        Initializes a new user with a name and an undefined ID (None).
        """
        self.nome = nome
        self.id = None
