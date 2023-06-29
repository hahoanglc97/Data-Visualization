# Data-Visualization
## Collect and analyze products on Shopee e-commerce platform

<hr />

``Along with the development of e-commerce platforms in Vietnam in recent years. I want to collect data and analyze products so that we can discover the product's price distribution, distribution of quantity sold, and rating of product``

## Tools usage
- selenium, BeautifulSoup, chromedriver for crawl data in website
- numpy, pandas, seaborn, matplotlib for EDA process

## Flow
1. Collecting
- Collect links of product on Shopee’s search page
- Access each link into list to get the necessary data

2. Cleaning
- Fill missing value 
- Cleaning data in some field 

3. Exploratory Data Analysis
- Visualize data

- Ratio of categories
![alt Ratio of categories](/Project/piechar.png) 

- Rating of categories
![alt Rating of categories](/Project/rating.png) 

- Price of categories
![alt Price of categories](/Project/Price.jpeg) 

- Number of product sold of categories
![alt Price of categories](/Project/ProductSold.jpeg) 

- Correlation Heatmap
![alt Correlation Heatmap](/Project/heatmap.png) 

4. Modeling
- Relationship between Total rating and product sold
![alt Relationship between Total rating and product sold](/Project/newplot.png) 

- Apply 3 machine learning algorithms: Linear Regression, Descision Tree and XGBoost

    + Using cross validation with k-fold = 5 to evaluate dataset

![alt Modeling](/Project/model.png) 

## Conclusion
- Through this project, we were able to practice and understand more about data collection and processing to better understand the data and derive knowledge from that data.



