# Product-Distributuion-Analysis
This project addresses production, distribution, and stock management by analyzing sales patterns and seasonal trends to reduce demand uncertainty. We also focus on optimizing warehouse space, enabling companies to store necessary products efficiently, balance stock levels, and cut costs while meeting customer demands.

![image](https://github.com/user-attachments/assets/b3b7c78b-0d46-4a7b-8cd3-9c9b9b46e2d8)

## Interpretation: 
The project is focused on demand forecasting or inventory optimization. 
This graph demonstrates significant variability in weekly order demand over the five-year period. This graph shows that weekly demand is highly irregular, requiring predictive models to account for unexpected spikes. The sharp peaks in 2014 and 2015 suggest situations where demand surged, possibly due to special promotions, market events, or seasonal factors. The irregularity also indicates the challenge of planning stock levels or resource allocation weekly without forecasting tools. Periods of low demand indicate possible off-season behaviour or reduced customer interest. The high volatility requires businesses to adopt a responsive inventory system to manage unexpected spikes while avoiding excess inventory during low-demand weeks. Predictive modelling could help smooth out demand forecasting, ensuring better operational efficiency. 


![image](https://github.com/user-attachments/assets/b8570ca5-7576-48eb-9429-1bc4cf84f38f)

## Interpretation: 
 
This graph aggregates weekly demand into monthly totals, smoothing out short-term fluctuations.  
The lines highlight recurring peaks and dips each year. There are consistent peaks in certain months each year, potentially reflecting a strong seasonal component in demand. 
The smoother trendlines make it easier to spot demand patterns compared to weekly data, which is more volatile. 
Businesses should plan production and inventory build - up in anticipation of peak months. Analysis of these patterns could inform marketing campaigns, aligning them with high-demand months to maximize revenue. 

![image](https://github.com/user-attachments/assets/6b614c87-cc38-4f2e-88e9-bdf39d85d7fd)

## Interpretation: 
 
This graph summarizes the cumulative demand for each year. The line consistently slopes upwards, indicating year-over-year growth. 
The project is focused on long-term growth trends or strategic planning.  
The upward trend shows that demand for Product_0031 has increased steadily, reflecting growing customer adoption or market penetration. This graph showcases long-term trends, revealing an upward trajectory in total yearly demand from 2012 to 2016. 
The graph provides a high-level view, which is useful for making decisions about scaling operations, such as increasing production capacity or entering new markets. 
Growth accelerates noticeably in later years, suggesting either market expansion or successful customer acquisition strategies. 
The data provides a macro view of increasing customer reliance on Product_0031 over time. The consistent growth indicates a positive market trajectory, encouraging businesses to invest in scaling operations. 


### These graphs collectively tell the story of demand variability, seasonality, and growth, which are critical inputs for designing efficient inventory systems, forecasting models, and strategic business decisions. 

## Analysis 
The analysis of these graphs provides insights into descriptive, diagnostic, and predictive analytics. Descriptively, the observed demand data for Product_0031 shows high volatility and erratic spikes, particularly in 2014 and 2015, which may indicate seasonal variations or external influences. Diagnostically, the sharp demand fluctuations suggest the need to identify potential causes, such as market events, promotions, or shifts in consumer behaviour, which could be driving these patterns. The cross-validation results play a vital role here by reducing the impact of outliers, enabling a clearer view of the underlying trends and mitigating the noise caused by extreme spikes. Predictively, the time series forecast demonstrates how historical patterns inform future projections, with the predictive model providing a relatively stable trend line while cautiously reflecting potential volatility. Together, these analytics showcase the critical importance of advanced techniques like cross-validation to enhance the reliability of forecasts for highly volatile datasets, ensuring better planning and decision-making. 

### Descriptive Analysis: Summarizing and understanding data to identify patterns, trends, and insights. "What happened?" / "What are the key patterns in the data? 
1.Demand for Product_0031 exhibits significant fluctuations over the observed period. 
2.Seasonal trends with periodic increases and decreases suggest patterns of high and low demand. 
 
### Predictive Analysis: Using past data to make educated guesses about the future. “ What is likely to happen?” 
1.	Cross-validation predictions were used to enhance the reliability of demand forecasts by reducing volatility. 
2.	The forecast suggests a stable demand in the first quarter, a drop in the second quarter, and a peak toward the end of the year. 
 
### Prescriptive Analysis: Figuring out the best actions to take based on the data. “What should we do?” by providing recommendation and strategies.  
1.	Predicted future demand indicates an upward trend, with fluctuations similar to historical patterns. 
2.	Simulation was conducted to evaluate stock levels of 10000, 20000, 30000, 40000 and 50000 gallons. 
 
 ## Simulation  
Simulation in prescriptive analysis involves creating scenarios to test different strategies for decision making. The objective of this simulation is to evaluate different demand levels and their corresponding stocking strategies to identify the most optimal balance between demand fulfilment, inventory management, and profitability. By simulating key metrics such as sales, underage, overage, profit, and the cost of lost sales, the goal is to align stocking quantities with predicted demand, minimize lost opportunities due to understocking, reduce excess inventory costs, and maximize overall profitability. This analysis aids in making data-driven decisions for efficient supply chain and inventory management. 
 
## Stocking quantities are as follows for the simulations: 
Stocking Quantity 
10000 
15000 
20000 
25000 
30000 
  
We have assumed our simulation product as “MILK” Assumptions – 
•	Selling Price – $5.50 
•	Cost Price – $2.50 
•	Formula used for calculating Cost of lost sales per unit = selling price – cost price 
•	Overage = max(0, stocking_quantity - demand) 
•	Underage = max(0, demand - stocking_quantity) 
•	Cost_of_lost_sales = underage * cost_of_lost_sales_per_unit 
•	Sales = min(demand, stocking_quantity)   
•	profit = (sales * selling_price) - (stocking_quantity * cost_price) - cost_of_lost_sales Simulation Tables – 
 
## Table 1 – Stocking Quantity: 10000 
 ![image](https://github.com/user-attachments/assets/faaf641e-0e87-495e-a45d-ebacbe852fbd)

  
 
## Table 2 – Stocking Quantity: 15000 
![image](https://github.com/user-attachments/assets/38b59c80-d852-4066-ac39-0e7967c995c8)
 
  
 ## Table 3 – Stocking Quantity: 20000 
 
  ![image](https://github.com/user-attachments/assets/e1b8c0a9-c5fa-4ef3-8ab6-ecc83447db1e)

 
## Table 4 – Stocking Quantity: 25000 
 
  
 ![image](https://github.com/user-attachments/assets/7c025c0c-f1ae-43c4-9235-4ccda8714b7f)

 
 
## Table 5 – Stocking Quantity: 30000 
  ![image](https://github.com/user-attachments/assets/38b1e9ff-9616-4746-8ad5-63381e7ceba6)

 
## Simulation Summary table – 
 
  ![image](https://github.com/user-attachments/assets/668277ad-e030-49cd-84fd-c2a854750ea2)

 
## Best Match for Predicted Model: Stocking Quantity is 30,000 gallons 
•	Average Sales: The average sales 29,025 are very close to the demand 30,813. 
•	Low Underage and Overage: The low underage 1,788 and overage 975 suggest efficient inventory management. 
•	Highest Total Profit: The total profit $79,272 is the highest among the simulations with low costs of lost sales $5,364. 
•	Comparative Analysis: Other demand points like 10,000 and 20,000 gallons are also efficient, but their profits are comparatively lower, making 30,000 gallons the most optimal stocking quantity. 
 
  # Conclusion 
The analysis and simulation provide a comprehensive understanding of how different demand levels impact sales performance, inventory management, and profitability. By evaluating key metrics such as underage, overage, cost of lost sales, and profit, the simulation highlights the importance of aligning stocking quantities with demand predictions to achieve optimal results. Among the analysed demand levels, a demand of 30,000 emerges as the most efficient, with average sales closely matching the predicted demand, minimal underage and overage, and the highest profit relative to costs. This demonstrates a well-balanced inventory strategy that maximizes revenue while minimizing inefficiencies. The simulation underscores the value of predictive modelling in decision-making, allowing businesses to optimize resources, reduce costs, and enhance profitability through data-driven insights. 





