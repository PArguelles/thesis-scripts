from PIL import Image

basewidth = 400
img = Image.open('D:/Dados/plot_3hisA02_GDT-HA_TM-score_km_5.png')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('D:/Dados/plot_3hisA02_GDT-HA_TM-score_km_5_resize.png') 