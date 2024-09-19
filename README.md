
# **End-to-End Data Engineering: Near Real-Time CDC Pipeline for AirBnB Data on Azure**
### **Introduction**
This project implements a **near real-time Change Data Capture (CDC) pipeline** for processing AirBnB data using Azure services, ensuring seamless integration and continuous data flow.

---
### **Architecture**
![Architecture](AirBnBApp3.png)

### **Technology Used**
1. **Programming Language**: Python  
2. **Scripting Language**: SQL  
3. **NoSQL**: CosmosDB  
4. **Azure Cloud Platform**:
   - Azure Data Lake Storage (ADLS)
   - Azure Data Factory
   - Azure Synapse Analytics

## **Table of Contents**
| Section | Description |
|---------|-------------|
| [1. Change Data Capture (CDC)](#1-change-data-capture-cdc) | Overview of CDC and its importance in transactional and NoSQL databases |
| [2. ADLS (Azure Data Lake Storage)](#2-adls-azure-data-lake-storage) | Managing incoming customer data in ADLS |
| [3. AirBnB Backend](#3-airbnb-backend) | Using Cosmos DB to manage AirBnB's backend booking data |
| [4. Pipeline 1: Customer Data Processing](#4-pipeline-1-customer-data-processing) | Description of the ADF pipeline for processing customer data |
| [5. Pipeline 2: Booking Data Processing](#5-pipeline-2-booking-data-processing) | Processing AirBnB booking data from Cosmos DB |
| [6. Pipeline 3: Execute Pipelines](#6-pipeline-3-execute-pipeline-1-and-pipeline-2) | Execution of the pipelines one and pipeline two |

---

### 1. **Change Data Capture (CDC)**

**Change Data Capture (CDC)** captures changes (inserts, updates, deletes) from transactional or NoSQL databases. This project implements a **CDC pipeline** on Azure to enable near real-time integration of AirBnB's customer and booking data.

---

### 2. **ADLS (Azure Data Lake Storage)**

**Azure Data Lake Storage (ADLS)** contains a container (e.g., "customer data") where **CSV files** with customer updates are received every 30 minutes.These files are processed, archived, and ingested into Synapse for further transformation and analysis.

---

### 3. **AirBnB Backend and Booking Data**

The AirBnB backend interacts with **Cosmos DB**, which stores booking data in the **Bookings** container. A Python script continuously generates booking data, and CDC updates triggered by the **Cosmos DB** UI ensure near real-time data flow for processing.

---

### 4. **Pipeline 1: Customer Data Processing**

This pipeline runs every two hours in **Azure Data Factory (ADF)** to:
- Retrieve customer files from ADLS.
- Copy data to a **Synapse table** for processing.
- Archive processed files.
- Perform **upsert** operations on customer data, transforming it into a **booking fact table**.
- Create a **materialized view** using a **Stored Procedure** in Synapse for reporting and analysis.

---

### 5. **Pipeline 2: Booking Data Processing**

This pipeline reads booking data from **Cosmos DB**, capturing CDC updates and ensuring that all booking-related changes are processed in real-time. It integrates the data for further analysis in downstream systems.

---

### 6. **Pipeline 3: Execute Pipelines**

This pipeline first triggers the execution of **Pipeline 1** (Customer Data Processing). Once **Pipeline 1** completes successfully, it proceeds to execute **Pipeline 2** (Booking Data Processing). 

---

### **Scripts and dataset for this Project**
1. [CosmosDB](CosmosDB/cosmosdb.py)
2. [Datasets](DataSets/customer_data_2024_08_29_06_58.csv)
3. [Datasets](DataSets/customer_data_2024_08_29_07_20.csv)
4. [Datasets](Datasets/customer_data_2024_08_29_08_13.csv)
5. [Synapse](Synapse/create_table_synapse.sql)

---

### Summary

This project demonstrates an **end-to-end data engineering pipeline** for processing AirBnB data in near real-time. By leveraging Azure services such as ADLS, ADF, Synapse, and Cosmos DB, the system captures, processes, and transforms customer and booking data seamlessly.

---



