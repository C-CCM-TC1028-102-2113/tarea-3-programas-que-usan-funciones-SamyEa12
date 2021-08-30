
def main():
    #escribe tu código abajo de esta línea
    def area(x,y):
        a=x*y
        return a
        
    def volumen(z):
        v=z*area(b,h)
        return v

    b=float(input("Dame la base: "))
    h=float(input("Dame la altura: "))
    p=float(input("Dame la profundidad: "))
    print("El volumen del prisma es: " + str(volumen(p)))

    pass

if __name__=='__main__':
    main()
