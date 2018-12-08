# bg_club

## Overview ##

Application for Think Big Foundation, a division of Big Brothers Big Sisters of the Ozarks.

You can find out more about the organization at http://www.bigbro.com/do/thinkbig/. I also own/control  https://www.thepurplebin.org which will eventually be the production domain for this project. 


# Goal #
The goal of this app is to provide a Think Big Foundation (TBF) with data about their Purple Bin program. There are two main components to this project:
  1. Simple, easily accessible interface for driver(s) to input information of donation bin pickups using a mobile device.
  2. Admin backend to view data/reports, manage users, and manage bin locations.

# Completion Schedule #

The biggest push is to have the user portion of the website completed. Preferably before the end of 2018. 

In order to complete the user side, some functionality in the admin side will need to be completed. Fancy reporting options can be worked on later. The admin will only need a way to download raw data in CSV format so they can manipulate in Excel for the time being.

# Verbiage / Definitions #

Bins - Steel boxes (painted purple to maintain brand identity and visibility) strategically located Springfield, Missouri and a few surrounding towns. People are encouraged to donate used clothing, shoes, books, and a host of other items in these bins. There are currently two different sizes of bins, regular and large.

User(s) - Driver(s) of the TBF truck. They are responsible for servicing the bins on a selected route which includes driving to bin location, unloading materials, primary sorting, recording of collection information, and delivery of material back to warehouse.

Admin(s) - Manager who has access to backend to view data/reporting and CRUD ability on users and bin location database. 

# User Stories Actions

Users will login to the application from the home page.

Users will be redirected to a list of bin locations on successful login.

Users cannot register an account themselves.

Only logged in users will have access to pages other than login.

New users will be set to Admin = False by default. Admins can make other users admins or they can take away admin status.

# Admin Stories / Actions

There will be an '/admin' section that will contain forms for CRUD operations on various database models. Records belonging to these models
will be able to be deleted, edited, created and viewed.

Only admin users will have access to the '/admin' section. There will be an Admin link that displays in the navigation if the user is an
admin.


# User Flow

1. Login with username and password.
2. Redirect to list of bin locations.
3. Select bin location
4. Indicate fill level of each bin (0, 25, 50, 100)
5. Notes for anything irregular (Damage to bin, dumping, forbidden items, Other)
6. Submit data / Mark pickup complete

# User Inputs for Each Location

Bin location / address
Fill Level
Notes / irregularities

# Logic / Metrics

Location arrival time (timestamp of bin selection action)
Location departure time (timestamp of marking pickup complete action)
Time at location (departure time less arrival time
Average pickup time (by location, by driver)
Average time at location (by location, by driver)
Gross profit per bin (by location, day, week, month, year, driver)
  - The basic gross profit equation is Gross Profit = (Bin Size) * (Fill Level) * ((Revenue per ton)/2000)
  - Purely for example, with a bin size that holds 800 pounds, 50% fill level and revenue per ton of $140, the gross profit of the bin would look like 800 x 0.5 x 0.07 = $28.00.
  - Revenue for donated clothing will be set in the admin backend. It will likely be a dollar amount per ton such as $140/ton. 
  - Bin size - The bin size will be set per location in the admin backend. Each bin size will have a 'weight when full' attribute which is determined by management after performing a weight study/average.
  - Fill level - how full the bin at time of servicing by user.


# Future Feature Ideas #

- Suggested bin locations - If the user is in the parking lot of Price Cutter at 1831 W Kearney, that bin location would be at the top of 'bin selection page' based on GPS location of user and compared with coordinates of bin location stored in the database.

- Picture notes - In addition to text notes, ability to upload/attach picture to DB record.

- Truck selection - When a user signs in, they can select which truck they are driving that day. Record odometer at beginning/end of day.

- Landing page stats - On the home page (https://thepurplebin.org) have a running counter that has a few encouraging stats such as Revenue Generated, Kids Helped, Pounds Recycled, etc. These would be connected to the DB and update at regular intervals.
