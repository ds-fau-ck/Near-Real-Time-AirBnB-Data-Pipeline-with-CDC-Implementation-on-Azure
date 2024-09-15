from azure.cosmos import CosmosClient, PartitionKey
import random
from datetime import datetime, timedelta
from faker import Faker
import time
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
# Initialize Faker
fake = Faker()
#key_vault_url="https://faudesecrets.vault.azure.net/secrets/CosmosDb-Password/81f7c88da21242f59b4f0664515634d3"
key_vault_url ="https://faudesecrets.vault.azure.net/"

# Connect to Azure Key Vault
credential = DefaultAzureCredential()
client = SecretClient(vault_url=key_vault_url, credential=credential)

# Fetch secrets from Azure Key Vault
endpoint = client.get_secret("cosmosDB-server-host").value
#database = "AirBnB" 
key = client.get_secret("cosmosDb-username").value
# Initialize the Cosmos client

client = CosmosClient(endpoint, key)
# Database and Container setup
database_name = 'AirBnB'
container_name = 'bookings'

database = client.create_database_if_not_exists(id=database_name)
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path="/booking_id"),
    offer_throughput=400
)

# Function to generate and insert booking data into Cosmos DB record by record
def generate_and_insert_booking_data(num_records, customer_ids):
    for _ in range(num_records):
        record = {
            'id': fake.uuid4(),  # Cosmos DB requires a unique 'id' field
            'booking_id': fake.uuid4(),
            'property_id': fake.uuid4(),
            'customer_id': random.choice(customer_ids),
            'owner_id': fake.uuid4(),
            'check_in_date': fake.date_this_year().strftime('%Y-%m-%d'),
            'check_out_date': (fake.date_this_year() + timedelta(days=random.randint(1, 14))).strftime('%Y-%m-%d'),
            'booking_date': fake.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'amount': round(random.uniform(50, 1000), 2),
            'currency': random.choice(['USD', 'EUR', 'GBP', 'CAD']),
            'property_location': {
                'city': fake.city(),
                'country': fake.country()
            },
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Insert each record individually into the Cosmos DB container
        container.create_item(body=record)
        print(f"Inserted record: {record}")
        
        # Sleep for a short time to simulate real-time data insertion
        time.sleep(5)

customer_ids = list(range(1, 101))

generate_and_insert_booking_data(100, customer_ids)
