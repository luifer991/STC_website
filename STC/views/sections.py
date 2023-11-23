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