#gui
import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
from auditor import realizar_escaneo
from scanner import validar_ip

class AuditoriaGUI:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Sistema de Auditoría")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#000000")

        font_style = ("Courier New", 12, "bold")
        entry_bg_color = "#1E1E1E"
        entry_fg_color = "#00FF00"

        self.output_text = scrolledtext.ScrolledText(self.root, height=28, width=85, wrap=tk.WORD, font=font_style, bg=entry_bg_color, fg=entry_fg_color)
        self.output_text.pack(padx=10, pady=10)
        self.output_text.insert(tk.END, "¡Bienvenido al sistema de auditoría!\nEsperando instrucciones...\n\n")

        input_label = tk.Label(self.root, text="Ingrese la dirección IP a escanear:", bg="#000000", fg="#00FF00", font=font_style)
        input_label.pack(pady=(10, 0))

        input_entry = tk.Entry(self.root, width=50, font=font_style, bg=entry_bg_color, fg=entry_fg_color, insertbackground="#00FF00")
        input_entry.pack(pady=10)

        def on_confirm(event=None):
            entrada = input_entry.get().strip()
            if not entrada:
                return

            input_entry.delete(0, tk.END)

            if entrada.lower() in ['clear', 'borrar', 'limpiar']:
                self.clear()
                return

            if not validar_ip(entrada):
                self.output_text.insert(tk.END, "Dirección IP no válida.\n")
                return

            self.output_text.insert(tk.END, f"Iniciando auditoría para la IP: {entrada}\n")

            # Limpia el área de texto antes de comenzar el escaneo
            self.clear_output_text()

            # Ejecuta el escaneo y captura la salida
            try:
                realizar_escaneo(entrada, self.output_text)
            except subprocess.CalledProcessError as e:
                self.output_text.insert(tk.END, f"Error al ejecutar Nmap: {e}\n")
            except FileNotFoundError:
                self.output_text.insert(tk.END, "No se puede encontrar el archivo Nmap (nmap.exe) en la ruta especificada.\n")
            except Exception as e:
                self.output_text.insert(tk.END, f"Error inesperado al ejecutar el escaneo: {e}\n")

        confirm_button = tk.Button(self.root, text="Confirmar", command=on_confirm, font=font_style, bg="#1E1E1E", fg="#00FF00", activebackground="#1E1E1E", activeforeground="#FFFFFF")
        confirm_button.pack(pady=10)

    def clear(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "¡Bienvenido al sistema de auditoría!\nEsperando instrucciones...\n\n")

    def clear_output_text(self):
        self.output_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AuditoriaGUI(root)
    root.mainloop()
