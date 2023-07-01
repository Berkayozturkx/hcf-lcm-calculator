#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class EbobEkok(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Ebob/Ekok Hesaplayıcı")
        grid = QGridLayout()
        
        grid.addWidget(QLabel("1.Sayıyı Giriniz:"),1,1)
        grid.addWidget(QLabel("2.Sayıyı Giriniz:"),2,1)
        
        self.sayi1 = QLineEdit()
        grid.addWidget(self.sayi1,1,2)
        
        self.sayi2 = QLineEdit()
        grid.addWidget(self.sayi2,2,2)
        
        
        self.buton = QPushButton("Hesapla")
        grid.addWidget(self.buton,3,2)
        self.buton.clicked.connect(self.hesapla)
        
        self.yazi = QLabel("")
        grid.addWidget(self.yazi,5,1)
        
        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(grid)
        v_box.addStretch()
        
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        
        
        self.setLayout(h_box)
        self.resize(350,140)
        self.show()
        
    def hesapla(self):
        sayi1 = 0
        try: sayi1 = int(self.sayi1.text())
        except: pass
        
        sayi2 = 0
        try: sayi2 = int(self.sayi2.text())
        except: pass
        
        ebob = 0
        ekok = 1
        if(sayi1 > 0 and sayi2 > 0):
            if (sayi1 < sayi2):
                for i in range(1,sayi1+1):
                    if(sayi1 % i == 0 and sayi2 % i == 0):
                        ebob = i
                ekok = int((sayi1*sayi2)/ebob)
                self.yazi.setText("Ebob: {}\nEkok: {}".format(ebob,ekok))
            elif (sayi2 < sayi1):
                if(sayi1 % i == 0 and sayi2 % i == 0):
                        ebob = i
                ekok = int((sayi1*sayi2)/ebob)
                self.yazi.setText("Ebob: {}\nEkok: {}".format(ebob,ekok))
            elif (sayi1 == sayi2):
                if(sayi1 % i == 0 and sayi2 % i == 0):
                        ebob = i
                ekok = int((sayi1*sayi2)/ebob)
                self.yazi.setText("Ebob: {}\nEkok: {}".format(ebob,ekok))
        elif (sayi1 == 0 and sayi2 == 0):
            self.yazi.setText("Ebob: 0\nEkok: 0")
        else:
            self.yazi.setText("Hatalı sayı girişi, lütfen pozitif sayılar giriniz.")
uygulama = QApplication(sys.argv)
pencere = EbobEkok()
sys.exit(uygulama.exec_())


# In[ ]:





# In[ ]:




