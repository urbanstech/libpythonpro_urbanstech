from unittest.mock import Mock
from libpythonpro_urbanstech.spam.enviador_de_email import Enviador
from libpythonpro_urbanstech.spam.main import EnviadorDeSpam
from libpythonpro_urbanstech.spam.modelos import Usuario
import pytest


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Marcos', email='marcos.urbanski@gmail.com'),
            Usuario(nome='Marcos2', email='marcos_urbanski@hotmail.com')
        ],
        [
            Usuario(nome='Marcos', email='marcos.urbanski@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'marcos.urbanski@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Marcos', email='marcos.urbanski@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'luciano@gmail.com',
        'marcos.urbanski@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
