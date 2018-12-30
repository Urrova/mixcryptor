# -*- coding: UTF-8 -*-

'''
MixCryptor 1.1
You can use, study the code, modify and share modified copies of this program, according to the GNU GPL v3
'''

import re
import os
import sys
import random
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as tkmb

######################################################Settings#########################################################################################################

try:
    config = open("config.txt","r")
    readed = config.read()
    idioma = int(readed.replace("lang=",""))
    config.close()
except FileNotFoundError:
    config = open("config.txt","w")
    config.write("lang=0")
    config.close()
    tkmb.showwarning("Recuperation Mode","The file \"config.txt\" was inexistent, and MixCryptor created it with lang = 0. MixCryptor will close.")
    sys.exit()
except ValueError:
    config = open("config.txt","w")
    config.write("lang=0")
    config.close()
    tkmb.showwarning("Recuperation Mode","The file \"config.txt\" was corrupted, and MixCryptor fixed it with lang = 0. MixCryptor will close.")
    sys.exit()
    

abc = "!\"#$%&'()*+, \n\t-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŒœŠšŸŽžƒˆ˜"
'''
Idioma 0: ingles
Idioma 1: español
'''

language_file=open("languages.txt","r")
lf_content = language_file.read()
language_file.close()

msgs = lf_content.split("\n")


c = 0

for i in msgs:
    msgs[c]=i.split(",")
    c+=1

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
        

def clearWindow():
    list = root.pack_slaves()
    for l in list:
        l.destroy()

#-----------------------------------------ENCRYPT----------------------------------------------------------------------------------------------------------------------
def encrypt(root, keyRoot, save):

    #entrada
    plaintext = ""


    #inicializa un array vacio para las claves
    key = []
    #Array inutil
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    #String vacio para el texto cifrado
    ciphertext = ""


    #intenta abrir el archivo de la ruta ingresada
    try:
        f = open(root, "r")
    #si no existe retorna
    except FileNotFoundError:
        tkmb.showerror("MixCryptor",msgs[18][idioma])
        return


    #lee el contenido
    contenido = f.read()
    #Y sigue leyendo el contenido hasta que no haya nada
    while contenido != "":
        plaintext += contenido
        contenido = f.read()
    f.close()


    #Intenta abrir clave
    try:
        keyfile = open(keyRoot,"r")
    #Si no existe retorna
    except FileNotFoundError:
        tkmb.showerror("MixCryptor",msgs[19][idioma])
        return

    #Va poniendo cada una de las claves
    indd = 0
    for line in keyfile:
        linee = line.replace("\n","")
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



    #Guarda
    savefile = open(save,"w")
    savefile.write(ciphertext)
    savefile.close()
    tkmb.showinfo("MixCryptor",msgs[20][idioma])




#-------------------------------------------DECRYPT--------------------------------------------------------------------------------------------------------------------
def decrypt(ruta, keyRoot, saveRoot):

    #setup
    #Inicializa el array del abc
    global abc
    #Array vacio para cargar las claves
    key = []
    #entrada
    #Intenta abrirlo
    try:
        cipherfile = open(ruta,"r")
    #Si no existe retorna
    except FileNotFoundError:
        tkmb.showerror("MixCryptor",msgs[18][idioma])
        return
    #Lee el archivo cifrado
    ciphertext = cipherfile.read()
    #Cierra cipherfile
    cipherfile.close()
    #Inicializa un string vacio "Plaintext"
    plaintext = ""

    #Intenta abrirlo
    try:
        keyfile = open(keyRoot,"r")
    #Si no existe retorna
    except FileNotFoundError:
        tkmb.showerror("MixCryptor",msgs[19][idioma])
        return

    #Va poniendo cada una de las claves
    indd = 0
    for line in keyfile:
        linee = line.replace("\n","")
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
    savefile = open(saveRoot, "w")
    savefile.write(plaintext)
    savefile.close()
    clearScreen()
    #Dice que lo desencripto con exito y espera
    tkmb.showinfo("MixCryptor",msgs[21][idioma])

#-----------------------------------------------------KEY GENERATOR----------------------------------------------------------------------------------------------------
def keyGenerate(saveRoot, lenght, formato):

    #GLobalizar el array del abc
    global abc
    #En este array se guardaran los numeros aleatorios generados en formato string
    key = []

    def randomNums():
        arr = []
        
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

    #String de numeros para elegir aleatoriamente
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    #Pide la ruta de guardado del archivo de claves
    ruta = saveRoot
    #Pide la longitud de cada clave
    leng = int(lenght)

    if formato == 0:
        nums = numsNums()
    elif formato == 1:
        nums = azminNums()
    elif formato == 2:
        nums = azmayNums()
    elif formato == 3:
        nums = azmixNums()
    elif formato == 4:
        nums = randomNums()
        
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
                tkmb.showerror("MixCryptor","Tiempo limite superado")
                return
            k+=1
        #Si es asi va al siguiente loop
        if saltar == True:
            continue
        #Si no le agrega el valor al array key
        key.append(keytoput)
        wtd = 300


    keyfile = open(ruta,"w")
    for val in key:
        keyfile.write(val+"\n")
    keyfile.close()

    tkmb.showinfo("MixCryptor",msgs[22][idioma])

#----------------------------------------------------SET LANUAGE-------------------------------------------------------------------------------------------------------
def setLanguage(num):
    
    global idioma
    
    configfile = open("config.txt","w")

    if num == 0  or num == 1 or num == 2:
        configfile.write("lang="+str(num))
        if idioma == 0:
            tkmb.showinfo("MixCryptor",msgs[23][idioma])
        if idioma == 1 or idioma == 2:
            tkmb.showinfo("MixCryptor",msgs[23][idioma])

    configfile.close()
    idioma = num

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - Ventanas - - - - - - - - - - - - - - - - - - - - Windoge - - - - - - - - - - - - - - - - skere - - - - - - -

def makeEncryptWindow():
    global root

    clearWindow()
    
    root.title("MixCryptor - Encrypt")
    root.resizable(False, False)
    root.geometry("250x300")

    Label(root, text=msgs[0][idioma],anchor="center", font=("Helvetica",30)).pack()

    Frame(root, width=250, height=3, relief=SUNKEN).pack()
    Frame(root, width=250, height=10).pack()

    Label(root, text=msgs[6][idioma],anchor="center").pack()
    rootEntry = Entry(root)
    rootEntry.pack()

    Label(root, text=msgs[7][idioma], anchor="center").pack()
    keyRootEntry = Entry(root)
    keyRootEntry.pack()

    Label(root, text=msgs[8][idioma], anchor="center").pack()
    saveRootEntry = Entry(root)
    saveRootEntry.pack()

    Separator(root, orient=HORIZONTAL).pack()

    boton_encrypt = Button(root,text=msgs[0][idioma], command=lambda: encrypt(rootEntry.get(), keyRootEntry.get(), saveRootEntry.get()))
    boton_encrypt.pack()

    Frame(root, width=250, height=10).pack()
    Frame(root, width=250, height=3, relief=SUNKEN).pack()
    Frame(root, width=250, height=10).pack()

    boton_back = Button(root,text=msgs[9][idioma], command=makeMainWindow)
    boton_back.pack()

def makeDecryptWindow():
    global root

    clearWindow()

    root.title("MixCryptor - Decrypt")
    root.resizable(False, False)
    root.geometry("250x300")

    Label(root, text=msgs[1][idioma],anchor="center", font=("Helvetica",30)).pack()

    Frame(root, width=250, height=3, relief=SUNKEN).pack()
    Frame(root, width=250, height=10).pack()

    Label(root, text=msgs[10][idioma],anchor="center").pack()
    rootEntry = Entry(root)
    rootEntry.pack()

    Label(root, text=msgs[7][idioma], anchor="center").pack()
    keyRootEntry = Entry(root)
    keyRootEntry.pack()

    Label(root, text=msgs[8][idioma], anchor="center").pack()
    saveRootEntry = Entry(root)
    saveRootEntry.pack()

    Separator(root, orient=HORIZONTAL).pack()

    boton_encrypt = Button(root,text=msgs[1][idioma], command=lambda: decrypt(rootEntry.get(), keyRootEntry.get(), saveRootEntry.get()))
    boton_encrypt.pack()

    Frame(root, width=250, height=10).pack()
    Frame(root, width=250, height=3, relief=SUNKEN).pack()
    Frame(root, width=250, height=10).pack()

    boton_back = Button(root,text=msgs[9][idioma], command=makeMainWindow)
    boton_back.pack()

def makeKeyWindow():

    clearWindow()
    
    #Arma la ventana
    root.title("MixCryptor - Generate Key")
    root.resizable(False, False)
    root.geometry("250x380")

    v = IntVar()
    v.set(0)  # initializing the choice, i.e. Python

    languages = [
        (msgs[13][idioma],1),
        (msgs[14][idioma],2),
        (msgs[15][idioma],3),
        (msgs[16][idioma],4),
        (msgs[17][idioma],5)
    ]
    
    Label(root, text=msgs[2][idioma],anchor="center", font=("Helvetica",25)).pack()

    Frame(root, width=250, height=3, relief=SUNKEN).pack()
    Frame(root, width=250, height=10).pack()

    Label(root, text=msgs[8][idioma],anchor="center").pack()
    saveEntry = Entry(root)
    saveEntry.pack()

    Label(root, text=msgs[11][idioma], anchor="center").pack()
    lenghtRootEntry = Entry(root)
    lenghtRootEntry.pack()

    Label(root, text=msgs[12][idioma], anchor="center").pack()
    
    for val, language in enumerate(languages):
        Radiobutton(root, 
                  text=language[0],
                  variable=v, 
                  value=val).pack(anchor=W)

    Separator(root, orient=HORIZONTAL).pack()

    boton_encrypt = Button(root,text=msgs[2][idioma], command=lambda: keyGenerate(saveEntry.get(), lenghtRootEntry.get(), v.get()))
    boton_encrypt.pack()

    Frame(root, width=250, height=10).pack()
    Frame(root, width=250, height=3, relief=SUNKEN).pack()
    Frame(root, width=250, height=10).pack()


    boton_back = Button(root,text=msgs[9][idioma], command=makeMainWindow)
    boton_back.pack()

def makeMainWindow():

    clearWindow()
    
    root.resizable(False,False)
    root.title("MixCryptor version 1.0")
    root.geometry("250x250")

    Label(root, text="MixCryptor",anchor="center", font=("Helvetica",30)).pack()

    Frame(root, width=250, height=3, relief=SUNKEN).pack()
    Frame(root, width=250, height=10).pack()

    
    
    
    

    boton_encriptar = Button(root,text=msgs[0][idioma], command=makeEncryptWindow)
    boton_encriptar.pack()

    boton_desencriptar = Button(root,text=msgs[1][idioma], command=makeDecryptWindow)
    boton_desencriptar.pack()

    boton_generadorClave = Button(root,text=msgs[2][idioma], command=makeKeyWindow)
    boton_generadorClave.pack()

    Frame(root, width=250, height=10).pack()
    Frame(root, width=250, height=3, relief=SUNKEN).pack()
    Frame(root, width=250, height=10).pack()

    boton_help = Button(root,text=msgs[3][idioma], command=makeLanguageWindow)
    boton_help.pack()

    boton_help = Button(root,text=msgs[4][idioma], command=showmethehelp)
    boton_help.pack()

    boton_credits = Button(root,text=msgs[5][idioma], command=showmethecredits)
    boton_credits.pack()

def makeLanguageWindow():

    v = IntVar()
    v.set(0)  # initializing the choice, i.e. Python

    
    languages = [
        ("English",0),
        ("Español",1),
        ("Portugues",2),
    ]

    clearWindow()
    
    root.resizable(False,False)
    root.title("MixCryptor - Change language")
    root.geometry("250x250")

    Label(root, text=msgs[3][idioma],anchor="center", font=("Helvetica",20)).pack()

    Frame(root, width=250, height=3, relief=SUNKEN).pack()
    Frame(root, width=250, height=10).pack()

    Label(root, text=msgs[24][idioma],anchor="center").pack()

    for val, language in enumerate(languages):
        
        
        Radiobutton(root, 
                  text=language[0],
                  variable=v, 
                  value=val).pack(anchor=W)

    boton_help = Button(root,text=msgs[3][idioma], command=lambda: setLanguage(v.get()))
    boton_help.pack()

    Frame(root, width=250, height=10).pack()
    Frame(root, width=250, height=3, relief=SUNKEN).pack()
    Frame(root, width=250, height=10).pack()

    boton_credits = Button(root,text=msgs[9][idioma], command=makeMainWindow)
    boton_credits.pack()

#-------------------------------------------PopUps--------------------------------------------------------------LOLXDWTF-----------------------------------------------

def showmethecredits():
    msg = msgs[25][idioma].replace("\\n","\n")
    tkmb.showinfo("MixCryptor",msg)

def showmethehelp():
    msg = msgs[26+idioma][0].replace("\\n","\n")
    tkmb.showinfo("MixCryptor",msg)

######################################################Programa principal###############################################################################################


root = Tk("MixCryptor version 1.0")
bit = root.iconbitmap('mcicon.ico')

makeMainWindow()

root.mainloop()
