from flet import Container, padding, Page, Column, Row, Text, MainAxisAlignment
from modules.color import DEEP_BLUE
from modules.fonctions import pourcentage

class Display(Container):
    def __init__(self, page: Page):
        super().__init__(
            bgcolor='white',
            border_radius=10,
            expand=True,
            height=page.window.height - 70,
            padding=padding.only(pourcentage(page.window.width, 10), 15, pourcentage(page.window.width, 10)),
        )
        self.content = Column([Row([Text("Fichiers", text_align='center', expand=True, color=DEEP_BLUE, weight='bold', size=50)])], alignment=MainAxisAlignment.CENTER)