import reflex as rx
import datetime
import STC.styles.styles as st
from STC.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="/STC.png",
                    padding_left=Size.big.value,
                    width=Size.extra.value,
                    height="auto",
        ),
        rx.spacer(),
        rx.span(
            f"© 2006-{datetime.date.today().year} Sistema Táctico de Combate. Todos los derechos reservados.",color=st.blanco),
        bg=st.negro,
        width="100%",
        padding=Size.high.value,
        margin_top="0px",
        display="flex"
    )