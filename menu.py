import tkinter as tk
import pong_game

# Initialize a custom font
custom_font = ("Verdana", 18, "normal")

def on_button_click(button_number, root):
    if button_number == 1:
        root.destroy()  # Schließt das Hauptmenüfenster
        pong_game.start_pong_game()
    else:
        print(f"{button_number} clicked.")

def main_menu():
    root = tk.Tk()
    root.title("Pong Main Menu")
    window_width = 800
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.configure(bg="black")

    button1 = tk.Button(root, text="Localpong", command=lambda: on_button_click(1, root), bg="white", fg="black", font=custom_font)
    button1.pack(pady=20)
    
    button2 = tk.Button(root, text="Player vs Bot", command=lambda: on_button_click(2, root), bg="white", fg="black", font=custom_font)
    button2.pack(pady=20)
    
    button3 = tk.Button(root, text="Multiplayer", command=lambda: on_button_click(3, root), bg="white", fg="black", font=custom_font)
    button3.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
