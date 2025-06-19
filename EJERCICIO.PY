nombres = ["Juan", "María", "Pedro"]
cargos = ["Auxiliar", "Técnico", "Analista"]
    
if "Pedro" in nombres:
    nombres.append("Lucía")

if "Analista" in cargos:
    cargos.append("Coordinador")
if "María" in nombres:
    nombres.remove("María")
if len(nombres) > 3:
    nombres.pop(0)  
if "Juan" in nombres:
    nombres[0] = "Julián"

equipo1 = [nombres[0], nombres[1]]
puestos_clave = [cargos[-3], cargos[-2]]

if "Lucia" in equipo1:
    tupla1 = ("Lucía", "Coordinador")
if "Auxiliar" in puestos_clave:
    puestos_clave.remove("Auxiliar")
if "Julián" in nombres:
    empleado = {
        "nombre" : "Julián",
        "cargo" : "Ténico",
        "activo" : True
    }
if empleado:
    empleado["contrato"] = "Indefinido"
if "Analista" in cargos:
    cargos.append("Practicante")
if "Lucía" not in nombres:
    nombres.append("Lucía")

print(nombres)
print(cargos)
print(equipo1)
print(puestos_clave)
print(empleado)

