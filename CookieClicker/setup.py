import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"]}
base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup( name="Cookie Clicker",
	version="0.1",
	description="Spiel des Vapor Launcher",
	options={"build_exe": build_exe_options},
	executables=[Executable("main.py", base=base)])