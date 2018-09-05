from PIL import Image

img = Image.open('D:/Dados/plot_T0859_RMSD_GDT-TS_fcm_2.png')
area = (0, 0, 430, 480)
cropped_img = img.crop(area)
cropped_img.show()
cropped_img.save('D:/Dados/cropped.png')