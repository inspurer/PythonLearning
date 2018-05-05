import qrcode
qr = qrcode.QRCode(version=10,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10, border=4)
qr.add_data('http://user.qzone.qq.com/306467355/blog/1439803492')
qr.make(fit=True)
img = qr.make_image()
img.save('D:\\Python_dfg.png')
