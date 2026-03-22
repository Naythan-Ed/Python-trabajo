import tkinter as tk
from tkinter import messagebox

# Listas y variables globales
lista_visitantes = []
recaudacion_total = 0.0

def procesar_pago(nombre, edad, juegos):
    """Calcula el total a pagar, aplica descuentos y guarda el registro."""
    global recaudacion_total
    costo_base = juegos * 50
    
    # Estructura de control para los descuentos
    if edad < 10:
        descuento = 0.25
    elif 10 <= edad <= 17:
        descuento = 0.10
    else:
        descuento = 0.0
        
    monto_descuento = costo_base * descuento
    total_pagar = costo_base - monto_descuento
    
    # Guardar en la lista
    lista_visitantes.append({
        "nombre": nombre,
        "edad": edad,
        "juegos": juegos,
        "total_pagar": total_pagar
    })
    
    recaudacion_total += total_pagar
    return total_pagar

def abrir_ejercicio_2(root):
    """Abre la ventana para el Sistema de pago del parque de diversiones."""
    ventana = tk.Toplevel(root)
    ventana.title("2. Sistema de pago en parque de diversiones")
    ventana.geometry("450x550")
    
    def registrar():
        nombre = entry_nombre.get().strip()
        edad_str = entry_edad.get().strip()
        juegos_str = entry_juegos.get().strip()
        
        # Validación de datos
        if not nombre:
            messagebox.showerror("Error", "Ingrese un nombre válido.", parent=ventana)
            return
            
        try:
            edad = int(edad_str)
            juegos = int(juegos_str)
            if edad < 0 or juegos < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "La edad y los juegos deben ser números enteros positivos.", parent=ventana)
            return
            
        # Llamada a la función
        total = procesar_pago(nombre, edad, juegos)
        
        # Mostrar resultados
        lbl_resultado.config(text=f"Total a pagar para {nombre}: {total:.2f} soles")
        lbl_recaudacion.config(text=f"Recaudación Total del Parque: {recaudacion_total:.2f} soles")
        
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_juegos.delete(0, tk.END)

    def mostrar_historial():
        text_historial.delete(1.0, tk.END)
        if not lista_visitantes:
            text_historial.insert(tk.END, "No hay visitantes registrados.")
            return
            
        # Estructura de control (Ciclo)
        for v in lista_visitantes:
            registro = f"Nombre: {v['nombre']} | Edad: {v['edad']}\nJuegos: {v['juegos']} | Pagó: {v['total_pagar']:.2f} soles\n{'-'*30}\n"
            text_historial.insert(tk.END, registro)

    tk.Label(ventana, text="Nombre del visitante:").pack(pady=(10, 0))
    entry_nombre = tk.Entry(ventana, width=30)
    entry_nombre.pack(pady=5)

    tk.Label(ventana, text="Edad:").pack()
    entry_edad = tk.Entry(ventana, width=30)
    entry_edad.pack(pady=5)

    tk.Label(ventana, text="Cantidad de juegos:").pack()
    entry_juegos = tk.Entry(ventana, width=30)
    entry_juegos.pack(pady=5)

    tk.Button(ventana, text="Calcular y Registrar", command=registrar, bg="lightgreen").pack(pady=10)
    
    lbl_resultado = tk.Label(ventana, text="Total a pagar: ", font=("Arial", 10, "bold"), fg="darkblue")
    lbl_resultado.pack(pady=5)
    
    lbl_recaudacion = tk.Label(ventana, text=f"Recaudación Total del Parque: {recaudacion_total:.2f} soles", font=("Arial", 10, "bold"), fg="darkred")
    lbl_recaudacion.pack(pady=5)

    tk.Button(ventana, text="Ver Historial de Visitantes", command=mostrar_historial).pack(pady=5)

    text_historial = tk.Text(ventana, width=50, height=10)
    text_historial.pack(pady=10)