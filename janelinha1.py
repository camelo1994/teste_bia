# -*- coding: utf-8 -*-

"""
Module implementing janelinha1.
"""

import sqlite3
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_formulario1 import Ui_Form


class db_class:
    def __init__(self,file):
        self.data=sqlite3.connect(file)
        self.cursor=self.data.cursor()
        self.update()


    def execute(self,line):
        self.cursor.execute(line)
        return self.cursor.fetchall()

    def commit(self):
        self.data.commit()
        self.update()

    def update(self):
        self.cursor.execute("SELECT * FROM sqlite_sequence WHERE name='clientela'")
        a=self.cursor.fetchall()
        self.seq=a[0][1]


db=None


class janelinha1(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(janelinha1, self).__init__(parent)
        self.setupUi(self)
        self.spinBox.setMaximum(db.seq)
    
    @pyqtSlot()#qa
    def on_pushButton_READ_clicked(self):
        print("Apertei bota READ")
        id=self.spinBox.value()

        aux='SELECT * FROM clientela WHERE id='+str(id)
        lista=db.execute(aux)

        a=lista[0]
        self.label_2.setText("Nome do pai: "+str(a[1]))
        self.label_3.setText("Tem medo de: "+str(a[2]))
        self.label_4.setText("Tamanho do pai: "+str(a[3]))

    
    @pyqtSlot()
    def on_pushButton_ADD_clicked(self):
       print("Apertei bota ADD")
       nome=str(self.lineEdit.text())
       medo=str(self.lineEdit_2.text())
       tamanho=self.lineEdit_3.text()


       aux="INSERT INTO clientela (name,xabs,sizea) VALUES ('" +nome+ "','" +medo+ "',"+str(tamanho)+")"
       db.execute(aux)
       db.commit()

       self.label_Feedback.setText("Added into sequence:"+str(db.seq))


