nombres = ["Juan", "María", "Pedro"]
cargos = ["Auxiliar", "Técnico", "Analista"]
    
if "Pedro" in nombres:
    nombres.append("Lucía")
    print("Se agregó Lucía")
else:
    print("No es necesario agregar Lucía")
    
if "Analista" in cargos:
    cargos.append("Coordinador")
    print("Se agregó Coordinador")
else:
    print("No es necesario agregar Coordinador")

if "María" in nombres:
    nombres.remove("María")
    print("Se removió María")
else:
    print("No es necesario remover María")

if len(nombres) > 3:
    nombres.pop(0) 
    print("Se eliminó")
else:
    print("No es necesario borrarlo")

if "Juan" in nombres:
    nombres[0] = "Julián"
    print("Se cambió Juan a Julian")
else:
    print("No es necesario")

equipo1 = [nombres[0], nombres[1]]
puestos_clave = [cargos[-3], cargos[-2]]

if "Lucía" in equipo1:
    tupla1 = ("Lucía", "Coordinador")
    print("Se agregó la tupla1")
    print(tupla1)
else:
    print("No es necesario crear la tupla")
    
if "Auxiliar" in puestos_clave:
    puestos_clave.remove("Auxiliar")
    print("Se removió Auxiliar")
elif "Auxiliar" not in puestos_clave:
    print("No es necesario remover Auxiliar")
    
if "Julián" in nombres:
    empleado = {
        "nombre" : "Julián",
        "cargo" : "Ténico",
        "activo" : True
    }
    print("Se agregó el diccionario empleado")
else:
    print("No es necesario crear el diccionario")
    
if empleado:
    empleado["contrato"] = "Indefinido"
    print("Se agregó los contratos")
else:
    print("No es necesario crear contrato")

if "Analista" in cargos:
    cargos.append("Practicante")
    print("Se agregó el rol Practicante en cargos")
else:
    print("No es necesario agregar Practicante")

if "Lucía" not in nombres:
    nombres.append("Lucía")
    print("Se agregó el nombre Lucía en nombres")
else:
    print("No es necesario agregar Lucía")

print("-----RESULTADOS--------")
print("EJERCICIO 5")
print(nombres)
print(cargos)
print(equipo1)
print(puestos_clave)
print(empleado)
#documeto
