def optimize_acos(current_acos, performance_trend):
    """
    Simple learning logic based on performance trend
    """
    if performance_trend == "improving":
        return round(current_acos * 0.95, 2)
    if performance_trend == "declining":
        return round(current_acos * 1.10, 2)

    return current_acos
