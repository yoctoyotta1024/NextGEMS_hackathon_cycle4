'''
Copyright (c) 2024 MPI-M, Clara Bayley


* ----- NextGEMS_hackathon_cycle4 -----
File: run_python.py
Project: scripts
Created Date: Tuesday 5th March 2024
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
'''


import sys
import pathlib

path = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(path+'/../libs/') # add path to src_py to PATH

from src_py import mock

mock.hello_world()
