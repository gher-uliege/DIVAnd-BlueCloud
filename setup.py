#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author: Giancarlo Panichi
#
# Created on 2020/06/12
#
import setuptools

with open("README.md", "r") as freadme:
    l_description = freadme.read()

with open("LICENSE.md", "r") as flicense:
    license_description = flicense.read()


setuptools.setup(
    name="sortapp",
    version="1.0.0",
    author="Giancarlo Panichi",
    author_email="giancarlo.panichi@isti.cnr.it",
    description="A application for sort un text file",
    long_description=l_description,
    long_description_content_type="text/markdown",
    license=license_description,
    url="https://code-repo.d4science.org/gCubeSystem/sortapp",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    entry_points={
        'console_scripts': [
            'sortapp=sortapp.sortapp:main',
            'DIVAnd=sortapp.sortapp:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: European Union Public Licence :: 1.1",
        "Operating System :: OS Independent",
    ],
    platforms=["Linux"],
    python_requires='>=3.6',
)
