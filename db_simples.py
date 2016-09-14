import PyQt5,janelinha1,sys,sqlite3





aux='db.db'
db=janelinha1.db_class(aux)
janelinha1.db=db



app=PyQt5.QtWidgets.QApplication(sys.argv)


ui=janelinha1.janelinha1()
ui.show()
sys.exit(app.exec_())

