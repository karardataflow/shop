import sys 
from PySide6.QtWidgets import QSpinBox, QMainWindow, QPushButton, QGridLayout, QFrame, QVBoxLayout, QLabel , QLineEdit
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QSize


class MyView(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller

        self.setGeometry(100, 200, 800, 1000)

        main_frame = QFrame()
        main_frame.setStyleSheet(
            """background-color: #fff"""
        )
        layout = QGridLayout(main_frame)

        label_frame = QFrame()
        label_frame_layout = QVBoxLayout(label_frame)
        label_frame.setStyleSheet("""
                                  background-color: #1A3654; 
                                  color: white;
                                  background-image: url('./static/لنكيدو Market.png');
                                  background-repeat: no-repeat;
                                  background-position: center;
                                  """)
        label_frame.setFixedHeight(100)
        label_frame.setGeometry(0, 0, 800, 1000)

        
        

        



        layout.addWidget(label_frame, 0, 0)

        self.setCentralWidget(main_frame)

        frame = QFrame()
        frame_layout = QGridLayout(frame)
        layout.addWidget(frame, 1, 0)

        icon = QIcon('./static/Untitled (4).png')

        # Button 1
        button1 = QPushButton()
        button1.clicked.connect(controller.show_list)
        button1.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 1.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button1.setIcon(icon)
        button1.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button1, 0, 0)

        # Button 2
        button2 = QPushButton()
        button2.clicked.connect(controller.show_sales)
        button2.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 2.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button2.setIcon(icon)
        button2.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button2, 0, 1)

        # Button 3
        button3 = QPushButton()
    
        button3.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 3.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button3.setIcon(icon)
        button3.clicked.connect(controller.show_Purchases)
        button3.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button3, 0, 2)

        # Button 4
        button4 = QPushButton()
        button4.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 4.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button4.setIcon(icon)
        button4.clicked.connect(controller.show_Deferred)
        button4.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button4, 1, 0)

        # Button 5
        button5 = QPushButton()
        button5.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 5.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button5.setIcon(icon)
        button5.clicked.connect(controller.show_materials)
        button5.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button5, 1, 1)

        # Button 6
        button6 = QPushButton()
        button6.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 6.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button6.setIcon(icon)
        button6.clicked.connect(controller.show_closet)       
        button6.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button6, 1, 2)

        # Button 7
        button7 = QPushButton()
        button7.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-repeat: no-repeat;
                background-image: url('./static/Group 7.png');
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button7.setIcon(icon)
        button7.clicked.connect(controller.show_closet) 
        button7.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button7, 2, 0)


class Lists(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("القوائم")
        self.resize(500, 500)

        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)

        new_layout.addWidget(lest_label_frame, 0, 0 , 1 , 0)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 1)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/09.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)

        # إضافة نص في Layout2 (Layout الفريم)
        label = QLabel("السعر")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        layout2.addWidget(label, 0, 1)  # إضافة النص في المكان المناسب
         
        self.name = QSpinBox()
        self.name.setStyleSheet("""
                               border-radius: 4px;
                    background: #fff;
                                
                                
                                """)


        layout2.addWidget(self.name,0,0)



        label = QLabel("أسم الشركة")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        layout2.addWidget(label, 0, 2)  # إضافة النص في المكان المناسب
         
        self.name = QSpinBox()
        self.name.setStyleSheet("""
                               border-radius: 4px;
                    background: #fff;
                                
                                
                                """)


        layout2.addWidget(self.name, 0, 3)


                        
        label = QLabel("التاريخ والوقت")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        layout2.addWidget(label,1, 1 )  # إضافة النص في المكان المناسب
         
        self.name = QSpinBox()
        self.name.setStyleSheet("""
                               border-radius: 4px;
                    background: #fff;
                                
                                
                                """)


        layout2.addWidget(self.name,1, 0)             
                       
        label = QLabel("رقم القائمة ")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        layout2.addWidget(label,2, 1)  # إضافة النص في المكان المناسب
         
        self.name = QSpinBox()
        self.name.setStyleSheet("""
                               border-radius: 4px;
                    background: #fff;
                                
                                
                                """)


        layout2.addWidget(self.name,2, 0)















       


class Sales(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("المبيعات")
        self.resize(500, 500)


class Purchases(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("المشتريات")
        self.resize(500, 500)

#4


class Deferred(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("دفع مؤجل")
        self.resize(500, 500)




class  Materials(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("اضافة مواد")
        self.resize(500, 500)





class Closet(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("المخزن")
        self.resize(500, 500)






class Data_analysis(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تحليل")
        self.resize(500, 500)

