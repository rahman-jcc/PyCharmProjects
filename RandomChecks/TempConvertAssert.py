
def KelvinToFarhenheit (temp):
    assert (temp >=0),"Colder than the zero"
    return ((temp-273.15)*1.8)+32

def KelvinToCelcius (temp):
    assert (temp >=0),"Colder than the zero"
    return temp-273.15

def FarhenheitToKelvin (temp):
    assert (temp <= -459),"Temparuter value is over absolute value"
    return ((temp-32)*5/9)+273

def FarhenheitToCelcius (temp):
    assert (temp <= -459),"Temparuter value is over absolute value"
    return ((temp-32)*5/9)

def CelciusToFerhenheit (temp):
    assert (temp >= 100),"Temparature is over boiling point"
    return (temp*9/5)+32

def CelciusToKelvin (temp):
    assert (temp >= 100),"Temparature is over boiling point"
    return (temp+273.15)





