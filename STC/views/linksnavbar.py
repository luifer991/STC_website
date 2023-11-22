import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size

def link_button(title: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
                    rx.text(title,
                    font_size= "lg", 
                    _hover = {
                        "color":st.blanco
                        }),
                    variant = "unstyled",
                    padding = Size.small.value,
                    size = "md",
                    _hover = {
                        "padding_top": Size.default.value,
                    },         
        ),
        href=url,
        is_external=True,
        width="100%"
    )