from cx_Freeze import setup, Executable
import os
build_exe_options = {"packages": ["numpy", "idna"]} 
executables = [Executable('main.py')]
os.environ['TCL_LIBRARY'] = "C:\\help\\tcl\\tcl86t.dll"
os.environ['TK_LIBRARY'] = "C:\\help\\tcl\\tk86t.dll"
setup(name='test_task',
       options = {"build_exe": build_exe_options },
      version='0.0.1',
      description='My test task',
      executables=executables)