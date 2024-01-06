#Requires AutoHotkey v2.0

!#^PgUp::
{
Run("Python C:\Users\Adam\Documents\GitHub\rpi-rs232-control\client\pyClient.py MVLUP",,"Hide")
}

!#^PgDn::
{
Run("Python C:\Users\Adam\Documents\GitHub\rpi-rs232-control\client\pyClient.py MVLDOWN",,"Hide")
}
return