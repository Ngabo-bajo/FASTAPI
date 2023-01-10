from fastapi import FastAPI

main = FastAPI()

@main.get('/')
def index():
  return "This is the front page"