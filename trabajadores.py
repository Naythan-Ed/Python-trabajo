import tkinter as tk
from tkinter import messagebox

# Lista para almacenar los registros de varios trabajadores
registro_pagos = []

def calcular_pago(nombre, horas_normales, pago_hora, horas_extras, hijos):
    """Calcula los diferentes conceptos de pago y el total."""
    pago_normales = horas_normales * pago_hora
    pago_extras = horas_extras * (pago_hora * 1.5)
    bono_hijos = hijos * 0.5
    
    pago_total = pago_normales + pago_extras + bono_hijos
    
    # Guardar en la lista
    registro_pagos.append({
        "nombre": nombre,
        "pago_normales": pago_normales,
        "pago_extras": pago_extras,
        "bono_hijos": bono_hijos,
        "pago_total": pago_total
    })
    
    return pago_normales, pago_extras, bono_hijos, pago_total

def abrir_ejercicio_10(root):
    ventana = tk.Toplevel(root)
    ventana.title("10. Sistema de pago de trabajadores")
    ventana.geometry("450x650")
    
    def registrar():
        nombre = entry_nombre.get().strip()
        
        if not nombre:
            messagebox.showerror("Error", "El nombre no puede estar vacío.", parent=ventana)
            return
            
        try:
            h_normales = float(entry_h_normales.get())
            pago_h = float(entry_pago_h.get())
            h_extras = float(entry_h_extras.get())
            hijos = int(entry_hijos.get())
            
            if h_normales < 0 or pago_h < 0 or h_extras < 0 or hijos < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos y positivos.", parent=ventana)
            return
            
        # Calcular
        p_norm, p_ext, bono, total = calcular_pago(nombre, h_normales, pago_h, h_extras, hijos)
        
        # Mostrar resultado individual
        resultado_txt = (
            f"Resultados para {nombre}:\n"
            f"Pago Normal: ${p_norm:.2f}\n"
            f"Pago Extras: ${p_ext:.2f}\n"
            f"Bono Hijos: ${bono:.2f}\n"
            f"TOTAL A PAGAR: ${total:.2f}"
        )
        lbl_resultado.config(text=resultado_txt, fg="darkgreen")
        
        # Limpiar campos
        entry_nombre.delete(0, tk.END)
        entry_h_normales.delete(0, tk.END)
        entry_pago_h.delete(0, tk.END)
        entry_h_extras.delete(0, tk.END)
        entry_hijos.delete(0, tk.END)
        entry_nombre.focus()

    def mostrar_reporte():
        text_reporte.delete(1.0, tk.END)
        
        if not registro_pagos:
            text_reporte.insert(tk.END, "No hay pagos registrados.")
            return
            
        text_reporte.insert(tk.END, "--- REPORTE DE PAGOS REALIZADOS ---\n\n")
        
        for t in registro_pagos:
            registro = (
                f"Trabajador: {t['nombre']}\n"
                f"Normales: ${t['pago_normales']:.2f} | Extras: ${t['pago_extras']:.2f}\n"
                f"Bono por Hijos: ${t['bono_hijos']:.2f}\n"
                f"Total Pagado: ${t['pago_total']:.2f}\n"
                f"{'-'*35}\n"
            )
            text_reporte.insert(tk.END, registro)

    # --- Elementos de la interfaz ---
    tk.Label(ventana, text="Nombre del trabajador:").pack(pady=(10, 2))
    entry_nombre = tk.Entry(ventana, width=30)
    entry_nombre.pack()

    tk.Label(ventana, text="Horas normales trabajadas:").pack(pady=(5, 2))
    entry_h_normales = tk.Entry(ventana, width=30)
    entry_h_normales.pack()

    tk.Label(ventana, text="Pago por hora normal ($):").pack(pady=(5, 2))
    entry_pago_h = tk.Entry(ventana, width=30)
    entry_pago_h.pack()

    tk.Label(ventana, text="Horas extras trabajadas:").pack(pady=(5, 2))
    entry_h_extras = tk.Entry(ventana, width=30)
    entry_h_extras.pack()

    tk.Label(ventana, text="Número de hijos:").pack(pady=(5, 2))
    entry_hijos = tk.Entry(ventana, width=30)
    entry_hijos.pack()

    tk.Button(ventana, text="Calcular y Registrar", command=registrar, bg="lightgreen").pack(pady=10)
    
    lbl_resultado = tk.Label(ventana, text="", font=("Arial", 10, "bold"))
    lbl_resultado.pack(pady=5)
    
    tk.Button(ventana, text="Ver Reporte de Pagos", command=mostrar_reporte).pack(pady=5)
    
    text_reporte = tk.Text(ventana, width=45, height=10)
    text_reporte.pack(pady=10)