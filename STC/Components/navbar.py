import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size
from STC.views.linksnavbar import link_button

def navbar():
    return rx.box(
        rx.hstack(
            rx.link(
                rx.image(
                        src="/shield.png",
                        alt="sheild",
                        padding_left=Size.extra.value,
                        width = "60%"
                        ),
                        href="#"
                        ),
        ),
        rx.spacer(),
        rx.menu(
            rx.hstack(
                link_button("inicio","#"),
                link_button("Quiénes Somos","#"),
                link_button("Nuestros Servicios","#"),
                link_button("Blog Táctico","#"),
                pr = Size.extra.value,
            ),
        ),
    style = st.navbar_style,
    )