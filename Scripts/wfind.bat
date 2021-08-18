@echo off

set fileName=%1

python "C:\Scripts\wfinder.py" %CD% %fileName%

pause
cls