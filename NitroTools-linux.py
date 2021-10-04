import random, string, os, requests, subprocess
from art import text2art
import time

# Black
fgBlack = "\033[30m"

# Red
fgRed = "\033[31m"

# Green
fgGreen = "\033[32m"
bgBrightGreen = "\033[42;1m"

# Magenta
fgMagenta = "\033[35m"
bgMagenta = "\033[45m"
fgMagenta162 = '\u001b[38;5;162m'
fgMagenta163 = '\u001b[38;5;163m'
fgMagenta164 = '\u001b[38;5;164m'
fgMagenta167 = '\u001b[38;5;167m'
fgMagenta168 = '\u001b[38;5;168m'
fgMagenta169 = '\u001b[38;5;169m'
fgMagenta170 = '\u001b[38;5;170m'
fgMagenta171 = '\u001b[38;5;171m'
fgMagenta198 = '\u001b[38;5;198m'
fgMagenta199 = '\u001b[38;5;199m'
fgMagenta200 = '\u001b[38;5;200m'
fgMagenta201 = '\u001b[38;5;201m'

#Cyan
fgBrightCyan = "\033[36m"


reset = "\033[0m"


def genCod():
    generated = 0

    try:
        num=int(input("\n{}¿Cuántos códigos quieres generar?  > {}".format(fgMagenta,reset)))
        print('\n')
        path = str(os.path.dirname(__file__)) + "codes.txt"

        f=open("codes.txt","w+", encoding='utf-8')

        for kele in range(num):
            nitro = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
            
            print('{}[GENERADO]{} https://discord.gift/{}'.format(fgMagenta,reset,nitro))

            generated += 1

            f.write('https://discord.gift/{}\n'.format(nitro))
        f.close()

        if num == 1:
            print("\nSe generó {}{}{} código nitro".format(fgMagenta,num,reset))

        else:
            print("\nSe generaron {}{}{} códigos nitro".format(fgMagenta,num,reset))
        input("\n{}Presiona Enter para volver al Menu de Inicio.{}".format(fgMagenta,reset))

        if input == input:
            #plataformas()
            main()

    except ValueError:
        genCod()


def clear():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")
    

def genCheckCod():
    contador = 0

    try:
        cantidadGenerar = int(input('cuantos códigos quieres {}generar{} y {}checkear{}  > '.format(fgMagenta,reset,fgMagenta,reset)))
    
    except ValueError:
        genCheckCod()

    print (f'''asegúrate de introducir la url de un webhook válido/activo ;) \n''')

    try:
        url = input('{}URL del WebHook: {} '.format(fgMagenta,reset))
        print('\n')
        while contador < cantidadGenerar:

            contador += 1

            code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
        

            def post_code(url, code):
                requests.post(url, data={'content':'@everyone\n'+code})

            def check(code):
                status_code = requests.get('https://discordapp.com/api/v9/entitlements/gift-codes/'+code+'?with_application=false&with_subscription_plan=true').status_code
                
                if status_code == 200:
                    print('{}{}[VÁLIDO] https://discord.gg/{}{}'.format(bgBrightGreen,fgBlack,code,reset))
                    post_code(url, code)

                else:
                    print('{}[INVÁLIDO] > https://discord.gg/{}{}'.format(fgRed,code,reset))

            check(code)


        try:        
            l = input("\n{}Presiona Enter para volver al Menu de Inicio.{}".format(fgMagenta,reset))

            if l ==  '':
                main()


        except ValueError:
            genCheckCod()


    except ValueError:
        print('introduzca un valor válido')
        genCheckCod()


def genCodWindows():
    clear()
    print('{}{}   Generador y Checker de códigos nitro Windows  {}\n'.format(bgMagenta,fgBlack,reset))


    contador = 0
    try:
        cantidadGenerar = int(input('cuantos códigos quieres {}generar{} y {}checkear{}> '.format(fgMagenta,reset,fgMagenta,reset)))
        print (f'''Asegúrese de introducir la url de un webhook válido/activo ;) ''')

        url = input('{}URL del WebHook: {} '.format(fgMagenta,reset))

        while contador < cantidadGenerar:
            contador += 1
            code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
        
            def post_code(url, code):
                requests.post(url, data={'content':'@everyone\n'+code})

            def check(code):
                status_code = requests.get('https://discordapp.com/api/v9/entitlements/gift-codes/'+code+'?with_application=false&with_subscription_plan=true').status_code
                
                if status_code == 200:
                    print('{}{}[VÁLIDO] https://discord.gg/{}{}'.format(bgBrightGreen,fgBlack,code,reset))
                    post_code(url, code)

                else:
                    print('{}[INVÁLIDO] > https://discord.gg/{}{}'.format(fgRed,code,reset))

            check(code)
    
        try:        
            l = input("\n{}Presiona Enter para volver al Menu de Inicio.{}".format(fgMagenta,reset))

            if input == input:
                main()

        except ValueError:
            main()

    except ValueError:
        genCodWindows()
    

def check():
    checked = 0
    valido = 0
    invalido = 0

    f=open("codes.txt","r+", encoding='utf-8')
    v=open("valid_codes.txt","w+", encoding='utf-8')

    for line in f:
        nitro = line.strip("\n")
        url = "https://discordapp.com/api/v9/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
        r = requests.get(url)
       
        if r.status_code == 200:
            print('{}[VÁLIDO]{}{}'.format(fgGreen,reset,nitro))
            v.write(f"{nitro}\n")
            checked += 1
            valido += 1

        else:
            print('{}[INVÁLIDO]{}{}'.format(fgRed,reset,nitro))
            checked += 1
            invalido += 1

    f.close()
    v.close()
    print("\nSe checkearon {}{}{} códigos nitro, {}{}{} Válidos ,{}{}{} Inválidos\n".format(fgMagenta,checked,reset,fgGreen,valido,reset,fgRed,invalido,reset))
    
    try:        
            l = input("\n{}Presiona Enter para volver al Menu de Inicio.{}".format(fgMagenta,reset))
            if input == input:
                main()

    except ValueError:
            main()

    
def creditos():
    clear()
    print('{}{}   CREDITOS   {}'.format(bgMagenta,fgBlack,reset))
    print('''

            {}Verduxo    ayuda + apoyo   {}https://github.com/Verduxo{}
            
            '''.format(fgMagenta,fgBrightCyan,reset))
    try:        
        l = input("\n{}Presiona Enter para volver al Menu de Inicio.{}".format(fgMagenta,reset))

        if input == input:
            main()

    except ValueError:
        main()
    

def repoWindows():
    clear()
    print('{}{}NitroTool-Windows descarga{}'.format(bgMagenta,fgBlack,reset))
    try:
        print('   ')
        respuesta = int(input('({}1{} para {}si{}, {}0{} para {}no{})\n¿desea descargar el repositorio? [{}1{}/{}0{}] '.format(fgGreen,reset,fgGreen,reset,fgRed,reset,fgRed,reset,fgGreen,reset,fgRed,reset)))

        if int(respuesta)== 1:
            cmdCommand = "git clone https://github.com/tt-viic/NitroTool-Windows"
            process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            print('   ')
            print('REPOSITORIO CLONADO EN: ', os.getcwd())
            try:        
                l = input("\n{}Presiona Enter para volver al Menu de Inicio.{}".format(fgMagenta,reset))

                if input == input:
                    main()

            except ValueError:
                main()


        elif int(respuesta) == 0:
            print('{}ok, pero si quieres, aquí tienes el link {}{}https://github.com/tt-viic/NitroTool-Windows{}{} :){} '.format(fgMagenta,reset,fgBrightCyan,reset,fgMagenta,reset))
        try:        
            l = input("\n{}Presiona Enter para volver al Menu de Inicio.{}".format(fgMagenta,reset))

            if input == input:
                main()

        except ValueError:
            main()
    
    except ValueError:
        repoWindows()


def banner():

    fuentes = ['speed','fuzzy','epic','drpepper','doom','cyber large','cosmic','computer','chunky','graffiti','banner4','Fire Font-k','Flower Power','Graceful','ogre','Rectangles','slant relief','small','Bloody','THIS']
    banner=text2art("  DISCORD  NITRO",fuentes[random.randrange(0,len(fuentes))])
    print('{}'.format(fgMagenta)+banner+'{}'.format(reset))
    

def opcionesLinux():
    clear()
    banner()
    print('   ')
    print('''
    ┌────────────────────────────────────────────────────────────────────────────────┐
    │                           ¿Qué quieres hacer?                          {}--LINUX{} │
    ├────────────────────────────────────────────────────────────────────────────────┤
    │  {}[1] Generar códigos de Discord Nitro {}                                         │
    │  {}[2] Generar y checkear códigos de Discord Nitro automáticamente{}               │
    │  {}[3] Checkear los códigos de Discord Nitro generados {}                          │
    │  {}[99] EXIT, saldrás del programa{}                                               │
    └────────────────────────────────────────────────────────────────────────────────┘
    '''.format(fgRed,reset,fgMagenta171,reset,fgMagenta170,reset,fgMagenta171,reset,fgMagenta199,reset))
    

def opcionesWindows():
    clear()
    banner()
    print('   ')
    print('''
    ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
    │                                              ¿Continúas?                                           {}--WINDOWS {}│
    ├──────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
    │  {}Bien, antes de nada, te recomiendo usar este repositorio {}https://github.com/tt-viic/NitroTool-Windows{}       │
    │          {}(Cumple exactamente la misma función que este pero tiene una mejor UI y optimización){}               │
    │                                                                                                              │
    │  {}[1]  Sí, deseo continuar en este script{}                                                                     │
    │  {}[2]  No, quiero instalar NitroTool-Windows{}                                                                  │
    │  {}[99] EXIT, saldrás del programa{}                                                                             │
    └──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    '''.format(fgRed,reset,fgMagenta198,fgBrightCyan,reset,fgMagenta198,reset,fgMagenta199,reset,fgMagenta200,reset,fgMagenta201,reset))


def opcionesWindows2():
    clear()
    banner()
    print('   ')
    print('''
    ┌──────────────────────────────────────────────────────────────────────────────┐
    │                         ¿Qué quieres hacer?                       {}--WINDOWS{}  │
    ├──────────────────────────────────────────────────────────────────────────────┤
    │  {}[1]  Generar códigos de Discord Nitro {}                                      │
    │  {}[2]  Generar y checkear códigos de Discord Nitro automáticamente{}            │
    │  {}[3]  Checkear los códigos de Discord Nitro generados {}                       │
    │  {}[99] EXIT, saldrás del programa{}                                             │
    └──────────────────────────────────────────────────────────────────────────────┘
    '''.format(fgRed,reset,fgMagenta198,reset,fgMagenta198,reset,fgMagenta199,reset,fgMagenta200,reset,fgMagenta201,reset))


def plataformas():
    print('''
    ╔════════════════════════════════════╗
    ║  ¿En qué plataforma se encuentra?  ║
    ╠════════════════════════════════════╣
    ║  {}[1]  Linux{}                        ║
    ║  {}[2]  Windows{}                      ║
    ║  {}[0]  Créditos{}                     ║
    ║  {}[99] salir{}                        ║
    ╚════════════════════════════════════╝
    '''.format(fgMagenta162,reset,fgMagenta163,reset,fgMagenta164,reset,fgMagenta164,reset))


def salir():
    clear()
    print('¡Hasta pronto! \033[31;1m<3')
    exit()


def main():
    clear()
    banner()
    plataformas()
    try:
        plataforma = int(input('{}plataforma: {}'.format(fgMagenta,reset)))

        if (plataforma == 1):

            try:
                opcionesLinux()
                opcionLinux = int(input('{}opción: {}'.format(fgMagenta,reset)))

                if opcionLinux == 1:
                    clear()
                    print(' {}{}   Nitro Code Generator by viic  \n{}'.format(bgMagenta,fgBlack,reset))
                    genCod()

                elif opcionLinux == 2:
                    clear()
                    print(' {}{}   Generador y Checker de códigos nitro   {}\n'.format(bgMagenta,fgBlack,reset))
                    genCheckCod()

                elif opcionLinux == 3:
                    clear()
                    print(' {}{}   Nitro Code Checker by viic   {}\n'.format(bgMagenta,fgBlack,reset))
                    check()

                elif opcionLinux == 99:
                    salir()
                
                else:
                    main()
            
            except ValueError:
                main()

        elif (plataforma == 2):

            
            opcionesWindows()
            try:
                opcionWindows = int(input('opción: '))

                if opcionWindows  == 1:
                    opcionesWindows2()
                    try:
                        
                        opcionWindows2 = int(input('opción: '))
                        if opcionWindows2 == 1:
                            clear()
                            print(' {}{}   Nitro Code Generator by viic  {}                      {}--WINDOWS{}\n'.format(bgMagenta,fgBlack,reset,fgRed,reset))
                            genCod()

                        elif opcionWindows2 == 2:
                            clear()
                            print('{}{}   Generador y Checker de códigos nitro   {}                      {}--WINDOWS{}\n'.format(bgMagenta,fgBlack,reset,fgRed,reset))
                            genCheckCod()

                        elif opcionWindows2 == 3:
                            clear()
                            print(' {}{}   Nitro Code Checker by viic   {}                      {}--WINDOWS{}\n'.format(bgMagenta,fgBlack,reset,fgRed,reset))
                            check()

                        elif opcionWindows2 == 99:
                            salir()
                
                        else:
                            main()
            
                    except ValueError:
                        main()

                elif opcionWindows == 2:
                    repoWindows()

                elif opcionWindows == 99:
                    salir()

                else:
                    main()
            
            except ValueError:
                main()

        elif (plataforma == 0):
            creditos()

        elif (plataforma == 99):
            salir()

        else:
            main()

    except ValueError:
        main()


banner()
main()
