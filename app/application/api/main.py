from fastapi import FastAPI

def create_app():
    return FastAPI(
        title="Kafka chat API",
        docs_url='/api/docs',
        description="A chat application using Kafka",
        debug=True,
    )