from libpythonpro_urbanstech.spam.enviador_de_email import Enviador
from libpythonpro_urbanstech.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'marcos.urbanski@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
