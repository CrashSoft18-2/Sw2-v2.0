import base64
import os

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def getCantidadDias(hoy, target):
    print(target, hoy)
    if target < hoy:
        cantidad_de_dias = 6 - target
    elif target > hoy:
        cantidad_de_dias = target - hoy
    else:
        cantidad_de_dias = 7
    return cantidad_de_dias
