import tkinter as tk

try:
    import sueldo
    import pago
    import tienda
    import validacion
    import rango
    import suma
    import acumulativa
    import limite
    import trabajadores # Importamos el nuevo módulo
except ImportError as e:
    print(f"Advertencia: Faltan archivos por crear en la carpeta. Error: {e}")

root = tk.Tk()
root.title("Menú Principal de Ejercicios")
root.geometry("380x680") # Aumentamos altura para que quepan todos los botones

tk.Label(root, text="Seleccione un ejercicio:", font=("Arial", 12, "bold")).pack(pady=15)

btn_ejercicio1 = tk.Button(root, text="1. Sistema de Aumento de Sueldos", command=lambda: sueldo.abrir_ejercicio_1(root), width=40, height=2)
btn_ejercicio1.pack(pady=5)

btn_ejercicio2 = tk.Button(root, text="2. Sistema de Pago en Parque", command=lambda: pago.abrir_ejercicio_2(root), width=40, height=2)
btn_ejercicio2.pack(pady=5)

btn_ejercicio3 = tk.Button(root, text="3. Sistema de Descuentos en Tienda", command=lambda: tienda.abrir_ejercicio_3(root), width=40, height=2)
btn_ejercicio3.pack(pady=5)

btn_ejercicio4 = tk.Button(root, text="4. Validación menor que 10", command=lambda: validacion.abrir_ejercicio_4(root), width=40, height=2)
btn_ejercicio4.pack(pady=5)

btn_ejercicio5 = tk.Button(root, text="5-6. Validación en rango e Historial", command=lambda: rango.abrir_ejercicio_5(root), width=40, height=2)
btn_ejercicio5.pack(pady=5)

btn_ejercicio7 = tk.Button(root, text="7. Suma de números enteros", command=lambda: suma.abrir_ejercicio_7(root), width=40, height=2)
btn_ejercicio7.pack(pady=5)

btn_ejercicio8 = tk.Button(root, text="8. Sistema de suma acumulativa", command=lambda: acumulativa.abrir_ejercicio_8(root), width=40, height=2)
btn_ejercicio8.pack(pady=5)

btn_ejercicio9 = tk.Button(root, text="9. Suma hasta superar límite (100)", command=lambda: limite.abrir_ejercicio_9(root), width=40, height=2)
btn_ejercicio9.pack(pady=5)


btn_ejercicio10 = tk.Button(root, text="10. Sistema de pago de trabajadores", command=lambda: trabajadores.abrir_ejercicio_10(root), width=40, height=2)
btn_ejercicio10.pack(pady=5)

tk.Button(root, text="Salir", command=root.quit, fg="red").pack(pady=15)

root.mainloop()