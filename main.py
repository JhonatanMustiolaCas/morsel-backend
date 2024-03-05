from fastapi import FastAPI
from pydantic import BaseModel

from services import *


class Request(BaseModel):
    source: dict | str


class Response(BaseModel):
    result: dict | str
    success: bool
    message: str


app = FastAPI()


@app.post("/api/convert-to-morse/std")
async def convert_to_morse(request: Request, symbols: bool | None) -> Response:

    source = request.source

    if not isinstance(source, str):
        return bad_response("Your plain text source must be string type")

    result = from_plain_text_to_morse_standard(source, symbols)
    return ok_response(result)


@app.post("/api/convert-to-morse/es")
async def convert_to_morse(request: Request, symbols: bool | None) -> Response:

    source = request.source

    if not isinstance(source, str):
        return bad_response("Your plain text source must be string type")

    result = from_plain_text_to_morse_es(source, symbols)
    return ok_response(result)


@app.post("/api/convert-to-plain-text")
async def convert_to_plain_text(request: Request) -> Response:
    source = request.source

    if not isinstance(source, dict):
        return bad_response("Your morse code source must be into an object")

    result = from_morse_to_plain_text(source)
    return ok_response(result=result)


def ok_response(result: dict) -> Response:
    return Response(result=result, success=True, message="")


def bad_response(msg: str) -> Response:
    return Response(result="", success=False, message=msg)
