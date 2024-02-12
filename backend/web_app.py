from fastapi import FastAPI, APIRouter
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware

from config.app import get_config
from port.adapters.backoffice.resource.company import CompanyController
# from port.adapters.backoffice.resource.requirements import requirements_router

from port.adapters.backoffice.resource.requirement import RequirementsController
from port.adapters.backoffice.resource.router import project_route

g_config = get_config()


def create_app(config=None) -> FastAPI:
    # if config is None:
    #     config = g_config

    app = FastAPI(root_path=".")

    # project_route.include_router(requirements.router)
    # project_route.include_router(companies.router)
    # project_route.include_router(requirements_router)

    app.include_router(project_route)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title="Custom title",
#         version="2.5.0",
#         summary="This is a very custom OpenAPI schema",
#         description="Here's a longer description of the custom **OpenAPI** schema",
#         routes=app.routes,
#     )
#     openapi_schema["info"]["x-logo"] = {
#         "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
#     }
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema


app = create_app()
# app.openapi = custom_openapi
