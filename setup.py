from setuptools import setup

setup(name='neovim',
      version='0.0.4',
      description='Python client to neovim',
      url='http://github.com/neovim/python-client',
      download_url='https://github.com/neovim/python-client/archive/0.0.4.tar.gz',
      author='Thiago de Arruda',
      author_email='tpadilha84@gmail.com',
      license='MIT',
      packages=['neovim'],
      install_requires=[
          'msgpack-python',
          'pyuv',
      ],
      zip_safe=False)
