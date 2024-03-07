'''
Copyright (c) 2024 MPI-M, Clara Bayley


----- NextGEMS_hackathon_cycle4 -----
File: run_python.py
Project: scripts
Created Date: Tuesday 5th March 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Thursday 7th March 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
'''


import sys
import pathlib

path = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(path+'/../src/') # add path to project src folder to PATH

from loaddata import *

print_data()
