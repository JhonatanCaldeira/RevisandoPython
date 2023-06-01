from classes.NotificacaoEmail import NotificacaoEmail
from classes.NotificacaoSMS import NotificacoSMS
from classes.Notificacao import Notificacao


def notificar(notificacao: Notificacao):
    notificacao.enviar()


sms = NotificacoSMS('qqch')
notificar(sms)

email = NotificacaoEmail('qqch')
notificar(email)
