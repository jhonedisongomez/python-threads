from threading import Thread, Semaphore
import time, random

# Hilo a arrancar
class MiHilo(Thread):
    # Se le pasa un numero identificador del hilo y un semaforo
    def __init__(self, numero_hilo, semaforo):
        Thread.__init__(self)
        self.semaforo=semaforo
        self.numero_hilo = numero_hilo
        
    def run(self):
        # Espera al semaforo
        semaforo.acquire()
        print "Entra hilo "+str(self.numero_hilo)
        # Pierde un tiempo aleatorio
        time.sleep(random.randrange(1,10,1))
        print "Fin hilo " + str(self.numero_hilo)
        # Pone verde el semaforo para el siguiente y
        # termina
        semaforo.release()          
        
if __name__ == '__main__':
    random.seed()
    # Semaforo que permite pasar a cinco simultaneamente
    semaforo = Semaphore(5)
    # Se arrancan diez hilos
    for i in range(0,10):
       hilo=MiHilo(i,semaforo)
       hilo.start()
       print "Arrancado hilo "+str(i)
