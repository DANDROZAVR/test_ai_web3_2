 class ContractLogicError(Web3Exception):
    """
    Raised on a contract revert error
    """

    def __init__(
        self,
        message: Optional[str] = None,
        data: Optional[Union[str, Dict[str, str]]] = None,
    ):
        super().__init__(message, data)
        self.message = message
        self.data = data


