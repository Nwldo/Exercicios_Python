def verificar_valor(valor):
    if valor is None:
        raise ValueError("O valor não pode ser None")
    else:
        print("O valor é válido")

try:
    verificar_valor(None)
except ValueError as e:
    print(f"Erro: {e}")