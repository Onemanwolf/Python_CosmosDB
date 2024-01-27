from azure.cosmos import CosmosClient, PartitionKey
import os
endpoint = os.getenv('END_POINT', 'END_POINT')
key = os.getenv('KEY', 'KEY')
database_name = os.getenv('DATABASE_NAME', 'END_POINT')
container_name = os.getenv('CONTAINER_NAME', 'END_POINT')
client = CosmosClient(endpoint, key)
client.create_database_if_not_exists(database_name)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)
import json

class Repository:
    def __init__(self):
        self.data = []

        # Create a Cosmos DB client


    def read_by_id(self, id):
        try:
            document = container.read_item(item=id, partition_key=id)
            return document
        except:
            print("Document does not exist")
            pass



    def create(self, employee):


        PartitionKey = employee.id

        employee_exist = container.read_all_items()
        for item in employee_exist:
            if item['id'] == employee.id:
                 print("Document already exists")
                 return
        try:
            container.create_item(body=employee.__dict__)
        except:
            print("Something went wrong ${employee.__dict__}")
            pass

        print("Document inserted successfully!")
    def read(self):
        data = container.read_all_items()
        for item in data:
            self.data.append(item)
            print(item)
        return self.data

    def update(self, id, employee):
        try:
            container.replace_item(item=id, body=employee.__dict__)
            print("Document updated successfully!")
        except:
            print("Document does not exist")


    def delete(self, id):
        try:
            container.delete_item(id,id)
            print("Document deleted successfully!")
        except:
            print("Document does not exist")


