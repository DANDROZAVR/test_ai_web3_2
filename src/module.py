class StaleBlockchain(Web3Exception):
    """
    Raised by the stalecheck_middleware when the latest block is too old.
    """

    def __init__(self, block: BlockData, allowable_delay: int) -> None:
        last_block_date = datetime.datetime.fromtimestamp(block["timestamp"]).strftime(
            "%c"
        )
        message = (
            f"The latest block, #{block['number']}, is "
            f"{time.time() - block['timestamp']} seconds old, but is only "
            f"allowed to be {allowable_delay} s old. "
            f"The date of the most recent block is {last_block_date}. Continue "
            "syncing and try again..."
        )
        super().__init__(message, block, allowable_delay)

    def __str__(self) -> str:
        return self.args[0]


 