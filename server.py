 ## setting up flask server for backend to qr code generator
import segno
import os
import time

from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app= Flask(__name__)
# CORS(app, origins=["http://127.0.0.1:8080"])
CORS(app, origins=["http://127.0.0.1:5500"])

default_scale = 2.5
@app.route('/generate', methods=['POST'])
def create_qr_code():
    data = request.json
    qr_content = data.get('inputString', 'www.qr4thepeople.com')  # Access the 'text' value, default to '' if not found
    scaleValue = data.get('scaleValue', default_scale)
    light_main = data.get('light_main', 'white')  # Access the 'text' value, default to '' if not found
    dark_main = data.get('dark_main', 'black')  # Access the 'text' value, default to '' if not found
    data_light=data.get('data_light', 'white')
    data_dark=data.get('data_dark', 'white')
    quiet_zone = data.get('quiet_zone', 'white')  # Access the 'text' value, default to '' if not found
    data_dark=data.get('dark_color', 'black')

    qrcode = segno.make(qr_content)


    # Save the QR code to a file
    filename = f"{str(time.time())}.png"
#     scale=5,
#     light="lightblue",
#     dark="green",
# )
    qrcode.save(
        f"./static/qr-images/{filename}", 
        scale=scaleValue, 
        light=light_main,
        dark=dark_main,
        data_light=data_light,
        data_dark=data_dark,
        quiet_zone=quiet_zone, 
    )
    
    # For this example, we'll just return it back in the response
    return jsonify({"filename": filename})


if __name__ == '__main__':
    app.run(debug=True, port=3000)


'''
qrcode.save(
    "green_datamodules_qrcode.png",
    scale=5,
    light="lightblue",
    dark="darkblue",
    data_dark="green",
    data_light="lightgreen",
    quiet_zone="maroon",

)
'''