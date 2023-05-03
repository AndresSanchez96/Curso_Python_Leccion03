print('Sistema de calificaciones')
nota = float(input('Digita la calificacion (0-10): '))
calificacion = None
if 9 <= nota <= 10:
    calificacion = 'A'
elif 8 <= nota < 9:
    calificacion = 'B'
elif 7 <= nota < 8:
    calificacion = 'C'
elif 6 <= nota < 7:
    calificacion = 'D'
elif 0 <= nota < 6:
    calificacion = 'F'
else:
    calificacion = 'Valor incorrecto'

print(f'Tu calificacion es: {calificacion}')