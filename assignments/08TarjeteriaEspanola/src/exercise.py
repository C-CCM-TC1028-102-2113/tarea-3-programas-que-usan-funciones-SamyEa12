
def main():
    #escribe tu código abajo de esta línea
    def tarjetas(x, y):
        tppl=x*12
        tpp=y*35
        if tppl >= tpp:
            return tpp
        elif tppl <= tpp:
            return tppl
    
    pl=int(input("Dame la cantidad de pliegos de papel albanene: "))
    p=int(input("Dame la cantidad de plumones: "))
    print("El número máximo de tarjetas que se pueden hacer es: " + str(tarjetas(pl, p)))
    pass

if __name__=='__main__':
    main()
