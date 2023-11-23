import reflex as rx
from enum import Enum

# Colores de marca

negro = "#000000"
gris = "#747474"
azul ="#19284C"
dorado = "#CBB26A"
dorado_claro = "#D8C690"
blanco ="#ffffff"

# tipografia

Bevan = "Bevan sans serif"
libre = "Libre Baskerville sans serif"



class Size (Enum):
    zero = "0px !important"
    small = "0.5em",
    medium = "0.8em",
    default = "1em",
    high = "1.5em",
    big = "2em",
    xl = "3em",
    extra = "4em",

font_style = {
    rx.Heading:{
        "color" : dorado, 
        "font_family" : Bevan,
        "font_size": Size.big.value,
    },
    rx.Text:{
    "font_family":libre, 
    "as_":"b", 
    "color": dorado_claro,
    "as_":"b", 
    "font_size": Size.big.value,
    },
    rx.Vstack:{
    "pt": Size.default.value,
    "justufy_content": "center",
    "px": Size.high.value
},
}

navbar_style = dict (
        position="fixed",
        width="100%",
        top="0px",
        z_index="999",
        bg=negro,
        padding_y=Size.high.value,
        display="flex",
)

header_style = dict (
    width = "100%",
    height="100vh",
    justify_content="center",
    align_items="center",
    display = "flex",
    margin_top = "0px",
    
)

button_style = dict(
    position = "relative; top: 40px",
    padding = Size.high.value,
    font_family = Bevan,
    font_size = "md",
    color = blanco,
    border_color = azul,
    _hover = {
        "padding_x": Size.xl.value,
        "color": negro,
        "border_color": blanco,
        "color_scheme": "black_alpha",
        "font_size":"md",
        "bg": dorado_claro,
    },
    margin_top = "50px !important"
)
box_style = dict (
    width = "100%",
    background_image = "url(/pelea.png)",
    background_size="cover",
    background_repeat="no-repeat",
    background_position ="top",
    #background_color = st.negro,
    #opacity = "0.6",
    background_attachment = "fixed",
    border_bottom = "0px !important"
)

text_secondary = dict(
    text_align = "justify", 
    font_size = Size.default.value,
    pt = Size.medium.value,
    color = blanco
)

