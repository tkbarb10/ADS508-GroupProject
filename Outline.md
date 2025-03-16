# EDA Process

- Basic info, descriptive stats and data types
- How to handle missing values in each dataset?
- Feature engineering.  What columns to remove?  Anything new features we can create that will be helpful?  Change data types accordingly (some of the date columns for instance)
- Any outliers among the numerical data?
- Once data is to our liking, create a DB and individual tables within for each dataset

## AWS Tools

- Clarify to detect bias among the categorical classes we're interested in (such as ObjectClass)
- Athena for table creation

---


# Goal 1: Analyzing object and debris growth from 1960 to present

- Can use the full satcat data from celestrek.  Can use it to plot # of objects by launch date ,the accumulation of objects over time, can break it down by type and by orbit
- Can merge with full esa data to break down by ObjectClass

## AWS Tools

- Athena
- Quicksight?

## Visuals

- Growth of objects
- Growth of debris
- Facet by objectClass

---

# Goal 2: Predicting debris growth in LEO

- Use the leo_objects data from space track.  Should be able to get all relevant info just from that one

## AWS Tools

- AutoML (Regression)

## Visuals

- Line plot with CI shading

---

# Goal 3: Clustering density for top 5 areas

- should be able to use full satcat and the esa data for location and size data

## AWS Tools

- Athena for filtering

## Other tools/methods

- Kmeans and DBSCAN

## Visuals

- 2d? Maybe we can find a way to make a 3d plot in AWS?

---

# Goal 4: Collision probability

- use full_esa (or satcat), simplified collision data, and lost_object data
- (we also have decayed object data and the historical tracking predictions so might be able to combine some of that to validate future predictions)

## AWS Tools

- AutoML (regression)