📊 Exploratory Data Analysis - Online Retail

A comprehensive exploratory data analysis project analyzing retail transaction data to uncover sales patterns, customer behavior, and business insights.

📖 Project Overview

This project performs in-depth exploratory data analysis on an online retail dataset to discover meaningful patterns and trends. The analysis focuses on data cleaning, statistical analysis, visualization, and deriving actionable insights for business decision-making.

🎯 Analysis Objectives

- Clean and preprocess retail transaction data
- Analyze sales trends across different time periods
- Identify top-performing products and countries
- Detect and handle outliers in the dataset
- Visualize key metrics and patterns
- Generate business insights from the data

📁 Dataset Information

Dataset: Online Retail.xlsx
Source: Online retail transaction data
Features: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

🔍 Key Analyses Performed

1. Data Cleaning
   - Handling missing values in CustomerID
   - Removing negative quantities and prices
   - Converting date formats
   - Creating derived features

2. Sales Analysis
   - Total sales by country
   - Monthly sales trends
   - Day-of-week sales patterns
   - Sales distribution analysis

3. Customer Segmentation
   - Top countries by revenue
   - Customer purchase patterns
   - Quantity vs price analysis

4. Product Analysis
   - Top-selling products
   - Product performance metrics
   - Price-quantity relationships

5. Outlier Detection
   - IQR-based outlier identification
   - Impact of outliers on analysis
   - Outlier treatment strategies

📊 Visualizations

The project includes various visualizations:
- Bar charts for country-wise sales
- Box plots for quantity and price distributions
- Scatter plots for quantity vs unit price
- Time series plots for sales trends

🛠️ Technologies Used

- Python 3.x
- pandas: Data manipulation and analysis
- matplotlib: Data visualization
- seaborn: Statistical data visualization
- numpy: Numerical computations

💻 Getting Started

Prerequisites:
- Python 3.7 or higher
- Required libraries: pandas, matplotlib, seaborn, numpy

Installation:
1. Clone this repository
2. Install required packages:
   pip install pandas matplotlib seaborn numpy

Usage:
1. Place the 'Online Retail.xlsx' file in the project directory
2. Run the analysis script:
   python retail.py
3. View generated visualizations and insights

📈 Key Findings

Based on the exploratory data analysis:
- Sales patterns vary significantly by country and time period
- Certain months show higher sales activity (seasonal trends)
- Specific days of the week have higher transaction volumes
- Product pricing shows interesting relationships with quantity sold
- Customer segmentation reveals distinct purchasing behaviors

📂 Project Structure

Exploratory-Data-Analysis/
├── retail.py                          # Main analysis script
├── Online Retail.xlsx                 # Dataset
├── Electric_Vehicle_Population_Data   # Additional dataset
├── Projectfile                        # Project configuration
└── README.md                          # Project documentation

🔮 Future Enhancements

- Implement advanced customer segmentation (RFM analysis)
- Add predictive modeling for sales forecasting
- Create interactive dashboards using Plotly or Dash
- Perform cohort analysis for customer retention
- Add sentiment analysis on product descriptions
- Implement market basket analysis

🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest new analysis techniques
- Improve visualizations
- Add new features

📄 License

This project is open source and available for educational purposes.

👤 Author

Prannessh2006
- GitHub: @Prannessh2006
- Repository: https://github.com/Prannessh2006/Exploratory-Data-Analysis

⭐ Show Your Support

If this project helped you learn exploratory data analysis or provided useful insights, give it a star!

📞 Contact

For questions, suggestions, or discussions:
- Open an issue on GitHub
- Explore the code and learn from implementations
- Share your improvements through pull requests

---

Happy Analyzing! 📊
