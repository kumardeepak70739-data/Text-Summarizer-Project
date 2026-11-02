from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_summary(text, max_length=130, min_length=30):
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs["input_ids"], 
        max_length=max_length, 
        min_length=min_length, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids, skip_special_tokens=True)
    return summary