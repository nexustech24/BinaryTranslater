import tkinter as tk
from tkinter import ttk

class BinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Converter")

        self.input_label = tk.Label(root, text="Input:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10)
        self.input_field = tk.Entry(root, width=40)
        self.input_field.grid(row=0, column=1, padx=10, pady=10)

        self.conversion_type_label = tk.Label(root, text="Conversion Type:")
        self.conversion_type_label.grid(row=1, column=0, padx=10, pady=10)
        self.conversion_type = ttk.Combobox(root, values=["Binary to Text", "Binary to Number", "Text to Binary", "Number to Binary"])
        self.conversion_type.grid(row=1, column=1, padx=10, pady=10)
        self.conversion_type.current(0)

        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.output_label = tk.Label(root, text="Output:")
        self.output_label.grid(row=3, column=0, padx=10, pady=10)
        self.output_field = tk.Text(root, height=5, width=40)
        self.output_field.grid(row=3, column=1, padx=10, pady=10)

    def convert(self):
        input_data = self.input_field.get()
        conversion = self.conversion_type.get()
        result = ""

        try:
            if conversion == "Binary to Text":
                result = self.binary_to_text(input_data)
            elif conversion == "Binary to Number":
                result = str(self.binary_to_number(input_data))
            elif conversion == "Text to Binary":
                result = self.text_to_binary(input_data)
            elif conversion == "Number to Binary":
                result = self.number_to_binary(int(input_data))

        except ValueError as e:
            result = f"Error: {e}"

        self.output_field.delete(1.0, tk.END)
        self.output_field.insert(tk.END, result)

    def binary_to_text(self, binary_str):
        binary_values = binary_str.split()
        ascii_characters = [chr(int(b, 2)) for b in binary_values]
        return ''.join(ascii_characters)

    def binary_to_number(self, binary_str):
        return int(binary_str, 2)

    def text_to_binary(self, text):
        return ' '.join(format(ord(char), '08b') for char in text)

    def number_to_binary(self, number):
        return bin(number)[2:]

if __name__ == "__main__":
    root = tk.Tk()
    app = BinaryConverterApp(root)
    root.mainloop()
