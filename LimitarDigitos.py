# Erick Hernandez
# Forma clasica
clasica = 49.568789
print("Manera clasica: %.2f" % clasica)  # Nomas 2 puntos ponemos

# Usando el .format()
f = 78.563254
print("Manera con el .format():", ("{0:.2f}".format(f)))

# Usando el metodo round()
h = round(158.45985, 2)  # Se pone cuantos decimales va a mostrar y el numero primero
print("Metodo round:", h)

# Usando el metodo .format() de manera directa
a = 15.123456
print("Metodo .format() de manera directa:", format(a, ".3f"))

# Usando F-String la mas nueva
new = 98.56789
print(f"Manera mas nueva(F-String): {new:.3f}")  # No nos olvidemos de la f al principio

print("\nAhora vemos con strings\n")

# Forma clasica
s = "Hola Mundo esto es Python"
print("Manera clasica: %.4s" % s)

# Metodo string-slicing
print("String-slicing: {0:.7s}".format(s))

# Metodo mas nuevo
print("Metodo mas nuevo:", format(s, ".13s"))