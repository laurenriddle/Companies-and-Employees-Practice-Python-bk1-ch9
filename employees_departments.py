# Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.
class Employee:
    def __init__(self):
        self.name = ""
        self.job_title = ""
        self.start_date = ""

# Create a Company type that employees can work for. A company should have a business name, address, and industry type.
class Company: 
    def __init__(self):
        self.name = ""
        self.address = ""
        self.industry_type = ""
        self.employees = []
    
    def add_employee(self, name):
        self.employees.append(name)
# Create two companies, and 5 people who want to work for them.
Chicken = Employee()
Chicken.name = "Chicken"
Chicken.job_title = "Cluck - Cluck"
Chicken.start_date = "Anytime!"

Bear = Employee()
Bear.name = "Bear"
Bear.job_title = "Mama Bear"
Bear.start_date = "TODAY"

Monkey = Employee()
Monkey.name = "Monkey"
Monkey.job_title = "Professional Banana Consumer"
Monkey.start_date = "Yesterday"


Frog = Employee()
Frog.name = "Frog"
Frog.job_title = "Experienced Jumper"
Frog.start_date = "Hop-fully next week"

Sloth = Employee()
Sloth.name = "Sloth"
Sloth.job_title = "Slow as molasses"
Sloth.start_date = "NEVER"


Zoo = Company()
Zoo.name = "Busy Bee"
Zoo.address = "Bee Street"
Zoo.industry_type = "Animal Wrangler"


Pound = Company()
Pound.name = "Turn Back Pound"
Pound.address = "Pound Street"
Pound.industry_type = "Sad"


# Assign 2 people to be employees of the first company. Assign 3 people to be employees of the second company.
Zoo.add_employee(Chicken)
Zoo.add_employee(Sloth)
Zoo.add_employee(Monkey)
Pound.add_employee(Frog)
Pound.add_employee(Bear)

# Output a report to the terminal the displays a business name, and its employees.
test1 = ""
for employee in Pound.employees:
    
    test1 += f"* {employee.name} "
print(f"{Pound.name} is in the {Pound.industry_type} industry and has the following employees: {test1}")

test2 = ""
for employee in Zoo.employees:
    
    test2 += f"* {employee.name} "
print(f"{Zoo.name} is in the {Zoo.industry_type} industry and has the following employees: {test2}")






