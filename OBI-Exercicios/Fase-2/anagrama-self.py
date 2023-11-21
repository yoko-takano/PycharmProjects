frase1 = str(input("Primeira: "))
frase2 = str(input("Segunda: "))

# Tratamento das strings
frase1abc = ''.join(sorted(frase1)).strip()
frase2abc = ''.join(sorted(frase2)).strip()
frase1abc = frase1abc.strip(".,")
frase2abc = frase2abc.strip(".,")

# Outputs
if frase1abc == frase2abc:
    print("Sim")
else:
    print("Não")

