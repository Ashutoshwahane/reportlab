from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

canvas = canvas.Canvas('report1.pdf', pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)
canvas.drawString(30,750, 'Iwarehouse')
canvas.drawString(30,735, 'EffCode Technology')
canvas.drawString(500,750, '11/09/2019')
canvas.line(480,747,580,747)

canvas.drawString(275,725,'Total bill : ')
canvas.drawString(500,725,'$100.00')
canvas.line(120,700,580,700)


canvas.drawString(30,703, 'Received by : ')
canvas.line(120,700,580,700)
canvas.drawString(120,703, "Willskhalifa")
canvas.save()


