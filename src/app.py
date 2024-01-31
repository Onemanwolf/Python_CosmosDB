from employee import Employee
from repository import Repository

document = {
    "id": "emp002",
    "name": "Jane Doe",
    "age": 30
}


repo = Repository()

repo.create(Employee("emp035", "Joyce Wise ", 80))
repo.update("emp010", Employee("emp010", "Tim Oleson", 54))
employee = repo.read_by_id("emp010")
print(employee)
repo.delete("emp007")
repo.read()