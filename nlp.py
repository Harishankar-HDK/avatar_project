import re

def clean_model_output(text):
    # Remove unwanted symbols like asterisks
    text = re.sub(r'\*+', '', text)  # Removes all asterisks
    # Remove any other non-alphanumeric characters except common punctuation
    text = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text)  
    # Collapse multiple spaces into a single space
    text = re.sub(r'\s+', ' ', text)
    # Remove leading/trailing spaces

    text = text.replace('.', ',')
    
    text = text.strip()
    
    return text
