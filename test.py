import libreria
assert (libreria.validar_partido("1")==False)
assert (libreria.validar_partido("1111")==False)
assert (libreria.validar_partido("Morado")==True)
assert (libreria.validar_partido("Amarillo")==True)
assert (libreria.validar_partido("Azul")==True)

print("validar partido --->OK")

assert (libreria.validar_nombre("j")==False)
assert (libreria.validar_nombre("Juan")==True)
assert (libreria.validar_nombre("12")==False)
assert (libreria.validar_nombre("NERY")==True)
assert (libreria.validar_nombre("Felipe")==True)
print("validar nombre --->OK")

assert (libreria.validar_aplicacion("messenger")==True)
assert (libreria.validar_aplicacion("whatssap")==True)
assert (libreria.validar_aplicacion("facebook")==True)
assert (libreria.validar_aplicacion("1234")==False)
assert (libreria.validar_aplicacion("987654")==False)
print("validar aplicacion---> ok")


assert (libreria.validar_numero_tel("95478623")==False)
assert (libreria.validar_numero_tel("954786234")==True)
assert (libreria.validar_numero_tel("aaaaaaa")==False)
assert (libreria.validar_numero_tel("123456789")==True)
assert (libreria.validar_numero_tel("9547811145664")==False)
print("validar numero telefonico ---> OK ")



assert (libreria.validar_resultado("12")==True)
assert (libreria.validar_resultado("20")==True)
assert (libreria.validar_resultado("AZUL")==False)
assert (libreria.validar_resultado("a24")==False)
assert (libreria.validar_resultado("AAAA")==False)
print("validar resultado --->OK")
