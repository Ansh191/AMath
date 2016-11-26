from distutils.core import setup, Extension

module1 = Extension('DateObject',
                    sources=['DateObject.c'])

setup(name='DateObject',
      version='0.1',
      description='DateObject',
      ext_modules=[module1])
