def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if x > y and y > z:
        print(z , y , x)
    elif  x > z and z > y:
        print(y , z , x)
    elif  y > x and x > z:
        print(z , x , y)
    elif  y > z and z > x:
        print(x , z , y)
    elif  z > x and x > y:
        print(y , x , z)
    elif  z > y and y > x:
        print(x , y , z)
    


if __name__=='__main__':
    main()
