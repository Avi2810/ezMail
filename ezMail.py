

from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib





class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(481, 471)
        main.setMinimumSize(QtCore.QSize(481, 471))
        main.setMaximumSize(QtCore.QSize(481, 471))
        main.setStyleSheet("\n"
"")

        main.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 481, 471))
        self.frame.setStyleSheet("QFrame{background-color: rgb(43, 5, 43);}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.l_from = QtWidgets.QLabel(self.frame)
        self.l_from.setGeometry(QtCore.QRect(70, 110, 41, 20))
        self.l_from.setObjectName("l_from")
        self.l_passw = QtWidgets.QLabel(self.frame)
        self.l_passw.setGeometry(QtCore.QRect(50, 140, 61, 20))
        self.l_passw.setObjectName("l_passw")
        self.fld_from = QtWidgets.QLineEdit(self.frame)
        self.fld_from.setGeometry(QtCore.QRect(140, 110, 221, 20))
        self.fld_from.setStyleSheet("QLineEdit{background-color: rgb(209, 209, 209);}\n"
"QLineEdit{border:1px}\n"
"QLineEdit{border-radius:10px}\n"
"")
        self.fld_from.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_from.setObjectName("fld_from")
        self.fld_passw = QtWidgets.QLineEdit(self.frame)
        self.fld_passw.setGeometry(QtCore.QRect(140, 140, 221, 20))
        self.fld_passw.setStyleSheet("QLineEdit{background-color: rgb(209, 209, 209);}\n"
"QLineEdit{border:1px}\n"
"QLineEdit{border-radius:10px}\n"
"")
        self.fld_passw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.fld_passw.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_passw.setObjectName("fld_passw")
        self.l_to = QtWidgets.QLabel(self.frame)
        self.l_to.setGeometry(QtCore.QRect(80, 180, 31, 20))
        self.l_to.setObjectName("l_to")
        self.fld_to = QtWidgets.QLineEdit(self.frame)
        self.fld_to.setGeometry(QtCore.QRect(140, 180, 221, 20))
        self.fld_to.setStyleSheet("QLineEdit{background-color: rgb(209, 209, 209);}\n"
"QLineEdit{border:1px}\n"
"QLineEdit{border-radius:10px}\n"
"")
        self.fld_to.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_to.setObjectName("fld_to")
        self.mail = QtWidgets.QTextEdit(self.frame)
        self.mail.setGeometry(QtCore.QRect(110, 280, 271, 121))
        self.mail.setStyleSheet("QTextEdit{background-color: rgb(209, 209, 209);}\n"
"QTextEdit{border:1px;border-radius:5px}\n"
"")
        self.mail.setObjectName("mail")
        self.l_passw_2 = QtWidgets.QLabel(self.frame)
        self.l_passw_2.setGeometry(QtCore.QRect(110, 240, 121, 20))
        self.l_passw_2.setObjectName("l_passw_2")
        self.btn_submit = QtWidgets.QPushButton(self.frame)
        self.btn_submit.setGeometry(QtCore.QRect(280, 240, 75, 23))
        self.btn_submit.setStyleSheet("QPushButton{background-color: rgb(209, 209, 209);}\n"
"QPushButton{border:1px;border-radius:5px}")
        self.btn_submit.setObjectName("btn_submit")
        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setGeometry(QtCore.QRect(140, 30, 211, 41))
        self.logo.setObjectName("logo")
        self.credit = QtWidgets.QLabel(self.frame)
        self.credit.setGeometry(QtCore.QRect(310, 450, 171, 20))
        self.credit.setObjectName("credit")
        self.error_msg = QtWidgets.QLabel(self.frame)
        self.error_msg.setGeometry(QtCore.QRect(190, 420, 111, 20))
        self.error_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.error_msg.setObjectName("error_msg")
        main.setCentralWidget(self.centralwidget)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

        self.btn_submit.clicked.connect(self.send_mail)
    
    
    
    def cli_cked(self):
        
        print(self.fld_from.text())
        print(self.fld_passw.text())
        print(self.fld_to.text())
        print(self.mail.toPlainText())
        self.fld_from.clear()
        self.fld_passw.clear()
        self.fld_to.clear()
        self.mail.clear()





    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "ezMail"))
        self.l_from.setText(_translate("main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#b9b0b2;\">Email</span></p></body></html>"))
        self.l_passw.setText(_translate("main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#b9b0b2;\">Password</span></p></body></html>"))
        self.l_to.setText(_translate("main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#b9b0b2;\">To</span></p></body></html>"))
        self.l_passw_2.setText(_translate("main", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#b9b0b2;\">Type Your Message</span></p></body></html>"))
        self.btn_submit.setText(_translate("main", "Send"))
        self.logo.setText(_translate("main", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#eaeaea;\">ezMail</span></p></body></html>"))
        self.credit.setText(_translate("main", "<html><head/><body><p><span style=\" color:#d1d1d1;\">created By- Abhishek Chakraborty</span></p></body></html>"))
        self.error_msg.setText(_translate("main", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#d1d1d1;\"></span></p></body></html>"))


    #3######################################################################################################
    ######################################################################################################
    def send_mail(self):

        _translate = QtCore.QCoreApplication.translate
        self.error_msg.setText(_translate("main", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#d1d1d1;\">sending</span></p></body></html>"))


        sender = self.fld_from.text()
        pass_word = self.fld_passw.text()
        receivers = [self.fld_to.text()]
        
        #message = """From: From Python <abhishekabhishek13001316@gmail.com>
        #To: To Abhishek <mynameavi2801@gmail.com>
        #Subject: SMTP e-mail test

        #This is a test e-mail message.
        #"""
        message = self.mail.toPlainText()


        self.fld_from.clear()
        self.fld_passw.clear()
        self.fld_to.clear()
        self.mail.clear()


        
        try:
            server= smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, pass_word)
            print("Login success....")
            server.sendmail(sender, receivers, message)      

            print("Successfully sent email")

            #_translate = QtCore.QCoreApplication.translate
            self.error_msg.setText(_translate("main", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#d1d1d1;\">sending</span></p></body></html>"))


        except:
            print("Error: unable to send email")

            _translate = QtCore.QCoreApplication.translate
            self.error_msg.setText(_translate("main", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#d1d1d1;\">Error !</span></p></body></html>"))


##############################################################################################################
##############################################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
