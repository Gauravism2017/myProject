from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("N_Queens.py")
)
