from rxconfig import config

import reflex as rx
from STC.Components.navbar import navbar
from STC.Components.header import header
from STC.Components.footer import footer
from STC.Components.section1 import sector
import STC.styles.styles as st
from STC.views.grid import great_grid
from STC.views.sections import section_1, section_2, grid

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
    rx.vstack(
        rx.box(
            header(),
        style = st.box_style
        ),  
        section_1(
            "Ha llegado el momentos más importante...",
            "empezar a tomar el control de tu seguridad personal.",
            "Y has llegado al lugar perfecto para hacerlo con STC.",
            ), 
        great_grid(),
        section_2("STC",
                  """STC es la defensa personal que se moldea a tu medida. 
                  Nuestro sistema se adapta a ti, no al revés, lo que lo hace fácil y rápido de aprender para cualquiera.
                  Con principios comprensibles desde la primera clase, descubrirás cómo proteger tu vida de la mejor manera. 
                  ¡Reserva tu clase gratis ahora y toma el control de tu seguridad!""",
                  "/legionariovencedor.jpeg", "¡Inscribete Ya!"),
        section_1("¡Vive con tranquilidad!,",
                  "¡Vive con seguridad!",
                  """Sentirte seguro no depende de saber muchas tecnicas de combate,
                    depende de tú astucia"""),
        section_2("Jorge Morales",
                  """Con más de 20 años de experiencia en la enseñanza de las artes marciales, 
                  poseo el título de cinturón negro segundo dan en karate shotokan desde 2006. 
                  Junto con el shihan soke Carlos Morales, creamos nuestro sistema de defensa personal, 
                  enfocado en capacitar a personas comunes sin experiencia para protegerse y enfrentar situaciones peligrosas. 
                  En STC, te brindamos la seguridad que necesitas para salir de tu casa sin preocupaciones, 
                  sabiendo que siempre estarás protegido. ¡Descubre cómo STC puede empoderarte y garantizar tu seguridad en todo momento!""",
                  "/Yo.png", "Quiero saber más"),
        
),
        footer(),
        bg = st.negro,
)
    

# Add state and page to the app.
app = rx.App(style=st.font_style)
app.add_page(index,
            title="STC | Sistema Táctico de Combate",
            description="Enseñamos defensa personal",)
app.compile()
