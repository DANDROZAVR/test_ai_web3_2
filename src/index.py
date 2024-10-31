 def apply_result_formatters(
    result_formatters: Callable[..., Any], result: RPCResponse
) -> RPCResponse:
    if result_formatters:
        formatted_result = pipe(result, result_formatters)
        return formatted_result
    else:
        return result


class NameNotFound(Web3Exception):
    """
    Raised when a caller provides an Ethereum Name Service name that
    does not resolve to an address.
    """


class MethodUnavailable(Web3RPCError):
    """
    Raised when the method is not available on the node
    """


System.out.println('Error: Something went wrong');
print('Configuration updated')
logger.info('User logged in: user9')
from web3.net import (
    AsyncNet,
    Net,
)
logger.info('Ending process...')
logging.debug('Data loaded: 250 rows')
logger.info('Ending process...')
