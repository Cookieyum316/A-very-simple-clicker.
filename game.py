import tkinter as tk
root = tk.Tk()
root.title("Clicker!")
root.geometry("1000x500")
score = 0
mult = 1
price = 75
rebirths = 0
reb = 2

def rebirth1():
    global rebirths
    global score
    global reb
    global mult
    global price
    if score >= 1000000:
        score = 0
        reb *= 2
        rebirths += 1
        price = 75
        mult = 1
        label.config(text=f"Your score is:{score}")
        labelreb.config(text=f"Rebirths:{rebirths}")
    else:
        label.config(text=f"Your score is:{score}")
    



def scoreup1():
    global score
    if score >= price:
        button2.config(bg="LightGreen")
        score += mult
        label.config(text=f"Your score is:{score}")
    else:
        score += mult
        button2.config(bg="White")
        label.config(text=f"Your score is:{score}")
    
def upgrade():
    global score
    global mult
    global price
    if score > price:
        score = score - price
        mult *= reb
        price *= 2
        label1.config(text=f"Current multiplier is:{mult}")
        button2.config(text=f"Upg cost:{price}")
        label.config(text=f"Your score is:{score}")
        button2.config(bg="LightGreen")
    else:
        label.config(text=f"Your score is:{score}")
    

label = tk.Label(root, text=f"Your score is:", font=("Arial", 20))
label.grid(row=0, columnspan=3, pady=10)

buttonr = tk.Button(root, text=f"Rebirth", font=("Arial", 20), width=10, height=2, bg="Pink", command=rebirth1)
buttonr.grid(row=2, column=6, pady=10)

labelreb = tk.Label(root, text=f"Rebirths:{rebirths}", font=("Arial", 20))
labelreb.grid(row=3, column=6, columnspan=2, pady=10)

button1 = tk.Button(root, text="Button", font=("Arial",20), width=10, height=4, command=scoreup1)
button1.grid(row=1, column=0, padx=20, pady=20)

button2 = tk.Button(root, text=f"Upg cost:{price}", font=("Arial",20), width=15, height=2, bg="White", command=upgrade)
button2.grid(row=2, column=0, pady=20)

label1 = tk.Label(root, text=f"Current multiplier is:{mult}", font=("Arial",20))
label1.grid(row=3, columnspan=2, pady=10)

root.mainloop()