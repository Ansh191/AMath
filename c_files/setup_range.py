from distutils.core import setup, Extension

module1 = Extension('range',
                    sources=['range.c'])

setup(name='range',
      version='0.1',
      description='Range',
      ext_modules=[module1])
