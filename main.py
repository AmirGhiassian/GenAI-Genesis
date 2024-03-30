import vertexai
from vertexai.generative_models import GenerativeModel, Part

def generate_text(project_id: str, location: str) -> str:

    model = GenerativeModel("gemini-1.0-pro-vision")

    response = model.generate_content(
            [
                Part.from_uri("gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"),
                "What is shown in this picture?"
            ]
            )
    print(response)
    return response.text


if __name__ == "__main__":
    generate_text("genai-genesis", "us-central1")
