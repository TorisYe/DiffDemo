# test.py

from employ import (
    Employee,
    compute_department_stats,
)  # or import from refactored if needed

# Create sample Employee instances
employees = [
    Employee("Alice", "HR", 60000, 6),
    Employee("Bob", "Engineering", 80000, 4),
    Employee("Charlie", "HR", 55000, 7),
    Employee("David", "Engineering", 90000, 8),
    Employee("Eve", "Sales", 70000, 5),
]

# Run the function with reasonable inputs
min_salary = 50000
min_years = 5
result = compute_department_stats(employees, min_salary, min_years)

# Output the result for verification or type inference
print(result)
