from distutils.core import setup, Extension

module1 = Extension('_iter',
                    sources=['_iter.c'])
                    # extra_compile_args=['/Zi'],
                    # extra_link_args=['/DEBUG'])

setup(name='_iter',
      version='0.1',
      description='Contains iteration stuffs',
      ext_modules=[module1])
