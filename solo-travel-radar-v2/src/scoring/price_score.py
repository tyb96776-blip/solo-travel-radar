def price_score(total_cost):
    if total_cost <= 120: return "target"
    if total_cost <= 160: return "cheap"
    if total_cost <= 210: return "moderate"
    return "normal"
