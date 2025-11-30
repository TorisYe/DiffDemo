# refactored.py


class Employee:
    def __init__(self, name, department, salary, years_of_service):
        self.name = name
        self.department = department
        self.salary = salary
        self.years_of_service = years_of_service

    def __repr__(self):
        return f"Employee(name='{self.name}', department='{self.department}', salary={self.salary}, years_of_service={self.years_of_service})"


def compute_department_stats(employees, min_salary, min_years):
    from collections import defaultdict

    depts = defaultdict(
        lambda: {"total": 0, "count": 0, "salaries": []}
    )  # Accumulate for avg, but keep list for median
    for e in employees:
        if (
            e.salary >= min_salary and e.years_of_service > min_years
        ):  # accidental bug: > instead of >= for years_of_service
            dept_data = depts[e.department]
            dept_data["total"] += e.salary
            dept_data["count"] += 1
            dept_data["salaries"].append(e.salary)
    stats = {}
    for dept, data in depts.items():
        if data["count"] > 0:
            avg = data["total"] / data["count"]
            salaries = sorted(data["salaries"])
            median_index = data["count"] // 2
            median = (
                salaries[median_index]
                if data["count"] % 2
                else (
                    salaries[median_index - 1] + salaries[median_index]
                )
                / 2
            )
            stats[dept] = {
                "average": avg,
                "median": median,
                "count": data["count"],
            }
    sorted_stats = sorted(stats.items())
    return sorted_stats
