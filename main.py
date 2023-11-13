from flet import *
import flet

bgcolor = '#100b36'

class Card(UserControl):
    def build(self):
        return Container(
            Column([
                Container(
                    Image(src='assets/visa.png'),
                    width=70,
                    margin=margin.only(270),
                    opacity=0.8,
                ),
                Container(
                    Image(src='assets/chip.png'),
                    width=50,
                    margin=margin.only(20),
                    opacity=0.5,
                ),
                Container(
                    Column([
                        Text(
                        "XXXX XXXX XXXX XXXX",
                        color='white',
                        size=20,
                        weight='w500'
                        ),
                        Container(
                            Text(
                                "XX/XX",
                                color='white',
                                size=18,
                                text_align='right'
                            ),
                            alignment=alignment.center
                        ),
                    ],spacing=0),
                        opacity=0.8,
                        margin=margin.only(20)
                ),
                Container(
                    Text(
                        "LUIS URDANETA",
                        color='white',
                        size=20,
                        weight='w500',
                    ),
                    opacity=0.7,
                    margin=margin.only(20)
                )
            ],spacing=0),
            width=376,
            height=232,
            top=100,
            left=100,
            bgcolor='#20f4f4f4',
            border_radius=12,
            blur=Blur(10,10,BlurTileMode.REPEATED),
            shadow=BoxShadow(
                1,
                15,
                colors.BLUE_GREY_300,
                Offset(2,2),
                ShadowBlurStyle.OUTER
            )
        )

class BackCircle(UserControl):
    def __init__(self,top,left,size):
        super().__init__()
        self.top = top
        self.left = left
        self.size = size
        self.bg = LinearGradient(
            colors=['#2fb8c5','#284584'],
            begin=alignment.bottom_left,
            end=alignment.top_right,
        )

    def build(self):
        return Container(
            width=self.size,
            height=self.size,
            gradient=self.bg,
            border_radius=260,
            top=self.top,
            left=self.left,
        )


body = Container(
    Stack([
        BackCircle(90,180,170),
        BackCircle(20,20,180),
        BackCircle(130,20,100),
        Card(),
    ]),
    width=576,
    height=432,
    bgcolor=bgcolor,
)

def manage(page:Page):
    page.window_min_width = 576
    page.window_min_height = 432
    page.window_max_width = 576
    page.window_max_height = 432
    page.window_width = 576
    page.window_height = 432

    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.padding = 0
    page.title = 'Card Design'
    page.add(
        body
    )

flet.app(manage)