from src.transform.padd_mapping import assign_padd

def test_texas_is_padd3():
    assert assign_padd("TX") == "PADD3"

def test_california_is_padd5():
    assert assign_padd("CA") == "PADD5"
