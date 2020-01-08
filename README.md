# trackbar_cv

This repository creates a simple parameterized open_cv trackbar for making live updates to an input image.

<br>

The trackbar is created with 2 key functions: a callback_function to handle parameter updates, and a function to draw the image

Use the callback_function to compute any changes from a parameter update. What is returned from the callback_function is provided to the draw function. 

<br>

Note: The python 2.7 code was moved to the python2.7 branch.
More documentation to follow

Note: (9/1/2019) Updated example.py to work around apparent opencv 4.0 bug.  Image must be uint8.
