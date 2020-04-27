# Neighborhood Delivery Tracker

Since the COVID-19 outbreak in the U.S., I have been working from home (lucky me).  My "office" is in my bedroom which faces my street. I can see all the traffic when I'm at my desk and that includes delivery trucks and food delivery services.

I started keeping track of every delivery truck I would see for no real reason other than to collect some data to play with.  The initial data collection was in an excel spreadsheet which worked well because I could access it via OneDrive from any device.  However, this became a little messy when doing calculations and making charts.  I am also more handy with Python and the Pandas module than I am with Excel.  Why not keep my current Python skills sharp while learning new things like plotting and database IO?

So, here's what I came up with:

The sqlite database is in a cloud accessible location.  I am now limited to using a desktop computer but the database is accessible anywhere.

**create-data.py**
- Using the sqlite3 module, this script opens or creates a new sqlite database and creates the table to store my observations.

**port-excel.py**
- Clean up column names in spreadsheet
- Move data from original spreadsheet to the sqlite db.

**manage-deliveries.py**
- CLI for adding a new delivery and viewing the data.
- Use today's date or type a custom date

**manage-deliveries.bat**
- Simple batch file to run the script with a variable flag:
```
View or Insert deliveries:
Flags:
        'add': Add a new delivery to the table
        'view': View all existing deliveries
        'count': Get a count of deliveries grouped by company
```
**AnalyzeDeliveries.ipynb**
- Query the deliveries database
- Get counts of companies
- Plot delivery counts

Sample data:
```
INSERT INTO deliveries (Date, Company, MyHouse) VALUES ("04/20/2020", "Amazon", "Yes");
INSERT INTO deliveries (Date, Company, MyHouse) VALUES ("04/20/2020", "Fed Ex", "No");
INSERT INTO deliveries (Date, Company, MyHouse) VALUES ("04/20/2020", "UPS", "No");
INSERT INTO deliveries (Date, Company, MyHouse) VALUES ("04/20/2020", "Uber Eats", "Yes");
```

If the following error occurs:
```
File "C:\ProgramData\Anaconda3\lib\sqlite3\dbapi2.py", line 27, in <module>
    from _sqlite3 import *
ImportError: DLL load failed: The specified module could not be found.
```
Add the Conda env Lib/Path path to the %PATH% variable (assuming Windows).
``` C:\ProgramData\Anaconda3\envs\python38\Library\bin ```

TODO:
- New UI to add and view deliveries from a mobile device. Web?
- Pre-process inout values.  Clean entered date values and strip special chars.  Restrict weird values.

