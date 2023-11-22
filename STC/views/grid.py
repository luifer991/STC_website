import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size

def great_grid() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Descubre el Poder de STC",
            padding_y = Size.small.value,
            font_size = Size.xl.value
        ),
        rx.grid(
    rx.grid_item(
        rx.image(
            src="/defensa.jpeg",
            width = "100%",
            height = "100%"
        ),
        col_span=2,
    ),
    rx.grid_item(
        rx.vstack(
            rx.heading("Prevención"),
            rx.text( """En el corazón de STC yace un principio irrefutable: 
                    la prevención. Nuestro sistema se basa en la premisa de evitar problemas en lugar de buscarlos, 
                    convirtiendo la seguridad en una certeza, no una incertidumbre.
                     Descubre un mundo donde la protección es proactiva y la confianza es inquebrantable.""" ,
                    style = st.text_secondary
                    ),
        ),
        col_span=2, #bg=st.gris
        ),
    rx.grid_item(
        rx.image(
            src="/entrenar.jpeg",
            width = "100%",
            height = "100%"
        ),
        col_span=2,
    ),
    rx.grid_item(
        rx.vstack(
            rx.heading("Disuación"),
            rx.text("""En el núcleo de STC, la disuasión se convierte en nuestro aliado principal. 
                    Evitamos enfrentamientos innecesarios y reducimos el riesgo de causar daños mayores. 
                    Descubre cómo la persuasión y la seguridad se unen para mantener el control en tus manos""",
                    style = st.text_secondary
                    ),
        ),
        col_span=2, #bg=st.gris
        ),
    rx.grid_item(
        rx.image(
            src="/patadaenlacara.jpeg",
            width = "100%",
            height = "100%"
        ),
        col_span=2,
    ),
    rx.grid_item(
        rx.vstack(
            rx.heading("Acción"),
            rx.text("""En el mundo de STC, la acción es el último recurso, pero no por eso menos vital. 
                    Aquí aprendes a defender tu vida cuando no hay alternativa, 
                    neutralizando amenazas con la fuerza necesaria. 
                    Descubre un sistema donde la preparación es tu mayor aliado 
                    y la seguridad es una garantía.""",
                    style = st.text_secondary
                    ),

        ),
        col_span=2, #bg=st.gris
        ),
    template_rows="repeat(2, 1fr)",
    template_columns="repeat(6, 1fr)",
    h="100vh",
    width="100%",
    gap=2,
    max_width = "1024px"
),
)