import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size



def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.high.value,
            height=Size.high.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )