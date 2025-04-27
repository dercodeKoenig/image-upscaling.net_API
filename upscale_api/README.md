# image-upscaling.net API Client

A simple Python package to interact with the free [image-upscaling.net](https://image-upscaling.net/) API. This client provides two key functions for uploading images for processing and querying their processing status.

## Features

- **Upload Images**: Send images to the upscaling service with 2 enhancement options.
- **Query Status**: Retrieve the processing status of your images, categorized as waiting, completed, or in progress. This will give you the urls to download processed images.

## Installation

Install the package using pip:

```bash
pip install image-upscaling-api
```

## Usage

### Uploading an Image

The `upload_image` function sends an image for upscaling.

Note: The `client_id` must be a 32-digit hexadecimal string of your choice to identify your requests.

```python
from image_upscaling_api import upload_image

# Example usage:
upload_image("r1.png", "481d40602d3f4570487432044df03a52", 
             use_face_enhance=False,
			 scale = 4)
```

#### Parameters:
- `image_path` (str): Path to the image file.
- `client_id` (str): Your 32-digit hexadecimal client ID.
- `scale` (int): target scale, can be 1/2/3/4
- `use_face_enhance` (bool): Enable to improve facial features (faces will not always match original faces).

### Querying Processing Status

The `get_uploaded_images` function retrieves the status of your uploaded images.

```python
from image_upscaling_api import get_uploaded_images

# Example usage:
waiting, completed, in_progress = get_uploaded_images("481d40602d3f4570487432044df03a52")
```

#### Returns:
- `waiting` (list): Images queued for processing.
- `completed` (list): Images that have been processed.
- `in_progress` (list): Images currently being processed.

## Availability
This project is fully donation-funded. If you find it useful, please consider making a contribution to help cover server costs and ensure its continued availability.

At the moment, the service is free to use, but its future depends on community support. If donations are insufficient to maintain operations, it may not be possible to sustain long-term availability.<br>

[<img src="https://image-upscaling.net/assets/images/pypl_donate.png" width=200>](https://www.paypal.com/donate/?hosted_button_id=C5BA3K93LY6TG)
[<img src="https://image-upscaling.net/assets/images/more_info.png" width=140>](https://image-upscaling.net/imageupscaling/lang/en/donations.html)

Join our Discord for updates, discussions, or support: https://discord.gg/utXujgAT8R

## License

This project is licensed under the MIT License.

## Source code:
[https://github.com/dercodeKoenig/image-upscaling.net_API](https://github.com/dercodeKoenig/image-upscaling.net_API)

## Full Example Notebook:
[https://github.com/dercodeKoenig/image-upscaling.net_API/blob/main/upscale_api/image_upscaling_api_demo.ipynb](https://github.com/dercodeKoenig/image-upscaling.net_API/blob/main/upscale_api/image_upscaling_api_demo.ipynb)




