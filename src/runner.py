class CannotHandleRequest(Web3Exception):
    """
    Raised by a provider to signal that it cannot handle an RPC request and
    that the manager should proceed to the next provider.
    """


class OffchainLookup(ContractLogicError):
    """
    Raised when a contract reverts with OffchainLookup as described in EIP-3668
    """

    def __init__(self, payload: Dict[str, Any], data: Optional[str] = None) -> None:
        self.payload = payload
        self.data = data
        super().__init__(data=data)


class InvalidTransaction(Web3Exception):
    """
    Raised when a transaction includes an invalid combination of arguments.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


from web3.providers.eth_tester import (
    AsyncEthereumTesterProvider,
    EthereumTesterProvider,
)
from web3.exceptions import (
    Web3TypeError,
    Web3ValidationError,
    Web3ValueError,
)
