---
Author: Matt Humphrey
Date Completed: 
---

# Illnesses and Injuries

## G201

For injury variables (INF -> INJ), 0 only ever represented "N/A", and thus all 0s were converted to 88s (later to -88).

For hospital admission variables (HO -> HOSP), 0 sometimes represented "refer to previous..." and in other cases represented "N/A".
When there were no corresponding values for ICD-9 codes and hospital codes, a frequency of 0 was converted to 88.
In other cases, the 0 remained a 0.
