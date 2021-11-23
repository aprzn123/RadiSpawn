from setuptools import setup

setup(
    name='radispawn',
    version='0.0.1',
    description='Launch programs and scripts using a radial menu.',
    py_modules=['radispawn.py'],
    package_dir={'' :'src'},
    install_requires=['PySide6']
)
