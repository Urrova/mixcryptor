# -*- coding: UTF-8 -*-

'''
MixCryptor 1.1
You can use, study the code, modify and share modified copies of this program, according to the GNU GPL v3
'''

import re
import os
import sys
import random
from colorama import init, Fore, Back, Style
init(autoreset=True)

######################################################Settings#########################################################################################################

try:
    config = open("config.txt","r")
    readed = config.read()
    idioma = int(re.sub("lang=","",readed))
    config.close()
except FileNotFoundError:
    print(Fore.YELLOW+Style.BRIGHT+"Recuperation Mode (ERROR: the file \"config.txt\" cant be founded (1))")
    print("Creating config.txt...")
    config = open("config.txt","w")
    print("Writing config.txt...")
    config.write("lang=0")
    config.close()
    print("The program will close.")
    input()
    sys.exit()
except ValueError:
    print(Fore.YELLOW+Style.BRIGHT+"Recuperation Mode (ERROR: invalid value (2))")
    print("Opening config.txt...")
    config = open("config.txt","w")
    print("Repairing config.txt...")
    config.write("lang=0")
    config.close()
    print("The program will close.")
    input()
    sys.exit()
    

abc = "!\"#$%&'()*+, \n\t-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸŽžƒˆ˜"
'''
Idioma 0: ingles
Idioma 1: español
'''

mcencrypt = [Fore.YELLOW+Style.BRIGHT+"MixCryptor -- Encrypt",Fore.YELLOW+Style.BRIGHT+"MixCryptor -- Encriptar"]
ptftbe = [Fore.CYAN+Style.BRIGHT+"Put the directory of the file to be encrypted:",Fore.CYAN+Style.BRIGHT+"Escribe el directorio del archivo a encriptar:"]
fnferror = [Fore.RED+Style.BRIGHT+"ERROR: the file cant be founded (1)",Fore.RED+Style.BRIGHT+"ERROR: el archivo no pudo ser encontrado (1)"]
ptkd = ["Puts the key directory\nmix>","Escribe el directorio del archivo de claves\nmix>"]
encrypting = ["Encrypting...","Encriptando..."]
ptdtbs = ["Put the directory to save the encrypted file:\nmix>","Escribe el directorio a guardar el archivo encriptado:\nmix>"]
feass = [Fore.GREEN+Style.BRIGHT+"File encripted and saved sucessfully!",Fore.GREEN+Style.BRIGHT+"Archivo encriptado y guardado exitosamente!"]

mcdecrypt = [Fore.YELLOW+Style.BRIGHT+"MixCryptor -- Decrypt",Fore.YELLOW+Style.BRIGHT+"MixCryptor -- Desencriptar"]
ptdtbd = ["Put the directory of the file to be decrypted:\nmix>","Escribe el directorio del archivo a ser desencriptado:\nmix>"]
decrypting = ["Decrypting...","Desencriptando..."]
savedf = [Fore.GREEN+Style.BRIGHT+"File decrypted!\n\nPuts the directory to save the decrypted file:",Fore.GREEN+Style.BRIGHT+"Archivo desencriptado!\n\nEscribe el directorio a guardar el archivo desencriptado:"]
fdass = [Fore.GREEN+Style.BRIGHT+"File decrypted and saved sucessfully!!!",Fore.GREEN+Style.BRIGHT+"Archivo desencriptado y guardado con exito!!!"]

mckeygenerator= [Fore.YELLOW+Style.BRIGHT+"MixCryptor -- Key Generator",Fore.YELLOW+Style.BRIGHT+"MixCryptor -- Generador de Claves"]
ptdtstkf = ["Put the directory to save the key file:\nmix>","Escribe el directorio a guardar el archivo de claves:\nmix>"]
ptlotk = ["Put the lenght of the keys\nmix>","Escribe el largo de las claves\nmix>"]
generatingkeys = ["Generating keys...","Generando claves..."]
kgas = ["Key generated and saved!","Archivo de claves generado y guardado!"]

mccredits = [Fore.WHITE+Style.BRIGHT+'''CREDITS:
        Programming and cipher design: @URROVA.
        Programmed in Python.
        Thanks you for using this program!
        And if you type \"easterspam\"?''',Fore.WHITE+Style.BRIGHT+'''CREDITOS:
        Programacion y diseño del cifrado mix: @URROVA.
        Programado en Python.
        Gracias por usar este programa!
        Y si escribes \"easterspam\"?''']

easterspam = [Fore.BLUE+Style.BRIGHT+"Easter Spam, "+Fore.YELLOW+"and Easter eggs... "+Fore.WHITE+"Meh, a very bad joke :v",Fore.BLUE+Style.BRIGHT+"Easter Spam, "+Fore.YELLOW+"y Easter eggs... "+Fore.WHITE+"Ñah, un chiste muy malo :v"]
helped = ["\nPut \"help\" or \"list\" to show a list of commands.","\nEscribe \"help\" o \"list\" para ver una lista de comandos."]

InvalidError = [Fore.RED+Style.BRIGHT+"ERROR: invalid value (2)",Fore.RED+Style.BRIGHT+"ERROR: valor invalido (2)"]
wtderror = [Fore.RED+Style.BRIGHT+"ERROR: Insufficient quantity or variety of characters (3)",Fore.RED+Style.BRIGHT+"ERROR: Cantidad o variedad insuficiente de caracteres (3)"]
cuantosCaracteres = ["How many characters do you want? ","Cuantos caracteres quieres? "]
formatkey = [
    '''Choose the format of the keys:
1: Numbers from 0 to 9
2: Lowercase letters
3: Uppercase letters
4: Uppercase and lowercase letters
5: Random characters
6: Custom characters
mix>''','''Elige el formato de las claves:
1: Numeros del 0 al 9
2: Letras minusculas
3: Letras mayusculas
4: Letras mayusculas y minusculas
5: Caracteres aleatorios
6: Caracteres personalizados
mix>'''
    ]
clserror = [Fore.RED+Style.BRIGHT+"ERROR: Cant clear the screen (4)",Fore.RED+Style.BRIGHT+"Error: No se pudo limpiar la pantalla (4)"]
InexistentCommand = ["ERROR: Inexistent command (6)","ERROR: Comando inexistente (6)"]
######################################################Funciones########################################################################################################

#funcion para limpiar la pantalla
def clearScreen():
    #si esta en windows
    if os.name == "nt":
        os.system("cls")
    #si esta en linux/mac
    elif os.name == "posix":
        os.system("clear")
    #y si no...
    else:
        raise "I cant clean the screen"
        print  ("<-I cant clean the screen->")

#-----------------------------------------ENCRYPT----------------------------------------------------------------------------------------------------------------------

#funcion de encriptacion
def encrypt():
    global abc
    print(mcencrypt[idioma])
    #Pide la ruta del archivo a encriptar
    print(ptftbe[idioma])
    #entrada
    plaintext = ""
    ruta = str(input("mix>"))
    #inicializa un array con el abecedario
    #inicializa un array vacio para las claves
    key = []

    nums = ["0","1","2","3","4","5","6","7","8","9"]
    #String vacio para el texto cifrado
    ciphertext = ""

    #intenta abrir el archivo de la ruta ingresada
    try:
        f = open(ruta, "r")
    #si no existe retorna
    except FileNotFoundError:
        print(fnferror[idioma])
        input()
        return
    #lee el contenido
    contenido = f.read()
    #Y sigue leyendo el contenido hasta que no haya nada
    while contenido != "":
        plaintext += contenido
        contenido = f.read()
    f.close()

    #Pide la ruta del archivo de la clave
    rutakey = input(ptkd[idioma])
    #Intenta abrirlo
    try:
        keyfile = open(rutakey,"r")
    #Si no existe retorna
    except FileNotFoundError:
        print(fnferror[idioma])
        input()
        return

    #Va poniendo cada una de las claves
    indd = 0
    for line in keyfile:
        linee = re.sub("\n","",line)
        if indd == 0:
            keyleng = int(linee)
            indd+=1
            continue
        key.append(linee)
        indd +=1
    #Cierra el archivo
    keyfile.close()

    #Declarando las partes de string
    parts = []
    jj = 0
    while jj < keyleng:
        parts.append("")
        jj+=1

    print(encrypting[idioma])
    #proceso
    longitud = len(plaintext)
    #I son las letras del texto plano
    i = 0

    #Loop hasta que i sea mayor o igual a la longitud del string
    while i < longitud:
        #Caracter es igual al caracter en la posicion "i" en plaintext
        caracter = plaintext[i]
        #J son las letras del abc
        j = 0
        abclong = len(abc)
        #Itera sobre las letras del abc
        while j < abclong:
            #Si combino con una letra del abecedario
            if plaintext[i] == abc[j]:
                #Divide la clave en index "j" en tres partes y se las suma a p1, p2 y p3
                kk = 0
                while kk < keyleng:
                    temppart = parts[kk]+key[j][kk]
                    parts[kk] = temppart
                    kk+=1
            #Suma uno a j
            j+=1
        #Suma uno a i
        i+=1

    #Junta las partes del texto cifrado
    ciphertext = ""
    ll = 0
    while ll < keyleng:
        ciphertext +=parts[ll]
        ll+=1
    #salida

    #Pide una ruta de guardado
    ruta_guardado = str(input(ptdtbs[idioma]))

    #Guarda
    savefile = open(ruta_guardado,"w")
    savefile.write(ciphertext)
    savefile.close()

    clearScreen()
    #Muestra que el texto ya ha sido cifrado y hace una pausa
    print(feass[idioma])

    input()

#-------------------------------------------DECRYPT--------------------------------------------------------------------------------------------------------------------
def decrypt():

    #setup
    #Inicializa el array del abc
    global abc
    #Array vacio para cargar las claves
    key = []
    #entrada
    print(mcdecrypt[idioma])
    #Pide una ruta de un archivo encriptado
    ruta = input(ptdtbd[idioma])
    #Intenta abrirlo
    try:
        cipherfile = open(ruta,"r")
    #Si no existe retorna
    except FileNotFoundError:
        print(fnferror[idioma])
        input()
        return
    #Lee el archivo cifrado
    ciphertext = cipherfile.read()
    #Cierra cipherfile
    cipherfile.close()
    #Inicializa un string vacio "Plaintext"
    plaintext = ""

    #Pide la ruta del archivo de claves
    rutakey = input(ptkd[idioma])
    #Intenta abrirlo
    try:
        keyfile = open(rutakey,"r")
    #Si no existe retorna
    except FileNotFoundError:
        print(fnferror[idioma])
        input()
        return

    #Va poniendo cada una de las claves
    indd = 0
    for line in keyfile:
        linee = re.sub("\n","",line)
        if indd == 0:
            keyleng = int(linee)
            indd+=1
            continue
        key.append(linee)
        indd +=1
    #Cierra el archivo
    keyfile.close()

    #proceso
    
    #Inicializa 3 punteros, que van tomanndo los numeros como claves, el puntero 1 es 0, el puntero 2 es el largo de ciphertext dividido tres, el puntero
    #tres es (el largo de ciphertext dividido tres) multiplicado por dos
    parts = []
    aa = 0
    while aa < keyleng:
        parts.append((len(ciphertext)/keyleng)*aa)
        aa+=1

    print(decrypting[idioma])
    #Queria hacer que muestre el porcentaje, pero vi que la escritura de mensajes en la pantalla ralentizaba la desencripcion
    porcentaje = "0"
    #Mientras p3 sea menor o igual al largo de ciphertext
    while parts[-1] <= len(ciphertext):
        #Elije tres numeros aleatorios (ej 0, 3 y 1) y los junta en un string (los numeros esos ya eran strings.
        #El ejemplo quedaria 031), almacena el valor en "keytouse"
        try:
            keytouse = ""
            bb = 0
            while bb < len(parts):
                keytouse+= ciphertext[int(parts[bb])]
                bb+=1
        except IndexError:
            break

        ind = 0
        #Itera en key hasta que se tope con un valor igual a keytouse
        while ind < len(key):
            #Si keytouse coincidio con key en el indice "ind"
            if keytouse == key[ind]:
                #Le suma la letra correspontiente de abc en el indice ind
                plaintext+=abc[ind]
                #Sale del loop infinito
                break
            ind +=1
        #Todos los punteros suman uno
        cc = 0
        while cc < len(parts):
            parts[cc]+=1
            cc+=1
    #Limpia la pantalla
    clearScreen()
    #Muestra el contenido y pide una ruta para guardar el archivo
    print(savedf[idioma])
    saveruta = input("mix>")
    savefile = open(saveruta, "w")
    savefile.write(plaintext)
    savefile.close()
    clearScreen()
    #Dice que lo desencripto con exito y espera
    print(fdass[idioma])

    input()


#-----------------------------------------------------KEY GENERATOR----------------------------------------------------------------------------------------------------
def keyGenerate():

    #GLobalizar el array del abc
    global abc
    #En este array se guardaran los numeros aleatorios generados en formato string
    key = []

    def randomNums():
        arr = []
        cantidad = int(input(cuantosCaracteres[idioma]+ "(<"+str(len(abc))+")\nmix>"))
        while len(arr) < 50:
            toput = abc[random.randint(0,len(abc)-1)]
            j=0
            continuar = False
            if toput == "\n":
                continue
            while j < len(arr)-1:
                if toput == arr[j]:
                    continuar = True
                j+=1
            if continuar:
                continue
            arr.append(toput)
        return arr

    def azminNums():
        return "abcdefghijklmnñopqrstuvwxyz"
    def azmayNums():
        return "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    def azmixNums():
        return "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
    def numsNums():
        return "0123456789"
    def customNums():
        return input("Input the characters you want\nmix>")

    #String de numeros para elegir aleatoriamente
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    print(mckeygenerator[idioma])
    #Pide la ruta de guardado del archivo de claves
    ruta = input(ptdtstkf[idioma])
    #Pide la longitud de cada clave
    leng = int(input(ptlotk[idioma]))

    carand = input(formatkey[idioma])
    if carand == "1":
        nums = numsNums()
    elif carand == "2":
        nums = azminNums()
    elif carand == "3":
        nums = azmayNums()
    elif carand == "4":
        nums = azmixNums()
    elif carand == "5":
        nums = randomNums()
    elif carand == "6":
        nums = customNums()
    else:
        print(InvalidError)
        input()
        return
    print(generatingkeys[idioma])
    
    key.append(str(leng))

    wtd = 300
    #Loop hasta que se acabe el abc
    while len(key) < len(abc):
        #Genera una secuencia aleatoria
        ii = 0
        keytoput = ""
        while ii < leng:
            ntoput = str(nums[random.randint(0,len(nums)-1)])
            keytoput+=ntoput
            ii+=1
        k = 0
        saltar = False
        #Verifica si hay alguna clave igual que la generada recientemente
        while k < len(key):
            if keytoput == key[k]:
                saltar = True
                wtd -=1
            if wtd < 1:
                print (wtderror[idioma])
                input()
                return
            k+=1
        #Si es asi va al siguiente loop
        if saltar == True:
            continue
        #Si no le agrega el valor al array key
        key.append(keytoput)
        wtd = 300

    print("Saving key...")
    #Guarda el archivo de claves en la ruta dicha anteriormente
    keyfile = open(ruta,"w")
    for val in key:
        keyfile.write(val+"\n")
    keyfile.close()

    #Exito y pausa
    print(kgas[idioma])
    input()

#----------------------------------------------------SET LANUAGE-------------------------------------------------------------------------------------------------------
def setLanguage():
    global idioma
    if idioma == 0:
        print("Put the number of the language:\n0: English\n1: Español")
    if idioma == 1:
        print("Escribe el numero del lenguaje:\n0: English\n1: Español")

    try:
        num = int(input("mix>"))
    except:
        if idioma == 0:
            print(Fore.RED+Style.BRIGHT+"ERROR: what? You put any character what is not a number >:( (5)")
            input()
            return
        if idioma == 1:
            print(Fore.RED+Style.BRIGHT+"ERROR: KHE? Metiste algo que no es un numero >:( (5)")
            input()
            return
    configfile = open("config.txt","w")

    if num == 0 or num == 1:
        configfile.write("lang="+str(num))
        if idioma == 0:
            print("The language changed sucessfully")
        if idioma == 1:
            print("El lenguaje se cambio exitosamente")
        input()
    else:
        configfile.write("lang="+str(idioma))
        configfile.close()
        if idioma == 0:
            print(InvalidError[idioma])
        if idioma == 1:
            print(InvalidError[idioma])
        input()
        return

    configfile.close()
    idioma = num
######################################################Programa principal###############################################################################################
print(Fore.WHITE+Back.BLUE+Style.BRIGHT+"MixCryptor v1.1 | by @URROVA                                                    "+Fore.CYAN+Style.BRIGHT+helped[idioma])

#Hace un loop infinito
while True:
    #Pide un comando
    command = input("mix>")
    #Si es "encrypt" va a la funcion encrypt()
    if command == "encrypt":
        clearScreen()
        encrypt()
        clearScreen()
    #Si es "decrypt" va a la funcion decrypt()
    elif command == "decrypt":
        clearScreen()
        decrypt()
        clearScreen()
    #Si es "generateKey" va a la funcion keyGenerate()
    elif command == "generateKey":
        clearScreen()
        keyGenerate()
        clearScreen()
    #Si es "exit" cierra el programa
    elif command == "exit":
        sys.exit(0)
    elif command == "language":
        clearScreen()
        setLanguage()
        clearScreen()
    #Si es "help" o "list" muestra una lista de comandos
    elif command == "help" or command == "list":
        if idioma == 0:
            print(Fore.YELLOW+Style.BRIGHT+"Commands List:")
            print(Fore.CYAN+Style.BRIGHT+"encrypt"+Fore.RESET+": Encrypt a file.")
            print(Fore.CYAN+Style.BRIGHT+"decrypt"+Fore.RESET+": Decrypt a file.")
            print(Fore.CYAN+Style.BRIGHT+"generateKey"+Fore.RESET+": Generate a key for encrypt/decrypt.")
            print(Fore.CYAN+Style.BRIGHT+"version"+Fore.RESET+": View the version of the program.")
            print(Fore.CYAN+Style.BRIGHT+"credits"+Fore.RESET+": View the credits.")
            print(Fore.CYAN+Style.BRIGHT+"language"+Fore.RESET+": Set the language")
            print(Fore.CYAN+Style.BRIGHT+"easterspam"+Fore.RESET+": ???")
            print(Fore.CYAN+Style.BRIGHT+"exit"+Fore.RESET+": Close the program.")
        elif idioma == 1:
            print(Fore.YELLOW+Style.BRIGHT+"Lista de comandos:")
            print(Fore.CYAN+Style.BRIGHT+"encrypt"+Fore.RESET+": Encriptar un archivo.")
            print(Fore.CYAN+Style.BRIGHT+"decrypt"+Fore.RESET+": Desencriptar un archivos.")
            print(Fore.CYAN+Style.BRIGHT+"generateKey"+Fore.RESET+": Generar un archivo de claves para la encripcion/desencripcion.")
            print(Fore.CYAN+Style.BRIGHT+"version"+Fore.RESET+": Ver la version del programa.")
            print(Fore.CYAN+Style.BRIGHT+"credits"+Fore.RESET+": Ver los creditos.")
            print(Fore.CYAN+Style.BRIGHT+"language"+Fore.RESET+": Configurar el lenguaje")
            print(Fore.CYAN+Style.BRIGHT+"easterspam"+Fore.RESET+": ???")
            print(Fore.CYAN+Style.BRIGHT+"exit"+Fore.RESET+": Cerrar el programa.")
    #Si es "credits" muestra los creditos
    elif command == "credits":
        if idioma == 0:
            print(Fore.WHITE+Style.BRIGHT+'''CREDITS:
            Programming and mix cipher design: @URROVA.
            Programmed in Python.
            Thanks you for using this program!''')
        elif idioma == 1:
            print(Fore.WHITE+Style.BRIGHT+'''CREDITOS:
            Programacion y diseño del cifrado mix: @URROVA.
            Programado en Python.
            Gracias por usar este programa!''')

    #Si es "version" muestra la version
    elif command == "version":
        print(Fore.CYAN+Style.BRIGHT+"MixCryptor version 1.0")
    #Un pequeño easter spam
    elif command == "easterspam":
        print(easterspam[idioma])
    #Si no es ninguna, marca un error
    else:
        print(Fore.RED+Style.BRIGHT+InexistentCommand[idioma])
        
