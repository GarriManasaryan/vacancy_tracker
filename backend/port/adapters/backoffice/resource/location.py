from application.location_service import LocationService
from domain.repo.location_repo import LocationRepo
from port.adapters.backoffice.location_model import (
    LocationCreationRequest,
    LocationBackofficeModel,
)


class LocationController:
    def __init__(self, repo: LocationRepo) -> None:
        self.service = LocationService(repo=repo)

    def save(self, creation_request: LocationCreationRequest) -> None:
        self.service.save(creation_request=creation_request)

    def all(self) -> list[LocationBackofficeModel]:
        return self.service.all()
