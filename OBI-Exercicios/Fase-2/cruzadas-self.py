# Inputs
horizontal = list(str(input("Digite a palavra horizontal: ")))
vertical = list(str(input("Digite a palavra vertical: ")))
tamHorizontal = len(horizontal)-1
tamVertical = len(vertical)-1

# Desenvolvimento
posHorizontal = -1
posVertical = -1
for i in range(tamHorizontal, -1, -1):
    for j in range(tamVertical, -1, -1):
        if vertical[j] == horizontal[i]:
            posVertical = j+1
            posHorizontal = i+1
        if posVertical != -1 and posHorizontal != -1:
            break
    if posVertical != -1 and posHorizontal != -1:
        break

# Outputs
print(posHorizontal, posVertical)
