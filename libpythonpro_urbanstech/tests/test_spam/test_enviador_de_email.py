from libpythonpro_urbanstech.spam.test_enviador_de_email import Enviador

def test_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None