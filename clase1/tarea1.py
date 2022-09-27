'''ACTVIDAD DE PYTHON'''

''' Librerias a importar para este codigo.'''
import pandas as pd
import matplotlib.pyplot as plt

'''Especificacion de la ruta del archivo csv.'''
ruta = r"C:\Users\MANUEL\Desktop\MAESTRIA - python\Buenas Practicas de Programacion con Python\1.ControlDeErroresPruebasyValidacionDeDatos\finanzas2020[1].csv"

'''Validacion de lectura del archivo csv.'''
try:
    df=pd.read_csv(ruta,sep="\t")
    print("Lectura Exitosa")
except Exception as e:
    print("Archivo no Encontrado : ",e)

'''Validacion del numero de columnas.'''
assert len(df.columns)==12, "El numero de columnas no es 12"




''' ESTE SCRIPT LIMPIA TODO, ASI LOS VALORES DE LAS COL SEAN STRING O INT. '''
try:
    for col in df:
        t=[]
        for x in df[col].values:
            try:
                if type(x)==str:
                    r=int(x.replace("'",''))
                    t.append(r)
                else:
                    r=int(x)
                    t.append(r)
            except Exception:
                if type(x)==int:
                    r=int(x)
                    t.append(r)
                else:
                    t.append(0)

        df[col]=t
    print("Datos validados correctamente")
except Exception as e:
    print("Error al validar los datos : ",e)


''' Capturamos los Gastos totales de todos los meses. '''
a = df.sum() 

print("=================================")
print("===========   REPORTE   =========")
print("=================================")
print("-  ¿Qué mes se ha gastado más?")

'''Recorrido para el mes de mayor gasto '''
for x,y in a.items():
    if y==a.min():
        print("==> Mes de mayor gasto: ",x,"(",y,")")

'''Recorrido para el mes de mayor ahorro '''
print("-  ¿Qué mes se ha ahorrado más?")
for x,y in a.items():
    if y==a.max():
        print("==> Mes de mayor ahorro: ",x,"(",y,")")


''' Logica para calcular los gastos e ingresos totales al año junto con la media de gastos '''
gastos=0
ingresos=0
i=0
for x,y in a.items():
    if y<0:
        gastos=gastos+y
        i+=1
    else:
        ingresos=ingresos+y

media=gastos/i

print("-  ¿Cuál es la media de gastos al año?")
print("==> Media de gastos: ",round(media,2))

print("-  ¿Cuál ha sido el gasto total a lo largo del año?")
print("==> Gasto total del año: ",gastos)

print("-  ¿Cuál ha sido el ingreso total a lo largo del año?")
print("==> Ingreso total del año: ",ingresos)


''' LOGICA PARA GENERAR UN DIAGRAMA DE BARRAS CON TODOS LOS DATOS POSITIVOS E INDICAR EN BARRA ROJA LOS MESES DE GASTOS '''
pos=[]
for x,y in a.items():
    if y<0:
        pos.append(abs(y))
    else:
        pos.append(y)


'''GRAFICO DE EVOLUCION DE GASTOS DURANTE LOS 12 MESES '''

plt.bar(a.index, pos, color=['#069AF3', '#FC5A50', '#FC5A50', '#069AF3', '#069AF3','#FC5A50', '#069AF3', '#FC5A50', '#069AF3', '#069AF3', '#069AF3', '#FC5A50'],label='Ingresos',align='center') #reemplazo a.values por pos[] y listo
plt.bar(a.index[0], 0, color='#FC5A50',label='Gastos')
plt.xticks(a.index, rotation ='vertical')
font1 = {'family':'serif','color':'black','size':15}
font2 = {'family':'serif','color':'darkred','size':10}
plt.xlabel("Meses",fontdict = font2)
plt.ylabel("Gastos",fontdict = font2)
plt.title('Evolución de Ingresos durante el Año',fontdict = font1)
plt.legend(loc='best')
plt.show()


#def cm_to_inch(value):
#    return value/2.54
#plt.figure(figsize=(3,3))
#plt.figure(figsize=(cm_to_inch(15),cm_to_inch(10)))
# df2 = pd.DataFrame([(a.index[0],a.values[0])],columns =["Meses","Gastos"])
# d = {'Meses': a.index, 'Ingresos y Gastos': a.values}
# df3=pd.DataFrame(data=d, index=a.index)#, index=[0, 1, 2, 3] or None)
# #df3n=df3.set_index('Meses') convierto una columna en index
# #print(df3n)
# ax=df3.plot(kind = 'bar',width=0.8,subplots=True,figsize=(10,8),xlabel="Meses",ylabel='Gastos',title="Evolución de Ingresos durante el Año")



# ax1.hist(["Enero","Febrero"],[10,20])
# ax1.set_ylabel('Gastos')
# ax1.set_xlabel('Meses')
# #plt.hist(a)
# plt.show()

#fig, ax = plt.subplots()

# ax.set(xlabel="x label", ylabel="y label")
#df3n.index.name = 'Gastos'









'''
print("Valores de Prueba para corroborar la limpieza")
print(df["Enero"][63])
print(df["Julio"][59])
print(df["Septiembre"][43])
print(df["Febrero"][63])
print(df["Noviembre"][90])
print(df["Octubre"][50])
#print(df.sum())


####################################### LIMPIA TODO SIEMPRE Q SEAN STRINGS (LOS VALORES DE TODAS LAS COL)
# for col in df:
#     t=[]
#     for x in df[col].values:
#         try:
#             r=int(x.replace("'",''))
#             t.append(r)
#         except Exception:
#             if type(x)==int:
#                 r=int(x)
#                 t.append(r)
#             else:
#                 t.append(0)

#     df[col]=t
#     t.clear()
# print(df)

#######################################
#df['Enero'] = [(x.replace("'","")) for x in df['Enero']]

#for column in df:
    #print(df[column])
    #df[column]= [(x.replace("'","")) for x in df[column]]

#for col in df:
#    df[col].values = [(x.replace("'","")) for x in df[col].values]

a=['-555','555',12,'555','556','bug',"13","'25'"]
ar="'25'"
ar2='25'
#print(str(ar2))
#print(ar2.replace("'",''))

k=[]
for p in ar:
    l=p.replace("'",'')
    k.append(l)
#print(k)
b = []
c = []
#for x in a:
#    new_dato=x.replace(" ' "," ")
#    b.append(new_dato)



for x in a:
    try:
        #x.replace("'",'')
        #r=int(x)
        r=int(x.replace("'",''))
        c.append(r)
    except Exception:
        if type(x)==int:
            r=int(x)
            c.append(r)
        else:
            c.append(0)
a = c
#print(a)
#print(b)
#for val in df['Enero']:
    #print(val) #todos los valores
    #val=str(val)
    #val.replace("'","")
    #val.strip("'")
    #df['Enero']=col.replace("'","")

#for col in df:
#    print(df[col].values) # los valores en una lista
    #for x in df[col].values:
    #    str(x).replace("'","")

def fun(col):
    df[col] = [(x.replace("'","")) for x in df[col]]

#fun('Enero')
'''


