import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size




def header() -> rx.Component:
    return rx.vstack(
            rx.heading(
                "CADA PERSONA ES ÚNICA", 
            ),
            rx.heading(
                "Y TU SEGURIDAD TAMBIÉN LO ES.", 
            ),
            rx.heading(
                "JUNTOS LA CREAREMOS CON STC", 
                ),
                rx.link(
                    rx.button(
                    "Aprende Más",
                    variant = "outline",
                    style = st.button_style,

                ),
                href= "#",
                ),
            style = st.header_style
    )
            
