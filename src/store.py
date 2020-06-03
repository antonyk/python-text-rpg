# define a store using oop principles



class Store:
  def __init__(self, name, departments):
    self.name = name
    self.init_departments(departments)

  def __str__(self):
    # this will print out the name of the store as well as any departments
    result = f"Store: {self.name}\n"
    for i in self.departments:
      result += " " + str(i) + ", \n"
    return result

  def init_departments(self, departments):
    self.departments = [Department(i+1, d) for i, d in enumerate(departments)]



class Department:
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def __str__(self):
    return f"{self.id}: {self.name}"

departments = [
  "apparel",
  "electronics",
  "beauty"
]

store = Store("My Store", departments)
print(store)

# add a way for users to select departments
selection = int(input("Select a department: "))

print(f"Your selected department: {departments[selection-1]} ")

