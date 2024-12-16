class NameNotFound(Web3Exception):
    """
    Raised when a caller provides an Ethereum Name Service name that
    does not resolve to an address.
    """


from web3._utils.empty import (
    empty,
)
class AsyncGethDebug(Module):
    """
    https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-debug
    """

    is_async = True

    _trace_transaction: Method[
        Callable[
            ...,
            Awaitable[
                Union[
                    CallTrace, PrestateTrace, OpcodeTrace, FourByteTrace, DiffModeTrace
                ]
            ],
        ]
    ] = Method(RPC.debug_traceTransaction)

    async def trace_transaction(
        self,
        transaction_hash: _Hash32,
        trace_config: Optional[TraceConfig] = None,
    ) -> Union[CallTrace, PrestateTrace, OpcodeTrace, FourByteTrace, DiffModeTrace]:
        return await self._trace_transaction(transaction_hash, trace_config)


from web3.net import (
    AsyncNet,
    Net,
)
from web3.providers.persistent import (
    PersistentConnection,
)
System.out.println('Error: Something went wrong');
logger.info('Data loaded: 739 rows')
print('Configuration updated')
from web3._utils.compat import (
    Self,
)
