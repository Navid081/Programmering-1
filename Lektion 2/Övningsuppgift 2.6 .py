import math

print('Hur många elever vill ha...')
van2 = 2 * int(input('två vanliga korvar: '))
van3 = 3 * int(input('tre vanliga korvar: '))
veg2 = 2 * int(input('två veganska korvar: '))
veg3 = 3 * int(input('tre veganska korvar: '))
dryck = int((van2 / 2) + (van3 / 3) + (veg2 / 2) + (veg3 / 3))

antal_van_korvar = van2 + van3
antal_veg_korvar = veg2 + veg3

antal_van_pkt = math.ceil(antal_van_korvar / 8)
antal_veg_pkt = math.ceil(antal_veg_korvar / 4)

print('.' * 25)
print('-' 'INKÖPSLISTA', '-')
print('.' * 25)
print('Vanlig korv: ', antal_van_pkt, 'förpackningar')
print('Vegansk korv: ', antal_veg_pkt, 'förpackningar')
print('Antal dricka: ', dryck, 'drickor')
print('-' * 25)

summa_van = antal_van_pkt * 20.95
summa_veg = antal_veg_pkt * 34.95
summa_dryck = dryck * 13.95

print('Kostnaden för vanliga korvar: ', summa_van, 'kr')
print('Kostnaden för veganska korvar: ', summa_veg, 'kr')
print('Kostnaden för drickor: ', summa_dryck, 'kr')
print('Total kostnaden: ', summa_van + summa_veg + summa_dryck, 'kr')
