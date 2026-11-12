from drafter import *
from dataclasses import dataclass
set_website_title("Hannah's Counter")
set_site_information(
    author="Hannah Collins",
    description="Clicker",
    sources="",
    planning="",
    links=[""]
)
hide_debug_information()
set_website_framed(False)

@dataclass
class State:
    clicks: int


@route
def index(state: State) -> Page:
    return Page(state, [
        "You have clicked " + str(state.clicks) + " times.\n",
        Button("Click me!", "add_click"),
    ])


@route
def add_click(state: State) -> Page:
    state.clicks = state.clicks + 1
    return index(state)


start_server(State(0))
