from Empleado import *
import pandas as pd

import plotly.graph_objects as go

empleados = []

# Crear un empleado
e1 = Empleado()
e1.setNombre("Jonathan")
e1.setApellido("Campos Lozano")
e1.setSueldo(1000000)
e1.setDiasLiquidados(30)

#añadirlo al arreglo vacio
empleados.append(e1)

# Crear el segundo empleado 
e2 = Empleado()
e2.setNombre("Pedro")
e2.setApellido("Marciano")
e2.setSueldo(3000000)
e2.setDiasLiquidados(10)
# añadi al arreglo
empleados.append(e2)


# Crear el segundo empleado 
e3 = Empleado()
e3.setNombre("Camila")
e3.setApellido("La Muñeca")
e3.setSueldo(1700000)
e3.setDiasLiquidados(30)
# añadi al arreglo
empleados.append(e3)

'''
for i in empleados:
    print('******************')
    print(i)
'''

row = []
for i in empleados:
    column = []
    column.append(i.getNombre())
    column.append(i.getApellido())
    column.append(i.getSueldo())
    column.append(i.salarioDevengado())
    row.append(column)

column_name = ["NOMBRES","APELLIDOS"
                ,"SUELDO","SALARIO"]

# comvierto el arreglo en un dataset

df = pd.DataFrame(row, columns = column_name)

#--------------------------------------#
# inicia histograma

fig = go.Figure()

fig.add_trace(go.Histogram(histfunc="sum", y=df["SUELDO"]
                            ,x = df["NOMBRES"]))

fig.add_trace(go.Histogram(histfunc="sum", y=df["SALARIO"]
                            ,x = df["NOMBRES"]))
fig.show()

# inicia grafico Pie

fig2 = go.Figure( data=[go.Pie(
                    labels=df["NOMBRES"],values = df["SALARIO"])])
fig2.show()                  

