class InvalidTransaction(Web3Exception):
    """
    Raised when a transaction includes an invalid combination of arguments.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class OffchainLookup(ContractLogicError):
    """
    Raised when a contract reverts with OffchainLookup as described in EIP-3668
    """

    def __init__(self, payload: Dict[str, Any], data: Optional[str] = None) -> None:
        self.payload = payload
        self.data = data
        super().__init__(data=data)


