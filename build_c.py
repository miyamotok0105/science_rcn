#python build_c.py build
from distutils.core import setup, Extension
import numpy

dilation_module = Extension(
    '_dilation',
    sources=['science_rcn/dilation/dilation.cc'],
)

setup (name = 'dilation_module',
       version = '1.0',
       description = 'This is a dilation_module',
       include_dirs = [numpy.get_include()],
       ext_modules = [dilation_module])

