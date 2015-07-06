#!/usr/bin/env python

from distutils.core import setup

setup(name='palib',
      version='1.0',
      description='python bindings for pulseaudio',
      author='Harry Karvonen',
      author_email='harry.karvonen@gmail.com',
      license='GPLv3+',
      url='https://code.google.com/p/pypactl/',
      packages=['palib'],
      provides=['palib'],
#     download_url='http://datatomb.de/~valodim/libpulseaudio-1.1.tar.gz'
     )
