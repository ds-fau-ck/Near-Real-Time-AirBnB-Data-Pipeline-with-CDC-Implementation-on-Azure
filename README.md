
## **End-to-End Data Engineering: Near Real-Time CDC Pipeline for AirBnB Data on Azure**

### **Introduction**
This project demonstrates the implementation of a **near real-time Change Data Capture (CDC) pipeline** for processing AirBnB data using various Azure services, ensuring seamless integration and continuous data flow.

---

### **Architecture**

![Architecture](AirBnBApp3.png)

---

### **Technologies Used**
1. **Programming Language**: Python  
2. **Scripting Language**: SQL  
3. **NoSQL**: CosmosDB  
4. **Azure Cloud Platform**:
   - Azure Data Lake Storage (ADLS)
   - Azure Data Factory (ADF)
   - Azure Synapse Analytics

---

## **Table of Contents**
| Section | Description |
|---------|-------------|
| [1. Change Data Capture (CDC)](#1-change-data-capture-cdc) | Overview of CDC and its importance in transactional and NoSQL databases |
| [2. Azure Data Lake Storage (ADLS)](#2-azure-data-lake-storage-adls) | Managing incoming customer data in ADLS |
| [3. Cosmos DB: AirBnB Booking Data](#3-cosmos-db-airbnb-booking-data) | Managing AirBnB's backend booking data in Cosmos DB |
| [4. Pipeline 1: Customer Data Processing](#4-pipeline-1-customer-data-processing) | ADF pipeline for processing customer data |
| [5. Pipeline 2: Booking Data Processing](#5-pipeline-2-booking-data-processing) | Real-time CDC processing of booking data from Cosmos DB |
| [6. Pipeline 3: Orchestration of Pipelines](#6-pipeline-3-orchestration-of-pipelines) | Executing and orchestrating both pipelines |

---

### 1. **Change Data Capture (CDC)**

**Change Data Capture (CDC)** captures changes (inserts, updates, deletes) from transactional or NoSQL databases. This project implements a **CDC pipeline** on Azure to enable near real-time data integration of AirBnB's customer and booking data.

---

### 2. **Azure Data Lake Storage (ADLS)**

**In the Azure Data Lake Storage (ADLS)**, incoming **CSV files** that contain customer updates are stored every 30 minutes. The files are processed, ingested into Synapse DWH for further transformation and analysis and then moved to the archived folder.

---

### 3. **Cosmos DB: AirBnB Booking Data**

The backend of the Python scripts interacts with **Cosmos DB**, which stores booking data in the **Bookings** container. A Python script simulates booking data generation. **CDC updates** triggered by Cosmos DB ensure near-real-time data flow for processing.

---

### 4. **Pipeline 1: Customer Data Processing**

This **Azure Data Factory (ADF)** pipeline runs every two hours to:
- Read customer files from ADLS.
- Move the processed files in the archieved folder.
- Read the data  from CosmosDB for further processing.
- Delete the file from Dustomer-Raw-Data folder.

![customer-data-processing](customer-data-processing-pipeline1.jpg)
---

### 5. **Pipeline 2: Booking Data Processing**
![Booking-data-processing](BookingDataProcessingPipeline2.jpg)
This pipeline captures **CDC updates** from **Cosmos DB** in near real-time. 
- Perform **upsert** operations on customer data.
- Transform the data into a **Booking Fact Table**.
- Create a **Materialized View** using a stored procedure in Synapse for reporting and analysis.
It processes booking-related data changes and integrates the data for downstream systems like Azure Synapse for further analysis.

![Data-Transformation-ADF](DataTransformation.jpg)
---

### 6. **Pipeline 3: Orchestration of Pipelines**

This pipeline orchestrates the execution of **Pipeline 1** (Customer Data Processing) and **Pipeline 2** (Booking Data Processing). It triggers **Pipeline 1** first, and once it completes successfully, **Pipeline 2** is executed.

![Orchestration of Pipelines](pipeline3.jpg)
---

### **Scripts and Datasets for the Project**

1. **Cosmos DB CDC Script**: [cosmosdb.py](CosmosDB/cosmosdb.py)
2. **Customer Data CSV**:
   - [customer_data_2024_08_29_06_58.csv](DataSets/customer_data_2024_08_29_06_58.csv)
   - [customer_data_2024_08_29_07_20.csv](DataSets/customer_data_2024_08_29_07_20.csv)
   - [customer_data_2024_08_29_08_13.csv](DataSets/customer_data_2024_08_29_08_13.csv)
3. **Synapse Table Creation Script**: [create_table_synapse.sql](Synapse/create_table_synapse.sql)

---
### **Summary**
This project demonstrates an **end-to-end data engineering pipeline** for processing AirBnB data in near real-time. By leveraging Azure services such as ADLS, ADF, Synapse, and Cosmos DB, the system captures, processes, and transforms customer and booking data seamlessly.

---

