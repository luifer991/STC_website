import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size
from STC.Components.link_icon import link_icon
from STC.Components.info_text import info_text
import STC.styles.contants as const
import datetime


def avatar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Jorge Morales",
                size="2xl",
                src="/Yo.png",
                color=st.dorado,
                bg=st.negro,
                padding="2px",
                border="4px",
                border_color=st.dorado_claro
            ),
            rx.vstack(
                rx.heading(
                    "Jorge Morales",
                    size="lg"
                ),
                rx.text(
                    "@STC",
                    margin_top=Size.zero.value,
                    color=st.dorado_claro,
                    font_size=Size.default.value
                ),
                rx.hstack(
                    link_icon(
                        "/facebook.svg",
                        const.FACEBOOK_URL,
                        "Facebook"
                    ),
                    link_icon(
                        "/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),

                    
                    spacing=Size.high.value
                ),
                align_items="start"
            ),
            spacing=Size.default.value
        ),
        rx.flex(
            info_text(
                f"{experience()}+",
                "años de experiencia"
            ),
            width="100%"
        ),
        rx.text(
            f"""
            Con más de 17 años de experiencia en la enseñanza de las artes marciales, 
            poseo el título de cinturón negro segundo dan en karate shotokan desde 2006. 
            Junto con el shihan soke Carlos Morales, creamos nuestro sistema de defensa personal, 
            enfocado en capacitar a personas comunes sin experiencia para protegerse y enfrentar situaciones peligrosas. 
            En STC, te brindamos la seguridad que necesitas para salir de tu casa sin preocupaciones, 
            sabiendo que siempre estarás protegido. 
            ¡Descubre cómo STC puede empoderarte y garantizar tu seguridad en todo momento!""",
            font_size=Size.default.value,
            color=st.dorado_claro
        ),
        spacing=Size.big.value,
        align_items="start",
        text_align = "justify",
        max_width= "560px"
    )


def experience() -> int:
    return datetime.date.today().year - 2006