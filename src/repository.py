from azure.cosmos import CosmosClient, PartitionKey
from config import CONFIG
from spec import EmployeeSpecification


class Repository:
    def __init__(self):
        self.employee_spec = EmployeeSpecification()
        self.config = CONFIG()
        self.endpoint = self.config.endpoint
        self.key = self.config.key
        self.database_name = self.config.database_name
        self.container_name = self.config.container_name
        self.client = CosmosClient(self.endpoint, self.key)
        self.create_database = self.client.create_database_if_not_exists(
            self.database_name
        )
        self.database = self.client.get_database_client(self.database_name)
        self.create_container = self.database.create_container_if_not_exists(
            id=self.container_name, partition_key=PartitionKey(path="/id")
        )
        self.container = self.database.get_container_client(self.container_name)

        self.data = []

    def read_by_id(self, id):
        try:
            document = self.container.read_item(item=id, partition_key=id)
            return document
        except:
            print("Document does not exist")
            pass

    def create(self, employee):
        employee_exist = self.container.read_all_items()
        for item in employee_exist:
            if item["id"] == employee.id:
                print("Document already exists")
               
                return
        try:
            if self.employee_spec.isSatifiesBy(employee):
                self.container.create_item(body=employee.__dict__)
                print("Document inserted successfully!")
            else:
                print("Invalid document")
                return

        except:
            print("Something went wrong ${employee.__dict__}")
            pass

        return

    def read(self):
        data = self.container.read_all_items()
        for item in data:
            self.data.append(item)
            print(item)
        return self.data

    def update(self, id, employee):
        try:
            self.container.replace_item(item=id, body=employee.__dict__)
            print("Document updated successfully!")
        except:
            print("Document does not exist")

    def delete(self, id):
        try:
            self.container.delete_item(id, id)
            print("Document deleted successfully!")
        except:
            print("Document does not exist")
