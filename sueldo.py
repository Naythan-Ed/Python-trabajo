import tkinter as tk
from tkinter import messagebox

# ==========================================
# ESTRUCTURAS DE DATOS Y LÓGICA 
# ==========================================
historial_trabajadores = []

def calcular_aumento(sueldo):
    """Calcula el porcentaje de aumento basado en las reglas de negocio."""
    if sueldo < 4000:
        return sueldo * 0.15
    elif 4000 <= sueldo <= 7000:
        return sueldo * 0.10
    else:
        return sueldo * 0.08

def procesar_datos_trabajador(nombre, sueldo):
    """Aplica la lógica y guarda los datos en la lista."""
    aumento = calcular_aumento(sueldo)
    nuevo_sueldo = sueldo + aumento
    
    # Guardar en la lista 
    historial_trabajadores.append({
        "nombre": nombre,
        "sueldo_base": sueldo,
        "aumento": aumento,
        "nuevo_sueldo": nuevo_sueldo
    })
    
    return nuevo_sueldo

# ==========================================
# INTERFAZ GRÁFICA (GUI)
# ==========================================

def abrir_ejercicio_1(root):
    """Abre la ventana para el Sistema de aumento de sueldos."""
    ventana_ej1 = tk.Toplevel(root)
    ventana_ej1.title("1. Sistema de aumento de sueldos")
    ventana_ej1.geometry("450x450")
    
    # --- Validaciones y Eventos ---
    def registrar():
        nombre = entry_nombre.get().strip()
        sueldo_str = entry_sueldo.get().strip()
        
        if not nombre:
            messagebox.showerror("Error de entrada", "El campo de nombre no puede estar vacío.", parent=ventana_ej1)
            return
            
        try:
            sueldo = float(sueldo_str)
            if sueldo < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error de entrada", "Por favor, ingrese un sueldo numérico válido y positivo.", parent=ventana_ej1)
            return
            
        nuevo_sueldo = procesar_datos_trabajador(nombre, sueldo)
        
        lbl_resultado.config(text=f"Resultado: {nombre} recibirá un nuevo sueldo de ${nuevo_sueldo:.2f}")
        
        entry_nombre.delete(0, tk.END)
        entry_sueldo.delete(0, tk.END)

    def mostrar_historial():
        text_historial.delete(1.0, tk.END) 
        
        if not historial_trabajadores:
            text_historial.insert(tk.END, "No hay registros en el historial.")
            return
            
        text_historial.insert(tk.END, "--- HISTORIAL DE TRABAJADORES ---\n\n")
        
        for t in historial_trabajadores:
            registro = f"Nombre: {t['nombre']}\nSueldo Anterior: ${t['sueldo_base']:.2f} | Aumento: ${t['aumento']:.2f}\nNuevo Sueldo: ${t['nuevo_sueldo']:.2f}\n{'-'*30}\n"
            text_historial.insert(tk.END, registro)

    # --- Elementos de la UI ---
    tk.Label(ventana_ej1, text="Nombre del trabajador:").pack(pady=(10, 0))
    entry_nombre = tk.Entry(ventana_ej1, width=30)
    entry_nombre.pack(pady=5)

    tk.Label(ventana_ej1, text="Sueldo básico ($):").pack()
    entry_sueldo = tk.Entry(ventana_ej1, width=30)
    entry_sueldo.pack(pady=5)

    tk.Button(ventana_ej1, text="Calcular y Registrar", command=registrar, bg="lightblue").pack(pady=10)
    
    lbl_resultado = tk.Label(ventana_ej1, text="Resultado: ", font=("Arial", 10, "bold"), fg="darkgreen")
    lbl_resultado.pack(pady=5)

    tk.Button(ventana_ej1, text="Ver Historial", command=mostrar_historial).pack(pady=5)

    text_historial = tk.Text(ventana_ej1, width=50, height=10)
    text_historial.pack(pady=10)