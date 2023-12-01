import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size
import STC.styles.contants as const




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
                href= const.LANDING_PAGE_URL,
                is_external=True
                ),
            style = st.header_style
    )
            
