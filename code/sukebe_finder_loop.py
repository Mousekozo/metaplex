from pyserum.connection import conn
from pyserum.market import Market
import time
from datetime import datetime, timedelta

check_supply = 100
supply = 725
mint_price = 3360
market_address = "BeqGJwPnRb3fJwhSrfhzgUYKqegUtGtvXajTYzEpgGYr"
cc = conn("https://api.mainnet-beta.solana.com/")

# 2W6ff8LajAwekXVxDARGQ9QFNcRbxmJPE2p3eNsGR7Qu
# legend    2qU6MtkBS4NQhzx7FQyxS7qfsjU3ZdbLVyUFjea3KBV2

# Opal JetJet	        2021/09/10 9:00:00	18,724	10,000	$300	8,000	$320	            2W6ff8LajAwekXVxDARGQ9QFNcRbxmJPE2p3eNsGR7Qu
# Fimbul BYOS Packlite	2021/09/10 10:00:00	1,605	725	    $3,360	875	    $3,640	            BeqGJwPnRb3fJwhSrfhzgUYKqegUtGtvXajTYzEpgGYr
# Calico Guardian	    2021/09/10 11:00:00	224	    100	    $30,950	80	    $33,895 40	$36,250	4TpCAobnJfGFRbZ8gAppS9aZBwEGG1k9tRVmx6FPUvUp

def now_str():
    return datetime.now().strftime('%H:%M:%S.%f')[:-4]

while True:

    # Load the given market
    market = Market.load(cc, market_address)
    bids = market.load_bids()
    t_bid_price = 0.0
    t_bid_size = 0.0
    size = 0
    t_bid_size_l = []

    bid_list = []

    for bid in bids:
        bid_list.append([bid.info.price,bid.info.size])

    last_bid = []
    size = 0
    check_disp = False

    for bid in reversed(bid_list):
        size += bid[1]

        if bid[0] <= mint_price:
            print(f"{now_str()} LowSize up:{last_bid}, out:{bid}, total:{size}, MintPrice:{mint_price}")
            break

        if size >= check_supply and not check_disp:
            print(f"{now_str()} Check up:{last_bid}, out:{bid}, total:{size}")
            check_disp = True

        if size >= supply:
            print(f"{now_str()} SizeMax up:{last_bid}, out:{bid}, total:{size}")
            break

        last_bid = bid

    time.sleep(3)