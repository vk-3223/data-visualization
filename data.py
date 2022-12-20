import justpy as jp


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp,text="Analysis of Course reviwes",classes="text-h4 text-center q-pa-md")
    p1=jp.QDiv(a=wp,text="This course analysis")

    return wp

jp.justpy(app)    