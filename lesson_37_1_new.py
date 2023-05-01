import sqlite3

conn = sqlite3.connect('lesson_37_database.db')

cur = conn.cursor()


#task 1
# cur.execute("""SELECT employees.first_name, employees.last_name,
#                         department.department_id, department.department_name
#                     FROM employees JOIN department ON employees.department_id;
#
#                 """)
#
# data = cur.fetchall()



#task2
# cur.execute("""SELECT employees.first_name, employees.last_name,department.department_name, locations.city,
# #                 locations.state_province FROM employees
# #                 JOIN department ON employees.department_id = department.department_id
# #                 LEFT JOIN locations ON department.location_id = locations.location_id;
# # """)
#
# data = cur.fetchall()
# print(data)


#task3
# cur.execute("""SELECT employees.first_name, employees.last_name,department.*
#                 FROM employees
#                 JOIN department ON employees.department_id = department.department_id
#                 WHERE employees.department_id BETWEEN 40 AND 80;
#
# """)
#
# data = cur.fetchall()
# print(data)



#task4
# cur.execute("""SELECT department.department_id, employees.first_name
#                 FROM department
#                 LEFT JOIN employees ON department.department_id = employees.department_id;
#
# """)
#
# data = cur.fetchall()
# print(data)


#task5
# I couldn't find the managers table in the data base

#task6
# cur.execute("""SELECT jobs.job_title, employees.first_name || ' ' || employees.last_name as full_name,
#                 (jobs.max_salary - employees.salary) as salary_diff
#                 FROM employees
#                 LEFT JOIN jobs ON employees.job_id = jobs.job_id;
#
# """)
#
# data = cur.fetchall()
# print(data)

#task 7
# Колонка з averages порожня

# task 8
#
# cur.execute("""SELECT  employees.first_name || ' ' || employees.last_name as full_name,
#                 employees.salary
#                 FROM employees
#                 LEFT JOIN department ON employees.department_id = department.department_id
#                 LEFT JOIN locations ON department.location_id = locations.location_id
#                 WHERE locations.city = 'London';
#
# """)

#
# data = cur.fetchall()
# print(data)


# task 9

# cur.execute("""SELECT department.department_name, COUNT(*) as employee_count
#                 FROM employees
#                 JOIN department ON employees.department_id = department.department_id
#                 GROUP BY department.department_name;
# """)
#
#
# data = cur.fetchall()
# print(data)

conn.commit()

conn.close()
