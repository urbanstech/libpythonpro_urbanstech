from libpythonpro_urbanstech.spam.db import Conexao, Sessao  # noqa: F401
from libpythonpro_urbanstech.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='marcos', email='marcos.urbanski@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Marcos', email='marcos.urbanski@gmail.com'),
        Usuario(nome='Marcos2', email='marcos_urbanski@hotmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
