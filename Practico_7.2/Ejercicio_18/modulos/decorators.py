import os,time

###############################################################################################
#                                                                                             #
#  -----------  Códigos ANSI para cambiar el color del texto en la salida  ------------       #
#                                                                                             #
###############################################################################################
def printc(text: str, color=None, background=None, style=None):
    styles = {
        "bold": "\033[1m",
        "underline": "\033[4m",
    }

    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "grey": "\033[90m",
        "black": "\033[30m",
        "reset": "\033[0m",
    }

    backgrounds = {
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "grey": "\033[47m",
        "reset": "\033[0m",
    }

    style_code = styles.get(style, "")
    color_code = colors.get(color, "")
    background_code = backgrounds.get(background, "")
    print(f"{background_code}{color_code}{style_code}{text}{colors['reset']}")
    


###############################################################################################
#                                                                                             #
#                       -----------   TITULO DEL PROGRAMA  ------------                       #
#                                                                                             #
###############################################################################################    
    
def print_box(text:str,color=None,style='bold'):

    text_length = len(text)

    printc("+" + "-" * (text_length + 2) + "+", color, style)
    printc("|" + f" {text} ".center(text_length + 2) + "|",color,style)
    printc("+" + "-" * (text_length + 2) + "+", color, style)

###############################################################################################
#                                                                                             #
#                        -----------   LIMPIAR CONSOLA  ------------                          #
#                                                                                             #
###############################################################################################   

def clear_console(tiempo=1.2) -> None:
    time.sleep(tiempo)
    os.system("cls")

###############################################################################################
#                                                                                             #
#                        -----------   MENSAJE DE ERROR  ------------                         #
#                                                                                             #
############################################################################################### 
    
def msg_error(text: str= 'Opcion invalida!!!') -> None:
    time.sleep(1)   
    printc(f"{text}\n","red","yellow")
    msg_continuar()
    clear_console()
    
    
###############################################################################################
#                                                                                             #
#                     -----------   MENSAJE DE CONTINUAR  ------------                        #
#                                                                                             #
###############################################################################################   

def msg_continuar():
    if(input("\nPresione enter para continuar...")):
            clear_console() 
    


###############################################################################################
#                                                                                             #
#                     -----------   MENSAJE DE SALIR  ------------                            #
#                                                                                             #
###############################################################################################   

def msg_salir():
    printc('Saliendo...', 'green', 'bold')
    clear_console() 
    




###############################################################################################
#                                                                                             #
#                         -----------   MENU PRINCIPAL  ------------                          #
#                                                                                             #
###############################################################################################   



# +++++++++++++++++++
# |      MENU       |  
# +++++++++++++++++++

def menu_principal(op: list, title: str = "MENU PRINCIPAL") -> int:
    clear_console()
    
    op_len =len(op) #obtengo el numero de opciones
    
    print_box(f"    {title}   ","yellow")
    for i in range(op_len):
        
        printc(f"{i+1}. {op[i]}","green")
        
    printc("0. Salir\n","green")
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion > op_len or opcion < 0:
            msg_error()
            menu_principal(op)
        clear_console()
        return opcion
    except ValueError:
        msg_error()
        clear_console()
        menu_principal(op)
        