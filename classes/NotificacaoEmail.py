from classes.Notificacao import Notificacao


class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool:
        print('E-mail: Enviando - ', self.mensagem)
        return True
