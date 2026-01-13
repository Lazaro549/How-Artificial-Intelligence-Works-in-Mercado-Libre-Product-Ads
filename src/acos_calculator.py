def calculate_acos(ad_spend: float, revenue: float) -> float:
    """
    Calculates ACOS (Advertising Cost of Sales)

    ACOS = (Ad Spend / Revenue) * 100
    """
    if revenue == 0:
        return 0.0
    return round((ad_spend / revenue) * 100, 2)


if __name__ == "__main__":
    ad_spend = 18000
    revenue = 180000

    acos = calculate_acos(ad_spend, revenue)
    print(f"ACOS: {acos}%")
