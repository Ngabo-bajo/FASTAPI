from fastapi import FastAPI

main = FastAPI()

@main.get('/')
def index():
  return "This is the front page"

@main.get('/about')
def about():
  return "About page"
#this is the backend comment
