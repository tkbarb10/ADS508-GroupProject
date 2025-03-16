# **Space-Track Data Dictionary**

## **1️⃣ `launch_sites` Class**
| **Field**       | **Description** |
|----------------|----------------|
| `SITE_CODE`    | A short identifier (5-character code) representing a launch site. |
| `LAUNCH_SITE`  | The full name of the launch site. |

---

## **2️⃣ `satcat` Class (Satellite Catalog)**
| **Field**       | **Description** |
|----------------|----------------|
| `INTLDES`      | International Designator, also known as `OBJECT_ID`. A unique identifier for the satellite, formatted as `YYYY-NNNA`. |
| `NORAD_CAT_ID` | Also known as `OBJECT_NUMBER` or `Catalog Number`. A sequential number assigned by the US Space Force. |
| `OBJECT_TYPE`  | The classification of the object (e.g., `PAYLOAD`, `ROCKET BODY`, `DEBRIS`). |
| `SATNAME`      | The common name of the satellite or object. |
| `COUNTRY`      | The nation or entity responsible for the object. |
| `LAUNCH`       | The launch date of the object in `YYYY-MM-DD` format. |
| `SITE`         | Launch site code corresponding to `launch_sites.SITE_CODE`. |
| `DECAY`        | Date the object re-entered the Earth's atmosphere (if applicable). |
| `PERIOD`       | The time (in minutes) the object takes to complete one full orbit. |
| `INCLINATION`  | The angle (in degrees) between the equator and the orbit plane. |
| `APOGEE`       | The maximum altitude (in kilometers) of the object's orbit. |
| `PERIGEE`      | The minimum altitude (in kilometers) of the object's orbit. |
| `COMMENT`      | Additional information about the object. |
| `COMMENTCODE`  | Encoded comments related to the object. |
| `RCSVALUE`     | Radar Cross Section (RCS) value. Measures how detectable an object is by radar. |
| `RCS_SIZE`     | Size classification based on RCS (e.g., `SMALL`, `MEDIUM`, `LARGE`). |
| `FILE`         | Unique identifier for the source file containing the object's data. Higher numbers indicate more recent uploads. |
| `LAUNCH_YEAR`  | The four-digit year the object was launched. |
| `LAUNCH_NUM`   | The sequential launch number within the year. |
| `LAUNCH_PIECE` | A three-letter code identifying the object's piece within a launch. |
| `CURRENT`      | Indicates if the object is still in orbit (`Y` = Yes, `N` = No). |
| `OBJECT_NAME`  | Alternative name for the object, usually the same as `SATNAME`. |
| `OBJECT_ID`    | Same as `INTLDES`, representing the **International Designator**. |
| `OBJECT_NUMBER`| Same as `NORAD_CAT_ID`, the catalog number assigned by US Space Force. |

---

## **3️⃣ `tip` Class (Tracking & Impact Prediction)**
| **Field**        | **Description** |
|-----------------|----------------|
| `NORAD_CAT_ID`  | Unique identifier for the object (same as `OBJECT_NUMBER`). |
| `MSG_EPOCH`     | The timestamp when the message was generated. |
| `INSERT_EPOCH`  | The timestamp when the record was inserted into the database. |
| `DECAY_EPOCH`   | The predicted date and time when the object will re-enter Earth's atmosphere. |
| `WINDOW`        | The uncertainty window (in minutes) around the predicted decay time. |
| `REV`           | The object's revolution number at the time of the message. |
| `DIRECTION`     | Orbital direction (`ascending` or `descending`). |
| `LAT`           | Latitude (in degrees) of the predicted decay point. |
| `LON`           | Longitude (in degrees) of the predicted decay point. |
| `INCL`          | Orbital inclination (degrees). |
| `NEXT_REPORT`   | Time until the next expected TIP report. |
| `ID`            | Internal tracking ID for the message. |
| `HIGH_INTEREST` | Indicates if the object is of high interest (`Y` = Yes, `N` = No). |
| `OBJECT_NUMBER` | Catalog number assigned by US Space Force (same as `NORAD_CAT_ID`). |

---

## **4️⃣ `decay` Class (Reentry Predictions)**
| **Field**        | **Description** |
|-----------------|----------------|
| `NORAD_CAT_ID`  | Unique identifier for the object (same as `OBJECT_NUMBER`). |
| `OBJECT_NUMBER` | Catalog number assigned by US Space Force. |
| `OBJECT_NAME`   | Common name of the object. |
| `INTLDES`       | International Designator (same as `OBJECT_ID`). |
| `OBJECT_ID`     | Same as `INTLDES`, representing the **International Designator**. |
| `RCS`           | Radar Cross Section (RCS) value. |
| `RCS_SIZE`      | Size classification based on RCS (`SMALL`, `MEDIUM`, `LARGE`). |
| `COUNTRY`       | The nation responsible for the object. |
| `MSG_EPOCH`     | The timestamp when the message was generated. |
| `DECAY_EPOCH`   | The predicted or actual decay date/time of the object. |
| `SOURCE`        | The organization providing the decay prediction. |
| `MSG_TYPE`      | Type of message (e.g., `TIP` for Tracking & Impact Prediction). |
| `PRECEDENCE`    | Lower values indicate more recent data. |

---

## **5️⃣ `boxscore` Class (Satellite Statistics by Country)**
| **Field**                     | **Description** |
|------------------------------|----------------|
| `COUNTRY`                    | The country or entity associated with the objects. |
| `SPADOC_CD`                  | Space Defense Operations Center code for the country. |
| `ORBITAL_TBA`                | Number of objects **To Be Announced** in orbit. |
| `ORBITAL_PAYLOAD_COUNT`      | Number of payloads currently in orbit. |
| `ORBITAL_ROCKET_BODY_COUNT`  | Number of rocket bodies currently in orbit. |
| `ORBITAL_DEBRIS_COUNT`       | Number of debris objects currently in orbit. |
| `ORBITAL_TOTAL_COUNT`        | Total number of orbital objects (sum of payloads, rocket bodies, and debris). |
| `DECAYED_PAYLOAD_COUNT`      | Number of payloads that have decayed (re-entered atmosphere). |
| `DECAYED_ROCKET_BODY_COUNT`  | Number of rocket bodies that have decayed. |
| `DECAYED_DEBRIS_COUNT`       | Number of debris objects that have decayed. |
| `DECAYED_TOTAL_COUNT`        | Total number of objects that have decayed. |
| `COUNTRY_TOTAL`              | Total number of tracked objects for the country, including orbital and decayed objects. |
