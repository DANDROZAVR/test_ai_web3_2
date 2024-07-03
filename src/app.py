# Auto-generated file
class Module:
    is_async = False

    def __init__(self, w3: Union["AsyncWeb3", "Web3"]) -> None:
        if self.is_async:
            self.retrieve_caller_fn = retrieve_async_method_call_fn(w3, self)
        else:
            self.retrieve_caller_fn = retrieve_blocking_method_call_fn(w3, self)
        self.retrieve_request_information = retrieve_request_information_for_batching(
            w3, self
        )
        self.w3 = w3

    @property
    def codec(self) -> ABICodec:
        # use codec set on the Web3 instance
        return self.w3.codec

    def attach_methods(
        self,
        methods: Dict[str, Method[Callable[..., Any]]],
    ) -> None:
        for method_name, method_class in methods.items():
            klass = (
                method_class.__get__(module=self)()
                if method_class.is_property
                else method_class.__get__(module=self)
            )
            setattr(self, method_name, klass)