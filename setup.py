#/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
"""
    Useful Python scripts and functions for APS 7BM data processing.
    This setup.py was created by DD in order to allow cython compilation
    on a wide range of Python environments using distutils.
    
    @author Alan Kastengren <akastengren@anl.gov>
    @author Daniel Duke <daniel.duke@monash.edu>
    
    @version 1.0.0
    @date 07/20/2018
    
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy # This ensures we can compile cython code against numpy's libraries.

long_description = """Useful Python scripts and functions for APS 7BM data processing."""

cython_modules = [
    Extension(
        "aps7bmlib.ArrayBin_Cython",
        ["aps7bmlib/ArrayBin_Cython.pyx"],
    )
    # More cython modules can be added here in future
]

setup(name="aps7bmlib",
      version="1.0.0",
      description="Python functions for APS 7BM.",
      author="Alan Kastengren",
      author_email="akastengren@anl.gov",
      long_description=long_description,
      packages=['aps7bmlib'],
      package_dir={'': '.'}, # aps7bmlib can be found in the cwd
      url='https://www.aps.anl.gov/Sector-7/7-BM',
      ext_modules=cythonize(cython_modules),
      include_dirs=[numpy.get_include()]
)
