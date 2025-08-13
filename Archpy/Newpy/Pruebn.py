precios_frutas={"Platano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
fruta_deseada=input("Desea alguna Fruta?(Platano, Manzana, Pera, Naranja): ").capitalize()
if fruta_deseada in precios_frutas:
    try:
      kilos=float(input(f"Cuantos kilos de {fruta_deseada} necesita? "))
      precio_total=precios_frutas[fruta_deseada]* kilos
      print(f"El precio total de {kilos} kilos de {fruta_deseada} es: ${precio_total:.2f}")
    except ValueError:
        print("Por favor, ingrese una cantidad de kilos valida.")
else:
    print(f"Lo siento, la fruta {fruta_deseada} no se encuentra en la lista.")
