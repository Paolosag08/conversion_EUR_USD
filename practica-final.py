tipo_conversion_EUR_MXN = 23.70
tipo_conversion_USD_MXN = 20.75

tipo_conv = input('Ingrese el tipo de cambio(EUR/USD): ')
tipo = tipo_conv.upper()

monto = float(input('Ingrese el monto a convertir: '))

if tipo == 'EUR':
    conversion = tipo_conversion_EUR_MXN * monto
    print('El resultado es: ', conversion, 'MXN')
elif tipo == 'USD':
    conversion = tipo_conversion_USD_MXN * monto
    print('El resultado es: ', conversion, 'MXN')
else:
    print('La conversion no esta disponible.')