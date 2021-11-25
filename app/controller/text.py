from fastapi import APIRouter
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelWithLMHead

router = APIRouter()

tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-sarcasm-twitter")
model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-sarcasm-twitter")


@router.post("/text/sarcastic", response_model=bool)
async def is_sarcastic(text: str):
    input_ids = tokenizer.encode(text + '</s>', return_tensors='pt')
    output = model.generate(input_ids=input_ids, max_length=3)
    dec = [tokenizer.decode(ids) for ids in output]
    label = dec[0]
    return label != 'normal'


@router.post("/text/positive", response_model=bool)
async def is_positive(text: str):
    sentiment_classifier = pipeline('sentiment-analysis')
    return sentiment_classifier(text)[0]['label'] == 'POSITIVE'


@router.post("/text/random", response_model=bool)
async def is_random(text: str):
    human_classifier = pipeline('sentiment-analysis', 'microsoft/DialogRPT-human-vs-rand')
    return human_classifier(text)[0]['label'] != 'HUMAN'


@router.post("/text/machine", response_model=bool)
async def is_machine(text: str):
    human_classifier = pipeline('sentiment-analysis', 'microsoft/DialogRPT-human-vs-machine')
    return human_classifier(text)[0]['label'] != 'HUMAN'
