import re

def clean_model_output(text):
    # Remove asterisks and unwanted symbols
    text = re.sub(r'\*+', '', text)  # Removes all asterisks
    text = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text)  # Removes any other non-alphanumeric characters except common punctuation
    
    # Optionally, you can handle any other unwanted symbols specifically
    # e.g., removing strange characters like "@" or extra spaces
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    
    # Strip leading or trailing spaces
    text = text.strip()
    
    return text

# Example model output with unwanted symbols
model_output = "Hello! I am your *assistant* here to help you with ***your query!***"

cleaned_output = clean_model_output(model_output)
print(cleaned_output)
