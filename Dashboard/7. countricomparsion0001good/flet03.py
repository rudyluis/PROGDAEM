import flet as ft

def factorial(n: int) -> int:
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def main(page: ft.Page):
    page.title = "Calculadora Matemática Avanzada"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20
    
    # Entrada de número
    txt_num = ft.TextField(label="Número entero", width=150, autofocus=True)
    
    # Opciones de operación
    dropdown_operacion = ft.Dropdown(
        label="Operación",
        width=150,
        options=[
            ft.dropdown.Option("Factorial"),
            ft.dropdown.Option("Doble"),
            ft.dropdown.Option("Cuadrado"),
            ft.dropdown.Option("Cubicar"),
        ],
        value="Factorial"
    )
    
    # Checkbox para mostrar historial
    chk_historial = ft.Checkbox(label="Mostrar historial")
    
    # Texto para resultados y errores
    resultado_txt = ft.Text(size=16, weight="bold", color=ft.Colors.BLUE)
    error_txt = ft.Text(color=ft.Colors.RED)
    
    # Lista para historial
    historial = ft.Column()
    
    def calcular(e):
        error_txt.value = ""
        resultado_txt.value = ""
        try:
            n = int(txt_num.value)
            if n < 0:
                error_txt.value = "Por favor, ingresa un número entero positivo"
                page.update()
                return
            op = dropdown_operacion.value
            if op == "Factorial":
                res = factorial(n)
            elif op == "Doble":
                res = n * 2
            elif op == "Cuadrado":
                res = n ** 2
            elif op == "Cubicar":
                res = n ** 3
            else:
                res = "Operación no reconocida"
            
            resultado_txt.value = f"Resultado: {res}"
            
            if chk_historial.value:
                historial.controls.append(ft.Text(f"{op} de {n} = {res}"))
                page.update()
            
        except ValueError:
            error_txt.value = "Entrada inválida. Debe ser un número entero."
        
        page.update()
    
    btn_calcular = ft.ElevatedButton(text="Calcular", on_click=calcular)
    
    # Layout organizado
    controls_row = ft.Row([txt_num, dropdown_operacion, btn_calcular], spacing=20)
    
    page.add(
        ft.Text("Calculadora Matemática", size=24, weight="bold"),
        controls_row,
        chk_historial,
        resultado_txt,
        error_txt,
        ft.Divider(),
        ft.Text("Historial:", weight="bold"),
        historial
    )

ft.app(target=main)
