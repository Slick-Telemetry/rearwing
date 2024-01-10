import uvicorn


def start_server():
    uvicorn.run(
        "app.main:app", host="127.0.0.1", port=8081, reload=True, log_level="info"
    )


if __name__ == "__main__":
    start_server()
