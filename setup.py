import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ceres",
    version="1.0.1",
    author="Laurent MOULIN",
    author_email="gignops@noemail.com",
    description="As simple as possible code generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laulin/ceres",
    packages=["ceres"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyyaml',
        'mako'
    ], 
    scripts=['bin/ceres'],
)
