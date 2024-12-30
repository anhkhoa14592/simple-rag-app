from model.request_scheme import UserRequestScheme


class QuestionController:
    def __init__(self, chain, rag):
        self.chain = chain
        self.rag = rag

    def ask_question(self, request: UserRequestScheme):
        docs = self.rag.similarity_search(request.question, k=5)

        user_input = {
            "question": request.question,
            "rag": docs
        }

        output = self.chain.invoke(user_input)
        return output
