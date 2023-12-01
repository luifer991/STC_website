import reflex as rx
from STC.styles.styles import Size
import STC.styles.styles as st


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(
            title,
            font_weight="bold",
            color=st.blanco
        ),
        f" {body}",
        font_size=Size.medium.value,
        color=st.dorado_claro
    )