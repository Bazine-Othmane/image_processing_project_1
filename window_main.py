import sys
from PyQt5 import QtWidgets ,QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from PIL import Image
from PIL.ImageQt import ImageQt
import numpy as np

from main import *

class window(QDialog): 
      
    def __init__(self):
        super(window, self).__init__()
        
        loadUi('projet.ui',self)
        self.imgpath=""
        test= QPixmap('./image/image.png').scaled(200,200)
        self.label1.setPixmap(test)
        self.label2.setPixmap(test)
        self.btn2.setIcon(QIcon('image/arrow.png'))
        self.btn2.setIconSize(QtCore.QSize(35,35))
        self.btn1.clicked.connect(self.browseimage) 
        self.btn4.clicked.connect(self.save) 
        self.btn5.clicked.connect(self.plt) 
        self.btn3.clicked.connect(self.process) 
        self.btn2.clicked.connect(self.switch) 
        self.rd4.toggled.connect(self.enable)
        self.rd6.toggled.connect(self.enable)
        self.rd7.toggled.connect(self.enable)
        self.rd8.toggled.connect(self.enable)
        self.test=QtWidgets.QPushButton('test',self)
        

    def process(self) : 
        
#---------------------------------------------------------------------------------------------------          
         if (self.rd1.isChecked() == True): #rgb to gray scale (question 1)
            if(type(self.imgpath)== str) :
                image= Image.open(self.imgpath) 
                self.rgb_to_gray(image)
            else :  self.rgb_to_gray(self.imgpath)
#---------------------------------------------------------------------------------------------------          
         if (self.rd2.isChecked() == True): #hsv to gray scale  (question 2)
             if(type(self.imgpath)== str) :
                 image= Image.open(self.imgpath) 
                 self.hsv_to_gray(image)
             else :  self.hsv_to_gray(self.imgpath)        
#---------------------------------------------------------------------------------------------------          
         if (self.rd3.isChecked() == True): #rgb to hsv (question 3)
             if(type(self.imgpath)== str) :
                 image= Image.open(self.imgpath) 
                 self.rgb_to_hsv(image)
             else : self.rgb_to_hsv(self.imgpath)   
#--------------------------------------------------------------------------------------------------          
         if (self.rd4.isChecked() == True): #Quantize image (question 4)
           if(type(self.imgpath)== str) :
                 image= Image.open(self.imgpath) 
                 self.Quantize(image)
           else : self.Quantize(self.imgpath)                     
#---------------------------------------------------------------------------------------------------          
         if (self.rd5.isChecked() == True): #histogram of image (question 5)
             if(type(self.imgpath)== str) :
                 image= Image.open(self.imgpath) 
                 self.hist(image)
             else :self.hist(self.imgpath)
#---------------------------------------------------------------------------------------------------          
         if (self.rd6.isChecked() == True): #adjust image dynamic (question 6)
            if(type(self.imgpath)== str) :
                 image= Image.open(self.imgpath) 
                 self.image_dynamic(image)
            else :self.image_dynamic(self.imgpath)
#---------------------------------------------------------------------------------------------------          
         if (self.rd7.isChecked() == True): # histogram equalization (question 7)
             if(type(self.imgpath)== str) :
                 image= Image.open(self.imgpath) 
                 self.hist_qual(image)
             else :self.hist_qual(self.imgpath)
#---------------------------------------------------------------------------------------------------          
         if (self.rd8.isChecked() == True): # Remove noise (question 8)
             if(type(self.imgpath)== str) :
                 image= Image.open(self.imgpath) 
                 self.noise(image)
             else :self.noise(self.imgpath)
         

    def enable(self): # enable and desable of button , combobox....ect
        if (self.rd4.isChecked() == True):
            self.cmb1.setEnabled(True)
            self.cmb2.setEnabled(False)
            self.spinbox1.setEnabled(False)
            self.spinbox2.setEnabled(False)
            self.spinbox3.setEnabled(False)
        elif (self.rd8.isChecked() == True): 
            self.cmb2.setEnabled(True)
            self.cmb1.setEnabled(False)
            self.spinbox1.setEnabled(False)
            self.spinbox2.setEnabled(False)
            self.spinbox3.setEnabled(False)
        elif (self.rd6.isChecked() == True): 
            self.cmb1.setEnabled(False)
            self.cmb2.setEnabled(False)
            self.spinbox1.setEnabled(True)
            self.spinbox2.setEnabled(True)
            self.spinbox3.setEnabled(False)
        elif (self.rd7.isChecked() == True): 
            self.cmb1.setEnabled(False)
            self.cmb2.setEnabled(False)
            self.spinbox1.setEnabled(False)
            self.spinbox2.setEnabled(False)
            self.spinbox3.setEnabled(True)
        else :
            self.cmb1.setEnabled(False)
            self.cmb2.setEnabled(False)
            self.spinbox1.setEnabled(False)
            self.spinbox2.setEnabled(False)
            self.spinbox3.setEnabled(False)


    def browseimage(self): #function for open an image from the PC
     
     try:
      
      fname = QtWidgets.QFileDialog.getOpenFileName(self,'open file', 'C:/', 'image file (*.jpg *.png)')
      if (fname[0]!=""): 
          self.hsv=""
          self.imgpath=fname[0]
          self.enable_rd(True)
      im = Image.open(self.imgpath) 
      if (im.size[0]>im.size[1]): im=im.resize((400,int((im.size[1]/im.size[0])*400)))
      else :  im=im.resize((int((im.size[0]/im.size[1])*400),400))
      image0= QPixmap(self.imgpath).scaled(im.size[0],im.size[1])
      self.label1.setPixmap(image0)
      self.label1.setAlignment(Qt.AlignCenter)
      self.btn3.setEnabled(True)
      self.btn3.setStyleSheet("background: #ffa31a  ; border-radius: 10px ; ")
     except :
        x= "eror\n'Choose another picture' "
        self.label2.setText(x)
        self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");
                 
      
    def rgb_to_gray(self, image_rgb): #rgb to gray scale (question 1)
        try :    
            
            rgb_gray=rgbTOgray(image_rgb) #function convert rgb to gray (in main.py file)
            pix=self.pil2pixmap(rgb_gray) #function convert PIL Image to Pixmap image
            self.label2.setPixmap(pix)  
            self.label2.setAlignment(Qt.AlignCenter) 
            self.active()  #function for active the buttons
            self.hsv=rgb_gray
            
            
        except :
            x= "The picture is completely gray scale\n'Choose another picture' "
            self.label2.setText(x)
            self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");
    

    def hsv_to_gray(self,image):#hsv to gray scale (question 2)
     try:
        if(image.mode=='RGB') : image=IMAGE_HSV(image)      
        hsv_gray= HSV_GRAY(image)
        pix=self.pil2pixmap(hsv_gray) #function convert PIL Image to Pixmap image
        self.label2.setPixmap(pix)
        self.label2.setAlignment(Qt.AlignCenter) 
        self.active() #function for active the buttons
        self.btn2.setEnabled(False)
        self.btn2.setStyleSheet("background: #C0C0C0  ; border-radius: 10px ; ")
        self.btn4.setEnabled(False)
        self.btn4.setStyleSheet("background: #C0C0C0  ; border-radius: 10px ; ")
        self.hsv=hsv_gray
        
     except :
        x= "The picture is completely gray scale\n'Choose another picture' "
        self.label2.setText(x)
        self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");


    def rgb_to_hsv(self,image): #rgb to hsv  (question 3)
     try:
        
        rgb_hsv=IMAGE_HSV(image) #function convert rgb to hsv (in main.py file)
        self.hsv=rgb_hsv
        pix=self.pil2pixmap(rgb_hsv)#function convert PIL Image to Pixmap image
        self.label2.setPixmap(pix)
        self.label2.setAlignment(Qt.AlignCenter) 
        self.active()#function for active the buttons
        self.btn4.setStyleSheet("background: #C0C0C0  ; border-radius: 10px ; ")
        self.btn4.setEnabled(False)
        
        
     except :
        x= "The picture is completely gray scale\n'Choose another picture' "
        self.label2.setText(x)
        self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");

    
    def Quantize(self, image): #Quantize image (question 4) 
     try :
        array= np.array(["Given range","0,1,3,...,119,...,253,255","0,3,7,...,119,...,251,255","0,7,15,..,119,..,247,255","0,15,31,..,111,..,239,255","0,31,63,..,127,..,223,255","0,63,127,255","0,127,255","0,255"])
        content= self.cmb1.currentText()
        index =np.where(array == content)
        index=int(index[0])
        if (index ==0):    
            x= "choose given range "
            self.label2.setText(x)
            self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");
        else :
            if(index ==1) : quantize_list =np.arange(1,256,2)
            if(index ==2) : quantize_list =np.arange(3,256,4)
            if(index ==3) : quantize_list =np.arange(7,256,8)
            if(index ==4) : quantize_list =np.arange(15,256,16)
            if(index ==5) : quantize_list =np.arange(31,256,32)
            if(index ==6) : quantize_list =np.arange(63,256,64)
            if(index ==7) : quantize_list =np.array([127,255])
            if(index ==8) : quantize_list =np.array([255])
            quantize_list =np.insert(quantize_list,0,0)

            im= Quantize_image(image, quantize_list) #function quantize image into a different levels (in main.py file)
            pix=self.pil2pixmap(im) #function convert PIL Image to Pixmap image
            self.label2.setPixmap(pix)
            self.label2.setAlignment(Qt.AlignCenter) 
            self.active() #function for active the buttons
            self.hsv=im
     except :
        x= "eror\n'Choose another picture' "
        self.label2.setText(x)
        self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");
      
      
    def hist(self,image) : #histogram of image (question 5)
      try: 
          im= histogram(image)  #function Extract histogram of image (in main.py file)
          pix=self.pil2pixmap(im)
          self.label2.setPixmap(pix)
          self.label2.setAlignment(Qt.AlignCenter) 
          self.active()
          self.btn2.setEnabled(False)
          self.btn2.setStyleSheet("background: #C0C0C0  ; border-radius: 10px ; ")
          self.hsv=im  
      except :
          x= "eror\n'Choose another picture' "
          self.label2.setText(x)
          self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");
    

    def image_dynamic(self,image) :#adjust image dynamic (question 6) 
     try :
       value1 = self.spinbox1.value()
       value2 = self.spinbox2.value()
       if (value1 >= value2 ):
        x= "'min range' cannot be greater \nthan the 'max range'\n\n\nChoose other numbers "
        self.label2.setText(x)
        self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");
       else: 
            im= improve_contrast(image, value1 , value2 )  #function improve image contrast (in main.py file)
            pix=self.pil2pixmap(im) #function convert PIL Image to Pixmap image
            self.label2.setPixmap(pix)
            self.label2.setAlignment(Qt.AlignCenter) 
            self.active()
            self.hsv=im
     except :
       
        x= "eror\n'Choose another picture' "
        self.label2.setText(x)
        self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");


    def hist_qual(self ,image):# histogram equalization (question 7)
      try : 
          value = self.spinbox3.value()
          im=histogram_equalization(image,value)   #function Apply histogram equalization on the input image (in main.py file)
          pix=self.pil2pixmap(im)
          self.label2.setPixmap(pix)
          self.label2.setAlignment(Qt.AlignCenter) 
          self.active()
          self.hsv=im  
      except :
          x= "eror\n'Choose another picture' "
          self.label2.setText(x)
          self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");
    

    def noise(self,image) : # Remove noise (question 8)
      try :
        array= np.array(["Filter matrix","3 * 3","5 * 5","7 * 7","9 * 9","11 * 11"])
        content= self.cmb2.currentText()
        index =np.where(array == content)
        index=int(index[0])
        if (index == 0):    
            x= "choose filter for matrix"
            self.label2.setText(x)
            self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");
        else : 
            if (index ==1):filt=3
            if (index ==2):filt=5
            if (index ==3):filt=7
            if (index ==4):filt=9
            if (index ==5):filt=11
            im= IMAGE_NOISE(image, filt)   #function remove noise from image (in main.py file)
            pix=self.pil2pixmap(im)
            self.label2.setPixmap(pix)
            self.label2.setAlignment(Qt.AlignCenter) 
            self.active()
            self.hsv=im
        
      except :
        x= "eror\n'Choose another picture' "
        self.label2.setText(x)
        self.label2.setStyleSheet("border-radius: 10px;color: rgb(255, 0, 0);font: 16pt ;text-align: center;background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));");
      

    def pil2pixmap(self, im): #function convert PIL Image to Pixmap image
      x=len(np.array(im).shape)
      if (im.size[0]>im.size[1]): im=im.resize((400,int((im.size[1]/im.size[0])*400)))
      else :  im=im.resize((int((im.size[0]/im.size[1])*400),400))
      
      if(x==2): 
         qim = ImageQt(im)
         img = QPixmap.fromImage(qim)
         pixmap= QPixmap(img)
      else: 
            im = im.convert("RGB")
            data = im.tobytes()
            qim = QtGui.QImage(data, im.size[0], im.size[1], 13)
            pixmap =QPixmap.fromImage(qim)
      return pixmap  


    def plt(self):#function for show image in matplotlib
            plt.imshow(self.hsv,cmap='gray', vmin = 0, vmax = 255)
            plt.show()
        
 
    def active(self) : #function for active the buttons
        self.btn2.setEnabled(True)
        self.btn2.setStyleSheet("background: #ffa31a  ; border-radius: 10px ; ")
        self.btn4.setEnabled(True)
        self.btn4.setStyleSheet("background: #ffa31a  ; border-radius: 10px ; ")
        self.btn5.setEnabled(True)
        self.btn5.setStyleSheet("background: #ffa31a  ; border-radius: 10px ; ")


    def save(self): 
        try:
         file= QtWidgets.QFileDialog.getSaveFileName(self, 'Save', "E:/default" , "image file (*.jpg *.png)")
         self.hsv.save(file[0])
        except :
            print()

    def enable_rd(self,boolen):
        self.rd1.setEnabled(boolen)
        self.rd3.setEnabled(boolen)
        self.rd4.setEnabled(boolen)
        self.rd5.setEnabled(boolen)
        self.rd6.setEnabled(boolen)
        self.rd7.setEnabled(boolen)
        self.rd8.setEnabled(boolen)
        if(boolen == False) :self.rd2.setChecked(True)

    def switch(self):
       test= QPixmap('E:\\programming\\python\\image\\image\\image').scaled(200,200)
       self.label2.setPixmap(test) 
       pix=self.pil2pixmap(self.hsv)
       self.label1.setPixmap(pix)
       self.label1.setAlignment(Qt.AlignCenter) 
       self.imgpath= self.hsv
       if (self.hsv.mode=="HSV") :
          self.enable_rd(False)

    

app= QApplication(sys.argv)
window=window()

widgt= QtWidgets.QStackedWidget()
widgt.addWidget(window)
widgt.move(100,50)
widgt.setFixedSize(1200,600)
widgt.setWindowTitle("IMAGE PRCESSING")
widgt.setWindowIcon(QtGui.QIcon("./image/icon.png"))
widgt.show()
app.exec_()
