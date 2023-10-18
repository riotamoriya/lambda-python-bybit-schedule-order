import os
from dotenv import load_dotenv
from pybit.unified_trading import HTTP

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

BYBIT_API_KEY:str = os.environ["BYBIT_API_KEY"]
BYBIT_API_SECRET:str = os.environ["BYBIT_API_SECRET"]

def order_bybit(event):
  session = HTTP(
      testnet=False,
      api_key=BYBIT_API_KEY,
      api_secret=BYBIT_API_SECRET
  )
  order_return = session.place_order(**event)
  
  return order_return

if __name__ == '__main__':
  print(order_bybit())