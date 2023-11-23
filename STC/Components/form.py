import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size

class User(rx.Model, table=True):
    username: str
    usercountry: str
    email: str

class AddUserForm(rx.State):
    username: User | None = None
    usercountry: User | None = None
    email: User | None = None

    def add_user(self, form_data: dict[str, str]):
        with rx.session() as session:
            session.add(self.username,
                        self.usercountry,
                        self.email)
            session.commit()
            session.refresh(self.username,
                            self.usercountry,
                            self.email)


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
                        placeholder="Primer Nombre",
                        id="first_name",color=st.blanco
                    ),
                    rx.input(
                        placeholder="País", id="country",color=st.blanco
                    ),
                    rx.input(
                        placeholder="Correo Electrónico", id="email",color=st.blanco
                    ),
                    rx.hstack(
                        rx.checkbox("Deseo recibir correos electronicos de STC", id="check", color=st.blanco),
                    ),
                    rx.button("Submit", type_="submit"),
                ),
                on_submit = AddUserForm.add_user,
            ),
        ),
    )