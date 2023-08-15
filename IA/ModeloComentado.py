###IMPOERTAMOS TODAS LAS LIBRERIAS QUE NECESITAMOS
##(NOTA): AQUI ESTAN INCLUIDAS LAS ***TKINDER***, ESAS SON **SOLO** PARA EL FORMULARIO GUI QUE HICE PRUEBAS Y ELEGIR, YA LE CAMBIO
##PARA ESCOGER DESDE EL SERVIDOR WEB, ES DECIR NO VAN AQUI EN EL ALGORTIMO FINAL
from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

######INGRESAMOS TODOS LOS SINTOMAS QUE PUEDE TENER LA PERSONA A LA CUAL VAMOS A HACER LA PREDICCION
l1=['picazón','erupciones_cutáneas','erupciones_nodales_en_la_piel','estornudos_continuos','temblores','escalofríos','dolor_articular','dolor_de_estómago','acidez','úlceras_en_la_lengua','desgaste_muscular','vómitos','ardor_micción','manchas_alorinar','fatiga',
'aumento_de_peso','ansiedad','manos_y_pies_fríos','cambios_de_ánimo','pérdida_de_peso','inquietud','letargo','parches_en_la_garganta',
'nivel_de_azúcar_irregular','tos','fiebre_alta','ojos_hundidos','faltadealiento','sudoración','deshidratación','indigestión',
'dolor_de_cabeza','piel_amarillenta','orina_oscura','náuseas','pérdida_de_apetito','dolor_detrás_de_los_ojos','dolor_de_espalda','estreñimiento',
'dolor_abdominal','diarrea','fiebre_leve','orina_amarilla','coloración_amarillenta_de_los_ojos','insuficiencia_hepática_aguda','sobrecarga_de_líquidos',
'hinchazón_del_estómago','ganglios_linfáticos_hinchados','malestar_general','visión_borrosa_y_distorsionada','flema','irritación_de_la_garganta',
'enrojecimiento_de_ojos','presión_sinusal','secreción_nasal','congestión','dolor_de_pecho','debilidad_en_extremidades','ritmo_cardiaco_rápido',
'dolor_durante_las_defecaciones','dolor_en_la_región_anal','hecesconsangre','irritación_en_el_ano','dolor_de_cuello','mareos','calambres',
'hematomas','obesidad','piernas_hinchadas','vasos_sanguíneos_hinchados','cara_y_ojos_hinchados','tiroides_agrandada','uñas_quebradizas',
'extremidades_hinchadas','hambre_excesiva','contactos_extramatriciales','sequedad_y_hormigueo_en_los_labios','dificultad_para_hablar','dolor_en_las_rodillas','dolor_en_las_articulaciones_de_la_cadera',
'debilidad_muscular','rigidez_de_cuello','hinchazón_de_articulaciones','rigidez_de_movimiento','movimientos_giratorios','pérdida_de_equilibrio','inestabilidad','debilidad_de_un_lado_del_cuerpo',
'pérdida_del_olfato','malestar_de_la_vejiga','mal_olor_de_la_orina','micción_frecuente','paso_de_gases','picazón_interna','aspecto_tóxico_(tifus)',
'depresión','irritabilidad','dolor_muscular','sensorio_alterado','manchas_rojas_en_el_cuerpo','dolor_de_vientre','menstruación_anormal','parches_discrómicos',
'lagrimeo_de_los_ojos','aumento_del_apetito','poliuria','antecedentes_familiares','esputo_mucoide','esputo_oxidado','falta_de_concentración','alteraciones_visuales',
'recibir_transfusión_de_sangre','recibir_inyecciones_no_estériles','coma','sangrado_estómago','distensión_del_abdomen','antecedentes_de_consumo_de_alcohol',
'sobrecarga_de_fluidos','sangre_en_el_esputo','venas_prominentes_en_la_pantorrilla','palpitaciones','dolor_al_caminar','espinillas_llenas_de_pus','puntos_negros','escurrimiento','descamación_de_la_piel',
'polvo_similar_a_la_plata','pequeñas_abolladuras_en_las_uñas','uñas_inflamadas','ampollas','llaga_roja_alrededor_de_la_nariz','exudado_costra_amarilla'
]
#############INGRESAMOS LA LISTA DE POSIBLES ENFERMEDADES QUE PUEDE TENER ALGUIEN, BASADO EN NUESTRA DATA
Enfermedad=['Infección fúngica','Alergia','ERGE','Colestasis crónica','Reacción a Fármacos',
'Enfermedad de úlcera péptica','SIDA','Diabetes','Gastroenteritis','Asma bronquial','Hipertensión',
'Migraña','Espondilosis cervical','Parálisis (hemorragia cerebral)','Ictericia','Paludismo',
'Varicela','Dengue','Tifus','Hepatitis A','Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E',
'Hepatitis Alcohólica','Tuberculosis','Resfriado Común','Neumonía','Hemorroides Dimórficas (almorranas)',
'Infarto','Varices','Hipotiroidismo','Hipertiroidismo','Hipoglucemia','Osteoartritis',
'Artritis','(Vértigo) Vértigo Posicional Paroymsal','Acné','Infección Urinaria','Psoriasis','Impétigo'
]
#### CREAMOS UNA LISTA DEL MISMO RANGO QUE L1, QUE NOS AYUDARA DESPUES, A MODO DE ARREGLO PARA RASTREAR SI UN
#### SINTOMA EN ESPECIFICO ESTA PRESENTE SE HACE 1 Y SI NO LO ESTA SE HACE 0
l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# PRUEBA DE DATOS
##### COMO INGRESAMOS LOS SINTOMAS ALISTAMOS NUESTRO CVS YA CON CADA ENFERMEDAD UN VALOR
##### Y LO AGREGAMOS A NUESTRO DATAFRAME DE PANDAS
##### ES DECIR ESTAMOS ETIQUETANDO LOS VALORES Y NORMALIZANDO DATOS
tr=pd.read_csv("CSV PRUEBA.csv")
tr.replace({'Pronosticos':{'Infección fúngica':0,'Alergia':1,'ERGE':2,'Colestasis crónica':3,'Reacción a fármacos':4,
'Enfermedad de úlcera péptica':5,'SIDA':6,'Diabetes':7,'Gastroenteritis':8,'Asma bronquial':9,'Hipertensión':10,
'Migraña':11,'Espondilosis cervical':12,
'Parálisis(hemorragia cerebral)':13,'Ictericia':14,'Paludismo':15,'Varicela':16,'Dengue':17,'Tifus':18,'Hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Hepatitis alcohólica':24,'Tuberculosis':25,
'Resfriado común':26,'Neumonía':27,'Hemorroides dimórficas (almorranas)':28,'Infarto de miocardio':29,'Varices':30,'Hipotiroidismo':31,
'Hipertiroidismo':32,'Hipoglucemia':33,'Osteoartritis':34,'Artritis':35,
'Vértigo Posicional Paroymsal':36,'Acné':37,'Infección de las Vías Urinarias':38,'Psoriasis':39,
'Impétigo':40}},inplace=True)

X_test = tr[l1] ## SON LAS CARACTERISTICAS DE PRUEBA CON LA QUE HARA LA EVALUACION BASADAS EN LA LISTA DE SINTOMAS DE L1
y_test = tr[["Pronosticos"]] ## SON LAS ETIQUETAS CON LAS QUE SE HARA LA EVALUACION
np.ravel(y_test)## DEVUELVE DATOS EN UN ARRAY

# ENTRENAMIENTO DE LA IA, CON NUESTROS DATOS
df=pd.read_csv("DATOS DE ENTRENAMIENTO.csv")
##NUEVAMENTE ETIQUETAMOS LOS DATOS, PERO AHORA NO CON LA DATA DE PRUEBA SINO CON LA DATA REAL DE PRONOSTICOS
df.replace({'Pronosticos':{'Infección fúngica':0,'Alergia':1,'ERGE':2,'Colestasis crónica':3,'Reacción a fármacos':4,
'Enfermedad de úlcera péptica':5,'SIDA':6,'Diabetes':7,'Gastroenteritis':8,'Asma bronquial':9,'Hipertensión':10,
'Migraña':11,'Espondilosis cervical':12,
'Parálisis (hemorragia cerebral)':13,'Ictericia':14,'Paludismo':15,'Varicela':16,'Dengue':17,'Tifus':18,'Hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Hepatitis alcohólica':24,'Tuberculosis':25,
'Resfriado común':26,'Neumonía':27,'Hemorroides dimórficas (almorranas)':28,'Infarto de miocardio':29,'Varices':30,'Hipotiroidismo':31,
'Hipertiroidismo':32,'Hipoglucemia':33,'Osteoartritis':34,'Artritis':35,
'Vértigo Posicional Paroymsal':36,'Acné':37,'Infección de las Vías Urinarias':38,'Psoriasis':39,
'Impétigo':40}},inplace=True)

X= df[l1] ##CARACTERISTICAS DEL ENTRENAMIENTO
y = df[["Pronosticos"]]## ETIQUETAS DEL ENTRENAMIENTO
np.ravel(y)##NUEVAMENTE LOS PONEMOS DENTRO DE UN ARREGLO

#########ES UN MENSAJE QUE VERIFICA QUE LOS 5 SINTOMAS ESTEN INGRESADOS PARA HACER NAIVE BAYES
######### CASO CONTRARIO DEPLEGAMOS QUE SE INGRESE LOS SINTOMAS CORRECTAMENTE
def message():
    if (Sintoma1.get() == "None" and  Sintoma2.get() == "None" and Sintoma3.get() == "None" and Sintoma4.get() == "None" and Sintoma5.get() == "None"):
        messagebox.showinfo("INGRESA LOS SINTOMAS CORRECTAMENTE")
    else :
        NaiveBayes()
######### FUNCION NAIVE BAYES PARA LA PREDICCION DE LA ENFERMEDAD
def NaiveBayes():
    ##CREAMOS EL OBJETO GNB QUE REPRESENTA UN CLASIFICADOR DE BAYES MULTINOMIAL
    gnb = MultinomialNB()
    ##USAMOS EL METODO FIT PARA ENTRENAR EL CLASIFICADOR CON LOS DATOS X Y LAS ETIQUETAS Y QUE ANTES DEFINIMOS
    gnb=gnb.fit(X,np.ravel(y))
    ##LOS CLASIFICA Y LOS VUELVE A GUARDAR
    y_pred = gnb.predict(X_test)
    ##PARA EVALUAR NUESTRA PREDICCION EN BASE AL CONJUNTO DE DATOS DE PRUEBA
    ##E IMPRIMIMOS LA PRECISION NORMALIZADA Y NO NORMALIZADA
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    ##RECOPILACION DE SINTOMAS INGRESADOS POR EL USUARIOPARA LA PREDICCION
    Sintomas = [Sintoma1.get(),Sintoma2.get(),Sintoma3.get(),Sintoma4.get(),Sintoma5.get()]


    ##L2 SE ACTUALIZA CON LOS SINTOMAS QUE PREDEFINIMOS EN L1 SI UN SINTOMA NO COINCIDE CON EL DE L1
    ##SE ACTUALIZA AL VALOR CORRESPONDIENTE QUE ESTA EN L2
    for k in range(0,len(l1)):
        for z in Sintomas:
            if(z==l1[k]):
                l2[k]=1
    ##CREAMOS UNA LISTA DE PRUEBA QUE CONTINENE LOS VALORES ACTUALIZADOS DE LOS SINTOMAS EN L2
    ##SE USA NUEVAMENTE EL CLASIFICADOR (GNB) Y GUARDAMOS EL RESULTADOS EN PREDICCION
    prueba = [l2]
    prediccion = gnb.prediccion(prueba)
    prediccionaux=prediccion[0]

    ##COMPARAMOS LAS PREDICCIONES CON LAS ALMACENADAS EN NUESTRA LISTA DE ENFERMEDADES
    ##Y SI ENCUENTRA LA COINCIDENCIA CAMBIA EL VALOR A YES
    h='no'
    for a in range(0,len(Enfermedad)):
        if(Enfermedad[prediccionaux] == Enfermedad[a]):
            h='yes'
            break
    ##VERIFICAMOS SI EL VALOR DE H ES YES Y MUESTRA EL NOMBRE DE LA ENFERMEDAD
    ##CASO CONTRARIO MOSTRAMOS NO TIENE ENFERMEDAD
    ##(NOTA)SIEMPRE NOS SALDRA QUE TIENE ALGUNA ENFERMEDAD YA QUE SIEMPRE SE PRESENTARAN SINTOMAS
    ##Y SI O SI TIENE ALGO
    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, Enfermedad[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "NO TIENE ENFERMEDAD")
#################################################################################################################
#################################################################################################################
#### ESTO SOLAMENTE FUE CREADO PARA HACER LA PRUEBA QUE FUNCIONABA EL ALGORITMO ##############
#### NO VA ESTO EN EL PROYECTO FINAL, PERO POR SI  SE LOS COMENTO #####################

#### VENTANA DE INTERFAZ
root = Tk()
root.title(" PREDICCION DE ENFERMEDADES USANDO ML, ALGORITMO NAIVE BAYES ")
root.configure()

#### CONFIGURACION DE VENTANA PRINCIPAL
#### CREAMOS 6 VARIABLES STRINGVAR PARA SELECCIONAR LOS SINTOMAS
Sintoma1 = StringVar()
Sintoma1.set(None)
Sintoma2 = StringVar()
Sintoma2.set(None)
Sintoma3 = StringVar()
Sintoma3.set(None)
Sintoma4 = StringVar()
Sintoma4.set(None)
Sintoma5 = StringVar()
Sintoma5.set(None)

#### LABELS PARA MOSTRAR TEXTO EN LA INTERFAZ
#### ESTO SE CREA EN BASE A FILAS Y COLUMNAS
w2 = Label(root, justify=LEFT, text=" PREDICCION DE ENFERMEDADES USANDO ML, ALGORITMO NAIVE BAYES ")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)

NameLb1 = Label(root, text="")
NameLb1.config(font=("Elephant", 20))
NameLb1.grid(row=5, column=1, pady=10,  sticky=W)

S1Lb = Label(root,  text="SINTOMA 1")
S1Lb.config(font=("Elephant", 15))
S1Lb.grid(row=7, column=1, pady=10 , sticky=W)

S2Lb = Label(root,  text="SINTOMA 2")
S2Lb.config(font=("Elephant", 15))
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root,  text="SINTOMA 3")
S3Lb.config(font=("Elephant", 15))
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root,  text="SINTOMA 4")
S4Lb.config(font=("Elephant", 15))
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root,  text="SINTOMA 5")
S5Lb.config(font=("Elephant", 15))
S5Lb.grid(row=11, column=1, pady=10, sticky=W)

lr = Button(root, text="PREDICCION",height=2, width=20, command=message)
lr.config(font=("Elephant", 15))
lr.grid(row=15, column=1,pady=20)

OPTIONS = sorted(l1)

#### ESTO ES PARA LA SELECCION EN EL MENU DEPLEGABLE
S1En = OptionMenu(root, Sintoma1,*OPTIONS)
S1En.grid(row=7, column=2)

S2En = OptionMenu(root, Sintoma2,*OPTIONS)
S2En.grid(row=8, column=2)

S3En = OptionMenu(root, Sintoma3,*OPTIONS)
S3En.grid(row=9, column=2)

S4En = OptionMenu(root, Sintoma4,*OPTIONS)
S4En.grid(row=10, column=2)

S5En = OptionMenu(root, Sintoma5,*OPTIONS)
S5En.grid(row=11, column=2)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 20))
NameLb.grid(row=13, column=1, pady=10,  sticky=W)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 15))
NameLb.grid(row=18, column=1, pady=10,  sticky=W)
#### CREAMOS UN CUADRO PARA MOSTRAR LA ENFERMEDAD
t3 = Text(root, height=2, width=30)
t3.config(font=("Elephant", 20))
t3.grid(row=20, column=1 , padx=10)
#### ABRIMOS LA VENTANA MODO LOOP
root.mainloop()