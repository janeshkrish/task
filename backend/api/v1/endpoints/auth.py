from fastapi import APIRouter

from backend.core.database.dependencies import DatabaseSession
from backend.schemas.requests.auth import LoginRequest
from backend.schemas.response.auth import LoginResponse
from backend.core.schemas.responses import SuccessResponse
from backend.services.auth import AuthService

router = APIRouter(
    prefix="/auth",
    rags = ["Auth"]
)

@router.post(
    "/login",
    response_model = LoginResponse
)
async def login(
    body : LoginRequest,
    session : DatabaseSession
) ->  LoginResponse:
    service = AuthService(session)
    data = await service().login(
        body
    )
    return SuccessResponse(
        success = True,
        message = "Login Successfully",
        data = data 
    )