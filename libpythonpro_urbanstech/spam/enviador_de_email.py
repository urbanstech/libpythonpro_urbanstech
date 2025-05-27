class Enviador:
    """
    Classe responsável por simular o envio de e-mails.
    Valida o endereço de e-mail do remetente antes de 'enviar'.
    """

    def enviar(self, remetente, destinatario, assunto, corpo):
        """
        Simula o envio de um e-mail.

        Parameters:
        remetente (str): Endereço de e-mail do remetente.
        destinatario (str): Endereço de e-mail do destinatário.
        assunto (str): Assunto do e-mail.
        corpo (str): Corpo do e-mail.

        Raises:
        EmailInvalido: Se o e-mail do remetente não for válido.

        Returns:
        str: O remetente do e-mail, caso o envio seja considerado válido.
        """
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente inválido: {remetente}')
        return remetente


class EmailInvalido(Exception):
    """
    Exceção personalizada usada para indicar que o e-mail do remetente é inválido.
    """
    pass
