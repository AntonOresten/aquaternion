from setuptools import setup, find_packages

VERSION = '0.2.0'
DESCRIPTION = 'A package for Quaternion arithmetic'

setup(
    name="aquaternion",
    version=VERSION,
    author="Periareion (Anton Sollman)",
    author_email="<periareion05@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['3D', 'rotation', 'quaternion'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

