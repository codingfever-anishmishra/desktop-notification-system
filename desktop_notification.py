from plyer import notification
from time import sleep
while True:
    notification.notify(title="Notification2",
                        message="this is notification2",
                        app_icon="/home/pc/Desktop/desktop_notification/pygame.ico",
                        timeout=5
                    )
    sleep(60*60)
