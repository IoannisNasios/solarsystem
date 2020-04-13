import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

here = os.path.abspath(os.path.dirname(__file__))
# What packages are required for this module to be executed?
try:
    with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
        REQUIRED = f.read().split('\n')
except:
    REQUIRED = []

setuptools.setup(
    name="solarsystem", 
    version="0.1.4",
    author="Ioannis Nasios",
    author_email="nasioannis5@gmail.com",
    description="Our Solar System. Planet's positions, Sun's and Moon' s position and rise/set",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IoannisNasios/solarsystem",
    download_url="https://github.com/IoannisNasios/solarsystem/archive/0.1.4.tar.gz",
    packages=setuptools.find_packages(exclude=["docs", "examples", "tests"]),
    install_requires = REQUIRED,
    classifiers=[

        'Programming Language :: Python',
	"Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
	"Programming Language :: Python :: 3.7",
	"Programming Language :: Python :: 3.8",
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',

        "Topic :: Software Development :: Libraries",
	"Topic :: Software Development :: Libraries :: Python Modules",

        "Operating System :: OS Independent",
    ],
)
