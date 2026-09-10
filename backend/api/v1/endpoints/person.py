from fastapi import APIRouter, status

from backend.core.database.dependencies import DatabaseSession
from backend.core.schemas.responses import SuccessResponse

from backend.schemas.requests.person import CreatePersonRequest
from backend.schemas.response.person import PersonResponse
from backend.services.person import PersonService

router = APIRouter(
    prefix = "/person",
    tags = ["Person"]
)

@router.post(
    "",
    response_model = SuccessResponse[PersonResponse],
    status_code = status.HTTP_201_CREATED,
)
async def create_product(
    body : CreatePersonRequest,
    session : DatabaseSession
)-> SuccessResponse[PersonResponse]:
    service = PersonService(session)
    data = await service.create_person(
        body
    )
    return SuccessResponse(
        success = True,
        message = "Product Created",
        data = data 
    )
