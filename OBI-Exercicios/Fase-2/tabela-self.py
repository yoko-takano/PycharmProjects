#from sympy import symbols, solve
jogos, pontos, vitorias, empates, derrotas = [int(i) for i in input().split()]

if jogos == -1:
    jogos = vitorias + empates + derrotas
if pontos == -1:
    pontos = 3*vitorias + empates
if vitorias == -1:
    vitorias = jogos - empates - derrotas
if empates == -1:
    empates = jogos - vitorias - derrotas
if derrotas == -1:
    derrotas = jogos - vitorias - empates

print(f"{jogos} {pontos} {vitorias} {empates} {derrotas}")
