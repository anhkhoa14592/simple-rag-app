from pydantic import BaseModel, Field


class UserRequestScheme(BaseModel):
    question: str = Field(description="question")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "question": "Bùi Minh Đức là ai?"
                }
            ]
        }
    }


class LLMOutput(BaseModel):
    answer: str = Field(description="answer the question.")
