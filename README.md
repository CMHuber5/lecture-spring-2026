# Lecture Spring 2026
![Tests](https://img.shields.io/github/actions/workflow/status/CMHuber5/lecture-spring-2026/python-app.yml?style=flat&label=tests%20🌸&color=ff69b4)
![License](https://img.shields.io/github/license/CMHuber5/lecture-spring-2026?style=flat&color=blue)

## Erlaeuterung des Timers
Fokus-Timer für das Terminal mit je 25 min Fokus-Intervall und 5 min Pausen-Intervall pro Session.
Die Anzahl an Sessions kann zu Beginn durch die/den BenutzerIn eingegeben werden.
- calculate_seconds(): Umwandlung von min in sec
- format_time_display(): Formatiert Zeit
- progress_bar(): Berechnet proz. Fortschritt und zeigt diesen als Ladebalken im Terminal an
- notify(): Ausgabe von message im Terminal
- countdown(): Steuert und aktualisiert Zeitanzeige
- start_timer(): Erfasst Eingabe der Anzahl von Sessions und wechselt  zw. Fokus- und Pausen-Intervall

Zu Testzwecken wurde TEST_MODE auf True gesetzt und die Zeit auf 1 % der Originaldauer verkürzt.

## KI-Nutzung
Zur Unterstuetzung wurde das KI-Tool ChatGPT für folgendes eingesetzt: 
- Inspiration für Test Funktionen
- Einbindung der test.py Datei in github
- Installation und Verwendung von ruff
- Anpassung des Designs der Badges
