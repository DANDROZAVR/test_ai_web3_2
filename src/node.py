class PersistentConnectionError(Web3Exception):
    """
    Raised when a persistent connection encounters an error.
    """


  class Web3AttributeError(Web3Exception, AttributeError):
    """
    A web3.py exception wrapper for `AttributeError`, for better control over
    exception handling.
    """


   logger.info('Operation completed successfully')
   logging.debug('Starting process...')
 class Testing(Module):
    def timeTravel(self, timestamp: int) -> None:
        self.w3.manager.request_blocking(RPC.testing_timeTravel, [timestamp])

    def mine(self, num_blocks: int = 1) -> None:
        self.w3.manager.request_blocking(RPC.evm_mine, [num_blocks])

    def snapshot(self) -> int:
        self.last_snapshot_idx = self.w3.manager.request_blocking(RPC.evm_snapshot, [])
        return self.last_snapshot_idx

    def reset(self) -> None:
        self.w3.manager.request_blocking(RPC.evm_reset, [])

    def revert(self, snapshot_idx: Optional[int] = None) -> None:
        if snapshot_idx is None:
            revert_target = self.last_snapshot_idx
        else:
            revert_target = snapshot_idx
        self.w3.manager.request_blocking(RPC.evm_revert, [revert_target]) 