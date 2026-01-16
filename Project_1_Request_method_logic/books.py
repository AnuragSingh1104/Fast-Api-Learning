from fastapi import FastAPI

app=FastAPI()

Books=[
    {'title'}
]

@app.get("/")
def first_api():
    return {'Message':'Hello Anurag'}