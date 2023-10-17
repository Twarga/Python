import tkinter as tk
from tkinter import ttk
import paramiko

# Function to establish an SSH connection
def connect_ssh():
    hostname = hostname_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    try:
        # Create an SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote server
        ssh_client.connect(hostname, port=22, username=username, password=password)

        # Execute a command (e.g., 'ls -l') and display the output in the GUI
        command = command_entry.get()
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode('utf-8')
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, output)

    except Exception as e:
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, f"Error: {str(e)}")

    finally:
        ssh_client.close()

# Create the main application window
app = tk.Tk()
app.title("SSH Client")

# Hostname, Username, and Password entry fields
hostname_label = ttk.Label(app, text="Hostname or IP:")
hostname_label.pack()
hostname_entry = ttk.Entry(app)
hostname_entry.pack()

username_label = ttk.Label(app, text="Username:")
username_label.pack()
username_entry = ttk.Entry(app)
username_entry.pack()

password_label = ttk.Label(app, text="Password:")
password_label.pack()
password_entry = ttk.Entry(app, show="*")
password_entry.pack()

# Command entry field and execute button
command_label = ttk.Label(app, text="SSH Command:")
command_label.pack()
command_entry = ttk.Entry(app)
command_entry.pack()

execute_button = ttk.Button(app, text="Execute Command", command=connect_ssh)
execute_button.pack()

# Output text area
output_text = tk.Text(app, height=10, width=40)
output_text.pack()

# Start the GUI application
app.mainloop()

