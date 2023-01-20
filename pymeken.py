import tkinter as tk
import sys

commands = {
    'жаз': 'print',
    'куту': 'class',
    'ыкмасы': 'def',
    'киргизүү': 'input',
    'учурунда': 'while',
    'учун': 'for',
    'ичинде': 'in',
    'өзү': 'self',
    'сандар': 'numbers',
    'эгерде': 'if',
    'башка': 'else',
    'кайтуу': 'return',
}

class OutputText(tk.Text):
    def write(self, string):
        self.insert("end", string)

def translate_commands(input_text):
    # Replace the kyrgyz commands with their corresponding English translations
    for kyrgyz, english in commands.items():
        input_text = input_text.replace(kyrgyz, english)
    return input_text

def translate_and_compile(event=None):
    # Get the user's input in the terminal
    input_text = terminal.get("1.0", "end")
    python_code = translate_commands(input_text)
    # Redirect the standard output and error to the output text widget
    sys.stdout = sys.stderr = output
    # Compile and execute the code
    try:
        exec(python_code)
    except Exception as e:
        print(e)

def clean_output():
    output.delete('1.0', 'end')


def copy():
    terminal.event_generate("<<Copy>>")

def paste():
    terminal.event_generate("<<Paste>>")


root = tk.Tk()
root.title("KyrgyPy")

frame1 = tk.Frame(root)
frame1.pack()


terminal = tk.Text(frame1, width=50)
terminal.pack()

# Create a button to trigger the translation and compilation
translate_button = tk.Button(frame1, text="Чурка", command=translate_and_compile)
translate_button.pack(side='left')

# Create a "Clean" button for the output
clean_button = tk.Button(frame1, text="Таза", command=clean_output)
clean_button.pack(side='right')

# Create copy and paste button
copy_button = tk.Button(frame1, text="Көчүрүү", command=copy)
copy_button.pack(side='left')
paste_button = tk.Button(frame1, text="Чаптоо", command=paste)
paste_button.pack(side='left')

frame2 = tk.Frame(root)
frame2.pack()

# Create a text widget for the output
output = OutputText(frame2, width=50, height=10)
output.pack()

root.mainloop()