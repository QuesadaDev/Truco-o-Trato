import random

personas = [
    {"nombre": "Juan", "edad": 25, "altura": 175},
    {"nombre": "María", "edad": 30, "altura": 160},
    {"nombre": "Pedro", "edad": 22, "altura": 180}
]

sustos = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
dulces = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]


def calc_letras(lista_letras):

    total_letras = sum(map(lambda persona: len(persona['nombre']) // 2, lista_letras))
    return total_letras


def calc_par(lista_par):

    total_par = len(list(filter(lambda edad: edad['edad'] % 2 == 0, lista_par)))
    return total_par


def calc_alt(lista_altura):

    tot_alt = sum(map(lambda persona: persona['altura'], lista_altura))
    return tot_alt


def calc_letras_dulces(lista_letras):

    total_letras = sum(map(lambda persona: len(persona['nombre']), lista_letras))
    return total_letras


def calc_age(lista_edad):

    dulce_edad = sum(list(map(lambda persona: 3 if persona['edad'] >= 10 else persona['edad'] // 3, lista_edad)))
    return dulce_edad


def calc_altura(lista_edad):

    dulces_altura = sum(list(map(lambda persona: 3 if persona['altura'] >= 150 else persona['altura'] // 50, lista_edad)))
    return dulces_altura


def suma_sustos(lista_sustos):
    sustos_letras = calc_letras(lista_sustos)
    sustos_par = calc_par(lista_sustos) * 2
    sustos_altura = calc_alt(lista_sustos) / 100 * 3

    total_sustos = sustos_letras + sustos_par + sustos_altura

    for i in range(int(total_sustos)):
        print(random.choice(sustos), end=" ")


def suma_dulces(lista_dulces):
    dulces_letras = calc_letras_dulces(lista_dulces)
    dulces_age = calc_age(lista_dulces)
    dulces_altura = calc_altura(lista_dulces) * 2

    total_dulces = dulces_letras + dulces_age + dulces_altura

    for i in range(int(total_dulces)):
        print(random.choice(dulces), end=" ")


def accion(tru_tra, lista):

    if tru_tra == "Truco":
        suma_sustos(lista)

    elif tru_tra == "Trato":
        suma_dulces(lista)


act = input("Truco o Trato: ").lower().capitalize()
accion(act, personas)


