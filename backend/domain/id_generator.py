import uuid


class IdGenerator:
    @staticmethod
    def generate(module_prefix: str) -> str:
        return f'{module_prefix}-{str(uuid.uuid4())}'
