@ECHO OFF

ECHO ----------------------------------------------------------

ECHO Creating/Replace PlanningDB.SDE connection file...

ECHO ----------------------------------------------------------

cd /d "%~dp0src"

::Update to refer to location of Python environment
"C:\Users\%USERNAME%\AppData\Local\ESRI\conda\envs\arcgispro-py3-clone\python.exe" "Configure SDE Connection.py" %USERNAME%
::"G:\Strategy\GPR\10. Support Applications & Tools\Python\ArcGIS Environment Files\arcgispro-py3-clone\python.exe" "Configure SDE Connection.py" %USERNAME%

PAUSE
