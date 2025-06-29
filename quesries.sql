CREATE TABLE IF NOT EXISTS personal_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    age INTEGER NOT NULL,
    email TEXT UNIQUE NOT NULL
);

INSERT INTO personal_info (first_name, last_name, middle_name, age, email) 
    VALUES('Python', 'Javascript', NULL, 20, 'python@javascript.com');

SELECT * FROM personal_info;
