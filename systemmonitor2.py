import shutil
import psutil
import serial

ser = serial.Serial("COM10", "9600", timeout=0, parity=serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS, rtscts=0)

ser.write("*".encode('Ascii'))


while True:
    du = shutil.disk_usage("/")
    bos_alan_yuzde = du.free / du.total * 100
    islemci = "CPU:%" + str(int(psutil.cpu_percent(1))).ljust(3)
    islemci_freq= "FRQ:" + str(int(psutil.cpu_freq().current)).rjust(4) + "MHz"
    islemci_satir = islemci + islemci_freq + "\n"
    toplam_alan = "DSKT:" + (str(int(du.total / 1024 / 1024 / 1024)) + "GB").ljust(6)
    bos_alan = " F:" + (str(int(du.free / 1024 / 1024 / 1024)) + "GB").ljust(6)
    # bos_yuzde = "F%" + str(int(bos_alan_yuzde)).ljust(2) + " "
    ram_total = int(psutil.virtual_memory().total / 1024 / 1024)
    ram_free = int(psutil.virtual_memory().free / 1024 / 1024)
    ram_percent = int(psutil.virtual_memory().percent)
    ram_satir = "M:" + str(ram_total).rjust(5) + "MB " + "F:" + (str(ram_free) + "MB").ljust(8)
    sistem_mesaji = "-----SYSTEM OK-----"
    ser.write("?".encode('Ascii'))
    ser.write(islemci_satir.encode('Ascii'))
    ser.write(toplam_alan.encode("Ascii"))
    ser.write(bos_alan.encode("Ascii"))
    ser.write(ram_satir.encode("Ascii"))
    ser.write(sistem_mesaji.encode("Ascii"))
    # ser.write(bos_yuzde.encode("Ascii"))

