 class InvalidTransaction(Web3Exception):
    """
    Raised when a transaction includes an invalid combination of arguments.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


from web3.module import (
    Module,
)
class NoABIEventsFound(Web3Exception):
    """
    Raised when an ABI doesn't contain any events.
    """


