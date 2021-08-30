
def main():
    #escribe tu código abajo de esta línea
    def area(x,y):
        a=x*y
        return a
    
    b=float(input("Dame la base: "))
    h=float(input("Dame la altura: "))
    print("El área del rectángulo es: " + str(area(b,h)))
    pass

if __name__=='__main__':
    main()
