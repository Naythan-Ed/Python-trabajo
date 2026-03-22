import tkinter as tk
from tkinter import messagebox

def abrir_ejercicio_9(root):
    ventana = tk.Toplevel(root)
    ventana.title("9. Suma hasta superar 100")
    ventana.geometry("400x450")
    
    estado = {
        "numeros": [],
        "suma_total": 0
    }
    
    def agregar_numero():
        valor_str = entry_numero.get().strip()
        
        try:
            numero = int(valor_str)
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número entero válido.", parent=ventana)
            entry_numero.delete(0, tk.END)
            return
            
        estado["numeros"].append(numero)
        estado["suma_total"] += numero
        
        lbl_parcial.config(text=f"Suma parcial: {estado['suma_total']}")
        entry_numero.delete(0, tk.END)
        
        if estado["suma_total"] > 100:
            finalizar_proceso()
        else:
            entry_numero.focus()

    def finalizar_proceso():
        entry_numero.config(state=tk.DISABLED)
        btn_agregar.config(state=tk.DISABLED)
        
        text_resultados.config(state=tk.NORMAL)
        text_resultados.delete(1.0, tk.END)
        
        cantidad = len(estado["numeros"])
        lista_formateada = ", ".join(map(str, estado["numeros"]))
        
        texto_final = (
            "--- LÍMITE SUPERADO (> 100) ---\n\n"
            f"Cantidad de números ingresados: {cantidad}\n\n"
            f"Lista de números:\n[{lista_formateada}]\n\n"
            f"Suma final: {estado['suma_total']}"
        )
        
        text_resultados.insert(tk.END, texto_final)
        text_resultados.config(state=tk.DISABLED)

    tk.Label(ventana, text="Ingrese un número entero:").pack(pady=(15, 5))
    
    entry_numero = tk.Entry(ventana, width=20)
    entry_numero.pack(pady=5)
    
    ventana.bind('<Return>', lambda event: agregar_numero() if entry_numero["state"] == tk.NORMAL else None)
    
    btn_agregar = tk.Button(ventana, text="Agregar Número", command=agregar_numero, bg="lightcoral")
    btn_agregar.pack(pady=5)
    
    lbl_parcial = tk.Label(ventana, text="Suma parcial: 0", font=("Arial", 10, "bold"), fg="blue")
    lbl_parcial.pack(pady=10)
    
    text_resultados = tk.Text(ventana, width=45, height=10, state=tk.DISABLED)
    text_resultados.pack(pady=10)