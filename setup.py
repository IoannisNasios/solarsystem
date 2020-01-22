import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="solarsystem", 
    version="0.1.1",
    author="Ioannis Nasios",
    author_email="nasioannis5@gmail.com",
    description="Our Solar System. Planet's positions, Sun's and Moon' s position and rise/set",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IoannisNasios/solarsystem",
    download_url="https://github.com/IoannisNasios/solarsystem/archive/0.1.1.tar.gz",
    packages=setuptools.find_packages(exclude=["docs", "examples"]),
    install_requires = [],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
