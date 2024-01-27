class EmployeeSpecification:
    def __init__(self) -> None:
        pass

    def isSatifiesBy(self, employee):
        if employee.id == None or employee.id == "":
            return False
        if employee.name == None or employee.name == " ":
            return False
        if employee.age == None or employee.age == "":
            return False
        return True
