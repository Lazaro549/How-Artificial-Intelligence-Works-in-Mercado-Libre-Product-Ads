def attributed_revenue(click_day_revenue, delay_factor=0.15):
    """
    Simulates 72h delayed attribution
    """
    delayed_revenue = click_day_revenue * delay_factor
    return round(click_day_revenue + delayed_revenue, 2)
