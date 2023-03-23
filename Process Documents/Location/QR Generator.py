import qrcode

# 1 - Streatham Court
# 2 - Peter Chalk
# 3 - Forum
# 4 - Queen's
# 5 - Amory

streatham_court = "https://event.exeter.ac.uk/venues/streatham-court"
peter_chalk = "https://event.exeter.ac.uk/venues/peter-chalk-centre"
forum = "https://www.exeter.ac.uk/departments/campusservices/facilitiesoperations/forum/"
queen = "https://event.exeter.ac.uk/venues/queens-building"
amory = "https://socialsciences.exeter.ac.uk/contact/"

# Creating an instance of each qrcode
qr1 = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)
qr2 = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)
qr3 = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)
qr4 = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)
qr5 = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)

qr1.add_data(streatham_court)
qr1.make(fit=True)
qr2.add_data(peter_chalk)
qr2.make(fit=True)
qr3.add_data(forum)
qr3.make(fit=True)
qr4.add_data(queen)
qr4.make(fit=True)
qr5.add_data(amory)
qr5.make(fit=True)

img1 = qr1.make_image(fill='black', back_color='white')
img1.save('qrPic/StreathamCourt.png')
img2 = qr2.make_image(fill='black', back_color='white')
img2.save('qrPic/PeterChalk.png')
img3 = qr3.make_image(fill='black', back_color='white')
img3.save('qrPic/Forum.png')
img4 = qr4.make_image(fill='black', back_color='white')
img4.save("qrPic/Queen's.png")
img5 = qr5.make_image(fill='black', back_color='white')
img5.save('qrPic/Amory.png')

# 1 - Streatham Court
# 2 - Peter Chalk
# 3 - Forum
# 4 - Queen's
# 5 - Amory