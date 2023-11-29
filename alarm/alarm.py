import time
from playsound import playsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def countdown(count_down_time):
    time_elapsed = 0

    print(CLEAR)

    while time_elapsed < count_down_time:
        time.sleep(1)

        time_elapsed += 1
        minutes_left = (count_down_time - time_elapsed) // 60
        seconds_left = (count_down_time - time_elapsed) % 60

        print(CLEAR_AND_RETURN, f"{minutes_left:02d}:{seconds_left:02d}")

    playsound("./sound.mp3")


def alarm(custom_time):
    current_time = time.strftime("%I:%M:%S")

    print(CLEAR)

    while current_time != custom_time:
        time.sleep(1)

        current_time = time.strftime("%I:%M:%S")

        print(CLEAR_AND_RETURN,
              f"Alarm will sound when it's ==={custom_time}=== \n current time ==={current_time}===")

    playsound("./sound.mp3")


if __name__ == "__main__":
    # user_time = int(input("Input the amount of seconds: "))
    user_time = input("Enter wake up time [00:00:00]: ")
    alarm(user_time)
