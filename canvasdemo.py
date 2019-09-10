from reportlab.pdfgen import canvas

c = canvas.Canvas("sample.pdf")
c.drawString(150, 200, "report lab is working")
c.save()
