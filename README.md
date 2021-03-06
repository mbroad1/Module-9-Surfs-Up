# Module 9 Challenge: Surfs Up

## Purpose:
The purpose of this analysis is to evaluate the temperatures in Oahu in the months of December and June in order to see whether a surf and ice cream shop is a viable year-long business as the business relies on warm temperatures to be successful. To perform this analysis, I queried both date and temperature data from a SQLite database called "hawaii" and filtered the data based on month for each of the June and December queries. From there, I converted the two separate query results into lists and converted them once again into Pandas DataFrames, so that I could run a statistical analysis of the temperatures in the months of June and December. This analysis was performed using Python and the following dependencies: Pandas, NumPy, and SQLAlchemy.
---
## Results:

### Statistics for the Temperature in June:
![June_Stats](https://github.com/mbroad1/Module-9-Surfs-Up/blob/main/Images/june_stats.png)
- In the month of June, on average, the temperature is about **74.9F**, which is a warm temperature.
  - Considering this average is from all the June's from 2010-2017, this means that June is a reliably warm month and thus surf and ice cream sales would be consistent and/or high in the month of June.
- The first quartile of the temperature data is **73F** meaning that the temperature in June around its lowest is only a couple of degrees less than the average.
  - Although, the minimum temperature is **64F**, that is the lowest temperature of all the 1700 counts, so looking at the first quartile gives a better idea of what the temperature on the "cooler" end in June would be.
-  Likewise, the third quartile of the temperature data is **77F**.
    -  So that means 25% of the time in June, it will be 77F or higher, 50% of the time in June, it will be 75F or higher, and 75% of the time in June, it will be 73F or higher, making June a great month for business for a surf and ice cream shop.

### Statistics for the Temperature in December:
![Dec_Stats](https://github.com/mbroad1/Module-9-Surfs-Up/blob/main/Images/dec_stats.png)
- In the month of December, on average, the temperature is about **71.0F**, which is a relatively warm temperature (not necessarily hot, but not cold either).
  - Since 71.0F is the average temperature in all December's from 2010-2017, that means that December is not necessarily a cold month in Oahu.
- The minimum temperature in December out of 1517 counts is **56F**.
  - Although 56F can be considered cold depending on where you live (e.g. if you grew up and live in California, 56F is considered cold, but if you grew up and live on the east coast, then 56F is considered warm weather), the first quartile is 69F, which is only a couple degrees away from the average temperature, and means that 25% of the time in the month of December, the weather is 69F or cooler which is far from the majority of the time.
- Lastly, 25% of the time in the month of December it is **74F** or hotter which is nice, warm temperature, 50% of the time in December it is **71F** or hotter, and 75% of the time it is **69F** or hotter, meaning December would still be a good business month for a surf and ice cream shop in Oahu.
---

## Summary:
Looking at the analysis, it seems that business for an ice cream shop in the months of June and December would still be great months for business because the weather is generally warm during those months. The average temperatures in June and December, respectively, are **74.9F** and **71.0F**, which means that the temperature in those months are more likely warm than not. Likewise, 75% of the time in June and December, respectively, it is hotter than **73F** and **69F**.

Two additional queries that I would perform to evaluate the weather data for June and December would be to gather the weather data from the station closest to where the surf and ice cream shop would be located because the weather data would be more accurate since weather may be slightly different in different parts of the island since it is a relatively big island. Another query that I would perform to evaluate the weather data for June and December if available would be to gather the humidity data in Oahu in the months of June and December. If there is humidity during those months, then the temperature will feel hotter than what the temperature recordings state, and thus, the surf and ice cream shop would have more business. Overall, the data shows that business in the months of June and December would be lucrative considering those months are generally hot.
