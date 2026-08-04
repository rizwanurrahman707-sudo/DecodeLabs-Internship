import cv2
import pytesseract
from pytesseract import Output
from pathlib import Path

# -----------------------------
# DecodeLabs - AI Project 4
# Path 1: Optical Character Recognition (OCR)
# -----------------------------

IMAGE_PATH = "sample_input.png"
CONFIDENCE_THRESHOLD = 80.0

# If Tesseract is not added to Windows PATH, uncomment and edit this line:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def main():
    image_path = Path(IMAGE_PATH)

    if not image_path.exists():
        print(f"Error: {IMAGE_PATH} was not found.")
        return

    image = cv2.imread(str(image_path))

    if image is None:
        print("Error: Could not read the image.")
        return

    # Step 1: Convert RGB/BGR image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Gaussian blur to reduce small noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 3: Adaptive thresholding for better contrast
    processed = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # OCR configuration: PSM 6 = a uniform block of text
    config = "--psm 6"

    data = pytesseract.image_to_data(
        processed,
        config=config,
        output_type=Output.DICT
    )

    detected_words = []
    accepted_scores = []

    for i, text in enumerate(data["text"]):
        text = text.strip()

        try:
            confidence = float(data["conf"][i])
        except (ValueError, TypeError):
            confidence = -1

        if text and confidence >= CONFIDENCE_THRESHOLD:
            detected_words.append(text)
            accepted_scores.append(confidence)

            x = data["left"][i]
            y = data["top"][i]
            w = data["width"][i]
            h = data["height"][i]

            cv2.rectangle(
                image, (x, y), (x + w, y + h), (0, 255, 0), 2
            )
            cv2.putText(
                image,
                f"{text} ({confidence:.0f}%)",
                (x, max(20, y - 5)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (0, 0, 255),
                1,
                cv2.LINE_AA
            )

    print("\n===== DecodeLabs Project 4: OCR =====")

    if detected_words:
        recognized_text = " ".join(detected_words)
        average_confidence = sum(accepted_scores) / len(accepted_scores)

        print("Recognized Text:")
        print(recognized_text)
        print(f"\nAverage Accepted Confidence: {average_confidence:.2f}%")
        print(f"Validation Threshold: {CONFIDENCE_THRESHOLD:.0f}%")

        if average_confidence >= CONFIDENCE_THRESHOLD:
            print("Validation: PASSED (80% minimum confidence achieved)")
        else:
            print("Validation: FAILED (below 80%)")

        output_path = "ocr_output.png"
        cv2.imwrite(output_path, image)
        print(f"Output image saved as: {output_path}")
    else:
        print("No text reached the 80% confidence threshold.")
        print("Try a clearer image or better lighting.")


if __name__ == "__main__":
    main()
