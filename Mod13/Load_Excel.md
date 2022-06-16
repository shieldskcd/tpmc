# Note on Loading Excel Files

In the next lecture, we will learn how to load Excel files in Python with *pandas*. For this, you need *pandas* (which you already have) and also need to install two other dependencies that *pandas* needs for opening Excel files. 

You can install them with pip (modified for my specific issue):
`%pip install openpyxl` > Needed to load Excel .XLSX files
`%pip install xlrd` > Needed to open *old* .XLS files