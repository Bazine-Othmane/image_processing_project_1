from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math
import statistics as st
import cv2


def rgbTOgray(image) :#function convert rgb to gray
  
    rgb= np.array(image)
    r, g, b = rgb[:,:,0].copy(), rgb[:,:,1].copy(), rgb[:,:,2].copy()
    
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    gray = gray.astype(np.uint8)
    gray= Image.fromarray(gray)
    gray=Image.merge('L',(gray,))
    return gray


def HSV_GRAY(image):#function convert hsv to gray
    hsv=np.array(image)
    h ,s ,v = hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]
    h,s,v= (h/255)*360,s/255,v/255
    
    delta= s*v
    x= delta*(1-abs(((h/60)%2)-1))
    rgb_min=v-delta

    R_r , G_g , B_b =delta.copy(),delta.copy() ,delta.copy()
    R_x , G_x , B_x =x.copy(), x.copy() ,x.copy()
    R_r[(h>=60) & (h<300)]=0
    G_g[(h>=180) | (h<60)]=0
    B_b[(h>=300) | (h<180)]=0
    R_x[((h>=120) & (h<240)) |  (h<60) | (h>=300)]=0
    G_x[((h>=60) & (h<180)) | ((h<360)& (h>=240))]=0
    B_x[((h>=0)& (h<120)) | ((h<300) & (h>=180))]=0
    R=np.around((R_r + R_x + rgb_min)*255).astype(np.uint8)
    G=np.around((G_g + G_x + rgb_min)*255).astype(np.uint8)
    B=np.around((B_b+ B_x + rgb_min)*255).astype(np.uint8)
    v = 0.2989 * R + 0.5870 * G + 0.1140 * B
    v=v.astype(np.uint8)
   
    h,s,v= Image.fromarray(v*0),Image.fromarray(v*0),Image.fromarray(v)
    image=Image.merge('HSV',(h,s,v))
    return image


def IMAGE_HSV(image) :#function convert image rgb to hsv 
  
  rgb= np.array(image)
  rgb=(rgb/255)
  r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
  R, G, B =  r.copy(), g.copy(), b.copy()
  R1, G1, B1 =  r.copy(), g.copy(), b.copy()
  rgb_max= np.maximum(R,G).copy()
  max_rgb=np.maximum(rgb_max,B).copy()
  rgb_min= np.minimum(R1,G1).copy()
  min_rgb=np.minimum(rgb_min,B1).copy()
  delta= max_rgb - min_rgb
  delta[delta == 0]=-1
  x=(((g-b)/delta +6)%6)/6 
  y=((b-r)/delta +2)/6
  z=((r-g)/delta +4)/6 
  delta=max_rgb - min_rgb
  x[(max_rgb != r) | (x == y)]=0
  y[(max_rgb != g) | (y == z)]=0
  z[(max_rgb != b) | (x == z)]=0
  HUE=x+y+z
  SATURATION = delta/max_rgb
  VALUE= max_rgb
  HUE,SATURATION,VALUE=(HUE* 255).astype(np.uint8),(SATURATION* 255).astype(np.uint8),(VALUE* 255).astype(np.uint8)
  HUE[HUE==255]=0
  HUE[delta==0]=0
  h,s,v= Image.fromarray(HUE),Image.fromarray(SATURATION),Image.fromarray(VALUE)
  image=Image.merge('HSV',(h,s,v))
  return image


def Quantize_image ( image ,quantize_list): #function quantize image into a different levels
  rgb= np.array(image)
  if (len(rgb.shape)==3): 
    r, g, b = rgb[:,:,0].copy(), rgb[:,:,1].copy(), rgb[:,:,2].copy()
    if(len(quantize_list)==2):
        r[r[:]<128]=0
        r[127<r[:]]=255
        g[g[:]<128]=0
        g[127<g[:]]=255
        b[b[:]<128]=0
        b[127<b[:]]=255
    else:
      r[r[:]<=quantize_list[0]]=quantize_list[0]
      r[quantize_list[-1]<r[:]]=quantize_list[-1]
      g[g[:]<=quantize_list[0]]=quantize_list[0]
      g[quantize_list[-1]<g[:]]=quantize_list[-1]
      b[b[:]<=quantize_list[0]]=quantize_list[0]
      b[quantize_list[-1]<b[:]]=quantize_list[-1]
      for i in range(len(quantize_list)-1) :
        r[(quantize_list[i]<r[:]) & (r[:]<quantize_list[i+1])]=quantize_list[i+1]
        g[(quantize_list[i]<g[:]) & (g[:]<quantize_list[i+1])]=quantize_list[i+1]
        b[(quantize_list[i]<b[:]) & (b[:]<quantize_list[i+1])]=quantize_list[i+1]
    r,g,b= Image.fromarray(r),Image.fromarray(g),Image.fromarray(b)
    image=Image.merge('RGB',(r,g,b))
    return image
  else: 
    gray= rgb.copy()
    if(len(quantize_list)==2):
       gray[gray[:]<128]=0
       gray[127<gray[:]]=255
    else:
      gray[gray[:]<=quantize_list[0]]=quantize_list[0]
      gray[quantize_list[-1]<gray[:]]=quantize_list[-1]
      for i in range(len(quantize_list)-1) :
          gray[(quantize_list[i]<gray[:]) & (gray[:]<quantize_list[i+1])]=quantize_list[i+1]
    gray= Image.fromarray(gray)
    return gray 


def histogram(image):#function Extract histogram of image 
  fig=plt.figure()
  hist, bins = np.histogram(image, bins=50)
  plt.bar(bins[:-1], hist,width=4)
  fig.canvas.draw()
  image= Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb()) 
  plt.close(fig)
  return image


def improve_contrast (image ,min_intensity,max_intensity):#function improve image contrast
  rgb=np.array(image)
  if(len(rgb.shape)==3): 
    r, g, b = rgb[:,:,0].copy(), rgb[:,:,1].copy(), rgb[:,:,2].copy()
    a=(max_intensity -min_intensity)/(np.max(r)-np.min(r))
    c=(np.max(r)*min_intensity - np.min(r)*max_intensity)/(max_intensity -min_intensity)
    r=(a*np.array(r)+c).astype(np.uint8)

    a=(max_intensity -min_intensity)/(np.max(g)-np.min(g))
    c=(np.max(g)*min_intensity - np.min(g)*max_intensity)/(max_intensity -min_intensity)
    g=(a*np.array(g)+c).astype(np.uint8)

    a=(max_intensity -min_intensity)/(np.max(b)-np.min(b))
    c=(np.max(b)*min_intensity - np.min(b)*max_intensity)/(max_intensity -min_intensity)
    b=(a*np.array(b)+c).astype(np.uint8)

    r,g,b= Image.fromarray(r),Image.fromarray(g),Image.fromarray(b)
    image_new=Image.merge('RGB',(r,g,b))
  else :
    a=(max_intensity -min_intensity)/(np.max(rgb)-np.min(rgb))
    c=(np.max(rgb)*min_intensity - np.min(rgb)*max_intensity)/(max_intensity -min_intensity)
    image_new = (a*rgb+c).astype(np.uint8)
    image_new = Image.fromarray(image_new)
    image_new=Image.merge('L',(image_new,))
  return (image_new)


def histogram_equalization (image , L_max): #function Apply histogram equalization on the input image
  im= np.array(image)
  length=im.shape[0]*im.shape[1]
  if(len(im.shape)==3):
    r, g, b = im[:,:,0].copy(), im[:,:,1].copy(), im[:,:,2].copy() 
    r1, g1, b1 = im[:,:,0].copy(), im[:,:,1].copy(), im[:,:,2].copy() 
    unique_r, counts_r = np.unique(r, return_counts=True)
    unique_g, counts_g = np.unique(g, return_counts=True)
    unique_b, counts_b = np.unique(b, return_counts=True)
    counts_r= (counts_r/length)*L_max 
    counts_r= (np.cumsum(counts_r)).astype(np.uint8)
    counts_g= (counts_g/length)*L_max 
    counts_g= (np.cumsum(counts_g)).astype(np.uint8)
    counts_b= (counts_b/length)*L_max 
    counts_b= (np.cumsum(counts_b)).astype(np.uint8)
    x= max(len(unique_r),len(unique_g),len(unique_b) )
    for i in range(x): 
      if(i < len(unique_r) ) : r1[r[:]==unique_r[i]]= counts_r[i]
      if(i < len(unique_g) ) : g1[g[:]==unique_g[i]]= counts_g[i]
      if(i < len(unique_b) ) : b1[b[:]==unique_b[i]]= counts_b[i]
    
    r1,g1,b1= Image.fromarray(r1),Image.fromarray(g1),Image.fromarray(b1)
    image_new=Image.merge('RGB',(r1,g1,b1))
  else :  
    gray=im.copy()
    unique, counts = np.unique(gray, return_counts=True)
    counts= (counts/length)*L_max 
    counts= (np.cumsum(counts)).astype(np.uint8)
    for i in range(len(unique)): 
      gray[im[:]==unique[i]]= counts[i]
    image_new = Image.fromarray(gray)
    image_new=Image.merge('L',(image_new,))
  return image_new
  

def IMAGE_NOISE(image, filter_size): #function remove noise from image  
 
   rgb=np.array(image)
   if (len(rgb.shape)==3):
      r, g, b = rgb[:,:,0].copy(), rgb[:,:,1].copy(), rgb[:,:,2].copy()
      for i in range(r.shape[0]-(filter_size-1)):
        for j in range(r.shape[1]-(filter_size-1)):
          noise_r= r[i:i+filter_size,j:j+filter_size]
          noise_g= g[i:i+filter_size,j:j+filter_size]
          noise_b= b[i:i+filter_size,j:j+filter_size]
          r[i+(filter_size//2),j+(filter_size//2)]=(np.sum(noise_r))//(filter_size**2)
          g[i+(filter_size//2),j+(filter_size//2)]=(np.sum(noise_g))//(filter_size**2)
          b[i+(filter_size//2),j+(filter_size//2)]=(np.sum(noise_b))//(filter_size**2)
      r1,g1,b1= Image.fromarray(r),Image.fromarray(g),Image.fromarray(b)
      rgb1=Image.merge('RGB',(r1,g1,b1))
      return rgb1
   else :
     gray=rgb.copy()
     for i in range(gray.shape[0]-(filter_size-1)):
       for j in range(gray.shape[1]-(filter_size-1)):
          noise_gray= rgb[i:i+filter_size,j:j+filter_size]
          gray[i+(filter_size//2),j+(filter_size//2)]=(np.sum(noise_gray))//(filter_size**2)
     gray= Image.fromarray(gray)
     gray=Image.merge('L',(gray,))
     return gray
 


