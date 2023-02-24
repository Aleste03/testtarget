def main():
    strInput = input("Entre com a palavra: ")

    start, end = 0, len(strInput) - 1

    while start < end:
        temp = strInput[end]
        strInput = strInput[:end] + strInput[start] + strInput[end + 1:]
        strInput = strInput[:start] + temp + strInput[start + 1:]
        start += 1
        end -= 1

    print(f"A palavra invertida é: {strInput}")


if __name__ == "__main__":
    main()


