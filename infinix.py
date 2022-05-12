# \\\\\
# <Button-1>

from tkinter import*
from math import*




def move() :
	global cx,cy,mx,my
	global vitesseX,vitesseY
	global alpha
	global directionX,directionY

	# vitesseX = sqrt((rayvit**2) - (sin(alpha)*rayvit)**2)
	# vitesseY = sqrt((rayvit**2) - (cos(alpha)*rayvit)**2)
	vitesseX = cos(alpha) * rayvit
	vitesseY = sin(alpha) * rayvit

	cx = cx + vitesseX
	cy = cy + vitesseY
	mx = cx + (cos(alpha)*rayb)
	my = cy + (sin(alpha)*rayb)
	mycanvas.coords(balle,cx - rayb ,cy - rayb,cx + rayb ,cy + rayb)


	


	if mx >= canWi :
		if sin(alpha) >= 0:
			angula = pi - (alpha + (pi/2))
			alpha += 2*angula
		else :
			angula = pi - (-alpha + (pi/2))
			alpha -= 2*angula


	if mx <= 0 :
		if sin(alpha) >= 0:
			angula = pi - ((alpha - pi) + (pi/2))
			alpha += 2*angula
		else :
			angula = pi - ((pi - alpha) + (pi/2))
			alpha -= 2*angula

	if my >= canHei :
		if cos(alpha) >= 0:
			angula = pi - (pi - alpha)
			alpha -= 2*angula
		else :
			angula = pi - (alpha)
			alpha += 2*angula	

	if my <= 0 :
		if cos(alpha) >= 0:
			angula = pi - ((alpha - (3*pi/2)) + (pi/2))
			alpha += 2*angula
		else :
			angula = pi - (((3*pi/2) - alpha ) + (pi/2))
			alpha -= 2*angula	# if mx >= canWi :
	# 	directionX *= -1

	# if mx <= 0 :
	# 	directionX *= -1

	# if my >= canHei :
	# 	directionY *= -1
	

	# if my <= 0 :
	# 	directionY *= -1

		

	ctx.after(20,move)

def letMove(event) :
	move()

alpha =(pi/10)


canWi = 500
canHei = 500
canBg = "white"
rayb = 15
ballBg = "green"
directionX = 1
directionY = 1

cx = 100
cy = 100
mx = cx + (cos(alpha)*rayb)
my = cy - (sin(alpha)*rayb)

rayvit = 15

vitesseX = cos(alpha) * rayvit
vitesseY = sin(alpha) * rayvit



ctx = Tk()

mycanvas = Canvas(width = canWi,height = canHei,bg = canBg)
balle = mycanvas.create_oval(cx - rayb ,cy - rayb,cx + rayb ,cy + rayb,fill = ballBg)

mycanvas.bind("<Button-1>",letMove)

mycanvas.grid(row = 0,rowspan = 10)

butt999 = Button(text = "Quittez",command = ctx.quit).grid(row = 1,column = 2)

ctx.mainloop()



















































