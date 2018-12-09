import io
import os
from google.cloud import vision_v1p3beta1 as vision


def detect_formula(path):
    """Detects handwritten characters in a local image.

    Args:
    path: The path to the local file.
    """
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # Language hint codes for handwritten OCR:
    # en-t-i0-handwrit, mul-Latn-t-i0-handwrit
    # Note: Use only one language hint code per request for handwritten OCR.
    image_context = vision.types.ImageContext(
        language_hints=['en-t-i0-handwrit'])

    response = client.document_text_detection(
        image=image,
        image_context=image_context)

    return response.full_text_annotation.text.strip()


def main():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../res/Pepper-4fd1ecb47687.json"
    path = "/Users/tluscre1/Documents/Studium.Local/ROBLAB/source/test/test_images"
    for filename in os.listdir(path):
        print(filename)
        print(detect_formula(path + "/" + filename))


if __name__ == "__main__":
    main()
