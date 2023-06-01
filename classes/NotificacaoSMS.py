from classes.Notificacao import Notificacao


class NotificacoSMS(Notificacao):

    def enviar(self) -> bool:
        print('SMS: Enviando - ', self.mensagem)
        return True
