def main():
    intInput = int(input("Entre com numero:"))

    num0, num1, num2 = 0, 1, 1

    if intInput in set([num0, num1, num2]):
        print("Pertence a sequencia")

    while num0 < intInput:
        num0 = num1 + num2
        num2 = num1
        num1 = num0

    if num0 == intInput:
        print("Pertence a sequencia")
    else:
        print("NÃO Pertence a sequencia")


if __name__ == "__main__":
    main()


