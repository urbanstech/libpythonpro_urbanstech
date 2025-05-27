from libpythonpro_urbanstech.spam.enviador_de_email import Enviador
from libpythonpro_urbanstech.spam.main import EnviadorDeSpam
from libpythonpro_urbanstech.spam.modelos import Usuario
import pytest


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'marcos.urbanski@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Marcos', email='marcos.urbanski@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'luciano@gmail.com',
        'marcos.urbanski@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
