## Introduction

A program to generate Inversion functions for the Jaynes-Cummings model, in particular to illustrate the phenomenon of collapse and revival.


## Installation

This program require installation of the Python module *matplotlib*.
It furthemore makes use of the following default modules:
⋅ *csv*
⋅ *itertools*
⋅ *decimal*
⋅ *datetime*
⋅ *math*

Testing was done through *pytest*.

To install the program, simply download and have all the four modules (**Simulation**, **Graphing**, **Config** & **Main**) in the same folder.

[Link to the GitHub repository.](https://github.com/Qualcunaltro/Exam_Project)


## How to Use

Before starting the program, set up the parameters in the **Config** module.
The parameters are:

⋅ Average number of photons in the system (**N_e**): this must be an integer, positive number. To see the collpse and revival effect, it should be 4 or more.

⋅ Time interval for the simulation (**T_x**): this must be either an integer or a decimal number up to 0.1, and in every case positive.
⋅ The approximation level for summations (**approx**), i.e. how many terms to consider in summation that would be, in theory, infinite: this is a positive integer value.

⋅ The animation time constant (**time_const**): the animated graph framerate is not constant, but dinamically decreases with increasing number of points, so that its duration doesn't become too long for longer time windows. 
If the animated graphs are still taking too long, decrease this integer, and viceversa.

⋅ Animated graph check (**anime**): a boolean value to determine if the produced graph is animated (True) or static (False).

⋅ Saving data check (**save**): a boolean value to determine if the data set produced is to be saved in a .csv file (True) or not (False)

Once the parameters have been set, to start the program execute the module **Main**.

To save static graph as images, use the interface in the image window.
Attempting to do the same to an animated graph will only save the current frame.
If the data had been requested as saved, a .csv file with the current time will be found in the folder where the modules are installed.


