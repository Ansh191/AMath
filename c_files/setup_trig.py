from distutils.core import setup, Extension

module1 = Extension('_trig',
                    sources=['test.c'])

setup(name='_trig',
      version='0.1',
      description='Contains trigonometry functions',
      ext_modules=[module1])
