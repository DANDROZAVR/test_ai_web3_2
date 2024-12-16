class NameNotFound(Web3Exception):
    """
    Raised when a caller provides an Ethereum Name Service name that
    does not resolve to an address.
    """


from web3.net import (
    AsyncNet,
    Net,
)
class MethodUnavailable(Web3RPCError):
    """
    Raised when the method is not available on the node
    """


from web3.providers import (
    AsyncBaseProvider,
    BaseProvider,
)
