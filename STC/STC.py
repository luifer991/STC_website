from rxconfig import config

import reflex as rx
from STC.Components.navbar import navbar
from STC.Components.header import header
from STC.Components.footer import footer
import STC.styles.styles as st
from STC.views.grid import great_grid
from STC.views.sections import section_1
from STC.Components.section2 import section_2
import STC.styles.texts as text
from STC.Components.avatar import avatar


class State(rx.State):
    pass
    
async def api_test(item_id: int): 
    return {"my_result": item_id}

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            header(),
        style = st.box_style
        ),  
        
        section_1(
            text.SECTION_TITLE_1,
            text.SECTION_TITLE_2,
            text.SECTION_TITLE_3,
            st.position_1,
            ), 
        rx.vstack(
        great_grid(),
        section_2(text.SECTION_2_TEXT_1,
                  text.SECTION_2_TEXT_2,
                  text.SECTION_2_img_1, 
                  text.SECTION_2_TEXT_4),
        ),
        section_1(text.SECTION_TITLE_4,
                  text.SECTION_TITLE_5,
                  text.SECTION_TITLE_6,
                  st.position_2),   
        rx.vstack(
            avatar()
        ),
        

        footer(),
        bg = st.negro,
)
    

# Add state and page to the app.
app = rx.App(
    stylesheets=st.STYLESHEETS,
    style=st.font_style
    )
app.add_page(index,
            title="STC | Sistema Táctico de Combate",
            description="Enseñamos defensa personal",)
app.compile()
