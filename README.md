# SRE Log Parser
A lightweight, memory-efficient Python utility designed for automated system log analysis.

## 🔍 Overview
This tool was developed to streamline the process of identifying critical system errors within Linux journal logs. It demonstrates core Site Reliability Engineering (SRE) principles by automating the "Observability" layer of system maintenance.

## 🚀 Key Features
* **High-Efficiency Parsing:** Uses Python context managers to process large-scale log files line-by-line, ensuring low memory overhead.
* **Automated Aggregation:** Categorizes log levels (INFO, ERROR) into a dictionary-based summary for rapid health checks.
* **Case-Insensitive Pattern Matching:** Utilizes robust string processing to capture error variants across diverse log formats.

## 🛠️ Usage
1. Place your target log file in the directory.
2. Run the script:
   `python log_parser.py`