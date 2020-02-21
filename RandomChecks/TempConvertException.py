
import TempConvertAssert

try:
    fh = open("TemperatureConverter.txt", "w")

    # Choosing the conversion method
    print ("Choose the conversion type:  ")
    print ("1. Kelvin to Ferhenheit")
    print ("2. Kelvin to Celcius")
    print ("3. Ferhenheit to Kelvin")
    print ("4. Ferhenheit to Celcius")
    print ("5. Celcius to Ferhenheit")
    print ("6. Celcius to Kelvin")
    choice_of_converter = input (" ")

    if int (choice_of_converter) == 1:
        print ("Please provide the temparature value in KELVIN scale: ")
        temp_kel = input(" " )
        converted_KelToFer = TempConvertAssert.KelvinToFarhenheit(float(temp_kel))

        try:
            fh.writelines(str (converted_KelToFer))
        finally:
            print ("Temperature is:", str(converted_KelToFer))
            print ("Converted value is saved to file")
            fh.close()


    if int (choice_of_converter) == 2:
        print ("Please provide the temparature value in KELVIN scale: ")
        temp_kel = input(" " )
        converted_KelToCel = TempConvertAssert.KelvinToCelcius(float(temp_kel))
        try:
            fh.writelines(str (converted_KelToCel))
        finally:
            print ("Temperature is:", str(converted_KelToCel))
            print ("Converted value is saved to file")
            fh.close()

    if int (choice_of_converter) == 3:
        print ("Please provide the temparature value in FERHEHEIT scale: ")
        temp_fer = input(" " )
        converted_FerToKel = TempConvertAssert.FarhenheitToKelvin(float(temp_fer))

        try:
            fh.writelines(str (converted_FerToKel))
        finally:
            print ("Temperature is:", str(converted_FerToKel))
            print ("Converted value is saved to file")
            fh.close()

    if int (choice_of_converter) == 4:
        print ("Please provide the temparature value in FERHEHEIT scale: ")
        temp_fer = input(" " )
        converted_FerToCel = TempConvertAssert.FarhenheitToCelcius(float(temp_fer))

        try:
            fh.writelines(str (converted_FerToCel))
        finally:
            print ("Temperature is:", str(converted_FerToCel))
            print ("Converted value is saved to file")
            fh.close()

    if int (choice_of_converter) == 5:
        print ("Please provide the temparature value in Celcius scale: ")
        temp_cel = input(" " )
        converted_CelToFer = TempConvertAssert.CelciusToFerhenheit(float(temp_cel))

        try:
            fh.writelines(str (converted_CelToFer))
        finally:
            print ("Temperature is:", str(converted_CelToFer))
            print ("Converted value is saved to file")
            fh.close()


    if int(choice_of_converter) == 6:
        print ("Please provide the temparature value in Celcius scale: ")
        temp_cel = input(" " )
        converted_CelToKel = TempConvertAssert.CelciusToKelvin(float(temp_cel))

        try:
            fh.writelines(str (converted_CelToKel))
        finally:
            print ("Temperature is:", str(converted_CelToKel))
            print ("Converted value is saved to file")
            fh.close()

            # assert temp_kel== str, "Please provide integer values!!"
    # Calling convertion function from TempConvertAssert .py



except IOError:
    print ("Error: can\'t find file or read data")