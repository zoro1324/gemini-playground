import PyPDF2
import os

import google.generativeai as genai

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_pdf_text(pdf_path: str) -> str:
    """Extract text from a PDF file."""
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def answer_question_about_pdf(pdf_path: str, question: str) -> str:
    """Read a PDF and answer questions about its content."""
    # Extract text from PDF
    pdf_text = extract_pdf_text(pdf_path)
    
    # Create the prompt
    prompt = f"""Here is the content of a PDF document:

{pdf_text}

Question: {question}

Please answer the question based on the PDF content provided above."""
    
    # Call Gemini API
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text

# Example usage
if __name__ == "__main__":
    pdf_file = "sample.pdf"
    user_question = "What is the main topic of this document?"
    
    answer = answer_question_about_pdf(pdf_file, user_question)
    print(f"Answer: {answer}")