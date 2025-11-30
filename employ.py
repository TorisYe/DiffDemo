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

    filtered = [
        e
        for e in employees
        if e.salary >= min_salary and e.years_of_service >= min_years
    ]
    depts = defaultdict(list)
    for e in filtered:
        depts[e.department].append(e.salary)
    stats = {}
    for dept, sals in depts.items():
        if sals:
            sals.sort()
            avg = sum(sals) / len(sals)
            median = (
                sals[len(sals) // 2]
                if len(sals) % 2
                else (sals[len(sals) // 2 - 1] + sals[len(sals) // 2])
                / 2
            )
            stats[dept] = {
                "average": avg,
                "median": median,
                "count": len(sals),
            }
    sorted_stats = sorted(stats.items())
    return sorted_stats
