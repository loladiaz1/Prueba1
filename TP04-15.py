"""
-----------------------------------------------------------------------------------------------
Título:TP04-15 | NUMERO A LETRAS

Fecha:1/10

Autor:Lappano Sofia

Descripción:Muchas aplicaciones financieras requieren que los números sean expresados también en letras. Por ejemplo, el número 
2153 puede escribirse como "dos mil ciento cincuenta y tres". Nos piden un programa con una función para convertir a 
texto un número entero entre 0 y casi mil millones (es decir, cifras hasta 999.999.999).
Revisando módulos desarrollados en el pasado por nuestro equipo de programadores encontramos una función para 
convertir números a texto, pero preparada para valores entre 0 y 999.999 (el profesor entregará esta función). Analizar 
la función recuperada y realizarle los cambios necesarios para que funcione hasta 999.999.999

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def convertir_a_texto(numero):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos",
                "setecientos", "ochocientos", "novecientos"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince"]

    def convertir_cifras(cifras):
        if cifras < 10:
            return unidades[cifras]
        elif cifras < 20:
            return especiales[cifras - 10]
        elif cifras < 100:
            if cifras % 10 == 0:
                return decenas[cifras // 10]
            else:
                return decenas[cifras // 10] + ' y ' + unidades[cifras % 10]
        elif cifras < 1000:
            if cifras % 100 == 0:
                return centenas[cifras // 100]
            else:
                return centenas[cifras // 100] + ' ' + convertir_cifras(cifras % 100)
        elif cifras < 1000000:
            miles = cifras // 1000
            resto = cifras % 1000
            if miles == 1:
                return 'mil ' + convertir_cifras(resto)
            else:
                return convertir_cifras(miles) + ' mil ' + convertir_cifras(resto)
        else:
            millones = cifras // 1000000
            resto = cifras % 1000000
            if millones == 1:
                return 'un millón ' + convertir_cifras(resto)
            else:
                return convertir_cifras(millones) + ' millones ' + convertir_cifras(resto)

    if numero == 0:
        return 'cero'
    else:
        return convertir_cifras(numero)





#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------.
...

#-------------------------------------------------
# Inicialización de variables
#-------------------------------------------------
numero = int(input("Introduce un número: "))


#-------------------------------------------------
# Procesos
#-------------------------------------------------
...

#-------------------------------------------------
# Resultados
#-------------------------------------------------
print(convertir_a_texto(numero))