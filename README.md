# TodoPY
![Estructura de la App</span><span>](https://github.com/rodragon737/TodoPY/blob/main/estructuras.PNG)
## python --version
Python 3.11.3							
## comenzamos con pip
pip install virtualenv

virtualenv venv --python=python3.11    		##<---

## Dentro de la carpeta ejecutar

.\venv\scripts\activate						## "deactivate" trun off

pip install flask							## install flask ¡¡¡¡¡ Importante se instala dentro del VENV !!!!!

pip freeze									## vemos dependencias

notepad requirements.txt					## Cramos requirements.txt y agragamos dependencias que se instalaran con pip

pip install -r requirements.txt				## instala las dependencias necesarias de python

## empezamos con el main.py  

$env:FLASK_APP="main.py"					##variable de env

flask run									## revisar http://127.0.0.1:5000

$env:FLASK_DEBUG=1							## Variable de debug ON

$env:FLASK_ENV="development"				##Entorno de test para evitar prod

## Conectarse a db Firebase Google

gcloud auth application-default login		##Login on GCP

## Ver entorno de Gcloud

gcloud config list

## Creacion del deploy de proyecto en G-Cloud

gcloud app deploy app.yaml
