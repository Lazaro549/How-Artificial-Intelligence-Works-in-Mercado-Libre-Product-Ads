def campaign_decision(acos: float, target_acos: float, conversion_rate: float):
    """
    Simulates real Product Ads decisions
    """
    if acos > target_acos * 1.2:
        return "Reduce bid or pause campaign"
    
    if conversion_rate < 1:
        return "Improve listing quality before increasing budget"
    
    if acos <= target_acos and conversion_rate >= 2:
        return "Scale budget"

    return "Maintain current strategy"
