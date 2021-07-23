import serial.tools.list_ports
import serial
import PySimpleGUI as sg
ser = None  #Global tanımlanmalı

def serial_ports():
    ports = serial.tools.list_ports.comports()
    print(ports)
    seri_port = []
    for p in ports:
        print(p.device)
        seri_port.append(p.device)
    print(seri_port)
    return seri_port
########################
def serial_baglan():
    com_deger = value[0]
    baud_deger = value[1]
    print("Baud Deger", value[1])
    global ser
    ser = serial.Serial(com_deger, baud_deger, timeout=0, parity=serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS, rtscts=0)
    window["-BAGLANDI_TEXT-"].update('Bağlandı...')

sg.theme("Reddit")

ekran_layout = [ [sg.Text("Ayarlamak istediğiniz metni girin...")], 
                 [sg.Multiline(size=(40,4), font=("Arial", 14), key="giris_text")],
                 [sg.Button(button_text="Yazdır", font=("Arial Black", 11), key="yazdir"), 
                 sg.Button(button_text="Temizle", font=("Arial Black", 11), key="temizle"), 
                 sg.Button(button_text="Işık", font=("Arial Black", 11), key="isik")]    
                ]

layout =[ [sg.Text("Port Seçiniz:"), sg.Combo(serial_ports(), size=(10,1)),
            sg.Text("Baud Seçiniz:"), sg.Combo(["110","300","600","1200", "2400", "4800", "9600", "14400", "19200", "38400", "57600", "115200", "128000", "256000"], default_value=9600), 
            sg.Button(button_text="Bağlan", key="-BAGLAN-", size=(10,1)) ],
            [sg.Text("", size=(10,1), key="-BAGLANDI_TEXT-")],
            [sg.Frame("LCD Ekran", ekran_layout)]
        ]

window = sg.Window("Python Seri Port", layout)

while True:
    event, value = window.read(timeout=1000) 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break    
    if event == "-BAGLAN-":
        if (value[0] == ""):
            sg.popup("Bir Port Seçiniz!", title="Hata", custom_text="Tamam") 
        elif (value[1] == ""):
            sg.popup("Baud Oranını Seçiniz!", title="Hata", custom_text="Tamam")
        else:
            serial_baglan()
    if event == "yazdir":
        print(value)
        yazdirilacak = value['giris_text']
        yazdirilacak = yazdirilacak[:-1]
        if(len(yazdirilacak) > 120):
            sg.Popup("Yazdirilacak Veri Çok Büyük!") 
        elif((len(yazdirilacak) > 80)):
            yazdirilacak = yazdirilacak + ((120 - len(yazdirilacak)) * " ") 
        elif((len(yazdirilacak) > 60)):
            yazdirilacak = yazdirilacak + ((80 - len(yazdirilacak)) * " ") 
        elif((len(yazdirilacak) > 40)):
            yazdirilacak = yazdirilacak + ((60 - len(yazdirilacak)) * " ") 
        elif((len(yazdirilacak) > 20)):
            yazdirilacak = yazdirilacak + ((40 - len(yazdirilacak)) * " ") 
        elif((len(yazdirilacak) > 1)):
            yazdirilacak = yazdirilacak + ((20 - len(yazdirilacak)) * " ") 
        else:
            pass

     
        print("Yazdirilacak", yazdirilacak)
        ser.write(yazdirilacak.encode('Ascii'))
    if event == "temizle":
        window['giris_text'].update("")
        ser.write('*'.encode('Ascii'))
    if event == "isik":
        ser.write('\\'.encode('Ascii'))
    #? ? lcd_home özelliği...
window.close()