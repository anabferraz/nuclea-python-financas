import re
resultado_validacao = True

def valida_rg():

    padrao_rg = r'\d{2}\.\d{3}\.\d{3}-\d{1}$'

    while True:
        rg = input("RG: ")
        rg_formatado = f"{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}"
        if re.match(padrao_rg, rg_formatado):
            return rg_formatado
        else:
            print("RG inválido. Tente novamente.")

if __name__ == "__main__":
    valida_rg()

