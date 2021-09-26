from transformers import BlenderbotSmallTokenizer, BlenderbotSmallForConditionalGeneration
mname = 'facebook/blenderbot_small-90M'
model = BlenderbotSmallForConditionalGeneration.from_pretrained(mname)
tokenizer = BlenderbotSmallTokenizer.from_pretrained(mname)

UTTERANCE = "My friends are cool but they eat too many carbs."
print("Human: ", UTTERANCE)
inputs = tokenizer([UTTERANCE], return_tensors='pt')
reply_ids = model.generate(**inputs)
print("Bot: ", tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0])

REPLY = "I'm not sure"
print("Human: ", REPLY)
NEXT_UTTERANCE = (
"My friends are cool but they eat too many carbs.</s> "
"<s>what kind of carbs do they eat? i don't know much about carbs.</s> "
"<s>I'm not sure."
)
print(type(NEXT_UTTERANCE))
print(NEXT_UTTERANCE)
inputs = tokenizer([NEXT_UTTERANCE], return_tensors='pt')
next_reply_ids = model.generate(**inputs)
print("Bot: ", tokenizer.batch_decode(next_reply_ids, skip_special_tokens=True)[0])


print('\n\n\n')

UTTERANCE = "hi"
print("Human: ", UTTERANCE)
inputs = tokenizer([UTTERANCE], return_tensors='pt')
reply_ids = model.generate(**inputs)
print("Bot: ", tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0])

print('\n\n\n')

UTTERANCE = input('>>you: ')
print("Human: ", UTTERANCE)
inputs = tokenizer([UTTERANCE], return_tensors='pt')
reply_ids = model.generate(**inputs)
print("Bot: ", tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0])

UTTERANCE = ""
count = 0
while True:
    prompt = input('>>you: ')
    if count == 0:
        UTTERANCE += prompt
        count += 1
    else:
        UTTERANCE += ('<s>' + prompt)
    inputs = tokenizer([UTTERANCE], return_tensors='pt')
    reply_ids = model.generate(**inputs)
    reply = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
    print("Bot: ", reply)
    UTTERANCE += ('</s> ' + '<s>' + reply + '</s>')