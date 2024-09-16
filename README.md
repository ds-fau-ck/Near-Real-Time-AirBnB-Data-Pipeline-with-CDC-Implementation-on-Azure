# Project Overview: 
### End-to-End Data Engineering Pipeline: Near Real-Time CDC Pipeline for AirBnB Data on Azure
![airbnbpic!](AirBnBApp3.png)

This project focuses on implementing a **near real-time Change Data Capture (CDC) pipeline** in Azure to process AirBnB data, ensuring seamless integration and continuous data flow. Below is an outline of the various components involved:

---

### 1. **Change Data Capture (CDC)**

When working with transactional or NoSQL databases, operations such as inserting, deleting, or updating data are common. This process is known as **Change Data Capture (CDC)**. Whenever a change occurs on the source side—whether it’s reading, inserting, updating, or deleting data—those changes must be captured. The way these changes are consumed or processed afterward depends on the specific use case.

This project implements such a use case where a CDC pipeline is set up on Azure to process AirBnB data in near real-time.

---

### 2. **ADLS (Azure Data Lake Storage)**

Inside **Azure Data Lake Storage (ADLS)**, there is a container, for example, named "customer data." Every four hours, a source system sends delta data for customers. This data includes any new customers onboarded or changes to existing customers within that period, delivered as a **CSV file**.

In this project, files are delivered to ADLS every 30 minutes. This means that within one hour, two files are expected, and within two hours, four files should be present. However, occasional delays in file processing can occur, but the system is designed to handle this scenario.

---

### 3. **AirBnB Backend**

In the backend of AirBnB, scalable NoSQL databases capture all data changes. In the context of Azure, **Cosmos DB** is used. The AirBnB application, including the mobile app, directly interacts with this NoSQL database, where data is continuously updated.

Within Cosmos DB, there is a database named **AirBnB**, and inside this database, a container named **Bookings**. Python scripts are used to continuously generate and write mock data into Cosmos DB. Additionally, updates can be made directly from the UI to observe how the pipeline captures and processes the CDC changes.

---

### 4. **Pipeline 1: Customer Data Processing**

We use **Azure Data Factory (ADF)** to design and manage the pipeline. The pipeline runs every two hours and performs the following steps:

- **Step 1**: Retrieve the list of files currently available in the "customer data" container in ADLS.
- **Step 2**: Copy the listed files into a **Synapse table** (used as a data warehouse).
- **Step 3**: Archive the processed files into an "archive" folder within the "customer data" container.
- **Step 4**: Read booking data for CDC and perform data transformations. These transformations include flattening the data and processing it into a **booking fact table** using an **upsert** operation.
- **Step 5**: After the upsert operation, create a **materialized view** using a **Stored Procedure** in Synapse to enhance performance.

---

### 5. **Pipeline 2: Booking Data Processing**

This pipeline reads booking data directly from **Cosmos DB** and processes the CDC changes for further analysis and integration.

---

### 6. **Pipeline 3: Execute Pipeline 1 and Pipeline 2**

This pipeline coordinates the execution of both **Pipeline 1** and **Pipeline 2**, ensuring synchronized processing of customer data and booking data.

---

### Summary

This project demonstrates how to implement a CDC pipeline using Azure components like ADLS, ADF, and Synapse. By continuously capturing and processing data from AirBnB's backend (Cosmos DB) and external customer data sources, this architecture ensures real-time integration and data flow with minimal delays.

---
### Setting Up The Environment

