from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
#importamos los sintomas que tendremos en nuestra ia, los cuales ayudan a predecir la afeccion que padece
l1 = ['picazón', 'erupciones_cutáneas', 'erupciones_nodales_cutáneas', 'estornudos_continuos', 'temblores', 'escalofríos', 'dolor_articular',
     'dolor_de_estómago', 'acidez', 'úlceras_en_la_lengua', 'desgaste_muscular', 'vómitos', 'ardor_micción', 'manchas_ al orinar', 'fatiga',
     'aumento_de_peso', 'ansiedad', 'manos_y_pies_fríos', 'cambios_de_ánimo', 'pérdida_de_peso', 'inquietud', 'letargo', 'parches_en_la_garganta',
     'nivel_de_azúcar_irregular', 'tos', 'fiebre_alta', 'ojos_hundidos', 'falta de aliento', 'sudoración', 'deshidratación', 'indigestión',
     'dolor_de_cabeza', 'piel_amarillenta', 'orina_oscura', 'náuseas', 'pérdida_de_apetito', 'dolor_detrás_de_los_ojos', 'dolor_de_espalda', 'estreñimiento',
     'dolor_abdominal', 'diarrea', 'fiebre_leve', 'orina_amarilla', 'coloración_amarillenta_de_los_ojos', 'insuficiencia_hepática_aguda', 'sobrecarga_de_líquidos',
     'hinchazón_del_estómago', 'ganglios_linfáticos_hinchados', 'malestar_general', 'visión_borrosa_y_distorsionada', 'flema', 'irritación_de_la_garganta',
     'enrojecimiento_de_ojos','presión_sinusal','secreción_nasal','congestión','dolor_de_pecho','debilidad_en_extremidades','ritmo_cardiaco_rápido',
     'dolor_durante_las_defecaciones','dolor_en_la_región_anal','heces con sangre','irritación_en_el_ano','dolor_de_cuello','mareos','calambres',
     'hematomas', 'obesidad', 'piernas_hinchadas', 'vasos_sanguíneos_hinchados', 'cara_y_ojos_hinchados', 'tiroides_agrandada', 'uñas_quebradizas',
     'extremidades_hinchadas', 'hambre_excesiva', 'contactos_extramatriciales', 'sequedad_y_hormigueo_en_los_labios', 'dificultad_para_hablar', 'dolor_en_las_rodillas', 'dolor_en_las_articulaciones_de_la_cadera',
     'debilidad_muscular','rigidez_de_cuello','hinchazón_de_articulaciones','rigidez_de_movimiento','movimientos_giratorios','pérdida_de_equilibrio','inestabilidad','debilidad_de_un_lado_del_cuerpo',
     'pérdida_del_olfato', 'malestar_de_la_vejiga', 'mal_olor_de_la_orina', 'micción_frecuente', 'paso_de_gases', 'picazón_interna', 'aspecto_tóxico_(tifus)',
     'depresión', 'irritabilidad', 'dolor_muscular', 'sensorio_alterado', 'manchas_rojas_en_el_cuerpo', 'dolor_de_vientre', 'menstruación_anormal', 'parches_discrómicos',
     'lagrimeo_de_los_ojos', 'aumento_del_apetito', 'poliuria', 'antecedentes_familiares', 'esputo_mucoide', 'esputo_oxidado', 'falta_de_concentración', 'alteraciones_visuales',
     'recibir_transfusión_de_sangre','recibir_inyecciones_no_estériles','coma','sangrado_estómago','distensión_del_abdomen','antecedentes_de_consumo_de_alcohol',
     'sobrecarga_de_fluidos', 'sangre_en_el_esputo', 'venas_prominentes_en_la_pantorrilla', 'palpitaciones', 'dolor_al_caminar', 'espinillas_llenas_de_pus', 'puntos_negros', 'escurrimiento', 'descamación_de_la_piel',
     'polvo_similar_a_la_plata','pequeñas_abolladuras_en_las_uñas','uñas_inflamadas','ampollas','llaga_roja_alrededor_de_la_nariz','exudado_costra_amarilla'
]

enfermedad = [ 'Infección Fungica','Alergia','ERGE','Colestasis crónica','Reacción a Fármacos',
                'Enfermedad de úlcera péptica','SIDA','Diabetes','Gastroenteritis','Asma bronquial','Hipertensión',
                'Migraña','Espondilosis cervical',
                'Parálisis (hemorragia cerebral)','Ictericia','Paludismo','Varicela','Dengue','Tifus','Hepatitis A',
                'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Hepatitis Alcohólica','Tuberculosis',
                'Resfriado Común','Neumonía','Hemorroides Dimórficas (almorranas)',
                'Infarto','Varices','Hipotiroidismo','Hipertiroidismo','Hipoglucemia','Osteoartritis',
                'Artritis','(Vértigo) Vértigo Posicional Paroymsal','Acné','Infección Urinaria','Psoriasis',
                'Impétigo'
    
]