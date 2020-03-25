#Juan Manuel Valencia
km_distancia=0
min_vuelo=0
mod_tiquete=(1,2,3)
n_maletas_a=0
t_vuelo=(n,i)
def f_calculoBase1(mod_tiquete):
    km_viajados=int(input("Ingrese el número de Km del vuelo"))
    min_vuelo=int(input("Ingrese el número de minutos del vuelo"))
    if mod_tiquete==1:
        valor_base=55000*((km_viajados)/100)
        print(valor_base)
    elif mod_tiquete==2:
        valor_base=(km_viajados/70)*25000+(min_vuelo/30)*10000
        print(valor_base)
    elif mod_tiquete==3:
        valor_base=((km_viajados/50)*25000)+(min_vuelo/60)*10000
        print(valor_base)
def f_costoAdicional():
    mod_tiquete=(int(input("Ingrese el tipo de tiquete que desea adquirir 1 ,2 o 3")
    n_maletas_a=(int(input("Ingrese el número de maletas adicionales que desea llevar")
    t_vuelo=(int(input("Ingrese el tipo de vuelo "n" nacional o "i" internacional")
    if 
                     
    
        
    
    
