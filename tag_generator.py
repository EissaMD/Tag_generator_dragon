from PIL import Image , ImageDraw , ImageFont
import os

flags = os.listdir(r'resources/flags')
flags = [flag.split('.')[0] for flag in flags]
print(flags)
flag_dict = {}
for f in flags:
    img = Image.open(f'resources/flags/{f}.png')
    flag_dict[f] = img.resize((150,150))
background = Image.open(r'resources/template.jpg')
tag_w = background.size[0]
# profile image
profile = Image.open(r'resources/profile_img/AND01.jpg')
profile = profile.resize((563,775))
# paste the profile image
background.paste(profile,(725,435))
# flag
background.paste(flag_dict['China'],(1500,900),flag_dict['China'])
# write the name 
draw = ImageDraw.Draw(background)  
font = ImageFont.truetype(r'resources/Roboto-Black.ttf', 80) 
text = 'Beijing International Dragon Boat Team'
# Team Name
draw.text((int(tag_w/2), 280), text,fill ="#ECECEC",font=font, align ="right" ,anchor='mm')  
# Crew member name
text = 'COLIN PANG TIANG KUAN'
draw.text((int(tag_w/2), 1300), text,fill ="#272B2C",font=font, align ="right" ,anchor='mm')  

font = ImageFont.truetype(r'resources/Roboto-Black.ttf', 50) 
text = 'KLS01'
draw.text((700, 1200), text,fill ="#4B758E",font=font, align ="right" ,anchor='rs') 
font = ImageFont.truetype(r'resources/Roboto-Black.ttf', 60)  
text = 'Male'
draw.text((750, 1465), text,fill ="#272B2C",font=font, align ="right" ,anchor='mm')  
text = "1990"
draw.text((1300, 1465), text,fill ="#272B2C",font=font, align ="right" ,anchor='mm')  
background.save("abc.jpg")