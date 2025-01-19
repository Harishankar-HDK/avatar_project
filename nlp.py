from transformers import AutoModelForCausalLM, AutoTokenizer

# Load Hugging Face Conversational Model
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(user_input):
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    response_ids = model.generate(
        inputs,
        max_length=100,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=2,  # Prevent repeating input
        do_sample=True,          # Add variability to response
        temperature=0.7          # Adjust creativity of response
    )
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response_text
