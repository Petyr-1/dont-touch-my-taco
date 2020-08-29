'''
Petyr Notario
29/05/2020
'''
asiasi = ""
tempo1 = 0
ciclo1 = 0
operador_s = 0

for p in [0, 1, 2, 3, 4]:
    palanca = "palanca{0}".format(p) + ".txt"
    escribir = open("E:\\DocumentosII\\Python\\calculadora\\{0}".format(palanca),"w")
    escribir.write("Petyr Notario\n")

archivo = open("E:\\DocumentosII\\Python\\calculadora\\tabla.txt","w")
archivo.write('Petyr Notario\n')

palanca0 = open("E:\\DocumentosII\\Python\\calculadora\\palanca0","a")
palanca1 = open("E:\\DocumentosII\\Python\\calculadora\\palanca1","a")
palanca2 = open("E:\\DocumentosII\\Python\\calculadora\\palanca2","a")
palanca3 = open("E:\\DocumentosII\\Python\\calculadora\\palanca3","a")
palanca4 = open("E:\\DocumentosII\\Python\\calculadora\\palanca4","a")
archivo = open("E:\\DocumentosII\\Python\\calculadora\\tabla.txt","a")

def valor1_f(valorado): #Funcion que crea los numeros en binario y luego los pasa por reparador
    valor = bin(valorado)
    valor = reparador(valor)
    return valor
def reparador(v1): #función que se encarga de transformar numeros en formato bin...
                   #... a un formato conveniete para mi. de la forma "0b1" a la forma "0001" por ejemplo
    v1 = v1[2:]   #v1 significa "valor1" y lon significa "longitud"
    lon = len(v1)
    if (lon < 4): #Este if se encarga de comprobar la longitud de caracteres del valor1 y agregarle los 0 necesarios para obtener 4 caracteres.
        if(lon == 3):
            v1 = '0' + v1
        elif(lon == 2):
            v1 = '00' + v1
        elif(lon == 1):
            v1 = '000' + v1
    return v1    #La salida de esta función sera el valor que obtenga v1
def resultado_f(valor1, valor2, operador): #Funcion encargada de hacer una operacion con los dos valores y devolver su resultado en binario
    valor1 = int(valor1, 2) #Convertimos en entero ambos valores que antes estaban en binario
    valor2 = int(valor2, 2)
    operacion = 0
    if (operador == "00"): #Este if se encarga de determinar que operación será realizada en base al codigo del operador creador por la funcion operador
        operacion = valor1 + valor2
    elif (operador == "01"):
        operacion = valor1 - valor2
    elif (operador == "10"):
        operacion = valor1 * valor2
    operacion = bin(operacion) #convertimos el resultado en decimal a binario
    operacion = reparador(operacion) #Pasamos el resultado en binario por la funcion reparador que se encarga de quitar 0b y si es requerido agregar 0
    return operacion
def operador_f(operador_s): #Funcion encargada de crear el codigo de operador basado en un while que se repite 3 veces
    operador_s = bin(operador_s) #Pasamos el valor del while mencionado a binario
    operador_s = operador_s[2:]
    if (len(operador_s) < 2): #Este if y la declaracion de arriba hacen algo similar a la funcion reparar
        operador_s = '0' + operador_s
    return operador_s
def selector(pin, codigo_activador):
    if (pin == 0):
        palanca0.write(codigo_activador)
    elif (pin == 1):
        palanca1.write(codigo_activador)
    elif (pin == 2):
        palanca2.write(codigo_activador)
    elif (pin == 3):
        palanca3.write(codigo_activador)
    elif (pin == 4):
        palanca4.write(codigo_activador)
#def agrupador(pin, estado): #Función que agrupa a los resultados en un documento de acuerdo a la salida activada y a la combinación que la activa
#    estado = estado[pin]
#    if (estado == "1"):
#        palanca = i

while operador_s < 3: #Este while hace que todo se repita 3 veces para realizar las 3 operaciones (suma, resta y multiplicación)
    while tempo1 < 16: #Subciclo que repite 16 veces el sub sub ciclo
        while ciclo1 < 16: #sub sub ciclo que repite 16 veces las funciones credas y a la vez escribe todos los resultados el documento
            valor1 = valor1_f(tempo1) #Se ocupa la función para la cuenta repetida
            valor2 = valor1_f(ciclo1) #Se ocupa la funcion para la cuenta seguida repetida
            operador = operador_f(operador_s) #Se convierte nuestro valor del while arriba en un codifo de operador binario
            resultado = resultado_f(valor1, valor2, operador) #Se hace la operacion, usando los dos valores y el codigo de operador
            archivo.write(valor1 + operador + valor2 + resultado + "\n") #Todos los datos se almacenan/escriben en el documento
            ciclo1 += 1
            print("ciclo1: %s" %(ciclo1))
        ciclo1 = 0
        tempo1 += 1
        print("tempo1: %s" %(tempo1))
    tempo1 = 0
    operador_s += 1
    print("operador_s: %s" %(operador_s))
print(asiasi)

#29/05/2020, 30/05/2020, 31/05/2020
