__author__ = 'nathan'

import nose

import app
import base64
import hashlib
import json
import os


def test_image_upload():
    with open("test/plate.jpg") as f:
        test_image = f.read()
        image_b64 = base64.b64encode(test_image)
        # Get the MD5 so we can check that the file exists
        md5 = hashlib.md5()
        md5.update(test_image)
        img_md5 = md5.hexdigest()
        # Get the server's response and parse the json
        response = app.app.test_client().post('/api/image_upload/', data={
            "img": "data:image/jpeg;base64," + image_b64
        })
        response_data = json.loads(response.data)
        assert response_data["success"] is True
        assert response_data["id"] == img_md5
        file_path = os.path.join("images", response_data["id"] + ".png")
        file_exists = os.path.exists(file_path)
        assert file_exists
        if file_exists:
            # clean up after ourselves
            os.remove(file_path)

if __name__ == "__main__":
    nose.runmodule()