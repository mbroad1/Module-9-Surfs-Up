# Module 9 Challenge: Surfs Up

## Purpose:
The purpose of this analysis is to evaluate the temperatures in Oahu in the months of December and June in order to see whether a surf and ice cream shop is a viable year-long business as the business relies on warm temperatures to be successful. To perform this analysis, I queried both date and temperature data from a SQLite database called "hawaii" and filtered the data based on month for each of the June and December queries. From there, I converted the two separate query results into lists and converted them once again into Pandas DataFrames, so that I could run a statistical analysis of the temperatures in the months of June and December. This analysis was performed using Python and the following dependencies: Pandas, NumPy, and SQLAlchemy.
---
## Results:
![June_Stats](https://github.com/mbroad1/Module-9-Surfs-Up/blob/main/Images/june_stats.png)
- In the month of June, on average, the temperature is about **74.9F**, which is a warm temperature
  - Considering this average is from all the Junes from 2010-2017, this means that June is a reliably warm month and thus surf and ice cream sales would be consistent and/or high in the month of June.
- The first quartile of the temperature data is **73F** meaning that the temperature in June around its lowest is only a couple of degrees less than the average.
  - Although, the minimum temperature is **64F**, that is the lowest temperature of all the 1700 counts, so looking at the first quartile gives a better idea of what the temperature on the "cooler" end in June would be.
-  Likewise, the third quartile of the temperature data is **77F*. 
  -  So that means 25% of the time in June, it will be 77F or higher, 50% of the time in June, it will be 75F or higher, and 75% of the time in June, it will be 73F or higher, making June a great month for business for a surf and ice cream shop.
