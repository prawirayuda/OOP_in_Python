import tkinter
main_window =tkinter.Tk()
print(main_window.__dict__)

label1 = tkinter.Label(main_window,text = "label1")
label2 = tkinter.Label(main_window,text = "label2")
tombol1 = tkinter.Button(main_window, text = "tombol1")
#method positioning
label1.pack()
label2.pack()
tombol1.pack()
#method menampilkan gui 

main_window.mainloop()

#noteed setiap hurufdepannya besar itu adalah kelas
#dan setiap awalan huruf nya kecil maka itu adalah method 