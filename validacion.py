import tkinter as tk
from tkinter import messagebox

def abrir_ejercicio_4(root):
    # Como siempre vendrá del main, usamos Toplevel directamente
    ventana = tk.Toplevel(root)
    ventana.title("4. Validación menor que 10")
    ventana.geometry("350x250")
    
    estado = {"intentos": 0}
    
    def verificar():
        valor_str = entry_numero.get().strip()
        
        try:
            numero = int(valor_str)
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número entero válido.", parent=ventana)
            entry_numero.delete(0, tk.END)
            return
            
        estado["intentos"] += 1
        
        if numero < 10:
            lbl_resultado.config(text=f"¡Correcto!\nNúmero ingresado: {numero}\nIntentos realizados: {estado['intentos']}", fg="green")
            entry_numero.config(state=tk.DISABLED)
            btn_verificar.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Número incorrecto. Debe ser menor que 10.", parent=ventana)
            lbl_resultado.config(text=f"Intentos realizados: {estado['intentos']}", fg="red")
            entry_numero.delete(0, tk.END)

    tk.Label(ventana, text="Ingrese un número entero menor que 10:").pack(pady=(20, 5))
    
    entry_numero = tk.Entry(ventana, width=20)
    entry_numero.pack(pady=5)
    
    btn_verificar = tk.Button(ventana, text="Verificar", command=verificar, bg="lightyellow")
    btn_verificar.pack(pady=10)
    
    lbl_resultado = tk.Label(ventana, text="", font=("Arial", 11, "bold"))
    lbl_resultado.pack(pady=15)