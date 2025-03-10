import tkinter as tk

root = tk.Tk()

root.configure(background="#0000AA")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()

root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w,h))
root.wm_attributes("-topmost", 1)

error_message = """

Your PC ran into a problem and needs to restart.
We're just collecting some error info, and then we'll restart for you.

If you'd like to know more, you can search online later for this error
"""
label_sign = tk.Label(root, text=":(", fg="white", bg="#0000AA", font=("Segoe UI", 80), justify="left", anchor="nw")
label_sign.pack(pady=100, padx=50, anchor="w")
label = tk.Label(root, text=error_message, fg="white", bg="#0000AA", font=("Segoe UI", 30), justify="left", anchor="nw")
label.pack(pady=5, padx=50, anchor="w")

progress_label = tk.Label(root, text="0% complete", fg="white", bg="#0000AA", font=("Segoe UI",30), justify="left", anchor="w")
progress_label.pack(pady=20,padx=50, anchor="w")

def update_progress(percentage=0):
    if percentage <= 100:
        progress_label.config(text=f"{percentage}% complete")
        root.after(500, update_progress, percentage+5)

update_progress()    
root.mainloop()