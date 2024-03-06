--Создайте таблицу `Employees` со следующими столбцами:
--- `employee_id` - идентификатор сотрудника (уникальный ключ)
--- `department_id` - идентификатор отдела, к которому относится сотрудник
--- `employee_name` - имя сотрудника
--- `salary` - заработная плата сотрудника
--- `hire_date` - дата приема на работу
--Вам нужно выполнить любые 5 запросов:
--1. Определить общее количество сотрудников в компании.
--2. Рассчитать среднюю заработную плату в компании.
--3. Определить количество сотрудников в каждом отделе.
--4. Найти самую высокооплачиваемую должность.
--5. Рассчитать общую сумму затрат на заработную плату для каждого отдела.
--6. Найти средний стаж работы сотрудников в компании.
--7. Определить месяц с наибольшим числом наймов сотрудников.
CREATE TABLE if NOT EXISTS employees (
employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
department_id INTEGER,
employee_name TEXT NOT NULL,
salary INTEGER,
hire_date TEXT
);
INSERT INTO employees (department_id, employee_name, salary, hire_date)
VALUES
(1, "Иванов Иван", 70000, "2022-09-30"),
(2, "Петров Виктор", 50000, "2021-03-15"),
(1, "Сидорова Ольга", 15000, "2022-03-01"),
(2, "Кузнецова Мария", 70000, "2020-03-15"),
(3, "Фёдоров Иван", 60000, "2020-05-10"),
(1, "Васильев Дмитрий", 100000, "2020-10-11"),
(3, "Новиков Сергей", 45000, "2021-07-06");
SELECT * FROM employees;
SELECT count (employee_id) as "кол-во сотрудников" FROM employees; 
SELECT avg(salary) as "средняя зарплата" FROM employees;
SELECT department_id, count(*) FROM employees GROUP by department_id;
--кол-во сотрудников в каждом отделе
SELECT max(salary) as "самая высокая зарплата" FROM employees;
SELECT sum(salary) as "сумма", department_id as "отдел" FROM employees GROUP by department_id;
SELECT avg(julianday("now") - julianday(hire_date)) as "средний стаж" FROM employees;
