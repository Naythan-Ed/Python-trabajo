import tkinter as tk
from tkinter import messagebox

# ==========================================
# ESTRUCTURAS DE DATOS Y LÓGICA
# ==========================================
compras_dia = []
total_vendido_dia = 0.0

# Lista para validación
MESES_VALIDOS = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio", 
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

def validar_mes(mes):
    """Valida que el mes ingresado exista."""
    return mes.strip().lower() in MESES_VALIDOS

def calcular_descuento(mes, importe):
    """Calcula el descuento según el mes promocional."""
    mes_str = mes.strip().lower()
    
    # Estructura de control para los descuentos
    if mes_str == "octubre":
        return importe * 0.15
    elif mes_str == "diciembre":
        return importe * 0.20
    elif mes_str == "julio":
        return importe * 0.10
    else:
        return 0.0

def procesar_compra(nombre, mes, importe):
    """Aplica el descuento, calcula el total y guarda el registro."""
    global total_vendido_dia
    
    descuento = calcular_descuento(mes, importe)
    total_final = importe - descuento
    
    # Guardar en la lista
    compras_dia.append({
        "nombre": nombre,
        "mes": mes.capitalize(),
        "importe_base": importe,
        "descuento": descuento,
        "total_final": total_final
    })
    
    total_vendido_dia += total_final
    return total_final, descuento

# ==========================================
# INTERFAZ GRÁFICA (GUI)
# ==========================================

def abrir_ejercicio_3(root):
    """Abre la ventana para el Sistema de descuentos por mes en tienda."""
    ventana = tk.Toplevel(root)
    ventana.title("3. Sistema de descuentos por mes")
    ventana.geometry("450x550")
    
    def registrar():
        nombre = entry_nombre.get().strip()
        mes = entry_mes.get().strip()
        importe_str = entry_importe.get().strip()
        
        # Validación de datos (Nombres y Mes)
        if not nombre:
            messagebox.showerror("Error", "Ingrese el nombre del cliente.", parent=ventana)
            return
            
        if not validar_mes(mes):
            messagebox.showerror("Error", "Ingrese un mes válido (ej. Enero, Octubre).", parent=ventana)
            return
            
        # Validación de datos (Importe numérico)
        try:
            importe = float(importe_str)
            if importe <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El importe debe ser un número positivo.", parent=ventana)
            return
            
        # Llamada a las funciones
        total, descuento = procesar_compra(nombre, mes, importe)
        
        # Mostrar resultados
        lbl_resultado.config(text=f"Total para {nombre}: ${total:.2f}\n(Descuento aplicado: ${descuento:.2f})")
        lbl_total_dia.config(text=f"Total Vendido en el Día: ${total_vendido_dia:.2f}")
        
        # Limpiar entradas
        entry_nombre.delete(0, tk.END)
        entry_mes.delete(0, tk.END)
        entry_importe.delete(0, tk.END)

    def mostrar_historial():
        text_historial.delete(1.0, tk.END)
        if not compras_dia:
            text_historial.insert(tk.END, "No hay compras registradas hoy.")
            return
            
        text_historial.insert(tk.END, "--- COMPRAS DEL DÍA ---\n\n")
        # Ciclo para recorrer la lista
        for c in compras_dia:
            registro = f"Cliente: {c['nombre']} | Mes: {c['mes']}\nImporte: ${c['importe_base']:.2f} | Dto: ${c['descuento']:.2f}\nPagó: ${c['total_final']:.2f}\n{'-'*30}\n"
            text_historial.insert(tk.END, registro)

    tk.Label(ventana, text="Nombre del cliente:").pack(pady=(10, 0))
    entry_nombre = tk.Entry(ventana, width=30)
    entry_nombre.pack(pady=5)

    tk.Label(ventana, text="Mes de la compra (ej. Julio):").pack()
    entry_mes = tk.Entry(ventana, width=30)
    entry_mes.pack(pady=5)

    tk.Label(ventana, text="Importe de la compra ($):").pack()
    entry_importe = tk.Entry(ventana, width=30)
    entry_importe.pack(pady=5)

    tk.Button(ventana, text="Calcular y Registrar Compra", command=registrar, bg="lightcoral").pack(pady=10)
    
    lbl_resultado = tk.Label(ventana, text="Total a pagar: ", font=("Arial", 10, "bold"), fg="purple")
    lbl_resultado.pack(pady=5)
    
    lbl_total_dia = tk.Label(ventana, text=f"Total Vendido en el Día: ${total_vendido_dia:.2f}", font=("Arial", 11, "bold"), fg="darkgreen")
    lbl_total_dia.pack(pady=10)

    tk.Button(ventana, text="Consultar Compras del Día", command=mostrar_historial).pack(pady=5)

    text_historial = tk.Text(ventana, width=50, height=10)
    text_historial.pack(pady=10)