def second_best_price(bids: list) -> float:
    """
    Simulates Mercado Libre second-best-price auction.
    """
    if len(bids) < 2:
        return bids[0]

    sorted_bids = sorted(bids, reverse=True)
    return round(sorted_bids[1] + 0.01, 2)


if __name__ == "__main__":
    bids = [3.50, 2.90, 3.10, 2.70]

    winning_cpc = second_best_price(bids)
    print(f"Winning CPC: ${winning_cpc}")
