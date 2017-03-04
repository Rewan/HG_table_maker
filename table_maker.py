from PIL import Image, ImageFont, ImageDraw

import glob

positions = [
    (116, 151), (338, 152), (560, 152), (801, 152), (1023, 152), (1244, 151),
    (117, 352), (339, 353), (560, 353), (801, 353), (1022, 353), (1244, 352),
    (116, 553), (338, 554), (560, 554), (801, 554), (1022, 554), (1244, 553),
    (117, 754), (339, 755), (560, 755), (801, 755), (1022, 755), (1244, 754) ]

textDW = 69
textDH = 153

def getXY(pos):
    return positions[pos-1]

def getScale(w, h, tw=139, th=123):
    return max(tw/w, th/h)

def getNewSize(size, tw=139, th=123):
    w, h = size
    scale = getScale(w, h, tw=tw, th=th)
    w, h = int(w*scale), int(h*scale)
    return (max(tw,w), max(th,h))

def resizeImg(image, tw=139, th=123):
    return image.resize(getNewSize(image.size, tw=tw, th=th))

def cropCenter(image, tw=139, th=123):
    w, h = image.size
    w, h = (w//2 - tw//2), (h//2 - th//2)
    return image.crop((w, h, w + tw, h + th))

def resizeAndCropCenter(image, tw=139, th=123):
    return cropCenter(resizeImg(image, tw=tw, th=th), tw=tw, th=th)

def addChampion(char, table):
    char = resizeAndCropCenter(char, tw=95, th=86)
    table.paste(char, (703, 40))

def addCharToTable(pos, char, table):
    if pos==1:
        addChampion(char, table)
        
    char = resizeAndCropCenter(char)
    table.paste(char, getXY(pos))

def addChampionName(name, draw):
    font = ImageFont.truetype("MTCORSVA.TTF", 18)
    
    w, h = draw.textsize(name, font)
    draw.multiline_text((750 - w//2, 138 - h//2), name, (0,0,0), font=font, align="center")

def addNameToTable(pos, name, draw):
    if pos==1:
        addChampionName(name, draw)
        
    font = ImageFont.truetype("MTCORSVA.TTF", 20)
    
    w, h = draw.textsize(name, font)
    cw, ch = getXY(pos)
    cw += textDW
    ch += textDH

    draw.multiline_text((cw - w//2, ch - h//2), name, (0,0,0), font=font, align="center")


def main():
    winners = glob.glob('images\*')

    #print("Winners list:", winners)

    table = Image.open("table.png")
    draw = ImageDraw.Draw(table)

    for winner in winners:
        char = Image.open(winner)
        
        name = winner.split('.')[0].split('\\')[1]
        pos = 25
        if ' ' in name:
            pos, name = name.split(' ',1)
            pos = int(pos)
        else:
            pos = int(name)
            name = ''
        
        addCharToTable(pos, char, table)

        if name != '':
            addNameToTable(pos, name, draw)

    table.save("new_table.png", "PNG")

if __name__=="__main__":
    main()
