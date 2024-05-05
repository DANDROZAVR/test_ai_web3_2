class PersistentConnectionError(Web3Exception):
    """
    Raised when a persistent connection encounters an error.
    """


  class Web3AttributeError(Web3Exception, AttributeError):
    """
    A web3.py exception wrapper for `AttributeError`, for better control over
    exception handling.
    """


 