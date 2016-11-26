from distutils.core import setup, Extension

module1 = Extension('_system',
                    sources=['_system.c'])

setup(name='_system',
      version='0.1',
      description='Basic system commands',
      ext_modules=[module1])
