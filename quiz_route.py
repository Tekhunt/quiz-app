from urllib.parse import urlparse
from fastapi import APIRouter, FastAPI
from quiz_ids import get_quiz_ids
from response_model import Quiz_Respose


# app = FastAPI()
quizRouter = APIRouter()


@quizRouter.get('/{store}', response_model=Quiz_Respose, responses={
    200: {"description": "Successful response, returns a list of quiz IDs."},
    404: {"description": "Store with the provided name or url not found."},
    500: {"description": "Internal server error occured."},
})
def fetch_quiz_ids(store: str):
    """
    Fetches the quiz IDs associated with a store.

    Args:
        store (str): The store name or identifier.

    Returns:
        List[str]: A list of quiz IDs associated with the store.
    """
    if not store:
        raise ValueError("The input cannot be empty. Please provide store name or url")
    print('store is: ',store)
    quiz_ids = get_quiz_ids(store)

    if not quiz_ids:
        return {"detail": "Store not found."}

    return Quiz_Respose(store_name=store, quiz_id=quiz_ids, count=len(quiz_ids))
