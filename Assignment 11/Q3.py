import pandas as pd

def find_good_deals(asking_prices, fair_prices):
    """
    Identify cars whose asking price is less than their fair price.

    Parameters:
        asking_prices (pd.Series): Series of car asking prices.
        fair_prices (pd.Series): Series of car fair prices.

    Returns:
        list: List of integer indices corresponding to the good deals.
    """
    good_deals = asking_prices[asking_prices < fair_prices].index.tolist()
    return good_deals

# Example usage
if __name__ == "__main__":
    # Example data
    asking_prices = pd.Series([15000, 18000, 12000, 20000, 17000])
    fair_prices = pd.Series([16000, 17500, 13000, 21000, 16500])

    good_deal_indices = find_good_deals(asking_prices, fair_prices)
    print("Good deal indices:", good_deal_indices)