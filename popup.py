import time
from plyer import notification

# Set the reminder text
reminder_text = "This is a reminder! for Faisal"

# Set the duration of the reminder in seconds
reminder_duration = 5

# Specify the absolute path to the icon file
app_icon = r"C:\Users\Admin\Pictures\icon.ico"

# Create the notification
notification.notify(
    title="Reminder",
    message=reminder_text,
    app_icon=app_icon,
)

# Wait for the reminder to expire
#time.sleep(reminder_duration)