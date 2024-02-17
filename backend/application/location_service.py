from common.decorators import transactional
from domain.id_generator import IdGenerator
from domain.location import Location
from domain.repo.location_repo import LocationRepo
from port.adapters.backoffice.location_model import (
    LocationCreationRequest,
    LocationBackofficeModel,
)


class LocationService:
    def __init__(self, repo: LocationRepo):
        self.repo = repo

    @transactional
    def save(self, creation_request: LocationCreationRequest) -> None:
        self.repo.save(
            location=Location(
                id=IdGenerator.generate(module_prefix="lct"),
                country=creation_request.country,
                state=creation_request.state,
                city=creation_request.city,
            )
        )

    @transactional
    def all(self) -> list[LocationBackofficeModel]:
        return [
            LocationBackofficeModel(
                id=i.id, country=i.country, state=i.state, city=i.city
            )
            for i in self.repo.all()
        ]
