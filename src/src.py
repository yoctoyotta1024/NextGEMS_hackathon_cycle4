'''
Copyright (c) 2024 MPI-M, Clara Bayley


----- NextGEMS_hackathon_cycle4 -----
File: src.py
Project: src
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


import numpy as np

def hello_world():
  """
  Prints 'Hello World!'.

  This function doesn't take any parameters.
  """

  print("Hello World!")

def area_circle(radius):
  """
  Calculate the area of a circle.

  Parameters:
      radius (float): The radius of the circle.

  Returns:
      float: The area of the circle.

  Examples:
    >>> area_circle(4.0)
    50.26548245743669...
  """

  return np.pi * radius * radius
