import time
from win10toast import ToastNotifier 

def conftiempo(): 
    hora = int(input("Horas :")) 
    minutos = int(input("Minutos :")) 
    segundos = int(input("Segundos :")) 
    tiempo_total = segundos+((minutos*60)-300)+(hora*3600) 
    return tiempo_total 
  
def notif(): 
    notificacion = ToastNotifier() 
    notificacion.show_toast("Reunión virtual en 5 minutos") 
    return 0
  
def tiempoinicio(intervalo_tiempo): 
    while True: 
        time.sleep(intervalo_tiempo) 
        notif() 
    
if __name__ == '__main__': 
    intervalo_tiempo = conftiempo() 
    tiempoinicio(intervalo_tiempo)