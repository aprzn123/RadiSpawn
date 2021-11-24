from setuptools import setup

setup(
    name='radispawn',
    version='0.0.1',
    description='Launch programs and scripts using a radial menu.',
    py_modules=['radispawn.py'],
    package_dir={'' :'src'},
    install_requires=['PySide6'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Utilities"
    ],
    entry_points={"console_scripts": ["radispawn = radispawn:main"]},
)
