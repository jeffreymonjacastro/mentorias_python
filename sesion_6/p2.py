# For

adn = input("Ingrese su cadena de ADN:")

# Comment
"""
Comment:
A -> T
C -> G
T -> A
G -> C
"""

new_adn = ""

# Iterando por los elementos de A
# for i in adn:
#     if i == "A":
#         new_adn += "T"
#     elif i == "C":
#         new_adn += "G"
#     elif i == "T":
#         new_adn += "A"
#     elif i == "G":
#         new_adn += "C"

# Iterando por índices
for i in range(len(adn)):
    if adn[i] == "A":
        new_adn += "T"
    elif adn[i] == "C":
        new_adn += "G"
    elif adn[i] == "T":
        new_adn += "A"
    elif adn[i] == "G":
        new_adn += "C"


print(f"La copia de ADN es: {new_adn}")

