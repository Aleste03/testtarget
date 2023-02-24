def main():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "OUTROS": 19849.53
    }

    soma = sum(map(lambda x: float(x), faturamento.values()))

    for uf, valor in faturamento.items():
        porcentual = (valor / soma) * 100
        print(f"{uf} – {porcentual:3.2f}%")


if __name__ == "__main__":
    main()


