
from distutils.core import setup
setup(
  name = 'shad',
  packages = ['shad'],
  version = '5.4.6',
  license='MIT', 
  description = 'shad library is a unofficial library for making bot in the shad. this library works with shad’s API',
  long_description='docs are ready at shadlib.ml',
  long_description_content_type='text/html',
  author = 'Mehdi0032',
  author_email = 'nehdi.hamid0012@gmail.com',
  url = 'https://github.com/Mehdi0032',
  download_url = 'https://github.com/archive/refs/tags/v_546.tar.gz',
  keywords = ["shad","bot","robot","library","shadlib","shadlib.ml","shadlib.ir","shad.ir"],
  install_requires=[
          'requests',
          'pycryptodome==3.10.1',
          'urllib3',
          'tqdm'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',   
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
