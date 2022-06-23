import tkinter as tk
from tkinter import *

app = tk.Tk()

app.geometry("1080x720")
app.title('Program Produksi Meja Pingpong')


def main_beli():
    root = Tk()
    root.geometry('520x540')
    root.title("Input Data Pembelian Barang")
    root.configure(background='grey')

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
            l8 = Label(root, text="Input telah sesuai", font=(
                "times", 9, "bold"), anchor="w", bg='grey')
            l8.place(x=70, y=370)
            l8.after(1000, l8.master.destroy)
        except ValueError:
            l8 = Label(root, text="Input tidak sesuai", font=(
                "times", 9, "bold"), anchor="w", bg='grey')
            l8.place(x=70, y=370)
            l8.after(1000, l8.master.destroy)

    def saveinfo():
        save()

    l1 = Label(root, text="Data Pembelian Barang", width=25,
               font=("times", 20, "bold"), bg='blue', fg='white')
    l1.place(x=70, y=50)
    l2 = Label(root, text="Nama Barang", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l2.place(x=70, y=130)
    e1 = Entry(root, width=30, bd=2)
    e1.place(x=240, y=130)
    l3 = Label(root, text="Harga", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l3.place(x=70, y=180)
    e2 = Entry(root, width=30, bd=2)
    e2.place(x=240, y=180)

    var = IntVar()

    l6 = Label(root, text="Jumlah", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l6.place(x=70, y=230)
    e3 = Entry(root, width=30, bd=2)
    e3.place(x=240, y=230)
    l7 = Label(root, text="Bulan pembelian", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l7.place(x=70, y=280)

    cvar = StringVar()
    cvar.set("Bulan pembelian")
    option = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    o = OptionMenu(root, cvar, *option)
    o.config(font=("times", 11), bd=3)
    o.place(x=240, y=280, width=190)

    b1 = Button(root, text='Submit', command=saveinfo, width=15,
                bg='green', fg='white', font=("times", 12, "bold"))
    b1.place(x=120, y=330)
    b2 = Button(root, text='Cancel', command=root.destroy, width=15,
                bg='maroon', fg='white', font=("times", 12, "bold"))
    b2.place(x=320, y=330)
    l8 = Label(root, text="Jika sudah klik submit otomatis tercatat di file data_pembelian.txt", font=(
        "times", 9, "bold"), anchor="w", bg='grey')
    l8.place(x=100, y=420)

    root.mainloop()


def main_jual():
    root = Tk()
    root.geometry('520x540')
    root.title("Input Data Penjualan Barang")
    root.configure(background='grey')

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
            l8 = Label(root, text="Input telah sesuai", font=(
                "times", 9, "bold"), anchor="w", bg='grey')
            l8.place(x=70, y=370)
            l8.after(1000, l8.master.destroy)
        except ValueError:
            l8 = Label(root, text="Input tidak sesuai", font=(
                "times", 9, "bold"), anchor="w", bg='grey')
            l8.place(x=70, y=370)
            l8.after(1000, l8.master.destroy)

    def saveinfo():
        save()

    l1 = Label(root, text="Data penjualan Barang", width=25,
               font=("times", 20, "bold"), bg='blue', fg='white')
    l1.place(x=70, y=50)
    l2 = Label(root, text="Nama Barang", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l2.place(x=70, y=130)
    e1 = Entry(root, width=30, bd=2)
    e1.place(x=240, y=130)
    l3 = Label(root, text="Harga", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l3.place(x=70, y=180)
    e2 = Entry(root, width=30, bd=2)
    e2.place(x=240, y=180)

    var = IntVar()

    l6 = Label(root, text="Jumlah", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l6.place(x=70, y=230)
    e3 = Entry(root, width=30, bd=2)
    e3.place(x=240, y=230)
    l7 = Label(root, text="Bulan penjualan", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l7.place(x=70, y=280)

    cvar = StringVar()
    cvar.set("Bulan penjualan")
    option = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    o = OptionMenu(root, cvar, *option)
    o.config(font=("times", 11), bd=3)
    o.place(x=240, y=280, width=190)

    b1 = Button(root, text='Submit', command=saveinfo, width=15,
                bg='green', fg='white', font=("times", 12, "bold"))
    b1.place(x=120, y=330)
    b2 = Button(root, text='Cancel', command=root.destroy, width=15,
                bg='maroon', fg='white', font=("times", 12, "bold"))
    b2.place(x=320, y=330)
    l8 = Label(root, text="Jika sudah klik submit otomatis tercatat di file data_penjualan.txt", font=(
        "times", 9, "bold"), anchor="w", bg='grey')
    l8.place(x=100, y=420)

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


def stok_data():
    f = baca_file('stok.txt')
    root = Tk()
    root.geometry("380x900")
    root.title('Stok Barang')
    root.maxsize(380, 900)
    root.minsize(380, 900)
    myLabel = Label(root, text='STOK BARANG', font=('times', 13, 'bold'))
    myLabel.grid(row=0, column=0)
    for i in range(len(f)):
        for j in range(2):
            if i == 0:
                myLabel = Label(
                    root, text=f[i][j] + '   ', font=('times', 10, 'bold'))
                myLabel.grid(row=3, column=j)
                myLabel = Label(
                    root, text=20*'_', font=('times', 10, 'bold'))
                myLabel.grid(row=4, column=j)
            else:
                if j == 0:
                    myLabel = Label(
                        root, text=f[i][j] + '  ', font=('times', 10, 'bold'))
                    myLabel.grid(row=i+4, column=0)
                else:
                    myLabel = Label(
                        root, text=f[i][j], font=('times', 10, 'bold'))
                    myLabel.grid(row=i+4, column=1)

    root.mainloop()


def update_data():
    root = Tk()
    root.geometry('520x540')
    root.title("Update Data Barang")
    root.configure(background='grey')

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
                                    font=("times", 20, "bold"), bg='blue', fg='white')
                    mylabel.place(x=70, y=240)
                    mylabel.after(1000, mylabel.master.destroy)
                else:
                    data_stok += [[e1.get().lower(), e2.get()]]

                    saveData('stok.txt', data_stok)
                    mylabel = Label(root, text="Data Berhasil Diupdate!", width=18,
                                    font=("times", 12, "bold"), bg='blue', fg='white')
                    mylabel.place(x=70, y=240)
                    mylabel.after(1000, mylabel.master.destroy)
            else:
                mylabel1 = Label(root, text="Jumlah harus lebih dari 0!", width=18,
                                 font=("times", 12, "bold"), bg='blue', fg='white')
                mylabel1.place(x=70, y=240)
                mylabel1.after(1000, mylabel1.master.destroy)
        except ValueError:
            mylabel1 = Label(root, text="Input tidak sesuai!", width=18,
                             font=("times", 12, "bold"), bg='blue', fg='white')
            mylabel1.place(x=70, y=240)
            mylabel1.after(1000, mylabel1.master.destroy)

    def saveinfo():
        save()

    l1 = Label(root, text="Data Pembelian Barang", width=25,
               font=("times", 20, "bold"), bg='blue', fg='white')
    l1.place(x=70, y=50)
    l2 = Label(root, text="Nama Barang", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l2.place(x=70, y=130)
    e1 = Entry(root, width=30, bd=2)
    e1.place(x=240, y=130)
    l3 = Label(root, text="Jumlah stok", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l3.place(x=70, y=180)
    e2 = Entry(root, width=30, bd=2)
    e2.place(x=240, y=180)

    var = IntVar()

    b1 = Button(root, text='Update', command=saveinfo, width=15,
                bg='green', fg='white', font=("times", 12, "bold"))
    b1.place(x=120, y=440)
    b2 = Button(root, text='Cancel', command=root.destroy, width=15,
                bg='maroon', fg='white', font=("times", 12, "bold"))
    b2.place(x=320, y=440)

    root.mainloop()


def hapus_data():
    root = Tk()
    root.geometry('520x540')
    root.title("Hapus Data Barang")
    root.configure(background='grey')

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
                            font=("times", 20, "bold"), bg='blue', fg='white')
            mylabel.place(x=70, y=240)
            mylabel.after(1000, mylabel.master.destroy)
        else:
            mylabel = Label(root, text="Barang tidak ditemukan!", width=18,
                            font=("times", 12, "bold"), bg='blue', fg='white')
            mylabel.place(x=70, y=240)
            mylabel.after(1000, mylabel.master.destroy)

    def saveinfo():
        save()

    l1 = Label(root, text="Hapus Data Barang", width=25,
               font=("times", 20, "bold"), bg='blue', fg='white')
    l1.place(x=70, y=50)
    l2 = Label(root, text="Nama Barang", width=20, font=(
        "times", 12, "bold"), anchor="w", bg='grey')
    l2.place(x=70, y=130)
    e1 = Entry(root, width=30, bd=2)
    e1.place(x=240, y=130)

    var = IntVar()

    b1 = Button(root, text='Hapus', command=saveinfo, width=15,
                bg='green', fg='white', font=("times", 12, "bold"))
    b1.place(x=120, y=440)
    b2 = Button(root, text='Cancel', command=root.destroy, width=15,
                bg='maroon', fg='white', font=("times", 12, "bold"))
    b2.place(x=320, y=440)

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


def catatan_bulanan():
    data_beli = baca_file('data_pembelian.txt')
    data_jual = baca_file('data_penjualan.txt')
    root = Tk()
    root.title('Stok Barang')
    myLabel = Label(root, text='Catatan Keuangan Bulanan',
                    font=('times', 13, 'bold'))
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
            root, text=f'{i+1}. Pendapatan bulan ke-{i+1}: {list_pendapatan[i]} rupiah')
        label1.pack()
    label2 = Label(root, text='\n'+20*'='+'\n')
    label2.pack()
    for i in range(12):
        label3 = Label(
            root, text=f'{i+1}. Pengeluaran bulan ke-{i+1}: {list_pengeluaran[i]} rupiah')
        label3.pack()

    root.mainloop()


labelmenu = Label(app, text='\n\n',
                  font=('times', 18, 'bold'))
labelmenu.grid(row=0)
pembelian = Button(app, text="Data Pembelian", width=20, command=main_beli,
                   bg="green", fg="white", borderwidth=3, relief=RIDGE)
pembelian.grid(row=1, sticky="w", padx=15, pady=5)
penjualan = Button(app, text="Data Penjualan", width=20, command=main_jual,
                   bg="green", fg="white", borderwidth=3, relief=RIDGE)
penjualan.grid(row=1, column=2, sticky="w", padx=15, pady=5)
stok = Button(app, text="Stock Barang", width=20, command=stok_data,
              bg="green", fg="white", borderwidth=3, relief=RIDGE)
stok.grid(row=2, sticky="w", padx=15, pady=5)
update = Button(app, text="Update Data", width=20, command=update_data,
                bg="green", fg="white", borderwidth=3, relief=RIDGE)
update.grid(row=2, column=2, sticky="w", padx=15, pady=5)
hapus = Button(app, text="Hapus Data", width=20, command=hapus_data,
               bg="green", fg="white", borderwidth=3, relief=RIDGE)
hapus.grid(row=3, sticky="w", padx=15, pady=5)
catatan_perbulan = Button(app, text="Catatan Perbulan", width=20, command=catatan_bulanan,
                          bg="green", fg="white", borderwidth=3, relief=RIDGE)
catatan_perbulan.grid(row=3, column=2, sticky="w", padx=15, pady=5)


app.mainloop()
