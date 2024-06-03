from fastapi import FastAPI
from routers import tasks as task_router, health as health_router
from configuration import configuration


app = FastAPI(
    title="Task API",
    summary="Task CRUD REST API.",
    version="1.0.0",
    openapi_tags=[
        health_router.health_tags_metadata,
        task_router.tasks_tags_metadata,
    ],
    redoc_url=None,
)
app.include_router(health_router.router, prefix="/api/tasks", tags=["health"])
app.include_router(task_router.router, prefix="/api/tasks", tags=["tasks"])


def main():
    import uvicorn

    configuration.configure()
    uvicorn.run("main:app", host="127.0.0.1", port=8081, reload=True)


if __name__ == "__main__":
    main()
