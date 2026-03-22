import tkinter as tk
from tkinter import messagebox

def abrir_ejercicio_8(root):
    ventana = tk.Toplevel(root)
    ventana.title("8. Sistema de suma acumulativa")
    ventana.geometry("400x500")
    
    # Estructura para guardar el estado: lista de números y la suma
    estado = {
        "numeros": [],
        "suma_total": 0
    }
    
    def agregar_numero():
        valor_str = entry_numero.get().strip()
        
        # Validación de datos
        try:
            numero = float(valor_str) # Usamos float por si ingresan decimales
            # Si quieres que sean estrictamente enteros, cambia float por int
            if numero.is_integer():
                numero = int(numero)
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número válido.", parent=ventana)
            entry_numero.delete(0, tk.END)
            return
            
        # Condición de paro: si ingresa 0
        if numero == 0:
            finalizar_proceso()
        else:
            # Guardar en la lista y sumar
            estado["numeros"].append(numero)
            estado["suma_total"] += numero
            
            # Actualizar la suma acumulada en pantalla
            lbl_acumulado.config(text=f"Suma acumulada actual: {estado['suma_total']}")
            
            # Limpiar el campo y devolver el foco para ingresar el siguiente rápido
            entry_numero.delete(0, tk.END)
            entry_numero.focus()

    def finalizar_proceso():
        """Se ejecuta al ingresar 0. Muestra los resultados finales y bloquea el ingreso."""
        entry_numero.config(state=tk.DISABLED)
        btn_agregar.config(state=tk.DISABLED)
        
        text_resultados.config(state=tk.NORMAL)
        text_resultados.delete(1.0, tk.END)
        
        cantidad = len(estado["numeros"])
        lista_formateada = ", ".join(map(str, estado["numeros"]))
        
        texto_final = (
            "--- PROCESO FINALIZADO (Se ingresó 0) ---\n\n"
            f"Lista de números ingresados:\n[{lista_formateada}]\n\n"
            f"Cantidad de números: {cantidad}\n"
            f"Suma total: {estado['suma_total']}"
        )
        
        text_resultados.insert(tk.END, texto_final)
        text_resultados.config(state=tk.DISABLED)
        
        lbl_acumulado.config(text="Suma acumulada actual: FINALIZADO", fg="blue")

    def reiniciar():
        """Permite limpiar todo y volver a empezar."""
        estado["numeros"].clear()
        estado["suma_total"] = 0
        
        entry_numero.config(state=tk.NORMAL)
        btn_agregar.config(state=tk.NORMAL)
        entry_numero.delete(0, tk.END)
        
        lbl_acumulado.config(text="Suma acumulada actual: 0", fg="black")
        
        text_resultados.config(state=tk.NORMAL)
        text_resultados.delete(1.0, tk.END)
        text_resultados.config(state=tk.DISABLED)

    # --- Elementos de la interfaz ---
    tk.Label(ventana, text="Ingrese un número (Ingrese 0 para detener):").pack(pady=(15, 5))
    
    entry_numero = tk.Entry(ventana, width=20)
    entry_numero.pack(pady=5)
    
    # Vinculamos la tecla "Enter" para que funcione igual que presionar el botón
    ventana.bind('<Return>', lambda event: agregar_numero() if entry_numero["state"] == tk.NORMAL else None)
    
    btn_agregar = tk.Button(ventana, text="Agregar Número", command=agregar_numero, bg="lightblue")
    btn_agregar.pack(pady=5)
    
    lbl_acumulado = tk.Label(ventana, text="Suma acumulada actual: 0", font=("Arial", 10, "italic"))
    lbl_acumulado.pack(pady=10)
    
    text_resultados = tk.Text(ventana, width=45, height=10, state=tk.DISABLED)
    text_resultados.pack(pady=10)

    tk.Button(ventana, text="Reiniciar Sistema", command=reiniciar).pack(pady=5)