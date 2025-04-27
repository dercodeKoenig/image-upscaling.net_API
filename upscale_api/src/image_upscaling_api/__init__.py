import requests
import json

server_url = "https://image-upscaling.net/"
#server_url = "https://ai-image-upscaling.2ix.de/"

def upload_image(path, client_id, scale=2, use_face_enhance=False):
    # URL to the PHP script
    url = server_url+"imageupscaling/upload.php"

    data = {}
    if use_face_enhance:
        data["fx"] = ""
    data["scale"] = scale

    # Cookie with a valid 32-digit hexadecimal client_id
    cookies = {
        "client_id": client_id
    }

    files = {
        "image": open(path, "rb")
    }

    headers = {
        "Origin": server_url
    }

    response = requests.post(url, data=data, files=files, cookies=cookies, headers=headers)

    return response.text


def get_uploaded_images(client_id):

  # URL to the PHP script
  url = server_url+"imageupscaling/get_images_client.php"

  # Cookie with a valid 32-digit hexadecimal client_id
  cookies = {
      "client_id": client_id
  }


  # Send the POST request
  response = requests.get(url, cookies=cookies)

  # Print the response from the server
  data = json.loads(response.text)

  # Access the arrays (lists)
  waiting = [server_url+"imageupscaling/"+i for i in data["images1"]]
  completed = [server_url+"imageupscaling/"+i for i in data["images2"]]
  in_progress = [server_url+"imageupscaling/"+i for i in data["images3"]]

  return waiting, completed, in_progress
  
  