import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size

def form() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="/shield.png"
        ),
        rx.spacer(),
        rx.vstack(
            rx.form(
                rx.vstack(
                    rx.heading(
                        "Formulario de Inscripción"
                    ),
                    rx.input(
                        placeholder="First Name",
                        id="first_name",color=st.blanco
                    ),
                    rx.input(
                        placeholder="Pais", id="pais",color=st.blanco
                    ),
                    rx.input(
                        placeholder="email", id="email",color=st.blanco
                    ),
                    rx.hstack(
                        rx.checkbox("Deseo recibir correos electronicos de STC", id="check", color=st.blanco),
                    ),
                    rx.button("Submit", type_="submit"),
                ),
                reset_on_submit	= True,
            ),
        ),
    )