from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "deepseek-ai/deepseek-r1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def analyze_text(text):
    inputs = tokenizer(text, return_tensors="pt")
    output = model.generate(**inputs, max_length=500)
    return tokenizer.decode(output[0], skip_special_tokens=True)

texts = fetch_tweets("earthquake") + fetch_news()
summaries = [analyze_text(text) for text in texts]
print(summaries)