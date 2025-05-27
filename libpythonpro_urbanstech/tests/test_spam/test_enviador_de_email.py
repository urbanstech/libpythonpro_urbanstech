from libpythonpro_urbanstech.spam.enviador_de_email import Enviador, EmailInvalido
import pytest


def test_criar_enviador_de_email():
    """
    Testa se o objeto Enviador é criado corretamente.
    
    Cria uma instância do Enviador e verifica se ela não é None.
    Isso garante que a classe Enviador pode ser instanciada com sucesso.
    """
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'marcos.urbanski@gmail.com']
)
def test_remetente(destinatario):
    """
    Testa o envio de email para destinatários válidos.
    
    Este teste usa o decorador @pytest.mark.parametrize para testar o mesmo comportamento
    com múltiplos valores de entrada (neste caso, dois emails válidos como destinatários).
    
    Verifica se o destinatário aparece no resultado da função enviar().
    """
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
    """
    Testa o envio de email com remetente inválido.
    
    Aqui usamos novamente o @pytest.mark.parametrize para testar dois cenários:
    - remetente vazio
    - remetente sem formato de email válido
    
    O teste espera que a exceção EmailInvalido seja lançada.
    Isso valida a regra de que o remetente precisa ter um formato de email válido.
    """
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'marcos_urbanski@hotmail.com',  # destinatário
            'Cursos Python Pro',            # assunto
            'Primeira turma Guido Von Rossum aberta.'  # corpo do email
        )
