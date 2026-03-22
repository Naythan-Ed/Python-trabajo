import tkinter as tk
from tkinter import messagebox

# Función reutilizable para validar rangos
def validar_en_rango(numero, min_val, max_val):
    return min_val < numero < max_val

def abrir_ejercicio_5(root):
    # Usamos Toplevel para que se abra como ventana secundaria del menú principal
    ventana = tk.Toplevel(root)
    ventana.title("5. Validación en rango (0, 20) e Historial")
    ventana.geometry("400x500")
    
    # Diccionario para almacenar el historial de números y el contador de errores
    estado = {
        "incorrectos": 0,
        "historial": []
    }
    
    def verificar():
        valor_str = entry_numero.get().strip()
        
        try:
            numero = int(valor_str)
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número entero válido.", parent=ventana)
            entry_numero.delete(0, tk.END)
            return
            
        # Guardar el número ingresado en la lista (Registro de intentos)
        estado["historial"].append(numero)
        
        # Uso de la función reutilizable para validar el rango
        if validar_en_rango(numero, 0, 20):
            lbl_resultado.config(text=f"¡Número correcto ingresado!: {numero}\nIntentos incorrectos totales: {estado['incorrectos']}", fg="green")
            entry_numero.config(state=tk.DISABLED)
            btn_verificar.config(state=tk.DISABLED)
        else:
            estado["incorrectos"] += 1
            messagebox.showerror("Error", f"El número {numero} está fuera del rango (0, 20).", parent=ventana)
            lbl_resultado.config(text=f"Intentos incorrectos: {estado['incorrectos']}", fg="red")
            entry_numero.delete(0, tk.END)

    def mostrar_historial():
        """Muestra la lista de todos los números ingresados."""
        text_historial.delete(1.0, tk.END)
        
        if not estado["historial"]:
            text_historial.insert(tk.END, "No hay intentos registrados.")
            return
            
        text_historial.insert(tk.END, "--- HISTORIAL DE NÚMEROS INGRESADOS ---\n\n")
        
        # Ciclo para recorrer la lista y mostrar los intentos
        for i, num in enumerate(estado["historial"], start=1):
            text_historial.insert(tk.END, f"Intento {i}: {num}\n")

    # --- Elementos de la interfaz ---
    tk.Label(ventana, text="Ingrese un número entero entre 0 y 20:").pack(pady=(15, 5))
    
    entry_numero = tk.Entry(ventana, width=20)
    entry_numero.pack(pady=5)
    
    btn_verificar = tk.Button(ventana, text="Verificar", command=verificar, bg="lightblue")
    btn_verificar.pack(pady=10)
    
    lbl_resultado = tk.Label(ventana, text="", font=("Arial", 11, "bold"))
    lbl_resultado.pack(pady=5)
    
    tk.Button(ventana, text="Ver Historial de Intentos", command=mostrar_historial).pack(pady=10)
    
    text_historial = tk.Text(ventana, width=40, height=10)
    text_historial.pack(pady=5)