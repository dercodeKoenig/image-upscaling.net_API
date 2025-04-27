# image-upscaling.net API Client

A simple Python package to interact with the free [image-upscaling.net](https://image-upscaling.net/online_tts) text to speech API.

## Features

- **Submit Text**: Send text to the tts service with selected voice and speed (visit the website for voices and character limit).
- **Query Status**: Retrieve the processing status of your requests. This will give you the urls to download processed mp3 files.

## Installation

Install the package using pip:

```bash
pip install text-to-speech-api
```

## Usage

### Submit Request

The `submit` function sends an image for upscaling.

Note: The `client_id` must be a 32-digit hexadecimal string of your choice to identify your requests.

```python
from text_to_speech_api import submit
res = submit(client_id, "Hello world", "am_adam", speed=1.2)
```

#### Parameters:
- `client_id` (str): Your 32-digit hexadecimal client ID.
- `text` (str): Your text to process
- `voice` (str): Select a voice
- `speed` (float): set output speed

### Querying Processing Status

The `get_status` function retrieves the status of your requests.

```python
from text_to_speech_api import get_status
results = get_status(client_id)
```

#### Returns:
a list of (id, output_path) for your requests

## Availability
This project is fully donation-funded. If you find it useful, please consider making a contribution to help cover server costs and ensure its continued availability.

At the moment, the service is free to use, but its future depends on community support. If donations are insufficient to maintain operations, it may not be possible to sustain long-term availability.<br>

[<img src="https://image-upscaling.net/assets/images/pypl_donate.png" width=200>](https://www.paypal.com/donate/?hosted_button_id=C5BA3K93LY6TG)
[<img src="https://image-upscaling.net/assets/images/more_info.png" width=140>](https://image-upscaling.net/online_tts/lang/en/donations.html)

Join our Discord for updates, discussions, or support: https://discord.gg/utXujgAT8R

## License

This project is licensed under the MIT License.

