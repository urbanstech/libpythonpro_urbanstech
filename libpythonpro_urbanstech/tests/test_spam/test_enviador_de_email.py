from libpythonpro_urbanstech.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado  = enviador.enviar(
        'marcos.urbanski@gmail.com',
        'marcos_urbanski@hotmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert 'marcos.urbanski@gmail.com' in resultado
