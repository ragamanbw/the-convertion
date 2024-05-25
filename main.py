import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *


class HalamanAwal(QtWidgets.QMainWindow):
    def __init__(self):
        super(HalamanAwal, self).__init__()
        uic.loadUi("Halaman Awal.ui", self)
        #mennghubungkan file ui yang telah dibuat pada Qt designer

        # mendefinisikan tombol yang ada pada tampilan
        self.pushButton_Mulai = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton_Keluar = self.findChild(QtWidgets.QPushButton, 'pushButton_2')

        #menghubungkan tombol yang ada pada fungsi yang sudah dibuat
        self.pushButton_Mulai.clicked.connect(self.goToPerhitungan)
        self.pushButton_Keluar.clicked.connect(self.keluarAplikasi)



    def goToPerhitungan(self):
        self.halamanPerhitungan = HalamanPerhitungan()
        self.halamanPerhitungan.show()
        self.close()
    #membuat fungsi untuk berpindah ke halaman perhitungan dan menutup tampilan awal


    def keluarAplikasi(self):
        self.close()
    # membuat fungsi keluar aplikasi
class HalamanPerhitungan(QtWidgets.QMainWindow):
    def __init__(self):
        super(HalamanPerhitungan, self).__init__()
        uic.loadUi("Halaman Perhitungan.ui", self)
        self.pushButton_Hitung_Hasil = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.pushButton_Hitung_Keluar = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.lineEdit_input = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.comboBox_Satuan = self.findChild(QtWidgets.QComboBox, 'comboBox')
        self.comboBox_Satuan.addItems(["Waktu","Panjang","Massa", "Arus Listrik", "Suhu", "Jumlah_Zat", "Intensitas Cahaya"])
        #membuat item satuan yang dapat dipilij
        self.pushButton_Hitung_Hasil.clicked.connect(self.hitung_konversi)
        self.pushButton_Hitung_Keluar.clicked.connect(self.keluarHalamanPerhitungan)

    def keluarHalamanPerhitungan(self):
        self.halamanPerhitungan = HalamanAwal()
        self.halamanPerhitungan.show()
        self.close()
    def hitung_konversi(self):
        try:
            nilai_yang_diinput = float(self.lineEdit_input.text())
            satuan_dipilih = self.comboBox_Satuan.currentText()
            hasil = 0
            simbol_satuan = ""
            #membuat variabel yang dibutuhkan

            if satuan_dipilih == "Waktu":
                hasil = nilai_yang_diinput * 60
                simbol_satuan = "s"
            elif satuan_dipilih == "Panjang":
                hasil = nilai_yang_diinput / 1000
                simbol_satuan = "m"
            elif satuan_dipilih == "Massa":
                hasil = nilai_yang_diinput * 1000
                simbol_satuan = "kg"
            elif satuan_dipilih == "Arus Listrik":
                hasil = nilai_yang_diinput * 1000
                simbol_satuan = "A"
            elif satuan_dipilih == "Suhu":
                hasil = (nilai_yang_diinput * 9/5) + 32
                simbol_satuan ="K"
            elif satuan_dipilih == "Jumlah_Zat":
                hasil = nilai_yang_diinput * 6.022e23
                simbol_satuan = "mol"
            elif satuan_dipilih == "Intensitas Cahaya":
                hasil = nilai_yang_diinput * 12.57
                simbol_satuan = "cd"

            message = f"Hasil konversi: {hasil} {simbol_satuan}"
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Hasil Konversi")
            msgBox.setText(message)
            msgBox.setIcon(QMessageBox.Information)
            #tampilan message box
            msgBox.setStyleSheet("QMessageBox {"
                                 "background-color: grey;"
                                 "color: #DDD;"
                                 "font: bold 14px; }"
                                 "QPushButton {"
                                 "color: #282828;"
                                 "background-color: orange;"
                                 "border-radius: 5px; }"
                                 "QPushButton:hover {"
                                 "background-color: #A0A0A0; }")
            msgBox.exec_()

        except ValueError:
            QMessageBox.warning(self, "Error", "Input harus berupa angka.")
        # menampilkan pesan error




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = HalamanAwal()
    window.show()
    sys.exit(app.exec_())