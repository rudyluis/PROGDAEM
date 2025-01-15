# 2do principio: agregar nuevas funcionalidades sin cambiar el codigo fuente
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por email a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")

class NotificadorWhatsapp(Notificador):
    def notificar(self):
        print(f"Enviando Whatsapp a {self.usuario.whatsapp}")

class NotificadorTwitter(Notificador):
    def notificar(self):
        print(f"Enviando twit a {self.usuario.twitter}")
