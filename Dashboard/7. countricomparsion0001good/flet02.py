import flet as ft

def factorial(n: int) -> int:
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def main(page: ft.Page):
    page.title = "Calculadora de Factorial"
    
    txt_num = ft.TextField(label="Ingresa un número entero", width=200)
    resultado_txt = ft.Text()
    
    def calcular_factorial(e):
        try:
            n = int(txt_num.value)
            if n < 0:
                resultado_txt.value = "Por favor, ingresa un número entero positivo"
            else:
                resultado_txt.value = f"Factorial de {n} = {factorial(n)}"
        except ValueError:
            resultado_txt.value = "Entrada no válida. Debe ser un número entero."
        page.update()
    
    btn_calcular = ft.ElevatedButton(text="Calcular", on_click=calcular_factorial)
    
    page.add(txt_num, btn_calcular, resultado_txt)

ft.app(target=main)
