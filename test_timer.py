from timer import calculate_seconds, format_time_display

def test_calculate_seconds_test_mode():
    # 25 Min * 60 Sek * 0.01 = 15 Sek
    assert calculate_seconds(25, is_test=True) == 15

def test_calculate_seconds_real_mode():
    # 5 Min * 60 Sek * 1.0 = 300 Sek
    assert calculate_seconds(5, is_test=False) == 300

def test_format_time_display():
    assert format_time_display(125) == "02:05"
    assert format_time_display(45) == "00:45"
    assert format_time_display(0) == "00:00"