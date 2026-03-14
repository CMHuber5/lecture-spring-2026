import time
import os
os.system('color')
TEST_MODE = True

"""Focus Timer: ein einfacher Timer für Fokus- und Pausen-Zeiten"""

# Logik-Funktion
def calculate_seconds(minutes, is_test=True):
    factor = 0.01 if is_test else 1.0
    return int(minutes * 60 * factor)

# Formatierungs-Funktion
def format_time_display(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{mins:02d}:{secs:02d}"

def notify(message):
    print(f"\n {message} \a")

def countdown(minutes, label):
    color = "\033[91m" if "FOCUS" in label else "\033[92m"
    reset = "\033[0m"
    seconds = calculate_seconds(minutes, is_test=TEST_MODE)
       
    while seconds > 0:
        time_display = format_time_display(seconds)
        print(f"{color}{label}: {time_display}{reset}", end="\r") 
        time.sleep(1)
        seconds -= 1

def start_timer():
    # Zielabfrage am Anfang
    try:
        goal = int(input("Please enter number of focus sessions: "))
    except ValueError:
        print("Please enter a valid number! Default set to 4.")
        goal = 4

    sessions_done = 0
    while sessions_done < goal:
        countdown(25, f"FOCUS ({sessions_done + 1}/{goal})")
        sessions_done += 1
        
        if sessions_done < goal:
            notify(f"Round {sessions_done} done! Time for a 5-minute coffee break.")
            countdown(5, "BREAK")
            input("\nBreak over! Press Enter to start the next round...")
        else:
            notify("\nWell done – you’ve successfully completed all the sessions.\nYou’ve earned yourself an after-work beer.\n")

if __name__ == "__main__":
    start_timer()