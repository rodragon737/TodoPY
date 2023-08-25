cls
echo ----"Recordar es necesario instalar Python 3.11"-----
echo -----------------------------------------------------
pause nul 

echo -----------"Cargando variables de entorno"-----------
$env:FLASK_APP="main.py" 
$env:FLASK_DEBUG=1
$env:FLASK_ENV="development" 
echo -----------------------------------------------------
pause nul

echo ------------"Instalando entorno virtual"-------------
pip install virtualenv
echo -----------------------------------------------------
echo ---------"Precione una tecla para continuar"---------
pause nul

echo -----"Instalando requerimientos de la aplicacion"----
pip install -r requirements.txt
echo -----------------------------------------------------
pause nul

echo  ------"Iniciando entorno virtual para la app"-------
.\venv\scripts\activate
echo -----------------------------------------------------
pause nul

echo ---------"Test y BluePrint de la aplicacion"---------
flask test
echo -----------------------------------------------------
pause nul

echo --"Iniciando la aplicacion  http://localhost:5000"---
echo -----------------------------------------------------
echo ---"Precionar teclas Ctrl+C para finalizar la app"---
echo -----------------------------------------------------
echo "Para terminar el entorno Virtual ingrese Deactivate"
echo ---"Cerrando el terminal finaliza de igual manera"---
echo -----------------------------------------------------
flask run

