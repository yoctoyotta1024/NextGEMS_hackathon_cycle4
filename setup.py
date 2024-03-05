'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- NextGEMS_hackathon_cycle4 -----
File: setup.py
Project: NextGEMS_hackathon_cycle4
Created Date: Tuesday 27th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Tuesday 5th March 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
setup for pre-commit tool
'''


from setuptools import setup, find_packages

setup(
    name='NextGEMS_hackathon_cycle4',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'sphinx',
    ],
)
