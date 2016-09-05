import functools
import os
import sys
import tkinter

from cx_Freeze import setup, Executable
from functools import partial
from tkinter import ttk

build_exe_options = {"includes": ["Tkinter", "string", "ttk",
								  "functools"]}


setup(
	name='Calculator',
	version='3.0',
	description="""A calculator created in python which allows the user to \
	calculate square roots in addition to adding, subtracting, multiplying, \
	and dividing.""",
	options={"build_exe": build_exe_options},
	executables=[Executable('calculator.py', base='Win32GUI')])
