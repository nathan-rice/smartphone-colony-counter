__author__ = 'nathan'

import flask
import re
import base64
import hashlib
import os
import json

app = flask.Flask(__name__)

data_url_pattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
image_file_directory = "images/"


@app.route('/api/image_upload/', methods=["POST"])
def image_upload():
    img = flask.request.form.get("img")
    img_b64 = data_url_pattern.match(img).group(2)
    if img_b64 is not None and len(img_b64) > 0:
        img_data = base64.b64decode(img_b64)
        # Get the MD5 to use as a filename
        md5 = hashlib.md5()
        md5.update(img_data)
        img_md5 = md5.hexdigest()
        # Now write the file out
        file_name = os.path.join(image_file_directory, img_md5 + ".png")
        with open(file_name, 'w+b') as f:
            f.write(img_data)
        return json.dumps({"success": True, "id": img_md5})
    return json.dumps({"success": False})


if __name__ == "__main__":
    app.run()