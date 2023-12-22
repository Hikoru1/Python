from tkinter import * 
from tkinter import messagebox
import base64
import os

def main_screen(): #Uygulamanın ana penceresini oluşturma
    global code #Şifre girişi için
    global screen
    global text1 #Metin girişi için

    screen = Tk()
    screen.geometry("375x398") #Ana pencere boyutu
    screen.title("Screen Message App") #Ana pencere ismi

    def encryption():
        password = code.get() #Girilen şifre code.get() ile alınır ve password değişkenine atanır
        if password == "1234":
            screen1 = Toplevel(screen) # screen1 adında yeni bir pencere oluşturur ve bu pencere screen penceresine bağlıdır
            screen1.title("encryption") #Oluşan
            screen1.geometry("400x200") #yeni pencereninin
            screen1.configure(bg="#ed3833") #özellikleri

            message = text1.get(1.0, END) #Metin kutusuna(text1) girilen değeri birinci satır birinci sütundan(1.0) sonuncu satır sonuncu sütüna kadar (END) alır ve message değişkenine atar
            encode_message = message.encode("ascii") #message değişkeninin ascii değerler olarak dönüştürür ve encode_message değişkenine atar
            base64_bytes = base64.b64encode(encode_message) #ASCII karakterleri içeren encode_message değişkenini base64.b64encode fonksiyonu ile Base64 formatında şifreler ve base64_bytes değişkenine atar
            encrypt = base64_bytes.decode("ascii") #base64_bytes değişkenini ASCII karakterler ile metne dönüştürür ve encrypt değişkenine atar

            Label(screen1, text="Encrypt", font="arial", bg="#ed3833", fg="white").place(x=10, y=0) #screen1 e bağlı bir pencere oluşturur ve bu pencere özelliklerini tanımlar
            text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0) #screen1 e bağlı bir metin kutusu oluşturur ve özelliklerini tanımlar bunu text2 değişkenine atar
            text2.place(x=10, y=40, width=380, height=150) #text2 yani az önce oluşan pencerenin boyutunu ve konumunu belirler.

            text2.insert(END, encrypt) #Şifrelenmiş metin kutusunu text2 ye görsel olarak koyar ve kullanıcının görmesi sağlanır
        
        elif password=="":
            messagebox.showerror("encryption","Input Password") 
        
        elif password !="1234":
                messagebox.showerror("encryption","Invaliad Password")
            
    def descryption():
        password = code.get() #Yukarıdaki fonksiyona ait aynı özellikle descryption fonksiyonunda da kullanılır. Bu fonksiyonun tek farkı gelen şifreli metni ASCII karakterleri ile anlaşılır metne dönüştürmesidir
        if password == "1234":
            screen2 = Toplevel(screen) 
            screen2.title("descryption")
            screen2.geometry("400x200")
            screen2.configure(bg="#00bd56")

            message = text1.get(1.0, END) 
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypt = base64_bytes.decode("ascii")

            Label(screen2, text="Decrypt", font="arial", bg="#00bd56", fg="white").place(x=10, y=0)
            text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, decrypt)
        
        elif password=="":
            messagebox.showerror("encryption","Input Password")
        
        elif password !="1234":
                messagebox.showerror("encryption","Invaliad Password")

    def reset(): #Girilen şifre ve yazıların silinmesi için oluşturulan bir fonksiyon
        code.set("")
        text1.delete(1.0, END)

    Label(text="Şifrelemek veya çözmek için metni girin", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)  #Şifrenin çözülmesi veya şifreleme yapmak için bir pencere oluşturur.

    Label(text="Parola", fg="black", font=("calbri", 13)).place(x=10, y=170) #Parolanın penceresidir.

    code = StringVar() #StringVar() Tkinter da kullanılan metin veya dize türü verileri tutmak için kullanılır.
    Entry(textvariable=code, width=19, bd=0, font=("arial", 20), show="*").place(x=10, y=200) #Bir giriş kutusu oluşturur ve bu veriyi code değişkenine StringVar değişkeni olarak tutar

    Button(text="Şifreleme", height=2, width=23, bg="#ed3833", fg="white", bd=0, command=encryption).place(x=10, y=250)
    Button(text="Çözme", height=2, width=23, bg="#00bd56", fg="white", bd=0, command=descryption).place(x=200, y=250)
    Button(text="Sıfırla", height=2, width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=350)
    #Yukarıdaki 3 kod satırı 3 adet buton oluşturur ve bunları belli konumlara özellikler dahilinde atar. command ile butona basıldığında yapacağı işlem belirtilir
    screen.mainloop() #Pencerenin sürekli çalışması için

main_screen() #Kodun sürekli çalışması için 
