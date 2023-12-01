import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size
import STC.styles.contants as const


def section_2(title: str, body: str, url: str, button: str) -> rx.Component:
    return rx.responsive_grid(
        rx.box(
                rx.image(src=url,
                     width = "100%",
                     height = "100%"
            ),
            row_span=2,
            col_span=3,
            justify_content="center",
        ),
        rx.box(
            rx.vstack(
                rx.heading(title),
                rx.text(body, style = st.text_secondary),
                rx.link(
                    rx.button(
                        button,                    
                    padding = Size.default.value,
                    variant= "ghost",
                    bg = st.gris,
                    color=st.blanco,
                    _hover ={
                        "bg": st.dorado_claro,
                        "color": st.negro,
                        "padding":Size.high.value
                    }
                    ),
                    href=const.WHATSAPP_URL,
                    position = "relative; left: 100px; top: 100px;",
                    is_external=True
                ),
            ),
            
            row_span=2,
            col_span=3,
            text_align="center",
            justify_content="center",
            display = "flex"
        ),
        columns=[1,1,2],
        gap=2,
        max_width= "1024px"
    )
