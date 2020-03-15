from distutils.core import setup, Extension

module1 = Extension('_statistics',
                    sources=['_statistics.c'])

setup(name='_statistics',
      version='0.1',
      description='Basic Statistical Functions',
      ext_modules=[module1])
