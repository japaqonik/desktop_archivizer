# Desktop Archivizer
Simple pyhon script that on run takes all files/directories from Desktop and pack it into another directory with name given as argument with subfolder named by todays date. Compiled to .exe and puted into autostart will help to keep your desktop clean.
###### How to build .exe file?
`pip install pyinstaller`

`pyinstaller .\src\main.py -c --onefile -i .\pic\storage.ico`

###### Usage:
```
usage: main.py [-h] [-s] [-v] archive_name

positional arguments:
  archive_name   Name of directory that will be created on Desktop. It will keep each day archive.

options:
  -h, --help     show this help message and exit
  -s, --silent   do not print progress bar
  -v, --verbose  increase output verbosity
  ```
