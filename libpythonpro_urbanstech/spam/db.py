from time import sleep


class Sessao:
    """
    Classe responsável por simular uma sessão com o "banco de dados".
    Armazena usuários em memória, atribuindo IDs automaticamente.
    """

    contador = 0  # Contador de IDs para os usuários
    usuarios = []  # Lista que simula os registros de usuários no banco

    def salvar(self, usuario):
        Sessao.contador += 1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)

    def listar(self):
        return self.usuarios

    def roll_back(self):
        self.usuarios.clear()

    def fechar(self):
        pass


class Conexao:
    """
    Classe responsável por simular uma conexão com o "banco de dados".
    Pode gerar novas sessões de acesso aos dados.
    """
    def __init__(self):
        sleep(10)

    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass
