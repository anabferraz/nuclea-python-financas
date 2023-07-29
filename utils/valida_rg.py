import re

def valida_rg(rg):

    padrao_rg = r'\d{2}\.\d{3}\.\d{3}-\d{1}$'

    if re.match(padrao_rg,rg):
        True
    else:
        return False
rg = "00.000.000-0"

print (valida_rg(rg))