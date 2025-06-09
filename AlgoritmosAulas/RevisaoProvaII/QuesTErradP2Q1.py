# Entrada dos dados
pA = float(input("População do país A (em mil): "))
pB = float(input("População do país B (em mil): "))
tA = float(input("Taxa de crescimento anual do país A (%): "))
tB = float(input("Taxa de crescimento anual do país B (%): "))

# Verificações básicas
if pA >= pB:
    print("A população do país A já é maior ou igual à do país B.")
elif tA <= tB:
    print("A população do país A nunca ultrapassará a do país B com uma taxa de crescimento menor ou igual.")
else:
    anos = 0
    while pA <= pB:
        pA += pA * (tA / 100)
        pB += pB * (tB / 100)
        anos += 1
    print(f"\nA população do país A ultrapassará a do país B em {anos} anos.")
