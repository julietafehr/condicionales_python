# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print(f"{texto_1} es mayor alfabeticamente que {texto_2}")
else:
    print(f"{texto_2} es mayor alfabeticamente que {texto_1}")


# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables. 
int(texto_1)
int(texto_2)

copia_texto_1 = texto_1
copia_texto_2 = texto_2


# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
if copia_texto_1 > copia_texto_2:
    print(f"{copia_texto_1} es mayor a {copia_texto_2}")
else:
    print(f"{copia_texto_2} es mayor a {copia_texto_1}")


# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
