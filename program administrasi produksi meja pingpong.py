import tkinter as tk
from tkinter import *

app = tk.Tk()

app.geometry("370x300")
app.title('Admnistrasi Produksi Meja Pingpong')
app.maxsize(370, 300)
app.minsize(370, 300)
app.configure(background='#79DAE8')



#Input Data Pembelian Barang
def main_beli():
    root = Tk()
    root.geometry('520x540')
    root.title("Input Data Pembelian Barang")
    root.configure(background='#79DAE8')

    def baca_file(file):
        f = open(file).readlines()
        data = []
        for line in f:
            data = data+[csvtoarray(line)]
        return data

    def csvtoarray(Arr):
        arr_baru = []
        idx = 0
        temp = 0

        for i in range(1, len(Arr)):
            if(i == len(Arr)-1):
                arr_baru += [Arr[temp:i]]

                if(Arr[-1:] != "\n"):
                    arr_baru[idx] = arr_baru[idx]+Arr[len(Arr)-1]

            else:
                if(Arr[i] == ';'):
                    idx += 1
                    string = Arr[temp:i]

                    arr_baru = arr_baru+[string]
                    temp = i+1
        return arr_baru

    def saveData(file, data):

        data = convert(data)

        f = open(file, "w")
        f.write(data)
        f.close()

    def convert(data):
        i = 0
        string = ""
        for tempData in data:
            i += 1
            tempDatas = [str(var) for var in tempData]
            string += ";".join(tempDatas)
            if i != len(data):
                string += "\n"
        return string

    def msg():
        bulan = cvar.get()
        select = var.get()

    def save():
        g = var.get()
        bulan = cvar.get()
        fs = open(('stok.txt'), 'a')
        data_stok = baca_file('stok.txt')
        condition = True
        index = 0
        try:
            for i in range(len(data_stok)):
                if str(e1.get().lower()) == data_stok[i][0]:
                    condition = False
                    index = i
            cek_input_harga = int(e2.get())
            cek_input_stok = int(e3.get())
            if condition == False:
                data_stok[index][1] = str(
                    int(data_stok[index][1]) + int(e3.get()))
                saveData('stok.txt', data_stok)
            else:
                s = '\n'+e1.get().lower()+';'+e3.get()
                fs.write(s)
                fs.close()
            s = '\n' + e1.get().lower()+';'+e2.get()+';'+e3.get()+';'+bulan
            f = open(('data_pembelian.txt'), 'a')
            x = baca_file('data_pembelian.txt')
            if (len(x)) == 0:
                f.write('Barang'+';'+'Harga'+';'+'Jumlah'+';'+'Bulan')
            f.write(s)
            f.close()
            l8 = Label(root, text="Input berhasil", font=(
                "times", 9, "bold"), anchor="w", bg='#79DAE8', fg='#2155CD')
            l8.place(x=70, y=370)
            l8.after(1000, l8.master.destroy)
        except ValueError:
            l8 = Label(root, text="Input gagal", font=(
                "times", 9, "bold"), anchor="w", bg='#79DAE8', fg='#2155CD')
            l8.place(x=70, y=370)
            l8.after(1000, l8.master.destroy)

    def saveinfo():
        save()

    l1 = Label(root, text="\tData Pembelian Barang", width=25,
               font=("helvetica", 14, "bold"), bg='#79DAE8', fg='#2155CD')
    l1.place(x=70, y=50)
    l2 = Label(root, text="Nama barang", width=20, font=(
        "times", 12), anchor="w", bg='#79DAE8', fg='#2155CD')
    l2.place(x=70, y=130)
    e1 = Entry(root, width=30, bd=2)
    e1.place(x=240, y=130)
    l3 = Label(root, text="Harga", width=20, font=(
        "times", 12), anchor="w", bg='#79DAE8',fg='#2155CD')
    l3.place(x=70, y=180)
    e2 = Entry(root, width=30, bd=2)
    e2.place(x=240, y=180)

    var = IntVar()

    l6 = Label(root, text="Jumlah", width=20, font=(
        "times", 12), anchor="w", bg='#79DAE8',fg='#2155CD')
    l6.place(x=70, y=230)
    e3 = Entry(root, width=30, bd=2)
    e3.place(x=240, y=230)
    l7 = Label(root, text="Bulan pembelian", width=20, font=(
        "times", 12), anchor="w", bg='#79DAE8',fg='#2155CD')
    l7.place(x=70, y=280)

    cvar = StringVar()
    cvar.set("Bulan pembelian")
    option = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    o = OptionMenu(root, cvar, *option)
    o.config(font=("times", 11), bd=1)
    o.place(x=240, y=280, width=190)

    b1 = Button(root, text='Submit', command=saveinfo, width=15,
                bg='green', fg='white', font=("times", 12, "bold"))
    b1.place(x=90, y=330)
    b2 = Button(root, text='Cancel', command=root.destroy, width=15,
                bg='maroon', fg='white', font=("times", 12, "bold"))
    b2.place(x=270, y=330)
    l8 = Label(root, text="Data tercatat di file data_pembelian.txt", font=(
        "times", 10, "bold"), anchor="w", bg='#79DAE8', fg='#2155CD')
    l8.place(x=150, y=420)

    root.mainloop()

#Input Data Penjualan Barang
def main_jual():
    root = Tk()
    root.geometry('520x540')
    root.title("Input Data Penjualan Barang")
    root.configure(background='#79DAE8')

    def baca_file(file):
        f = open(file).readlines()
        data = []
        for line in f:
            data = data+[csvtoarray(line)]
        return data

    def csvtoarray(Arr):
        arr_baru = []
        idx = 0
        temp = 0

        for i in range(1, len(Arr)):
            if(i == len(Arr)-1):
                arr_baru += [Arr[temp:i]]

                if(Arr[-1:] != "\n"):
                    arr_baru[idx] = arr_baru[idx]+Arr[len(Arr)-1]

            else:
                if(Arr[i] == ';'):
                    idx += 1
                    string = Arr[temp:i]

                    arr_baru = arr_baru+[string]
                    temp = i+1
        return arr_baru

    def saveData(file, data):

        data = convert(data)

        f = open(file, "w")
        f.write(data)
        f.close()

    def convert(data):
        i = 0
        string = ""
        for tempData in data:
            i += 1
            tempDatas = [str(var) for var in tempData]
            string += ";".join(tempDatas)
            if i != len(data):
                string += "\n"
        return string

    def msg():
        bulan = cvar.get()
        select = var.get()

    def save():
        g = var.get()
        bulan = cvar.get()

        s = '\n' + e1.get().lower()+';'+e2.get()+';'+e3.get()+';'+bulan
        f = open(('data_penjualan.txt'), 'a')
        x = baca_file('data_penjualan.txt')

        data_stok = baca_file('stok.txt')
        condition = True
        index = 0
        try:
            for i in range(len(data_stok)):
                if str(e1.get().lower()) == data_stok[i][0]:
                    condition = False
                    index = i
            cek_input_harga = int(e2.get())
            cek_input_stok = int(e3.get())
            if condition == False:
                if (int(data_stok[index][1]) - int(e3.get())) < 0:
                    l10 = Label(root, text="Stok tidak mencukupi", font=(
                        "times", 9, "bold"), anchor="w", bg='grey')
                    l10.place(x=70, y=280)
                else:
                    data_stok[index][1] = str(
                        int(data_stok[index][1]) - int(e3.get()))
                    saveData('stok.txt', data_stok)
                    if (len(x)) == 0:
                        f.write('Barang'+';'+'Harga'+';'+'Jumlah'+';'+'Bulan')
                    f.write(s)
            else:
                l11 = Label(root, text="Barang tidak tersedia", font=(
                    "times", 9, "bold"), anchor="w", bg='grey')
                l11.place(x=70, y=280)
            f.close()
            l8 = Label(root, text="Input berhasil", font=(
                "times", 9, "bold"), anchor="w", bg='#79DAE8', fg='#2155CD')
            l8.place(x=70, y=370)
            l8.after(1000, l8.master.destroy)
        except ValueError:
            l8 = Label(root, text="Input gagal", font=(
                "times", 9, "bold"), anchor="w", bg='#79DAE8', fg='#2155CD')
            l8.place(x=70, y=370)
            l8.after(1000, l8.master.destroy)

    def saveinfo():
        save()

    l1 = Label(root, text="\tData Penjualan Barang", width=25,
               font=("helvetica", 14, "bold"), bg='#79DAE8', fg='#2155CD')
    l1.place(x=70, y=50)
    l2 = Label(root, text="Nama Barang", width=20, font=(
        "times", 12), anchor="w", bg='#79DAE8',fg='#2155CD')
    l2.place(x=70, y=130)
    e1 = Entry(root, width=30, bd=2)
    e1.place(x=240, y=130)
    l3 = Label(root, text="Harga", width=20, font=(
        "times", 12), anchor="w", bg='#79DAE8', fg='#2155CD')
    l3.place(x=70, y=180)
    e2 = Entry(root, width=30, bd=2)
    e2.place(x=240, y=180)

    var = IntVar()

    l6 = Label(root, text="Jumlah", width=20, font=(
        "times", 12), anchor="w", bg='#79DAE8',fg='#2155CD')
    l6.place(x=70, y=230)
    e3 = Entry(root, width=30, bd=2)
    e3.place(x=240, y=230)
    l7 = Label(root, text="Bulan penjualan", width=20, font=(
        "times", 12), anchor="w", bg='#79DAE8',fg='#2155CD')
    l7.place(x=70, y=280)

    cvar = StringVar()
    cvar.set("Bulan penjualan")
    option = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    o = OptionMenu(root, cvar, *option)
    o.config(font=("times", 11), bd=3)
    o.place(x=240, y=280, width=190)

    b1 = Button(root, text='Submit', command=saveinfo, width=15,
                bg='green', fg='white', font=("times", 12, "bold"))
    b1.place(x=90, y=330)
    b2 = Button(root, text='Cancel', command=root.destroy, width=15,
                bg='maroon', fg='white', font=("times", 12, "bold"))
    b2.place(x=270, y=330)
    l8 = Label(root, text="Data tercatat di file data_penjualan.txt", font=(
        "times", 9, "bold"), anchor="w", bg='#79DAE8', fg='#2155CD')
    l8.place(x=150, y=420)

    root.mainloop()


def baca_file(file):
    f = open(file).readlines()
    data = []
    for line in f:
        data = data+[csvtoarray(line)]
    return data


def csvtoarray(Arr):
    arr_baru = []
    idx = 0
    temp = 0

    for i in range(1, len(Arr)):
        if(i == len(Arr)-1):
            arr_baru += [Arr[temp:i]]

            if(Arr[-1:] != "\n"):
                arr_baru[idx] = arr_baru[idx]+Arr[len(Arr)-1]

        else:
            if(Arr[i] == ';'):
                idx += 1
                string = Arr[temp:i]

                arr_baru = arr_baru+[string]
                temp = i+1
    return arr_baru

#Data stok
def stok_data():
    f = baca_file('stok.txt')
    root = Tk()
    root.geometry("380x900")
    root.title('Stok Barang')
    root.maxsize(380, 900)
    root.minsize(380, 900)
    root.configure(background='#79DAE8')

    myLabel = Label(root, text='STOK BARANG', font=('helvetica', 13, 'bold'), bg='#79DAE8', fg ='#2155CD')
    myLabel.grid(row=0, column=0)
    for i in range(len(f)):
        for j in range(2):
            if i == 0:
                myLabel = Label(
                    root, text=f[i][j] + '   ', font=('times', 10, 'bold'),bg='#79DAE8', fg='#2155CD')
                myLabel.grid(row=3, column=j)
                myLabel = Label(
                    root, text=20*'_', font=('times', 10, 'bold'),bg='#79DAE8',fg='#2155CD')
                myLabel.grid(row=4, column=j)
            else:
                if j == 0:
                    myLabel = Label(
                        root, text=f[i][j] + '  ', font=('times', 10, 'bold'),bg='#79DAE8',fg='#2155CD')
                    myLabel.grid(row=i+4, column=0)
                else:
                    myLabel = Label(
                        root, text=f[i][j], font=('times', 10, 'bold'),bg='#79DAE8',fg='#2155CD')
                    myLabel.grid(row=i+4, column=1)

    root.mainloop()

#Mengupdate Data
def update_data():
    root = Tk()
    root.geometry('520x540')
    root.title("Update Data Barang")
    root.configure(background='#79DAE8')

    def baca_file(file):
        f = open(file).readlines()
        data = []
        for line in f:
            data = data+[csvtoarray(line)]
        return data

    def csvtoarray(Arr):
        arr_baru = []
        idx = 0
        temp = 0

        for i in range(1, len(Arr)):
            if(i == len(Arr)-1):
                arr_baru += [Arr[temp:i]]

                if(Arr[-1:] != "\n"):
                    arr_baru[idx] = arr_baru[idx]+Arr[len(Arr)-1]

            else:
                if(Arr[i] == ';'):
                    idx += 1
                    string = Arr[temp:i]

                    arr_baru = arr_baru+[string]
                    temp = i+1
        return arr_baru

    def saveData(file, data):

        data = convert(data)

        f = open(file, "w")
        f.write(data)
        f.close()

    def convert(data):
        string = ""
        for tempData in data:
            tempDatas = [str(var) for var in tempData]
            string += ";".join(tempDatas)
            string += "\n"
        return string

    def msg():
        select = var.get()

    def save():
        g = var.get()

        data_stok = baca_file('stok.txt')
        condition = True
        index = 0
        try:
            cek_input_stok = int(e2.get())
            if int(e2.get()) >= 0:
                for i in range(len(data_stok)):
                    if str(e1.get().lower()) == data_stok[i][0]:
                        condition = False
                        index = i
                if condition == False:
                    data_stok[index][1] = str(e2.get())
                    saveData('stok.txt', data_stok)
                    mylabel = Label(root, text="Data Berhasil Diupdate!", width=25,
                                    font=("times", 18, "bold"), bg='#2155CD', fg='#E8F9FD')
                    mylabel.place(x=70, y=240)
                    mylabel.after(1000, mylabel.master.destroy)
                else:
                    data_stok += [[e1.get().lower(), e2.get()]]

                    saveData('stok.txt', data_stok)
                    mylabel = Label(root, text="Data Berhasil Diupdate!", width=20,
                                    font=("times", 12, "bold"), bg='#2155CD', fg='#E8F9FD')
                    mylabel.place(x=70, y=240)
                    mylabel.after(1000, mylabel.master.destroy)
            else:
                mylabel1 = Label(root, text="Jumlah harus lebih dari 0!", width=25,
                                 font=("times", 12, "bold"), bg='#2155CD', fg='#E8F9FD')
                mylabel1.place(x=70, y=240)
                mylabel1.after(1000, mylabel1.master.destroy)
        except ValueError:
            mylabel1 = Label(root, text="Input tidak sesuai!", width=25,
                             font=("times", 12, "bold"),bg='#2155CD', fg='#E8F9FD')
            mylabel1.place(x=70, y=240)
            mylabel1.after(1000, mylabel1.master.destroy)

    def saveinfo():
        save()

    l1 = Label(root, text="\tData Pembelian Barang", width=25,
               font=("helvetica", 14, "bold"), bg='#79DAE8',fg='#2155CD')
    l1.place(x=70, y=50)
    l2 = Label(root, text="Nama Barang", width=20, font=(
        "times", 12), anchor="w", bg='#79DAE8',fg='#2155CD')
    l2.place(x=70, y=130)
    e1 = Entry(root, width=30, bd=2)
    e1.place(x=240, y=130)
    l3 = Label(root, text="Jumlah stok", width=20, font=(
        "times", 12), anchor="w", bg='#79DAE8',fg='#2155CD')
    l3.place(x=70, y=180)
    e2 = Entry(root, width=30, bd=2)
    e2.place(x=240, y=180)

    var = IntVar()

    b1 = Button(root, text='Update', command=saveinfo, width=15,
                bg='green', fg='white', font=("times", 12, "bold"))
    b1.place(x=85, y=350)
    b2 = Button(root, text='Cancel', command=root.destroy, width=15,
                bg='maroon', fg='white', font=("times", 12, "bold"))
    b2.place(x=250, y=350)

    root.mainloop()

#Menghapus Data
def hapus_data():
    root = Tk()
    root.geometry('520x540')
    root.title("Hapus Data Barang")
    root.configure(background='#79DAE8')

    def baca_file(file):
        f = open(file).readlines()
        data = []
        for line in f:
            data = data+[csvtoarray(line)]
        return data

    def csvtoarray(Arr):
        arr_baru = []
        idx = 0
        temp = 0

        for i in range(1, len(Arr)):
            if(i == len(Arr)-1):
                arr_baru += [Arr[temp:i]]

                if(Arr[-1:] != "\n"):
                    arr_baru[idx] = arr_baru[idx]+Arr[len(Arr)-1]

            else:
                if(Arr[i] == ';'):
                    idx += 1
                    string = Arr[temp:i]

                    arr_baru = arr_baru+[string]
                    temp = i+1
        return arr_baru

    def saveData(file, data):

        data = convert(data)

        f = open(file, "w")
        f.write(data)
        f.close()

    def convert(data):
        i = 0
        string = ""
        for tempData in data:
            i += 1
            tempDatas = [str(var) for var in tempData]
            string += ";".join(tempDatas)
            if i != len(data):
                string += "\n"
        return string

    def msg():
        select = var.get()

    def save():
        g = var.get()

        data_stok = baca_file('stok.txt')
        condition = True
        index = 0
        for i in range(len(data_stok)):
            if str(e1.get().lower()) == data_stok[i][0]:
                condition = False
                index = i
        if condition == False:
            data_stok.remove(data_stok[index])
            saveData('stok.txt', data_stok)
            mylabel = Label(root, text="Data Berhasil Dihapus!", width=25,
                            font=("times", 20, "bold"), bg='#2155CD', fg='#E8F9FD')
            mylabel.place(x=70, y=240)
            mylabel.after(1000, mylabel.master.destroy)
        else:
            mylabel = Label(root, text="Barang tidak ditemukan!", width=25,
                            font=("times", 12, "bold"),bg='#2155CD', fg='#E8F9FD')
            mylabel.place(x=70, y=240)
            mylabel.after(1000, mylabel.master.destroy)

    def saveinfo():
        save()

    l1 = Label(root, text="\tHapus Data Barang", width=25,
               font=("times", ), bg='#79DAE8', fg='#2155CD')
    l1.place(x=70, y=50)
    l2 = Label(root, text="Nama Barang", width=20, font=(
        "times", 12), anchor="w", bg='#79DAE8',fg='#2155CD')
    l2.place(x=70, y=130)
    e1 = Entry(root, width=30, bd=2)
    e1.place(x=240, y=130)

    var = IntVar()

    b1 = Button(root, text='Hapus', command=saveinfo, width=15,
                bg='green', fg='white', font=("times", 12, "bold"))
    b1.place(x=80, y=350)
    b2 = Button(root, text='Cancel', command=root.destroy, width=15,
                bg='maroon', fg='white', font=("times", 12, "bold"))
    b2.place(x=280, y=350)

    root.mainloop()


def baca_file(file):
    f = open(file).readlines()
    data = []
    for line in f:
        data = data+[csvtoarray(line)]
    return data


def csvtoarray(Arr):
    arr_baru = []
    idx = 0
    temp = 0

    for i in range(1, len(Arr)):
        if(i == len(Arr)-1):
            arr_baru += [Arr[temp:i]]

            if(Arr[-1:] != "\n"):
                arr_baru[idx] = arr_baru[idx]+Arr[len(Arr)-1]

        else:
            if(Arr[i] == ';'):
                idx += 1
                string = Arr[temp:i]

                arr_baru = arr_baru+[string]
                temp = i+1
    return arr_baru

#Data catatan 
def catatan_bulanan():
    data_beli = baca_file('data_pembelian.txt')
    data_jual = baca_file('data_penjualan.txt')
    root = Tk()
    root.title('Data keuangan')
    root.configure(background='#79DAE8')

    myLabel = Label(root, text='\nCatatan Keuangan Bulanan\n',
                    font=('times', 13, 'bold'),background='#79DAE8',fg='#2155CD')
    myLabel.pack()
    list_pendapatan = [0 for i in range(12)]
    list_pengeluaran = [0 for i in range(12)]
    for i in range(1, len(data_beli)):
        bulan = int(data_beli[i][3])
        list_pengeluaran[bulan -
                         1] += (int(data_beli[i][2]))*(int(data_beli[i][1]))
    for i in range(1, len(data_jual)):
        bulan = int(data_jual[i][3])
        list_pendapatan[bulan-1] += int(data_jual[i][2])*int(data_jual[i][1])
    for i in range(12):
        label1 = Label(
            root, text=f'{i+1}. Pendapatan bulan ke-{i+1}: {list_pendapatan[i]} ,00',bg='#79DAE8')
        label1.pack()
    label2 = Label(root, text='\n'+20*'='+'\n',background='#79DAE8',fg='#2155CD')
    label2.pack()
    for i in range(12):
        label3 = Label(
            root, text=f'{i+1}. Pengeluaran bulan ke-{i+1}: {list_pengeluaran[i]} ,00',bg='#79DAE8')
        label3.pack()

    root.mainloop()


#button
labelmenu = Label(app, text='\n\n',
                  font=('times', 18, 'bold'),bg='#79DAE8')
labelmenu.grid(row=0)

#pembelian
pembelian = Button(app, text="Data Pembelian", width=20, command=main_beli,
                   bg="#E8F9FD", fg="#0AA1DD", borderwidth=3, relief=RIDGE)
pembelian.grid(row=1, sticky="w", padx=15, pady=5)

#penjualan
penjualan = Button(app, text="Data Penjualan", width=20, command=main_jual,
                   bg="#E8F9FD", fg="#0AA1DD", borderwidth=3, relief=RIDGE)
penjualan.grid(row=1, column=2, sticky="w", padx=15, pady=5)

#stok
stok = Button(app, text="Stock Barang", width=20, command=stok_data,
              bg="#E8F9FD", fg="#0AA1DD", borderwidth=3, relief=RIDGE)
stok.grid(row=2, sticky="w", padx=15, pady=5)

#pdate
update = Button(app, text="Update Data", width=20, command=update_data,
                bg="#E8F9FD", fg="#0AA1DD", borderwidth=3, relief=RIDGE)
update.grid(row=2, column=2, sticky="w", padx=15, pady=5)

#delete
hapus = Button(app, text="Hapus Data", width=20, command=hapus_data,
               bg="#E8F9FD", fg="#0AA1DD", borderwidth=3, relief=RIDGE)
hapus.grid(row=3, sticky="w", padx=15, pady=5)

#catatan
catatan_perbulan = Button(app, text="Catatan Perbulan", width=20, command=catatan_bulanan,
                          bg="#E8F9FD", fg="#0AA1DD", borderwidth=3, relief=RIDGE)
catatan_perbulan.grid(row=3, column=2, sticky="w", padx=15, pady=5)


app.mainloop()
