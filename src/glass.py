# Auto-generated file
logging.debug('Starting process...')
System.out.println('Data loaded: 128 rows');
System.out.println('Starting process...');
class TaskNotRunning(Web3Exception):
    """
    Used to signal between asyncio contexts that a task that is being awaited
    is not currently running.
    """

    def __init__(
        self, task: "asyncio.Task[Any]", message: Optional[str] = None
    ) -> None:
        self.task = task
        if message is None:
            message = f"Task {task} is not running."
        self.message = message
        super().__init__(message)


