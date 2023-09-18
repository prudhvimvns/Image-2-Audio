# Image 2 Audio Story Generator 📸🔉✨

Welcome to the Image 2 Audio Story Generator! This Python script allows you to turn images into text and generate audio stories based on the image content. 🚀

## How it Works 🤖

1. **Image to Text**: The script first converts the uploaded image into text using the [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base) model.

2. **Generate Story**: It then generates a creative story based on the image content using the GPT-2 text generation model.

3. **Text to Speech**: Finally, it converts the generated story into audio using the [espnet/kan-bayashi_ljspeech_vits](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits) text-to-speech model.

## Usage 📝

1. Clone this repository.

2. Install the required Python packages using `pip install -r requirements.txt`.

3. Run the script using `python main.py`.

4. Upload an image, and the magic happens! 🪄

## Dependencies 🛠️

- [PyTorch](https://pytorch.org/)
- [transformers](https://huggingface.co/transformers/)
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://docs.python-requests.org/en/latest/)
- [jinja2](https://jinja.palletsprojects.com/en/3.0.x/)
- [streamlit](https://streamlit.io/)

## Configuration 🔧

Make sure to set your [Hugging Face API Token](https://huggingface.co/docs/hub/security-tokens) in a `.env` file as `HUGGINGFACEHUB_API_TOKEN`.

## Output 🎧

The generated audio story will be saved as `audio.mp3`.

## Credits 👏

- Image to Text Model: [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)
- Text Generation Model: [GPT-2](https://huggingface.co/gpt2)
- Text to Speech Model: [espnet/kan-bayashi_ljspeech_vits](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits)

## Author 📝

- [[Prudhvi]](https://github.com/prudhvimvns)

Happy Image to Audio Storytelling! 📚🎉
