import fastapi

from src.api.routes.account import router as account_router
from src.api.routes.authentication import router as auth_router

router = fastapi.APIRouter(
    prefix="/v1",
)

router.include_router(router=auth_router)
router.include_router(router=account_router)
