# Full esa data

- removing these columns but we aren't using them ['vimpelId', 'satno', 'predDecayDate', 'active', 'mission', 'shape', 'mass', 'width', 'height', 'depth', 'xSectMax', 'xSectMin'] (*selection*)

    - first 5 either have too many missing values (like active), are redundant info (satno) or are ID's from other catalogues and don't provide any more useful info (vimpelId)
    - Shape, mass, width, height and depth aren't need to make the predicitions we're trying to make
    - We have xSectAvg and that's enough to make collision estimates for our purposes

- first_epoch to datetime (*transformation*)
- I think we use the full_esa data to plot objectClass with the full differentiation, then collapse the values into the 4 object types when making LEO predictions (*transformation*)
- imputed the median for diameter, span, and xSectAvg (more resistant to outliers) then standardized them to prepare for modeling (*transformation*)


# LEO object data

- Dropping the following ['DECAY', 'COMMENT', 'COMMENTCODE', 'FILE', 'LAUNCH_YEAR', 'LAUNCH_NUM', 'RCSVALUE', 'OBJECT_NUMBER', 'OBJECT_ID, 'OBJECT_NAME, 'CURRENT'] (*selection*)
    - Some like Decay, Comment and RCSVALUE are empty.  CommentCode, File, Launch Num and Launch Piece aren't useful for what we're doing.  Launch_year we already have with the full launch date.  Object number is the same as Norad Cat ID. OBJECT_ID and INTLDES are the same.  OBJECT_NAME and SATNAME are the same.  Current is all Y values

- NORAD CAT ID to string from int and change launch to datetime (*transformation*)
- For missing values in RCS_SIZE, impute the distribution of the corresponding class (*transformation*)


# Full satcat

- Dropping ['Unnamed: 0', 'DATA_STATUS_CODE', 'RCS', 'OPS_STATUS_CODE']
    - The codes are unnecessary for our purposes.  RCS is the estimated Cross-Sectional size of the object in meters, we're using the binned category values instead (*selection*) (**Though maybe best to transform RCS into binned values**)
- Subsetting ORBIT CENTER values that aren't Earth and dropping since we don't care about object beyond earth's orbit (*selection*)
- For Object Type, change values to full name for clarity and consistency with the other data frames (*transformation*)
- Change Period, apogee, inclination and perigee to 0 if the orbit type is impact or landing, even if the values are positive, since that was the last recorded data, not current information (*transformation*)
- for the rest of the NA values in PERIOD, INCLINATION, etc, subsetting by Orbit Type 'ORB' and filling with the median, otherwise the median value is 0 (*transformation*)
- Adding a 'HAS_DECAYED' binary column.  We want to keep decay dates, and this covers the close to 30k NA values in there in case we want to use this for modeling


# Collision Data

- changing NORAD CAT ID's to strings (*transformation*)
- changing TCA to date time (*transformation*)
- Standardizing the numerical columns (*transformation*)


# Lost Object data

- Removing last row because it's an artifact from scraping the data
- Changing data types of norad ID to string and launch and last data dates to datetime objects (*transformation*)
- Changing names of Object type values to be consistent with the other dataframes