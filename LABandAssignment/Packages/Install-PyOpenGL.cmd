pushd "%~dp0"

py -3.7 -m pip install .\lib\numpy-1.16.1-cp37-cp37m-win_amd64.whl
py -3.7 -m pip install .\lib\scipy-1.2.1-cp37-cp37m-win_amd64.whl
py -3.7 -m pip install .\lib\pygame-1.9.4-cp37-cp37m-win_amd64.whl
py -3.7 -m pip install .\lib\PyOpenGL-3.1.3b2-cp37-cp37m-win_amd64.whl
py -3.7 -m pip install .\lib\PyOpenGL_accelerate-3.1.3b2-cp37-cp37m-win_amd64.whl

copy .\lib\glut\freeglut.dll C:\Windows
