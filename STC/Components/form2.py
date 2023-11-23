import os
import asyncio
from datetime import datetime
import json
import httpx

from email_validator import EmailNotValidError, validate_email
from sqlmodel import Field

import reflex as rx
from pcweb import styles
from pcweb.base_state import State
from pcweb.components.spline import spline_component
from pcweb.pages.docs.library import library
from pcweb.pages.docs.getting_started.introduction import introduction
from pcweb.pages.docs.styling.overview import styling_overview
from pcweb.pages.docs.database import database_overview
from pcweb.pages.docs.state.overview import state_overview
from pcweb.pages.docs.hosting.self_hosting import self_hosting
from pcweb.pages.docs.hosting.deploy import deploy
from pcweb.pages.docs.wrapping_react.overview import overview as wrapping_react_overview
from pcweb.templates import webpage
from pcweb import constants

link_style = {
    "color": "black",
    "font_weight": styles.BOLD_WEIGHT,
    "_hover": {"color": styles.ACCENT_COLOR},
}


class Confetti(rx.Component):
    """Confetti component."""

    library = "react-confetti"
    tag = "ReactConfetti"
    is_default = True


confetti = Confetti.create


class Waitlist(rx.Model, table=True):
    email: str
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class IndexState(State):
    """Hold the state for the home page."""

    # Whether to show the call to action.
    show_c2a: bool = True

    # The waitlist email.
    email: str

    # Whether the user signed up for the waitlist.
    signed_up: bool = False

    # Whether to show the confetti.
    show_confetti: bool = False

    def close_c2a(self):
        """Close the call to action."""
        self.show_c2a = False

    def add_contact_to_loops(self, contact_data):
        url = "https://app.loops.so/api/v1/contacts/create"
        loops_api_key = os.getenv("LOOPS_API_KEY")
        if loops_api_key is None:
            print("Loops API key does not exist")
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {loops_api_key}",
        }

        try:
            with httpx.Client() as client:
                response = client.post(url, headers=headers, json=contact_data)
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

        except httpx.RequestError as e:
            print(f"An error occurred: {e}")

    def signup(self):
        """Sign the user up for the waitlist."""
        # Check if the email is valid.
        try:
            validation = validate_email(self.email, check_deliverability=True)
            self.email = validation.email
        except EmailNotValidError as e:
            # Alert the error message.
            return rx.window_alert(str(e))

        # Check if the user is already on the waitlist.
        with rx.session() as session:
            user = session.query(Waitlist).filter(Waitlist.email == self.email).first()
            if user is None:
                # Add the user to the waitlist.
                session.add(Waitlist(email=self.email))
                session.commit()
                contact_data = json.dumps({"email": self.email})
                self.add_contact_to_loops(contact_data)

        self.signed_up = True
        return IndexState.play_confetti

    async def play_confetti(self):
        """Play confetti for 5sec then stop."""
        self.show_confetti = True
        yield
        await asyncio.sleep(5)
        self.show_confetti = False
        yield


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.container(
        *children,
        **kwargs,
    )


def tag(text):
    return rx.text(
        text,
        color="#5646ED",
        bg="#F5EFFE",
        padding_x="0.5em",
        padding_y="0.25em",
        border_radius="8px",
        font_weight=600,
    )


def landing():
    return container(
        rx.cond(
            IndexState.show_confetti,
            confetti(),
        ),
        rx.hstack(
            rx.center(
                rx.vstack(
                    rx.text(
                        rx.span("[", color="#DACEEE"),
                        rx.span("Frontend", color="#696287"),
                        rx.span("]", color="#DACEEE"),
                        rx.span("[", color="#DACEEE"),
                        rx.span("Backend", color="#696287"),
                        rx.span("]", color="#DACEEE"),
                        rx.span("[", color="#DACEEE"),
                        rx.span("Hosting", color="#696287"),
                        rx.span("]", color="#DACEEE"),
                        font_family=styles.MONO,
                        mb=2,
                    ),
                    rx.text(
                        "Web apps in pure Python.",
                        font_family=styles.MONO,
                        font_style="normal",
                        font_weight="600",
                        font_size="6xl",
                        line_height="1.2",
                        letter_spacing="-0.02em",
                    ),
                    rx.text(
                        "Build web apps in minutes. Deploy with a single command.",
                        color="#342E5C",
                        font_size="1.1em",
                        font_family=styles.SANS,
                        padding_top="1em",
                    ),
                    rx.cond(
                        ~IndexState.signed_up,
                        rx.wrap(
                            rx.input_group(
                                rx.input_left_element(
                                    rx.image(
                                        src="/landing_icons/custom_icons/email.png",
                                        height="1.2em",
                                    ),
                                ),
                                rx.input(
                                    placeholder="Your email address...",
                                    on_blur=IndexState.set_email,
                                    style=styles.INPUT_STYLE,
                                    type="email",
                                ),
                                style=styles.INPUT_STYLE,
                            ),
                            rx.button(
                                "Join Hosting Waitlist",
                                on_click=IndexState.signup,
                                style=styles.ACCENT_BUTTON,
                            ),
                            justify="left",
                            should_wrap_children=True,
                            spacing="1em",
                            padding_x=".25em",
                            padding_y="1em",
                        ),
                        rx.text(
                            rx.icon(
                                tag="check",
                            ),
                            " You're on the waitlist!",
                            color=styles.ACCENT_COLOR,
                        ),
                    ),
                    align_items="left",
                    padding="1em",
                ),
                width="100%",
            ),
            spline_component(),
        ),
        padding_top="6em",
        padding_bottom="6em",
        width="100%",
    )


def list_circle(text):
    return rx.flex(
        rx.text(text),
        width="2em",
        height="2em",
        border_radius="6px",
        bg="#F5EFFE",
        color="#5646ED",
        align_items="center",
        justify_content="center",
        font_weight="800",
    )
