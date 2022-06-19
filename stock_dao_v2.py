'''
dao means: 'data access object'
stock dao means: this program takes care of accessing stock related info in db


level 4 - UI layer - Web

level 3 - service layer - all your busincess logic

level 2 - entity layer - stock class object / price class object / financial_data class object

level 1 - dao layer - stock dao / price dao / financial_data dao

level 0 - database layer - sqlite3 + dbeaver

'''
import sqlite3
from python_0623_stock_entity import stock




GET_ALL_STOCKS = "select * from stock;"

GET_STOCK_BY_ID = "select * from stock where id = ?;"







def connect():
    return sqlite3.connect("../program6/python_0490_database.db")


def get_all_stocks(connection):
    with connection:
        tup_list = connection.execute(GET_ALL_STOCKS).fetchall()
        stock_list = [stock(*t) for t in tup_list]
        return stock_list


def get_by_id(connection, id):
    with connection:
        tup = connection.execute(GET_STOCK_BY_ID, (id,)).fetchone() # single value tuple must use comma
        s = stock(*tup)
        return s


def get_by_ticker(connection, ticker):
    pass

def get_by_name(connection, name):
    pass



# TEST CODE -------------------------------------

def print_menu():
    menu = '''
    --------------------------
     a int value:
    1) get all stocks
    2) get stock by id
    3) get stock by ticker
    4) get stock by name
    '''
    print(menu)



if __name__ == "__main__":

    conn = connect()

    print_menu()

    command = int(input())



    # ret = get_all_stocks(conn)
    # print(ret)
    #
    # stock = get_by_id(conn, 1)
    # print(stock)
