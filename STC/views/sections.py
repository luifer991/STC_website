import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size
from STC.views.card import card_a


def section_1(title_1:str,title_2:str,body:str, position:str) -> rx.Component:
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
    st.section_1_style,
    background_position = position,
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