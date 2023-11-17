import tkinter as tk
from tkinter import ttk

def calculate_position(*args):
    trade_type = trade_type_var.get()
    funds = float(funds_var.get())
    risk_percentage = float(risk_percentage_var.get())
    buy_price = float(buy_price_var.get())
    stop_loss = float(stop_loss_var.get())

    day_risk = (funds * risk_percentage) / 100
    price_gap = abs(buy_price - stop_loss)
    position_size = int(day_risk / price_gap)
    lot1 = position_size // 2
    lot2 = position_size - lot1  # Calculate Lot 2

    if trade_type == "long":
        target1 = 0.6 * price_gap + buy_price
        target2 = 1 * price_gap + buy_price
    else:  # trade_type == "short"
        target1 = buy_price - 0.6 * price_gap
        target2 = buy_price - 1 * price_gap

    result_label.config(text=f"Position Size: {position_size}\nLot 1: {lot1}\nLot 2: {lot2}\nTarget 1: {target1:.2f}\nTarget 2: {target2:.2f}")

# Create the main application window
app = tk.Tk()
app.title("Risk Calculator")

# Create and place widgets (labels, entries, buttons) in the window
ttk.Label(app, text="Trade Type:").grid(row=0, column=0, sticky="w")
trade_type_var = tk.StringVar(value="long")
trade_type_combobox = ttk.Combobox(app, textvariable=trade_type_var, values=["long", "short"])
trade_type_combobox.grid(row=0, column=1, pady=5)

ttk.Label(app, text="Funds:").grid(row=1, column=0, sticky="w")
funds_var = tk.StringVar()
funds_entry = ttk.Entry(app, textvariable=funds_var)
funds_entry.grid(row=1, column=1, pady=5)
funds_entry.bind("<Return>", calculate_position)

ttk.Label(app, text="Risk Percentage:").grid(row=2, column=0, sticky="w")
risk_percentage_var = tk.StringVar()
risk_percentage_entry = ttk.Entry(app, textvariable=risk_percentage_var)
risk_percentage_entry.grid(row=2, column=1, pady=5)
risk_percentage_entry.bind("<Return>", calculate_position)

ttk.Label(app, text="Buy Price:").grid(row=3, column=0, sticky="w")
buy_price_var = tk.StringVar()
buy_price_entry = ttk.Entry(app, textvariable=buy_price_var)
buy_price_entry.grid(row=3, column=1, pady=5)
buy_price_entry.bind("<Return>", calculate_position)

ttk.Label(app, text="Stop Loss:").grid(row=4, column=0, sticky="w")
stop_loss_var = tk.StringVar()
stop_loss_entry = ttk.Entry(app, textvariable=stop_loss_var)
stop_loss_entry.grid(row=4, column=1, pady=5)
stop_loss_entry.bind("<Return>", calculate_position)

calculate_button = ttk.Button(app, text="Calculate", command=calculate_position)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label = ttk.Label(app, text="")
result_label.grid(row=6, column=0, columnspan=2)

# Start the Tkinter event loop
app.mainloop()
