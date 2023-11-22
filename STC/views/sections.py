import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size
from STC.views.card import card_a

def section_1(title_1:str,title_2:str,body:str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title_1,
        ),
        rx.heading(
            title_2,
        ),
        rx.text(
            body,
            padding_top = Size.medium.value,
            color = st.blanco,
            font_size = Size.high.value,
        ),
    width = "100%",
    height="50vh",
    justify_content="center",
    align_items="center",
    background_color = st.azul,
    margin_top = "0px !important",
    display = "flex",
    background_image = "url(/shieldblack.png)",
    background_size="400px auto",
    background_repeat="no-repeat",
    background_position ="-100px 100px",
    )




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

def grid() -> rx.Component:
    return rx.responsive_grid(
        rx.hstack( 
            card_a(),
            card_a(),
            card_a(),
            card_a(),
        ),


    columns=[4],
    spacing="50",
    margin_y= Size.xl.value,
    display="flex",
)


        #rx.flex(
        #    grid(),
         #   justify_content = "center",
          #  align_items = "center",
           # width = "100%"
        #),  