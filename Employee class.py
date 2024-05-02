class Employee:
    def __init__(self, name, empID, department, jobTitle, basicSalary, age, dateOfBirth, passportID, passportExpiry, managerID):
        self.name = name
        self.empID = int(empID)
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.age = int(age)
        self.dateOfBirth = dateOfBirth
        self.passportID = passportID
        self.passportExpiry = passportExpiry
        self.managerID = int(managerID)
