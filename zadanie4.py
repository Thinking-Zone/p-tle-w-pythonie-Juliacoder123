tekst = input("Podaj ciąg znaków: ")
odwrocony = ""

# Odwrócenie ciągu znaków
for i in range(len(tekst) - 1, -1, -1):
    odwrocony += tekst[i]

print("Odwrócony ciąg znaków:", odwrocony)
