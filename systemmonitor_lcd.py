import shutil
import psutil
import serial

ser = serial.Serial("COM10", "9600", timeout=0, parity=serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS, rtscts=0)

ser.write("*".encode('Ascii'))


while True:
    du = shutil.disk_usage("/")
    bos_alan_yuzde = du.free / du.total * 100
    islemci = "Islemci:%" + str(int(psutil.cpu_percent(1))) + "      \n"
    toplam_alan = "Toplam:" + str(int(du.total / 1024 / 1024 / 1024)) + "GB" + " \n"
    bos_alan = "Bos:" + str(int(du.free / 1024 / 1024 / 1024)) + "GB" + " \n"
    bos_yuzde = "Bos Yuzde:%" + str(int(bos_alan_yuzde))  + "    \n"
    ser.write("?".encode('Ascii'))
    ser.write(islemci.encode('Ascii'))
    ser.write(toplam_alan.encode("Ascii"))
    ser.write(bos_alan.encode("Ascii"))
    ser.write(bos_yuzde.encode("Ascii"))

