import random
import requests

dc = "https://discord.com/gifts/"
lett = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open('nitro.txt', 'w') as f:
    for _ in range(int(input("Introduce los codigos que quieres que genere: "))):
        code1 = ''.join(random.sample(lett, 16))
        gifts = dc + code1

        try:
            response = requests.get(gifts)
            if response.status_code == 202:
                print(f"¡Código válido! {gifts}")
                f.write(gifts + '\n')
            else:
                print(f"Código no válido: {gifts} (Status code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error al comprobar el código: {e}")
