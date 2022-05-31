import time
import akshare as ak


while True:
    try:
        data = ak.stock_zh_a_hist("000001", "daily", "20100101", "20220520", "")
        print(type(data))
        print(data)
        break
    except: # error!
        print('Error! ')
        time.sleep(5)

