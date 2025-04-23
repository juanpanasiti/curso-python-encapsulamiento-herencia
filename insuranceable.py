from typing import Optional


class Insuranceable():  # "Asegurable"
    def __init__(self, policy_number: Optional[str] = ''):
        self._policy_number: str = policy_number

    @property
    def policy_number(self) -> str:
        return self._policy_number

    @policy_number.setter
    def policy_number(self, policy_number: str) -> None:
        self._policy_number = policy_number
