from pyserum.connection import conn
from pyserum.market import Market

cc = conn("https://api.mainnet-beta.solana.com/")
market_address = "2qU6MtkBS4NQhzx7FQyxS7qfsjU3ZdbLVyUFjea3KBV2" # Address for OPAL-Jet

# Load the given market
market = Market.load(cc, market_address)
bids = market.load_bids()
t_bid_price = 0.0
t_bid_size = 0.0
size = 0
t_bid_size_l = []
for bid in bids:
    print(f"price: {bid.info.price}, size: {bid.info.size} ")
    if bid.info.price >= 5000:
        size += bid.info.size

    # if t_bid_price == bid.info.price:
    #     t_bid_size += bid.info.size
    #     t_bid_size_l.append(bid.info.size)
    # else:
    #     if t_bid_size == 0.0:
    #         print(f"price: {t_bid_price}, size: {bid.info.size} [{bid.info.size}].")
    #     else:
    #         print(f"price: {t_bid_price}, size: {t_bid_size} {t_bid_size_l}.")
    #     t_bid_size_l = []
    #     t_bid_price = 0.0
    #     t_bid_size = 0.0
    #     t_bid_price = bid.info.price

print(size)