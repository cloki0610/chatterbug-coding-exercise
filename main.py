import requests
from fastapi import Body, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils import generate_password, is_valid_lat_long

app = FastAPI()


# Class for validate password input
class PasswordOptions(BaseModel):
    length: int = Body(..., gt=0)
    lowercase: bool = True
    uppercase: bool = True
    digits: bool = True
    symbols: bool = True


# Routers
@app.get("/", summary="Redirect user to the build in docs page.")
def index():
    """Redirect user to the /docs endpoint"""
    return RedirectResponse("/docs")


@app.post(
    "/generate-password",
    summary="Accept input payload then generate a new password as response with required length.",
    response_description="The new password as string in required length",
)
async def generate_password_endpoint(options: PasswordOptions = Body(...)):
    """
    API endpoint to generate a password.
    """
    try:
        password = generate_password(
            options.length,
            options.lowercase,
            options.uppercase,
            options.digits,
            options.symbols,
        )
        return JSONResponse(
            status_code=200, content={"password": password, "length": options.length}
        )
    except (TypeError, ValueError) as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.get(
    "/weather/",
    summary="Get weather data from open-meteo Weather Forcast API",
    response_description="Response data from open-meteo Weather Forcast API with time and temperature",
)
async def get_weather(lat: int = 0, lon: int = 0):
    """
    Fetches weather data(temperature) by latitude and longtitude using open-meteo Weather Forcast API.
    """
    if not is_valid_lat_long(lat, lon):
        raise HTTPException(
            status_code=422, detail="Invalid latitude or longitude values"
        )
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return JSONResponse(status_code=200, content=data)
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail="Failed to retrieve weather data",
            )
    except (ValueError, HTTPException) as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.exception_handler(HTTPException)
def http_exception_handler(_: Request, exc: HTTPException):
    """HTTPException handler"""
    return JSONResponse(
        status_code=422, content={"details": exc, "type": "HTTPException"}
    )
