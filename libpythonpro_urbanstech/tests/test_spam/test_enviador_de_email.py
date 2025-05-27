from libpythonpro_urbanstech.spam.enviador_de_email import Enviador, EmailInvalido
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'marcos.urbanski@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'marcos_urbanski@hotmail.com',  # remetente
        'Cursos Python Pro',            # assunto
        'Primeira turma Guido Von Rossum aberta.'  # corpo do email
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'marcos']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'marcos_urbanski@hotmail.com',  # destinatário
            'Cursos Python Pro',            # assunto
            'Primeira turma Guido Von Rossum aberta.'  # corpo do email
        )
