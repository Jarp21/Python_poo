from unicodedata import name


def run():
    print(f(1000))

def f(x):
    respuesta = 0

    # 1000 conteos
    for i in range(1000):
        respuesta += 1

    # x conteos
    for i in range(x):
        respuesta += x

    # 2x^2 conteos
    for i in range(x):
        for i in range(x):
            respuesta += 1
            respuesta += 1

    return respuesta

if __name__ == "__main__":
    run()