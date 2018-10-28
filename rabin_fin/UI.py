import tkinter
from Rabin_cryptosystem import Decipher,Cipher,testing,bytes_from_file,read_from_f

ciphr_but_text = 'Encryption mode'
deciphr_but_text = 'Decryption mode'
ciph_but = 'Lets\'s chipher! '
deciph_but = 'Lets\'s dechipher! '
go_back_but = 'Go back'

text_1 = 'Enter N: '
text_2 = 'Enter B: '
text_3 = 'Enter P: '
text_4 = 'Enter Q: '

error_text = 'One of parametrs is false'
error_text_2 = 'Empty fields'

text_1_out = 'Start file: '
text_2_out = 'Cipher file: '
text_3_out = 'Decipher file: '




def out_inf(t1,t2,t3,mode='c',*w,**kw):

    def go_back(*w,**kw):
        root1.destroy()
        mainframe()



    root1 = tkinter.Tk()
    root1.geometry('500x400')
    root1.title('Rabin Cryptosystem')
    # button
    back_button = tkinter.Button(root1, text=go_back_but, bg='Dodger Blue', fg='White', width=20,
                                 command=(lambda: go_back()))
    back_button.place(relx=.8, rely=0.3)


    # text
    tk_text_1 = tkinter.Text(root1,width=70, height=2)
    tk_text_1.place(relx=.03, rely=.3)

    tk_text_2 = tkinter.Text(root1,width=70, height=2)
    tk_text_2.place(relx=.03, rely=.5)

    if mode == 'd':
        tk_text_3 = tkinter.Text(root1,width=70, height=2)
        tk_text_3.place(relx=.03, rely=.7)

    # labels
    label_1 = tkinter.Label(root1, text=text_1_out, height=1)
    label_1.place(relx=.03, rely=.2)

    label_2 = tkinter.Label(root1, text=text_2_out, height=1)
    label_2.place(relx=.03, rely=.4)

    if mode == 'd':
        label_3 = tkinter.Label(root1, text=text_3_out, height=1)
        label_3.place(relx=.03, rely=.6)

    tk_text_1.delete('1.0', tkinter.END)
    tk_text_2.delete('1.0', tkinter.END)
    if mode == 'd':
        tk_text_3.delete('1.0', tkinter.END)

    tk_text_1.insert(tkinter.END,''.join(str(x)+' ' for x in t1[0:20]))
    tk_text_2.insert(tkinter.END, ''.join(str(x)+' ' for x in t2[0:20]))
    if mode == 'd':
        tk_text_3.insert(tkinter.END, ''.join(str(x)+' ' for x in t3[0:20]))

    #root1.mainloop()


def mainframe():

    def create_encrypt(*w,**kw):
        Main_Window.destroy()
        encryption_frame()

    def create_decrypt(*w,**kw):
        Main_Window.destroy()
        decryption_frame()


    Main_Window = tkinter.Tk()
    Main_Window.geometry('500x400')
    Main_Window.title('Rabin Cryptosystem')

    # make GUI
    button_one = tkinter.Button(Main_Window, text=ciphr_but_text, bg='Dodger Blue', fg='White', width=20, command= (lambda : create_encrypt()))
    button_one.place(relx=.5 - .1, rely=.5)

    button_two = tkinter.Button(Main_Window, text=deciphr_but_text, bg='Dodger Blue', fg='White', width=20, command = (lambda  : create_decrypt()))
    button_two.place(relx=.5 - .1, rely=.6)

    Main_Window.update_idletasks()
    # end of prog
    Main_Window.mainloop()


def encryption_frame(*w,**kw):

    def go_back(*w,**kw):
        root2.destroy()
        mainframe()

    def go_ciph(*w,**kw):
        from tkinter import messagebox
        from tkinter.filedialog import askopenfilename

        n = n_entry.get()
        b = b_entry.get()
        out_array_0 = []

        if not(n == '' or b == ''):
            n = int(n)
            b = int(b)

            if testing(b, n):
                filename = askopenfilename()
                Cipher(filename, n, b)

            else:
                messagebox.showerror('Error',error_text)
        else:
            messagebox.showerror('Error',error_text_2)

        for byte in bytes_from_file(filename):
            out_array_0.append(byte)
        out_array_1 = read_from_f(filename+'.cph')
        root2.destroy()
        out_inf(out_array_0,out_array_1,[])





    root2= tkinter.Tk()
    root2.geometry('500x250')
    root2.title('Encryption')



    # GUI N1

    ciph_button = tkinter.Button(root2, text=ciph_but, bg='Dodger Blue', fg='White', width=20, command = (lambda : go_ciph()))
    ciph_button.place(relx=.4,rely=0.3)

    back_button = tkinter.Button(root2, text=go_back_but, bg='Dodger Blue', fg='White', width=20, command= (lambda : go_back()))
    back_button.place(relx=.4,rely=0.5)

    # entrys

    n_var = tkinter.IntVar()
    b_var = tkinter.IntVar()
    n_var = ''
    b_var = ''

    n_entry = tkinter.Entry(textvariable=n_var)
    n_entry.place(relx=.1, rely=.3, width=100)

    b_entry = tkinter.Entry(textvariable=b_var)
    b_entry.place(relx=.1, rely=.5, width=100)

    # labels


    label_1 = tkinter.Label(root2, text=text_1,height=1)
    label_1.place(relx=.1, rely=.2)

    label_2 = tkinter.Label(root2, text=text_2,height=1)
    label_2.place(relx=.1, rely=.4)

    #root2.mainloop()


def decryption_frame(*w,**kw):

    def go_back(*w,**kw):
        root3.destroy()
        mainframe()

    def go_deciph(*w,**kw):
        from tkinter import messagebox
        from tkinter.filedialog import askopenfilename
        p = p_entry.get()
        q = q_entry.get()
        b = b_entry.get()

        if not (p == '' or  q == '' or b == ''):
            p = int(p)
            q = int(q)
            b = int(b)
            out_array_0 = []
            out_array_1 = []


            if testing(b, p*q,p,q):
                filename = askopenfilename()
                out_array_2 = Decipher(filename,p,q, b)
                for byte in bytes_from_file(filename[:len(filename) - 4]):
                    out_array_0.append(byte)

                out_array_1 =read_from_f(filename)

                root3.destroy()
                out_inf(out_array_0, out_array_1, out_array_2, 'd')
            else:
                messagebox.showerror('Error',error_text)
        else:
            messagebox.showerror('Error',error_text_2)






    root3 = tkinter.Tk()
    root3.geometry('500x300')
    root3.title('Decryption')



    # GUI N1

    deciph_button = tkinter.Button(root3, text=deciph_but, bg='Dodger Blue', fg='White', width=20, command = (lambda : go_deciph()))
    deciph_button.place(relx=.4,rely=0.4)

    back_button = tkinter.Button(root3, text=go_back_but, bg='Dodger Blue', fg='White', width=20, command= (lambda : go_back()))
    back_button.place(relx=.4,rely=0.6)

    # entrys

    q_var = tkinter.IntVar()
    p_var = tkinter.IntVar()
    b_var = tkinter.IntVar()
    p_var = ''
    b_var = ''
    q_var = ''

    q_entry = tkinter.Entry(textvariable=q_var)
    q_entry.place(relx=.1, rely=.3, width=100)

    p_entry = tkinter.Entry(textvariable=p_var)
    p_entry.place(relx=.1, rely=.5, width=100)

    b_entry = tkinter.Entry(textvariable=b_var)
    b_entry.place(relx=.1, rely=.7, width=100)

    # labels


    label_1 = tkinter.Label(root3, text=text_3,height=1)
    label_1.place(relx=.1, rely=.2)

    label_2 = tkinter.Label(root3, text=text_4,height=1)
    label_2.place(relx=.1, rely=.4)

    label_3 = tkinter.Label(root3, text=text_2,height=1)
    label_3.place(relx=.1, rely=.6)


    #root3.mainloop()



if __name__ == '__main__':
    mainframe()




