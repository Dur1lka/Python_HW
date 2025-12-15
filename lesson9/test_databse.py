from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

# Подключение к базе данных
def test_db_connection():
    inspector =inspect(db)
    names=inspector.get_table_names()
    assert names[1] == 'company'

# Поиск из таблицы
def test_select():
    connection= db.connect()
    result= connection.execute(text("SELECT * FROM company"))
    rows= result.mappings().all()
    rowl= rows[0]

    assert rowl['id'] == 1
    assert rowl ['name'] == "QA Студия 'ТестировщикЪ'"

    connection.close()

# Поиск из таблицы с фильтром
def test_select_1_row():
    connection= db.connect()
    sql_statement= text ("SELECT * FROM company WHERE id= :company_id")
    result=connection.execute(sql_statement,{"company_id":1})
    rows=result.mappings().all()

    assert len(rows) == 1
    assert rows[0] ["name"] == "QA Студия 'ТестировщикЪ'"

    connection.close()

# Поиск из таблицы с двумя фильтрами
def tesdt_select_1_row_2():
    connection= db.connect()
    sql_statement= text("SELECT * FROM company"
                        "WHERE \"is_active\"=:is_active AND id>=:id")
    result=connection.execute(sql_statement, {"id":65,"is_active":True})
    rows=result.mappings().all()

    assert len(rows) == 14