from fastapi import FastAPI
import uvicorn

import routes

app = FastAPI(title="Sports Scraper API")

# Include router
app.include_router(routes.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8003, reload=True)
