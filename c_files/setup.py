from distutils.core import setup, Extension

module1 = Extension('_basic',
                    sources=['_basic.c'])

setup(name='_basic',
      version='0.1',
      description='Basic functions',
      ext_modules=[module1])
