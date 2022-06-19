import sqlite3

CREATE_PRICE_TABLE = '''
drop table if exists price;

create table price (
    id integer not null primary key,
    stock_id integer, 
    trade_date text,
    open real,
    high real,
    low real,
    close real,
    turnover_by_volume integer, 
    turnover_by_value integer,  
    change_rate real            
);

'''

def connect():
    return sqlite3.connect("../program6/python_0490_database.db")

def create_price_table(conn):
    conn.executescript(CREATE_PRICE_TABLE)

# TEST CODE ------------------------

if __name__ == "__main__":
    conn = connect()
    create_price_table(conn)
