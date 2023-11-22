import reflex as rx
import STC.styles.styles as st
from STC.views.sections import section_1, section_2, grid
from STC.views.grid import great_grid


def sector() -> rx.Component:
    return rx.vstack(
        section_2("STC",
                  """STC es la defensa personal que se moldea a tu medida. 
                  Nuestro sistema se adapta a ti, no al revés, lo que lo hace fácil y rápido de aprender para cualquiera.
                  Con principios comprensibles desde la primera clase, descubrirás cómo proteger tu vida de la mejor manera. 
                  ¡Reserva tu clase gratis ahora y toma el control de tu seguridad!""",
                  "/legionariovencedor.jpeg"),      
    )