from functions.factor import getFactorizedExpression
from functions.interfaz import Window, Widget, Widget
from tkinter import Label, Button, Entry, Tk, messagebox as ms
from functions.help import getHelp

# Ventana
class App(Window):
    # Constructor App
    def __init__(self, root, w, h, cl, ttl, resz):
        self.root = root
        self.w = w 
        self.h = h
        self.cl = cl
        self.ttl = ttl
        self.resz = resz 
        # Constructor Window
        super().__init__(self.root, self.w, self.h, self.cl, self.ttl, self.resz)

class WidgetApp(App):
    def __init__(self):
        # Gestor de ventana TKinter
        self.root = Tk()
        # Constructor super() => App
        App.__init__(self, self.root, 400, 400, "black", "Factorized Expression", [False, False])

        self.elements = [Label, Entry, Button, Label, Label, Button]
        self.widgets = Widget(self.root, self.elements)
        self.optionsElents = [
            {"fg":"red", "font":("Helvetica", 12, "bold"), "bg":"black", "text":"Ingrese la expresión a factorizar"},
            {"fg":"green", "font":("Helvetica", 12, "bold"), "bg":"black", "insertbackground":"red", "justify":"center"},
            {"fg":"red", "font":("Helvetica", 12, "bold"), "bg":"black", "text":"Factorizar", "height":1},
            {"fg":"green", "font":("Helvetica", 12, "bold"), "bg":"black", "text":"Factorizado/Simplificado:\n\n"},
            {"fg":"white", "font":("monospace", 12), "bg":"black", "text":"By ©SRM - 2024"},
            {"fg":"red", "font":("Helvetica", 8), "bg":"black", "text":"Help"},
        ]       
        self.typePack = ["place" for _ in self.elements]
        self.packOp = [
            {"relx":0.5,"y":22, "anchor":"center"},
            {"relx":0.5,"y":52, "anchor":"center"},
            {"relx":0.5,"y":92, "anchor":"center"},
            {"relx":0.5,"y":152, "anchor":"center"},
            {"relx":0.5,"rely":0.95, "anchor":"center"},
            {"relx":0.8,"rely":0.15, "anchor":"w"}
        ]
        
        self.widgets.widgetsCreate(self.optionsElents, self.typePack, self.packOp) 
        self.widgets.widgetsList[1].insert(0, "(2*(x**2)-x-3)/(x+1)")
        self.widgets.widgetsList[2].configure(command=lambda: self.setTxtLabel(getFactorizedExpression(self.widgets.getText(1)), self.widgets.widgetsList[3]))   
        self.widgets.widgetsList[5].configure(command=self.alertHelp)

    def setTxtLabel(self, txt, label):
        label.configure(text="Factorizado/Simplificado:\n\n"+str(txt))
    
    def alertHelp(self):
        container = ms.showinfo("Ayuda.", getHelp())


def run():
    app = WidgetApp()
    app.root.mainloop()