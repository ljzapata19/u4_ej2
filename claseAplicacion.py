from tkinter import *
from tkinter import ttk,font, messagebox
import tkinter as tk
class Aplicacion(tk.Tk):
    __ventana = None
    
    __psiniva = None
    __iva = None
    __pconiva = None
    
    
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Calculo IVA')
        fuente=font.Font(font='Verdana 10',weight='normal')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        
        label_titulo=ttk.Label(mainframe, text="Cálculo de IVA", background= 'light blue')
        opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
        label_titulo.grid(column=0, row=0, columnspan=2, **opts)
        
        self.__psiniva = StringVar()
        self.__pconiva = StringVar()
        
        ttk.Label(mainframe, text="Precio sin IVA").grid(column=0, row=1,padx=10,pady=10)
        self.psinivaEntry = ttk.Entry(mainframe, width=15, textvariable=self.__psiniva)
        self.psinivaEntry.grid(column=1,row=1,padx=10,pady=10)
        
        self.valor=tk.IntVar()
        self.__iva = StringVar()
        labelFrameSeleccione=tk.LabelFrame(mainframe, text='Seleccione:',font=fuente,borderwidth=2, padx=5, pady=5)
        labelFrameSeleccione.grid(row=2, column=0, **opts)
        ttk.Radiobutton(labelFrameSeleccione, text='IVA 21%', value=0, variable=self.valor,command=self.cambiaValor).grid(row =3, column=0, columnspan=1, sticky='w')
        ttk.Radiobutton(labelFrameSeleccione, text='IVA 10.5%', value=1, variable=self.valor,command=self.cambiaValor).grid(row =4, column=0, columnspan=1,sticky='w')
        
        
        ttk.Label(mainframe, text="IVA").grid(column=0, row=5,padx=10,pady=10)
        ttk.Label(mainframe, textvariable=self.__iva).grid(column=1, row=5, sticky=(E))
        
        ttk.Label(mainframe, text="Precio con IVA").grid(column=0, row=6,padx=10,pady=10)
        ttk.Label(mainframe, textvariable=self.__pconiva).grid(column=1, row=6, sticky=(E))
        
        ttk.Button(mainframe, text='Calcular IVA',command=self.calculaIVA).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=2, row=7, sticky=W)
        
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        self.__ventana.mainloop()
        
    def cambiaValor(self):
        if self.valor.get()==0:
            self.__iva.set('21')
        else:
            if self.valor.get()==1:
                self.__iva.set('10.5')
       
    
    def calculaIVA(self):
        try:
            monto= float(self.psinivaEntry.get())
            iva=(monto*float(self.__iva.get())/100)
            print(iva)
            self.__iva.set(iva)
            self.__pconiva.set(monto + iva)
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar valores numéricos')
            self.__psiniva.set('')
