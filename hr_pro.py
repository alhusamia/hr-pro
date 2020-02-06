from datetime import datetime



class Employee:
	today = datetime.now()

	def __init__(self, name, age, salary, employment_year):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_year = employment_year

	def get_working_years(self):
		 return (int(self.today.year) - int(self.employment_year))



	def __str__(self):
		return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()}"


class Manager(Employee):
	def __init__(self, name, age, salary, employment_year,bonus_percentage):
		super().__init__(name, age, salary, employment_year)
		self.bonus_percentage = bonus_percentage
	def get_bonus(self):
		return (float(self.bonus_percentage) * int(self.salary))

	def __str__(self):
		return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()} Bonus: {self.get_bonus()}"


def main():
	# main code here.
	options = ["Show Employees", "Show Managers", "Add An Employee", "Add A Manager", "Exit"]
	employee = []
	manager = []
	dd = True
	j = 1
	while dd:
		print()
		print("options: ")
		for i in options:
			print(f"    {j}. {i}")
			j =j+ 1
		j = 1
		print()
		x = int(input("What would you like to do? "))
		if x == 1:
			print("-" * 17)
			print("Employees")
			for x in employee:
				print(x.__str__())


		elif x == 2:
			print("-" * 17)
			print("Managers")
			for y in manager:
				print(y.__str__())

		elif x == 3:
			num = 0
			print("-" * 17)
			name = input("name: ")
			age = input("age: ")
			salary = (input("salary: "))
			employment_year =(input("employment_year: "))
			print("Employee added succesfully")
			p1 = Employee(name, age, salary, employment_year)
			employee.append(p1)
		elif x == 4:
			name = input("name: ")
			age = input("age: ")
			salary =(input("salary: "))
			employment_year = input("employment_year: ")
			bonus_percentag =(input("Bonus Percentage: "))
			print("Manager added succesfully")
			p2 = Manager(name, age, salary, employment_year,bonus_percentag)
			manager.append(p2)

		elif x == 5:
			dd = False


if __name__ == '__main__':
	main()
