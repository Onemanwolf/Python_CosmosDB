from employee import Employee
from repository import Repository
# # Import the required libraries
# from azure.cosmos import CosmosClient, PartitionKey
# import os
# # Define the connection string and database details
# endpoint = os.getenv('END_POINT', 'END_POINT')
# key = os.getenv('KEY', 'KEY')
# database_name = os.getenv('DATABASE_NAME', 'END_POINT')
# container_name = os.getenv('CONTAINER_NAME', 'END_POINT')

# # Create a Cosmos DB client
# client = CosmosClient(endpoint, key)
# client.create_database_if_not_exists(database_name)
# # Get a reference to the database
# database = client.get_database_client(database_name)
# # container = database.create_container_if_not_exists(
# #     id=container_name,
# #     partition_key=PartitionKey(path="/id")
# # )


# # Get a reference to the container
# container = database.get_container_client(container_name)

# # Define the JSON document to be inserted
document = {
    "id": "emp002",
    "name": "Jane Doe",
    "age": 30
}

# # Insert the document into the container
# container.create_item(body=document)
#
# print("Document inserted successfully!")
repo = Repository()

repo.create(Employee("emp035", "Joyce Wise ", 80))
repo.update("emp010", Employee("emp010", "Tim Oleson", 54))
employee = repo.read_by_id("emp010")
print(employee)
repo.delete("emp007")
repo.read()