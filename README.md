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

- Ratio of categories
<br>

![alt Ratio of categories](/piechar.jpg)

- Rating of categories
<br>

![alt Rating of categories](/rating.png) 

- Price of categories
<br>

![alt Price of categories](/Price.jpeg) 

- Number of product sold of categories
<br>

![alt Price of categories](/ProductSold.jpeg) 

- Correlation Heatmap
<br>

![alt Correlation Heatmap](/heatmap.png) 

4. Modeling
- Relationship between Total rating and product sold
<br>

![alt Relationship between Total rating and product sold](/newplot.png) 

- Apply 3 machine learning algorithms: Linear Regression, Descision Tree and XGBoost

    + Using cross validation with k-fold = 5 to evaluate dataset

<br>

![alt Modeling](/model.jpg) 

## Conclusion
- Through this project, I was able to practice and understand more about data collection and processing to better understand the data and derive knowledge from that data.



