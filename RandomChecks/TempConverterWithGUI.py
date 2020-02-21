from tkinter import Tk, Label, Button, StringVar
import TempConvertAssert


class MyFirstGUI:
    LABEL_TEXT = [
        "Temperature calculator",
    ]

    def __init__(self, master):
        self.master = master
        master.title("Temparature Calculator")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        self.greet_button = Button(master, text="Provide a number in between 1-6", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        choice_of_converter = input(" ")
        if int(choice_of_converter) == 1:
            print("Please provide the temparature value in KELVIN scale: ")
            temp_kel = input(" ")
            converted_KelToFer = TempConvertAssert.KelvinToFarhenheit(float(temp_kel))
            print("Temperature is:", str(converted_KelToFer))

        if int(choice_of_converter) == 2:
            print("Please provide the temparature value in KELVIN scale: ")
            temp_kel = input(" ")
            converted_KelToCel = TempConvertAssert.KelvinToCelcius(float(temp_kel))
            print("Temperature is:", str(converted_KelToCel))

        if int(choice_of_converter) == 3:
            print("Please provide the temparature value in FERHEHEIT scale: ")
            temp_fer = input(" ")
            converted_FerToKel = TempConvertAssert.FarhenheitToKelvin(float(temp_fer))
            print("Temperature is:", str(converted_FerToKel))

        if int(choice_of_converter) == 4:
            print("Please provide the temparature value in FERHEHEIT scale: ")
            temp_fer = input(" ")
            converted_FerToCel = TempConvertAssert.FarhenheitToCelcius(float(temp_fer))
            print("Temperature is:", str(converted_FerToCel))

        if int(choice_of_converter) == 5:
            print("Please provide the temparature value in Celcius scale: ")
            temp_cel = input(" ")
            converted_CelToFer = TempConvertAssert.CelciusToFerhenheit(float(temp_cel))
            print("Temperature is:", str(converted_CelToFer))

        if int(choice_of_converter) == 6:
            print("Please provide the temparature value in Celcius scale: ")
            temp_cel = input(" ")
            converted_CelToKel = TempConvertAssert.CelciusToKelvin(float(temp_cel))
            print("Temperature is:", str(converted_CelToKel))

        print("Greetings!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT)  # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()