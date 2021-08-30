
def main():
    #escribe tu código abajo de esta línea
    def es_bisiesto(x):
        if x%400==0 and x%4==0 and x%100==0:
            return "True"
        elif x%4==0 and x%100==0:
            return "False"
        elif x%4==0:
            return "True"
        else:
            return "False"

    año=int(input())
    print(es_bisiesto(año))
    
    pass

if __name__=='__main__':
    main()
