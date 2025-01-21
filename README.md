
# UPI QR Code Generator

## Description
This script generates UPI payment QR codes for various payment apps, including PhonePe, Paytm, and Google Pay. The QR codes are generated based on the UPI ID provided by the user and can be saved or displayed.

## How It Works
1. The user enters their UPI ID.
2. The script creates a UPI payment URL for PhonePe, Paytm, and Google Pay.
3. QR codes are generated for each payment URL using the `qrcode` library.
4. The QR codes can either be displayed or saved as images.

## Features
- Generate QR codes for **PhonePe**, **Paytm**, and **Google Pay**.
- Display the generated QR codes directly.
- Save the QR codes as image files for sharing or later use.

## UPI URL Format
The UPI payment URL follows the format:
```
upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE
```
- `pa`: Recipient UPI ID
- `pn`: Recipient Name
- `am`: Amount (optional)
- `cu`: Currency (optional, default is INR)
- `tn`: Transaction message (optional)

## Prerequisites
- Python 3.x
- `qrcode` library (install it using `pip install qrcode`)

## Installation
1. Clone this repository or download the script.
2. Install the required Python library using:
   ```bash
   pip install qrcode
   ```
3. Run the script using:
   ```bash
   python upi_qr_code_generator.py
   ```

## Usage
1. Enter your UPI ID when prompted.
2. The script will generate QR codes for PhonePe, Paytm, and Google Pay.
3. The QR codes will be displayed, and you can optionally save them.

## Saving QR Codes
To save the generated QR codes as images, uncomment the following lines in the script:
```python
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')
```



## Acknowledgements
- Built using the `qrcode` Python library.
