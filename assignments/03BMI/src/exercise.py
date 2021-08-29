def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
   if altura > 0 and peso > 0:
    imc = peso / altura ** 2
    if imc < 20:
        print("PESO BAJO:")
    elif imc < 25:
        print("NORMAL")
    elif imc < 30:
        print("SOBREPESO")
    elif imc < 40:
        print("OBESIDAD")
    else:
        print("OBESIDAD MORBIDA")
   else:
    print("Revisa tus datos, alguno de ellos es erróneo.")
    pass

if __name__=='__main__':
    main()
