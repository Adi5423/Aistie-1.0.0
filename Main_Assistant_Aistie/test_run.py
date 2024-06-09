import tkinter as tk
from tkinter import ttk

class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Chat Application")

        # Create frames for the chat log and input
        self.chat_frame = tk.Frame(master)
        self.chat_frame.pack(fill="both", expand=True)

        self.input_frame = tk.Frame(master)
        self.input_frame.pack(fill="x")

        # Chat Log
        self.chat_log = tk.Text(self.chat_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.chat_log.pack(fill="both", expand=True)

        # Input Area
        self.input_entry = tk.Entry(self.input_frame)
        self.input_entry.pack(side=tk.LEFT, fill="x", expand=True)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT)

    def send_message(self):
        # Get the user input
        message = self.input_entry.get()
        
        # Add user input to chat log
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, "You: " + message + "\n")
        self.chat_log.config(state=tk.DISABLED)

        # Clear the input field
        self.input_entry.delete(0, tk.END)

        # Simulate a response from Aistie
        response = "Aistie: " + "Here is a response."  # Replace with actual backend logic
        
        # Add Aistie's response to chat log
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, response + "\n")
        self.chat_log.config(state=tk.DISABLED)

        # Scroll chat log to the bottom
        self.chat_log.see(tk.END)

# Create the main window and run the application
root = tk.Tk()
app = ChatApp(root)
root.mainloop()