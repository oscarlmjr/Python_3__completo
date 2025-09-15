from abc import ABC, abstractmethod


class Notificacao(ABC):
	def __init__(self, mensagem) -> None:
		self.mensagem = mensagem

	@abstractmethod
	def enviar(self) -> bool:
		print(__class__.__name__)
		...


class NotificacaoEmail(Notificacao):
	def enviar(self) -> bool:
		print('E-mail: enviando:', self.mensagem)
		return True


class NotificacaoSMS(Notificacao):
	def enviar(self) -> bool:
		print('SMS: enviando - ', self.mensagem)
		return True

# def notificar(notificacao: str):
def notificar(notificacao: Notificacao):
	notificacao_enviada = notificacao.enviar()

	if notificacao_enviada:
		print('Notificação enviada')

	else:
		print('Notificação NÃO enviada')

notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)
