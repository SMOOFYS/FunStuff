def add_mission_control():
    document.querySelector("#mission-control").style.display = "flex"


def add_rocket():
    rocket_element = document.getElementById("rocket")
    rocket_element.style.display = "block"


def set_launch_code(launch_code):
    document.querySelector("#launch-code-input").dataset.launchCode = launch_code


def set_countdown_time(countdown_time):
    if not isinstance(countdown_time, int):
        raise Exception(
            f"Error in set_countdown_time()\n"
            f"  - '{countdown_time}' should be a number without quotes!"
        )
    document.querySelector("#countdown").dataset.countdownTime = countdown_time
