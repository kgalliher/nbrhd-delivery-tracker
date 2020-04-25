# Neighborhood Delivery Tracker

Since the COVID-19 outbreak in the U.S., I have been working from home (lucky me).  My "office" is in my bedroom which faces my street. I can see all the traffic when I'm at my desk and that includes delivery trucks and food delivery services.

I started keeping track of every delivery truck I would see for no real reason other than to collect some data to play with.  The initial data collection was in an excel spreadsheet which worked well because I could access it via OneDrive from any device.  However, this became a little messy when doing calculations and making charts.  I am also more handy with Python and the Pandas module than I am with Excel.  Why not keep my current Python skills sharp while learning new things like plotting and database IO?

So, here's what I came up with:

The sqlite database is now in a cloud accessible location.  I am now limited to using a desktop computer but the database is accessible anywhere.

create-data.py
- Using the sqlite3 module, this script opens or creates a new sqlite database and creates the table to store my observations.

port-excel.py
- Clean up column names in spreadsheet
- Move data from original spreadsheet to the sqlite db.

add-delivery.py
- CLI for adding a new delivery.
- Use today's date or type a custom date

AnalyzeDeliveries.ipynb
- Query the deliveries database
- Get counts of companies
- Plot delivery counts

TODO:
- New UI to add and view deliveries from a mobile device. Web?
- Pre-process inout values.  Clean entered date values and strip special chars.  Restrict weird values.
