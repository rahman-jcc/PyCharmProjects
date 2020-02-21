def calculate(abc):
    feet = StringVar()
    meters = StringVar()
    value = float(feet.get())    
    return meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)