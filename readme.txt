-------------------ALISTAMIENTO DEL ENVIROMENT
INSTALAR WINDOWS TERMINAL DE LA MS STORE

INSTALAR POWERSHELL TAMBIEN DE LA MS STORE

INCIAR EL ENTORNO VIRTUAL 
*EN CASO QUE NO ESTE INSTALADO INSTALAR VIRTUALENV 

#iniciar el entorno virtual dentro de la carpeta del proyecto
PYTHON -M VIRTUALENV ENV (desde la carpeta donde esta el proyecto)

#instalamos django
pip install django==version (para nuestro proyecto 4.2.3)

#seteamos nuestra carpeta donde se ejecutara todo, el corazon de la carpeta, el centro del proyecto
django-admin startproject core . 

------------ABRIMOS EL VS CODE Y NOS SETEAMOS EN LA CARPETA DONDE ESTA EL PROYECTO

*************__init__.py ********* para que django reconozca la folder, siempre debe estar
-------------------------------------------------------------------------------------------------------------
EMPEZAREMOS USANDO URLS.PY 
Y TAMBIEN SETTIGS.PY QUE SON LOS MAS IMPORTANTES DE NUESTRO PROJECT

********** creamos nuestro requierements.txt y empezamos 
--------------------requierements.txt
# version de django instalada
django==4.2.3
# hace que contrasenias y todo lo que requiera seguridad, sea encriptado protecciones,autorizaciones
django-environ==0.10.0
# ver quien accede a mi api y dar o no acceso(se configura para que mas personas puedan acceder)
django-cors-headers==4.2.0
#
djangorestframework==3.14.0
#
Pillow==10.0.0
# para guardar imagenes y que se agreguen en un cdn
django-storages==1.13.2
#para mod opciones de texto negrita, tipo=italica, etc,etc,etc
django-ckeditor==6.6.1
# para trabajar con postgresql
psycopg2 2.9.6
**************INSTALAR TODAS LAS DEPENDENCIAS ANTERIORES (JUNTAS O SEPARADAD)

******************* creamos el archivo .env
que sirve para guardar contrasenias  que no se quieren revelar

******************* creamos el archivo .gitignore
sirve para controlar que queremos o no subir al git

******************* creamos el .gitignore (la creamos en linea con gitignore create)
---------------------------------------------------------------------------------------------codigo gitignore(copiado de createg
de todo ese proyecto comentamos build para que si se suba ya que ese necesitamos
tambien comentamos los statics y cerramos

--------------------------------------------------------------------------------------------hacemos el commit desde el mismo vs code
----------------------------------creamos una nueva rama llamada staging ***por si acaso nos equivoquemos ya que en master(main) no podemos
 
seguimos haciendo en el settings.py  y cambiamos los modos 
secret_key
debug
allowe_host

-------------------------------------------------------------------------
tambien en el settings creamos 
django_apps

project_apps

third_apps

con sus respectivas librerias
--------------------------------------------------------------------------------
creamos la carpeta media
--------------------------------------------------------------------------------
CTRL+SHIFT+P === PARA ABRIR LA DATABASE SQLITE
--------------------------------------------------------------------------------
instalamos tailwindcss

instalamos react-router-dom

instalamos mas herramientas para react 
redux redux-thunk react-redux redux-devtools-extension react-router-dom axios
#### consultar cada una #####
--------------------------------------------------------------------------------
REDUX es un contenedor de variables de estado
es decir el estado en q se encuentran y guardan nuestras variables y podemos acceder