import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="urup",
    version="0.1",
    author="Thomas Titscher",
    author_email="thomas.titscher@gmail.com",
    description="Convert commented python code to markdown",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TTitsche/Urup",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={'console_scripts': ['urup=urup.to_md:main']}
)
