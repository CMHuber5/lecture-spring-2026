import timer


def test_calculate_seconds_test_mode():
    # Prüft, ob im Testmodus Zeit verkürzt berechnet wird
    assert timer.calculate_seconds(25, is_test=True) == 15


def test_calculate_seconds_real_mode():
    # Prüft Umrechnung von min in sec
    assert timer.calculate_seconds(5, is_test=False) == 300


def test_format_time_display():
    # Prüft, ob Sekunden als MM:SS angezeigt werden
    assert timer.format_time_display(125) == "02:05"
    assert timer.format_time_display(45) == "00:45"
    assert timer.format_time_display(0) == "00:00"


def test_progress_bar():
    # Prüft Ladebalken bei 50 %
    assert timer.progress_bar(10, 5, length=10) == "[█████-----]  50%"


def test_notify_outputs_message(capsys):
    # Prüft, ob message auf der Konsole erscheint
    timer.notify("Test message")
    captured = capsys.readouterr()
    assert "Test message" in captured.out


def test_countdown_runs(monkeypatch):
    # Simuliert Countdown ohne time.sleep
    monkeypatch.setattr(timer.time, "sleep", lambda _: None)

    timer.countdown(1, "FOCUS")

def test_start_timer_runs(monkeypatch):
    # Simuliert Eingabe und testet, ob start_timer() ohne Eingabe läuft
    monkeypatch.setattr("builtins.input", lambda _: "1")
    monkeypatch.setattr(timer, "countdown", lambda min, label: None)
    monkeypatch.setattr(timer, "notify", lambda m: None)

    timer.start_timer()