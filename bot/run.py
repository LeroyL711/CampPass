from checking.checking import Checking
from datetime import datetime, timedelta
import keyboard
import time

with Checking() as bot:
    
    bot.land_first_page()
    bot.garibaldi_click()

    while True:
        # Array to store date and availability
        pass_availabilities = []

        start_time = time.time()
        # formats dates
        current_date = bot.format_date(datetime.now())
        next_date = bot.format_date(datetime.now() + timedelta(days=1))
        date_after = bot.format_date(datetime.now() + timedelta(days=2))

        # Call for current date
        bot.select_date(current_date)
        bot.select_pass_type()
        pass_availabilities.append([current_date, bot.availability_status()])

        # Call for day after
        bot.select_date(next_date)
        pass_availabilities.append([next_date, bot.availability_status()])

        # Call for two days after
        bot.select_date(date_after)
        pass_availabilities.append([date_after, bot.availability_status()])
        print(pass_availabilities)
        time.sleep(11)
        end_time = time.time()
        elapsed_time = end_time - start_time
        seconds = int(elapsed_time % 60)
        print("Elapsed time: " + str(seconds) + " seconds")
        bot.driver.refresh()

        # Breaks loop when q is pressed
        if keyboard.is_pressed("q"):
            bot.driver.quit()