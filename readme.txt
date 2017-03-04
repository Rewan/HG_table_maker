Table Maker v1.0 made by Toph

HOWTO:
1. Put images with names "[1-24] <name>.*" into "images/" folder.
	1.1) Optional: replace initial "table.png" with table you need to be modified, name must be "table.png"
2. Run "table_maker.exe/.py" and wait till it ends his work.
3. Get "new_table.png" from initial "table.png" with inputed images from "images/" folder.


To run "table_maker.py" you need Python 3.4+ and Pillow package.


How it works:
1. Script get array images from "images/"
2. Foreach image script gets his position and name from file name. (Character name could be with EOL ('\n') character, i'm using multiline text draw)
3. Script resize image to one with one or both sides equals to table cell 139x123.
4. Script cuts image from step 3 to 139x123 with respect to center.
5. Script paste to table image from step 4.
6. Script draws name to cell below the image, with center of the text be right in center of the cell.
7. For image with name "1 <name>.*" script also makes steps 2-6 with championcell which 95x86.