from transformers import AutoTokenizer

# Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

# Encode the inputs
input_ids = tokenizer('The <extra_id_1> walks in <extra_id_2> park', return_tensors='pt').input_ids

# Encode the labels
lm_labels = tokenizer('<extra_id_1> cute dog <extra_id_2> the <extra_id_3>', add_special_tokens=True, return_tensors='pt').input_ids

# Replace tokenizer.encode with tokenizer to make it more concise
# Added 'add_special_tokens=True' for clarity, it's usually the default behavior
