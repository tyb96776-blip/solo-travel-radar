from src.scoring.price_score import price_score

def test_price_score():
    assert price_score(100) == "target"
    assert price_score(150) == "cheap"
