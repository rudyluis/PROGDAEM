import flet as ft
import plotly.express as px
import pandas as pd
import tempfile
import os

def main(page: ft.Page):
    df = pd.DataFrame({
        "Frutas": ["Manzanas", "Naranjas", "Plátanos", "Fresas"],
        "Cantidad": [10, 15, 7, 12]
    })

    fig = px.bar(df, x="Frutas", y="Cantidad", title="Cantidad de frutas")

    # Guardar gráfico a archivo HTML temporal
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, "grafico.html")
    fig.write_html(file_path)

    # Mostrar gráfico en Flet usando WebView
    webview = ft.WebView(src=file_path, width=700, height=500)
    page.add(webview)

ft.app(target=main)
