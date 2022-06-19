from python_0625_stock_dao_v2 import connect, get_all_stocks
import akshare as ak
import time



def load_price_from_akshare(stock):

    print(f"LOG - handling {stock} -------------------------------------")

    while True:
        try:
            prices = ak.stock_zh_a_hist(stock.get_ticker_value(), "daily", "20100101", "20220619", "")
            print(prices)
            return prices
        except:  # error!
            print('Error! ')
            time.sleep(5)


# TEST CODE ------------------------

def persist_price_to_db(stock, prices):
    pass


if __name__ == "__main__":

     conn = connect()

     stocks = get_all_stocks(conn)

     print(f"LOG - stocks: {stocks}")

     for stock in stocks:

         prices = load_price_from_akshare(stock)

         persist_price_to_db(stock, prices)
