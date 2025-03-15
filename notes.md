# General Project

- make sure to get the versions of each package installed and set it in stone so it can continue to be rerun

**examples**

!pip install --disable-pip-version-check -q pip --upgrade > /dev/null
!pip install --disable-pip-version-check -q wrapt --upgrade > /dev/null  *prevent pip upgrade*

!pip install --disable-pip-version-check -q awscli==1.18.216 boto3==1.16.56 botocore==1.19.56 *template for all packages*

- include sources in design doc and readme for all data sources
- Will probably need a definitions sections for all the acronyms
- Can use NORAD CAT ID from simplified collision data to get the name from full satcat to get the info from full ESA to pinpoint top 100 at risk of collision objects and idenfity common features


# Entities DF from ESA

- I can connect this to objects but it'll take awhile, probably have that or similar data in the CelesTrek or Space-Track data


# Celestrek 

- Scraped the lost object data from their webpage

# Goal 1: Analyzing object and debris growth from 1960 to present

- Can use the full satcat data from celestrek.  Can use it to plot # of objects by launch date ,the accumulation of objects over time, can break it down by type and by orbit
- Can merge with full esa data to break down by ObjectClass

# Goal 2: Predicting debris growth in LEO

- Use the leo_objects data from space track.  should be able to get all relevant info just from that one

# Goal 3: Clustering density for top 5 areas

- should be able to use full satcat and the esa data for location and size data

# Goal 4: Collision probability

- use full_esa (or satcat), simplified collision data, and lost_object data
- (we also have decayed object data and the historical tracking predictions so might be able to combine some of that to validate future predictions)


# ESA Full Data

- Can drop VimpelID, that just connects to another tracking org
- Lot of NA's, can drop all the records that are missing if there are no identifiers