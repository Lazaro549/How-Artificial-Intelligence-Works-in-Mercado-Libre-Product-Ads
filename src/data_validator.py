def validate_metrics(impressions, clicks, revenue):
    if impressions < clicks:
        raise ValueError("Clicks cannot exceed impressions")
    if revenue < 0:
        raise ValueError("Revenue cannot be negative")
    return True
