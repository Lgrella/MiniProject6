from mylib.etlfunctions import connect, create, insert, read, update, delete
import os


if os.path.exists("payroll_example.db"):
    os.remove("payroll_example.db")
connect, cursor = connect("payroll_example.db")

# Create / insert
create(cursor)
insert(cursor, 1, "Lilly", "Grella", 2000, "Data Scientist")
insert(cursor, 2, "Kenneth", "Zalke", 4000, "Consultant")
insert(cursor, 3, "Patti", "Dinkins", 1000, "Teacher")

# Read
info = read(cursor)
print(info)

# Update
update(cursor, 1, "Lilly", "Grella", 3000, "Data Scientist")
info = read(cursor)
print(info)

# Delete
delete(cursor, 2)
info = read(cursor)
print(info)

connect.commit()
connect.close()