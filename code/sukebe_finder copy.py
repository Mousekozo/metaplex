from pyserum.connection import conn
from pyserum.market import Market

cc = conn("https://api.mainnet-beta.solana.com/")
market_address = "2z52mwzBPqA2jGf8jJhCQijHTJ1EUEscX5Mz718SBvmM" # Address for OPAL-Jet

# Load the given market
market = Market.load(cc, market_address)
bids = market.load_bids()
for bid in bids:
    print(f"price: {bid.info.price}, size: {bid.info.size}.")