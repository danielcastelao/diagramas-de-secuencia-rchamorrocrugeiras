class Second:
    def mensaje(self):
        print("Second: procesando mensaje()")

        valor_retorno = "Hola desde Second"
        return valor_retorno


def main():
    print("Main: iniciando interacción")

    second = Second()

    respuesta = second.mensaje()

    print("Main: valor retornado ->", respuesta)


if __name__ == "__main__":
    main()