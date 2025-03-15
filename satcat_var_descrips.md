# ESA Space Object Data Fields

This document provides descriptions of various fields used in the ESA's space object database.

## Field Descriptions

### **OBJECT_NAME**  
- Satellite Name(s)  
- **Object Types:**
  - **R/B(1)** = Rocket body, first stage  
  - **R/B(2)** = Rocket body, second stage  
  - **DEB** = Debris  
  - **PLAT** = Platform  
- Items in parentheses are alternate names.  
- Items in brackets indicate the type of object.  
  - Example: `BREEZE-M DEB [TANK]` = tank  
- An ampersand (&) indicates two or more objects are attached.

---

### **OBJECT_ID**  
- International Designator (`YYYY-NNNAAA`)  
  - **YYYY** = Launch year (4 digits)  
  - **NNN** = Launch sequence of the year (3 digits)  
  - **AAA** = Piece of the launch (1-3 alphabetic characters, excluding I and O)  

---

### **NORAD_CAT_ID**  
- NORAD Catalog Number  

---

### **OBJECT_TYPE**  
- **PAY** = Payload  
- **R/B** = Rocket body  
- **DEB** = Other debris  
- **UNK** = Unknown  

---

### **OPS_STATUS_CODE**  
- Operational Status Code  

---

### **OWNER**  
- Ownership of the object  

---

### **LAUNCH_DATE**  
- Launch Date `[year-month-day]` (ISO 8601)  

---

### **LAUNCH_SITE**  
- Launch Site  

---

### **DECAY_DATE**  
- Decay Date, if applicable `[year-month-day]` (ISO 8601)  

---

### **PERIOD**  
- Orbital period **[minutes]**  
- Null if no data available
- Refers to time it takes to make a full orbit around its central body  

---

### **INCLINATION**  
- Inclination **[degrees]**  
- Null if no data available
- Angle between the objects orbital plane and the equitorial plane of its central body  

---

### **APOGEE**  
- Apogee Altitude **[kilometers]**  
- Null if no data available  
- Highest point in an objects orbit from its central body
- 500km is LEO, 35,786 is GEO and 400,000 is Lunar

---

### **PERIGEE**  
- Perigee Altitude **[kilometers]**  
- Null if no data available 
- Closest point in an objects orbit to its central body 

---

### **RCS**  
- Radar Cross Section **[meters²]**  
- Null if no data available  

---

### **DATA_STATUS_CODE**  
- Data status code (blank otherwise)  
  - **NCE** = No Current Elements: Means not up to date
  - **NIE** = No Initial Elements: Means no orbital data available since launch  
  - **NEA** = No Elements Available: Nothing available at this time
  - blank means object data is up to date

---

### **ORBIT_CENTER**  
- Orbit center identifiers:  
  - **AS** = Asteroid  
  - **CO** = Comet  
  - **EA** = Earth  
  - **ELx** = Earth Lagrange (e.g., **EL1** = Earth L1, **EL2** = Earth L2)  
  - **EM** = Earth-Moon Barycenter  
  - **JU** = Jupiter  
  - **MA** = Mars  
  - **ME** = Mercury  
  - **MO** = Moon (Earth)  
  - **NE** = Neptune  
  - **PL** = Pluto  
  - **SA** = Saturn  
  - **SS** = Solar System Escape  
  - **SU** = Sun  
  - **UR** = Uranus  
  - **VE** = Venus  

---

### **NORAD_CAT_ID (Docked Objects)**  
- NORAD Catalog Number for docked objects  

---

### **ORBIT_TYPE**  
- **ORB** = Orbit  
- **LAN** = Landing  
- **IMP** = Impact  
- **DOC** = Docked to another object in the SATCAT  
- **R/T** = Roundtrip  
