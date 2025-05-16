from fastapi import APIRouter, HTTPException
from exceptions import ArticleNotFoundError, NoValidParagraphError
from file_context_manager import QueryFileWriter
from schemas import QuestionRequest
from wiki_scraper import get_first_5_sentences_from_wikipedia

router = APIRouter()

# Question URL, user sends it's question to this url


@router.post("/question")
async def post_queston(request: QuestionRequest):
    try:
        result = get_first_5_sentences_from_wikipedia(request.text)
        with QueryFileWriter(request.text) as f:
            f.write(result)
        return {"result": "Data successfully scraped and written to the file"}
    except ArticleNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except NoValidParagraphError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {str(e)}")
