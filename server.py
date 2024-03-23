 ## setting up flask server for backend to qr code generator
import segno
import os
import time

from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app= Flask(__name__)
CORS(app, origins=["http://127.0.0.1:8080"])

default_scale = 2.5
@app.route('/generate', methods=['POST'])
def create_qr_code():
    data = request.json
    qr_content = data.get('text', 'HI!')  # Access the 'text' value, default to '' if not found
    light_main = data.get('light_main', 'white')  # Access the 'text' value, default to '' if not found
    dark_main = data.get('dark_main', 'black')  # Access the 'text' value, default to '' if not found
    border_color = data.get('border_color', 'white')  # Access the 'text' value, default to '' if not found

    # try:
    #     scale=float(data.get('scale', '2')),
    # except Exception as e:
    #     print(f"Could not convert {data.get('scale')} to type float, defaulting to {default_scale}")
    #     scale = default_scale

    data_dark=data.get('dark_color', 'black')
    data_light=data.get('light_color', 'white')



    qrcode = segno.make(qr_content)

    # Save the QR code to a file
    filename = f"{str(time.time())}.png"
#     scale=5,
#     light="lightblue",
#     dark="green",
# )
    qrcode.save(
        f"./{filename}", 
        scale=2, 
        quiet_zone=border_color, 
        light=light_main,
        dark=dark_main,
        data_dark=data_dark,
        data_light=data_light
    )
    
    # For this example, we'll just return it back in the response
    return jsonify({"filename": filename})


if __name__ == '__main__':
    app.run(debug=True, port=3000)
