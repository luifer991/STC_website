import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size
from STC.views.linksnavbar import link_button

def navbar()-> rx.Component:
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
                link_button("inicio","/"),
                link_button("Quiénes Somos","https://luifer991.wixsite.com/stcsistema/qui%C3%A9nes-somos"),
                link_button("Nuestros Servicios","#"),
                link_button("Blog Táctico","https://luifer991.wixsite.com/stcsistema/blog"),
                pr = Size.extra.value,
            ),
        ),
    style = st.navbar_style,
    )