@ECHO OFF

ECHO --------------------------------------------

ECHO Lot - Zoning Incremental Update

ECHO --------------------------------------------

ECHO User is %USERNAME%

cd /d "%~dp0src"

ECHO Loading Python Environment files...

::Update to reference location of python environment
::"C:\Users\%USERNAME%\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\python.exe" "Lot Planning Refresh.py" %USERNAME%
"G:\Strategy\GPR\10. Support Applications & Tools\Python\ArcGIS Environment Files\arcgispro-py3-clone\python.exe" "Lot Planning Refresh.py" %USERNAME%

PAUSE
