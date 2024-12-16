import sys 

from PySide6.QtWidgets import QApplication ,QMainWindow , QPushButton, QGridLayout, QFrame ,QLabel
from PySide6.QtGui import QIcon , QAction ,QPixmap
from PySide6.QtCore import Qt


a= QApplication(sys.argv)
#الشاشه

s = QMainWindow()
s.setGeometry(100, 200, 800, 1000)

#الفريم الاعلى 

frem = QFrame(s)
frem.setStyleSheet("background-color: #1A3654; color: white;")
frem.setFixedHeight(100)
frem.setFixedWidth(800)
frem.setGeometry(0,0,800,1000)


lebl = QLabel( frem)
icon = QPixmap("lnk.png")
lebl.setPixmap(icon)
lebl.setAlignment(Qt.AlignCenter ) 
lebl.setStyleSheet("background-color: #1A3654; color: white;")


leut = QGridLayout (frem)
leut.addWidget(lebl)



#الزر
frame = QFrame(s)

s.setCentralWidget(frame)

layout = QGridLayout(frame)


butn1 = QPushButton ("")
layout.addWidget(butn1,0,0)
butn1.setStyleSheet("background-image: url('1.1.png') ")  
butn1.setFixedSize(150, 150)



butn2= QPushButton("")
layout.addWidget(butn2,0,1)
butn2.setStyleSheet("background-image: url('1.1.png') ")  
butn2.setFixedSize(150, 150)




butn3 = QPushButton ("")
layout.addWidget(butn3,0,2)
butn3.setStyleSheet("background-image: url('1.1.png') ")  
butn3.setFixedSize(150, 150)



butn4 = QPushButton ("")
layout.addWidget(butn4,1,0)
butn4.setStyleSheet("background-image: url('1.1.png') ")  
butn4.setFixedSize(150, 150)



butn5 = QPushButton ("")
layout.addWidget(butn5,1,1)
butn5.setStyleSheet("background-image: url('1.1.png') ")  
butn5.setFixedSize(150, 150)



butn6 = QPushButton ("")
layout.addWidget(butn6,1,2)
butn6.setStyleSheet("background-image: url('1.1.png') ")  
butn6.setFixedSize(150, 150)




butn7 = QPushButton ("")
layout.addWidget(butn7,2,0)
butn7.setStyleSheet("background-image: url('1.1.png') ")  
butn7.setFixedSize(150, 150)












s.show()
sys.exit(a.exec_())
