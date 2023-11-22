import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size


def card_a() -> rx.Component:
    return rx.box(
            rx.vstack(
            rx.image(

            src="/shield.png",
            alt="sheild",
            p= Size.small.value
        ),
        rx.card(
            rx.card(
            rx.text("Body of the Card Component",font_size = Size.medium.value),
            header=rx.heading("Header", font_size = Size.big.value),
            footer=rx.heading("Footer", font_size = Size.default.value),
            variant="outline"
        ),
        ),
        box_shadow = "10px 10px rgba(0, 0, 0, 0.1)" 
        ),
    )