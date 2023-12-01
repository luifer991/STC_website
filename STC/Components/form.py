import os
import reflex as rx
import STC.styles.styles as st
from STC.styles.styles import Size as Size
import asyncio
import json
import httpx

from email_validator import EmailNotValidError, validate_email

class User(rx.Model, table=True):
    username: str
    usercountry: str
    email: str
    check: bool

class AddUserForm(rx.State):
    username: str
    usercountry: str
    email: str
    check: bool
    # Whether to show the call to action.
    show_c2a: bool = True

    # Whether the user signed up for the waitlist.
    signed_up: bool = False


    def close_c2a(self):
        """Close the call to action."""
        self.show_c2a = False
    
    def add_contact_to_loops(self, contact_data):
        url = "driver://user:pass@localhost/stc"
        loops_api_key = os.getenv("LOOPS_API_KEY")
        if loops_api_key is None:
            print("Loops API key does not exist")
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {loops_api_key}",
        }

        try:
            with httpx.Client() as client:
                response = client.post(url, headers=headers, json=contact_data)
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx)

        except httpx.RequestError as e:
            print(f"An error occurred: {e}")

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

    def add_user(self):
        with rx.session() as session:
            session.add(
                 User(
                    username=self.username, 
                    usercountry=self.usercountry, 
                    email=self.email, 
                    check=self.check
                )
            )
            session.commit()

    def signup(self):
        """Sign the user up for the waitlist."""
        # Check if the email is valid.
        try:
            validation = validate_email(self.email, check_deliverability=True)
            self.email = validation.email
        except EmailNotValidError as e:
            # Alert the error message.
            return rx.window_alert(str(e))
         # Check if the user is already on the user.
        with rx.session() as session:
            user = session.query(User).filter(User.email == self.email).first()
            if user is None:
                # Add the user to the user.
                session.add(
                    User(
                    username=self.username,
                    usercountry=self.usercountry,
                    email=self.email,
                    check=self.check
                    )
                )
                session.commit()
                contact_data = json.dumps({"username": self.username,
                                           "usercountry": self.usercountry,
                                           "email": self.email,
                                           "check": self.check,})
                self.add_contact_to_loops(contact_data)

        self.signed_up = True


def form() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Contactanos",
            font_size=st.Size.extra.value,
            margin_top= st.Size.default.value
        ),
        rx.hstack(
        rx.image(
            src="/legionatriopeleando.jpeg",
            alt="Legionario en combate",
            margin_y = Size.xl.value,
            width = "60%",
            height = "60%",

        ),
        rx.spacer(),
        rx.spacer(),
        rx.vstack(
            rx.form(
                rx.vstack(
                    rx.heading(
                        "Formulario de Inscripción"
                    ),
                    rx.input(
                        placeholder="Primer Nombre",
                        id="username",color=st.blanco, type_="name"
                    ),
                    rx.input(
                        placeholder="País", id="country",color=st.blanco
                    ),
                    rx.input(
                        placeholder="Correo Electrónico", id="email",color=st.blanco,
                        on_blur=AddUserForm.set_email,
                                    type="email",
                    ),
                    rx.hstack(
                        rx.checkbox("Deseo recibir correos electronicos de STC", id="check", color=st.blanco),
                    ),
                    rx.button("Submit", type_="submit",
                              on_click=AddUserForm.signup,),
                ),
                on_submit = AddUserForm.handle_submit,
            ),
        ),
        margin_top = Size.big.value,
    ),
)