print('Etapas de la vida ')
edad = int(input('Digita tu edad: '))
etapa = None
if edad > 0 and edad <= 10:
    etapa = 'La infancia es increible...'
elif edad > 10 and edad <= 20:
    etapa = 'Muchos cambios y mucho estudio...'
elif edad > 20 and edad <= 30:
    etapa = 'Amor y comienza el trabajo...'
else:
    etapa = 'Etapa de vida no reconocida'

print(f'Tu edad de {edad} años esta en la etapa de {etapa}')