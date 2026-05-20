from observer_practice.canal import CanalNoticias
from observer_practice.suscriptores import SuscriptorEmail, SuscriptorSMS

# Crear canal
canal = CanalNoticias("Noticias Principales")

# Crear suscriptores
ana = SuscriptorEmail("Ana")
luis = SuscriptorSMS("Luis")

# Suscribir al canal
canal.suscribir(ana)
canal.suscribir(luis)

# Publicar un mensaje
canal.publicar("Nueva noticia del día")

# Ver mensajes recibidos
print(ana.mensajes)
print(luis.mensajes)