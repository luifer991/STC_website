import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size


def section_2(title: str, body: str, url: str, button: str) -> rx.Component:
    return rx.grid(
        rx.grid_item(
                rx.image(src=url,
                     width = "100%",
                     height = "100%"
            ),
            row_span=2,
            col_span=3,
            justify_content="center",
        ),
        rx.grid_item(
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
                    href="#",
                    position = "relative; left: 100px; top: 100px;",
                ),
            ),
            
            row_span=2,
            col_span=3,
            text_align="center",
            justify_content="center",
            display = "flex"
        ),
        template_rows="repeat(2, 1fr)",
        template_columns="repeat(6, 1fr)",
        h="60vh",
        width="100%",
        gap=2,
        max_width= "1024px"
    )
