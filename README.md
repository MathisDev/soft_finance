**Project Name: Stock Price History Analysis**

---

### Introduction
This project aims to provide a comprehensive solution for retrieving historical stock price data and analyzing it to derive meaningful metrics. By leveraging various tools and techniques, it offers insights into the performance and trends of different stocks over time. The project primarily focuses on the following key objectives:

1. **Data Retrieval**: Fetching historical stock price data from reliable sources.
2. **Metric Generation**: Calculating essential metrics such as moving averages, volatility, and returns.
3. **Analysis and Visualization**: Analyzing the data and presenting insights through visualization techniques.
4. **Integration**: Integrating different components to streamline the process of data retrieval, metric generation, and analysis.

### Features
- **Data Retrieval**: Utilizes APIs or web scraping techniques to fetch historical stock price data from various sources such as Yahoo Finance or Alpha Vantage.
- **Metric Generation**: Computes key metrics including but not limited to:
  - Moving Averages (e.g., Simple Moving Average, Exponential Moving Average)
  - Volatility Measures (e.g., Standard Deviation, Average True Range)
  - Returns (e.g., Daily Returns, Cumulative Returns)
- **Analysis**: Utilizes libraries like Pandas for analyzing data .
- **Linking Metrics**: Establishes relationships between different metrics to uncover patterns and trends in stock price behavior.
  
### Installation
To use this project, follow these steps:
1. Clone the repository: `git clone https://github.com/MathisDev/soft_finance.git)`
2. Install dependencies: `sudo apt-get update;sudo apt-get install docker-compose-plugin`

### Usage
1. **Data Retrieval**: Run the data retrieval script providing necessary parameters like stock symbol and time range.
   ```bash
   docker-compose up
