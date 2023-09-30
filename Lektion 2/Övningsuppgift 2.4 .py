age = int(input('Hur gammal är du: '))

if age < 18:
    print('Du är myndig om', 18 - age, 'år!')

else:
    print('Du är redan myndig')