import os

from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter

from controller.QuestionController import QuestionController
from resource import download
from service.langchain import generate_chain
from service.rag import stored_embedding

load_dotenv(dotenv_path=".env")

if not os.getenv("GEMINI_API"):
    print('Lack of gemini api in .env')
    exit(1)

rag = stored_embedding()
download.start()

app = FastAPI()

chain = generate_chain()

controller = QuestionController(chain=chain, rag=rag)

router = APIRouter(prefix="/gemini")
router.add_api_route("/ask", controller.ask_question, methods=["POST"], response_model=dict)
app.include_router(router)
