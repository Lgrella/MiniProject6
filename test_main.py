from mylib.etlfunctions import connect, create, insert, read, update, delete
import os


def test_create():
    if os.path.exists("payroll_example.db"):
        os.remove("payroll_example.db")
    _, cursor = connect("payroll_example.db")
    assert os.path.exists("payroll_example.db")
    create(cursor)

    table_name = "payroll"
    cursor.execute(f"PRAGMA table_info({table_name})")
    result = cursor.fetchall()
    assert result is not None


def test_insert():
    if os.path.exists("payroll_example.db"):
        os.remove("payroll_example.db")
    _, cursor = connect("payroll_example.db")
    create(cursor)
    insert(cursor, 1, "Lilly", "Grella", 2000, "Data Scientist")
    cursor.execute("SELECT * FROM payroll")
    result = cursor.fetchone()
    assert result is not None


def test_read():
    if os.path.exists("payroll_example.db"):
        os.remove("payroll_example.db")
    _, cursor = connect("payroll_example.db")
    create(cursor)
    insert(cursor, 1, "Lilly", "Grella", 2000, "Data Scientist")
    insert(cursor, 2, "Kenneth", "Zalke", 4000, "Consultant")
    insert(cursor, 3, "Patti", "Dinkins", 1000, "Teacher")

    info = read(cursor)
    assert len(info) == 3


def test_update():
    if os.path.exists("payroll_example.db"):
        os.remove("payroll_example.db")
    _, cursor = connect("payroll_example.db")
    create(cursor)
    insert(cursor, 1, "Lilly", "Grella", 2000, "Data Scientist")
    insert(cursor, 2, "Kenneth", "Zalke", 4000, "Consultant")
    insert(cursor, 3, "Patti", "Dinkins", 1000, "Teacher")

    update(cursor, 1, "Lilly", "Grella", 2500, "Data Scientist II")
    info = read(cursor)
    assert info[0] == (1, "Lilly", "Grella", 2500, "Data Scientist II")


def test_delete():
    if os.path.exists("payroll_example.db"):
        os.remove("payroll_example.db")
    _, cursor = connect("payroll_example.db")
    create(cursor)
    insert(cursor, 1, "Lilly", "Grella", 2000, "Data Scientist")
    insert(cursor, 2, "Kenneth", "Zalke", 4000, "Consultant")
    insert(cursor, 3, "Patti", "Dinkins", 1000, "Teacher")

    delete(cursor, 1)
    delete(cursor, 2)
    delete(cursor, 3)
    info = read(cursor)
    assert len(info) == 0
