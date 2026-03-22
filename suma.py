import tkinter as tk
from tkinter import messagebox

def calcular_suma_y_secuencia(n):
    """Calcula la suma de los primeros n números y genera la secuencia."""
    suma_total = 0
    secuencia_str = ""
    
    # Estructura de control (Ciclo)
    for i in range(1, n + 1):
        suma_total += i
        if i == n:
            secuencia_str += str(i)
        else:
            secuencia_str += f"{i} + "
            
    return suma_total, secuencia_str

def abrir_ejercicio_7(root):
    ventana = tk.Toplevel(root)
    ventana.title("7. Suma de números enteros")
    ventana.geometry("400x350")
    
    def procesar():
        valor_str = entry_n.get().strip()
        
        # Validación: debe ser un número entero, positivo y máximo 1000
        try:
            n = int(valor_str)
            if n <= 0 or n > 1000:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número entero positivo entre 1 y 1000.", parent=ventana)
            entry_n.delete(0, tk.END)
            return
            
        # Llamada a la función
        suma, secuencia = calcular_suma_y_secuencia(n)
        
        # Mostrar resultados en el cuadro de texto
        text_resultado.config(state=tk.NORMAL)
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, f"Secuencia sumada:\n{secuencia}\n\n")
        text_resultado.insert(tk.END, f"Resultado final: {suma}")
        text_resultado.config(state=tk.DISABLED)
        
        entry_n.delete(0, tk.END)

    # --- Elementos de la interfaz ---
    tk.Label(ventana, text="Ingrese un número entero positivo (máximo 1000):").pack(pady=(15, 5))
    
    entry_n = tk.Entry(ventana, width=20)
    entry_n.pack(pady=5)
    
    tk.Button(ventana, text="Calcular Suma", command=procesar, bg="lightgreen").pack(pady=10)
    
    tk.Label(ventana, text="Resultados:", font=("Arial", 10, "bold")).pack(pady=5)
    
    text_resultado = tk.Text(ventana, width=45, height=8, state=tk.DISABLED)
    text_resultado.pack(pady=5)