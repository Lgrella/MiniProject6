from mylib.etlfunctions import (
    connect,
    create,
    insert,
    read,
    update,
    delete,
    sort_payroll,
    print5_query,
)
import os


if os.path.exists("payroll_example.db"):
    os.remove("payroll_example.db")
connect, cursor = connect("payroll_example.db")

# Create / insert
print("Creating...")
create(cursor)
insert(cursor, 1, "Lilly", "Grella", 2000, "Data Scientist")
insert(cursor, 2, "Kenneth", "Zalke", 4000, "Consultant")
insert(cursor, 3, "Patti", "Dinkins", 1000, "Teacher")

print("\n")

print("Reading...")
# Read
info = read(cursor)
print(info)
# query
print("\n")
print("Sorting By Pay Amount...")
sort_payroll(cursor)
print("\n")
print("Printing Top 5...")
print5_query(cursor)

# Update
print("\n")
print("Updating Lilly's Record with increased pay to 3000...")
update(cursor, 1, "Lilly", "Grella", 3000, "Data Scientist")
info = read(cursor)
print(info)

print("\n")
print("Deleting Kenneth's Record...")
# Delete
delete(cursor, 2)
info = read(cursor)
print(info)

connect.commit()
connect.close()
