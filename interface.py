import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cripto import criptografar_arquivo  # Importa a função de criptografia do seu script de criptografia

class CryptographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptographer")

        # Define as cores em RGB
        self.bg_color = "#f0f0f0"  # Fundo cinza claro
        self.button_color = "#4caf50"  # Verde
        self.button_hover_color = "#45a049"  # Verde escuro
        self.text_color = "#000000"  # Preto
        self.label_color = "#333333"  # Cinza escuro

        # Define a fonte
        self.font = ("Helvetica", 12)

        # Cria o frame principal
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Título
        self.label_title = tk.Label(self.main_frame, text="Cryptographer", font=("Arial", 24, "bold"), fg=self.label_color, bg=self.bg_color)
        self.label_title.pack(pady=(20, 10))

        # Entrada de arquivo
        self.label_entrada = tk.Label(self.main_frame, text="Selecione o arquivo de entrada:", font=self.font, fg=self.label_color, bg=self.bg_color)
        self.label_entrada.pack()

        self.entry_entrada = tk.Entry(self.main_frame, font=self.font, bg="white", fg=self.text_color, bd=1, relief=tk.SOLID)
        self.entry_entrada.pack(pady=5, padx=10, ipady=5, fill=tk.X)

        self.button_entrada = tk.Button(self.main_frame, text="Selecionar Arquivo", font=self.font, bg=self.button_color, fg="white", bd=0, relief=tk.FLAT, padx=10, pady=5, command=self.select_input_file)
        self.button_entrada.pack(pady=5)

        # Botão de criptografar
        self.encrypt_button = tk.Button(self.main_frame, text="Criptografar Arquivo", font=self.font, bg=self.button_color, fg="white", bd=0, relief=tk.FLAT, padx=10, pady=5, command=self.encrypt_file)
        self.encrypt_button.pack(pady=20)

    def select_input_file(self):
        file_path = filedialog.askopenfilename()
        self.entry_entrada.delete(0, tk.END)
        self.entry_entrada.insert(0, file_path)

    def encrypt_file(self):
        arquivo_entrada = self.entry_entrada.get()

        if not arquivo_entrada:
            messagebox.showerror("Erro", "Por favor, selecione um arquivo de entrada.")
            return

        chave = os.urandom(32)  # Chave de 256 bits (32 bytes) para AES-256

        # Define o nome do arquivo de saída com a mesma raiz do arquivo de entrada, mas com a extensão .encrypted
        arquivo_saida = arquivo_entrada + ".encrypted"

        # Criptografa o arquivo usando a função do script de criptografia
        criptografar_arquivo(arquivo_entrada, arquivo_saida, chave)

        messagebox.showinfo("Sucesso", "Arquivo criptografado com sucesso!")

root = tk.Tk()
app = CryptographyApp(root)
root.mainloop()
