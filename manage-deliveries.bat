ECHO OFF
set flag = %1
set id = %2
C:/ProgramData/Anaconda3/python.exe c:/data/covid-python/manage-deliveries.py %1 %2
PAUSE