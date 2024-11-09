import qrcode

#Taking upi_id
upi_id = input("Enter your upi_id: ")

#upi_id format
#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE
#pa = Recipient upi id
# pn= Recipient name

#Defining the payment url based on the UPI ID and the payment app

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#Create qrcode
phonepe_qr =  qrcode.make(phonepe_url)
google_pay_qr =qrcode.make(google_pay_url )
paytm_qr  = qrcode.make(paytm_url)

#Save the qrcode

# phonepe_qr.save('phonepe_qr.png')
# paytm_qr.save('paytm_qr.png')
# google_pay_qr.save('google_pay_qr')


#Display the qrcode

phonepe_qr.show()
google_pay_qr.show()
paytm_qr.show()
