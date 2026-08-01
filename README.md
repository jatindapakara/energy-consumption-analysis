# Energy Consumption Analysis

A Python application for analyzing household energy consumption data from CSV files. The project performs statistical analysis, detects outliers, and visualizes energy usage to provide meaningful insights into energy optimization.

---

## Overview

This project demonstrates the use of Python for data analysis by processing energy consumption datasets, computing statistical metrics, identifying anomalies, and generating visualizations.

---

## Features

- Read energy consumption data from CSV files
- Calculate total energy consumption
- Calculate total energy savings
- Compute average energy consumption
- Identify maximum and minimum consumption
- Calculate variance and standard deviation
- Detect statistical outliers
- Generate cleaned datasets
- Visualize consumption trends using graphs

---

## Technologies Used

- Python
- NumPy
- Matplotlib
- CSV Module

---

## Project Structure

```text
energy-consumption-analysis/
│
├── data/
│   ├── energy_data.csv
│   └── cleaned_energy_data.csv
│
├── screenshots/
│   ├── terminal-output.png
│   ├── energy-graph.png
│   └── savings-graph.png
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/jatindapakara/energy-consumption-analysis.git
```

Navigate to the project directory:

```bash
cd energy-consumption-analysis
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## Sample Output

```text
Total Energy Consumption : 930

Average Consumption : 132.8

Maximum Consumption : AC

Minimum Consumption : Fan

Standard Deviation : 37.42

Outliers Detected : Heater
```

---

## Screenshots

### Terminal Output

![Terminal Output](screenshots/terminal-output.png)

### Energy Consumption Analysis

![Energy Graph](screenshots/energy-graph.png)

### Energy Savings

![Savings Graph](screenshots/savings-graph.png)

---

## Concepts Demonstrated

- File Handling
- CSV Processing
- Data Analysis
- Statistical Computation
- Standard Deviation
- Outlier Detection
- Data Cleaning
- Data Visualization
- Modular Programming

---

## Future Enhancements

- Interactive dashboard
- Graphical user interface
- Support for multiple datasets
- Automated report generation
- Machine learning based consumption prediction
- Export analysis reports

---

## Author

**Jatin Dapakara**

B.Tech Artificial Intelligence & Data Science

GitHub: https://github.com/jatindapakara
