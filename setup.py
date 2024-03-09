from setuptools import setup, Extension
from Cython.Build import cythonize
import pybind11

example_module = Extension(
    'example',
    sources=['example.cpp'],
    include_dirs=[pybind11.get_include()],
    language='c++',
    extra_compile_args=['-std=c++11'],
)

setup(
    name='example',
    version='0.1',
    description='A pybind11 example that passes a dict to C++ std::map',
    ext_modules=[example_module],
)
