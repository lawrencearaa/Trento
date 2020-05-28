from googletrans import Translator

#create translator object
trans = Translator()
t = trans.translate('Bom dia')

print(f'Source: {t.src}')
print(f'Destination: {t.dest}')
print(f'{t.origin} -> {t.text}')