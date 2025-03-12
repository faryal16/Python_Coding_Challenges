# 🚀 Mission:
# Create a simple alarm clock that plays a sound at a specified time.

import time
import datetime
import winsound

def play_alarm():
    """Plays an alarm sound. """
    print("\n⏰ Time's up! Wakeup! 🔔\n")
    for _ in range(5):
        winsound.Beep(1000, 500)
        time.sleep(1)
        
def countdown(alarm_time):
    """Displays a live countdown until the alarm time."""
    print(f"\n⏳ Alarm set for {alarm_time.strftime('%I:%M:%S %p')}. Waiting...\n")
    
    while True:
        now  = datetime.datetime.now()
        remaining_time = (alarm_time - now).total_seconds()  
        
        if remaining_time <= 0:
            play_alarm()
            return snooze_option(alarm_time)   
        
        # Convert seconds to H:M:S
        hours, remainder = divmod(int(remaining_time) , 3600)
        minutes , seconds = divmod(remainder , 60)
        
        print(f"⌛ Time Left: {hours:02}:{minutes:02}:{seconds:02}", end="\r \n")
        time.sleep(1)
        
def snooze_option(alarm_time):
    """Allows the user to snooze the alarm or stop it."""
    while True:
        snooze = input("\n🔄 Snooze for 5 minutes? (y/n): ").strip().lower()
        if snooze == 'y':
            snooze_time = alarm_time + datetime.timedelta(minutes=5)
            print(f"⏳ Snoozing... Next alarm at {snooze_time.strftime('%I:%M:%S %p')}")
            return countdown(snooze_time)  # Restart countdown with snooze time
        elif snooze == 'n':
            print("\n✅ Alarm stopped.")
            return False  # Stop the program
        else:
            print("❌ Invalid choice. Please enter 'y' or 'n'.")
           
def main():
    """Main function to set and start the alarm."""
    print("\n\t\t⏰ WElcome to my Alaram Clock App!! ⏰\n")
    while True:
        user_time = input("🚀Set alarm time (HH:MM:SS AM/PM): ").strip()
        try:
            # Convert user input to datetime
            alarm_time = datetime.datetime.strptime(user_time, "%I:%M:%S %p")
            now = datetime.datetime.now()

            # Ensure alarm is set for today or tomorrow if time has passed
            alarm_time = now.replace(hour=alarm_time.hour, minute=alarm_time.minute, second=alarm_time.second)
            if alarm_time < now:
                alarm_time += datetime.timedelta(days=1)

            # Start the alarm countdown
            if countdown(alarm_time) is False:  # If snooze_option() returns False, exit program
                break
        except ValueError:
            print("❌ Invalid format! Please use HH:MM:SS AM/PM (e.g., 07:30:00 PM)")

if __name__ == "__main__":
    main()