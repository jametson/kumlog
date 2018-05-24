from setuptools import setup

# Package details
setup(
    name="kumlog",
    version="0.0.1",
    author="Alam Listyadi",
    author_email="alam.listyadi@gmail.com",
    url="https://github.com/jametson/kumlog",
    description="Kumparanian Log Format",
    long_description=open("README.rst", "r").read(),
    license="BSD 3-Clause License",
    packages=[
        "logformat",
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)