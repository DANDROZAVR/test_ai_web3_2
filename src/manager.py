 def _validate_response(
    response: RPCResponse,
    error_formatters: Optional[Callable[..., Any]],
    is_subscription_response: bool = False,
    logger: Optional[logging.Logger] = None,
    params: Optional[Any] = None,
) -> None:
    if "jsonrpc" not in response or response["jsonrpc"] != "2.0":
        _raise_bad_response_format(
            response, 'The "jsonrpc" field must be present with a value of "2.0".'
        )

    response_id = response.get("id")
    if "id" in response:
        int_error_msg = (
            '"id" must be an integer or a string representation of an integer.'
        )
        if response_id is None and "error" in response:
            # errors can sometimes have null `id`, according to the JSON-RPC spec
            pass
        elif not isinstance(response_id, (str, int)):
            _raise_bad_response_format(response, int_error_msg)
        elif isinstance(response_id, str):
            try:
                int(response_id)
            except ValueError:
                _raise_bad_response_format(response, int_error_msg)
    elif is_subscription_response:
        # if `id` is not present, this must be a subscription response
        _validate_subscription_fields(response)
    else:
        _raise_bad_response_format(
            response,
            'Response must include an "id" field or be formatted as an '
            "`eth_subscription` response.",
        )

    if all(key in response for key in {"error", "result"}):
        _raise_bad_response_format(
            response, 'Response cannot include both "error" and "result".'
        )
    elif (
        not any(key in response for key in {"error", "result"})
        and not is_subscription_response
    ):
        _raise_bad_response_format(
            response, 'Response must include either "error" or "result".'
        )
    elif "error" in response:
        web3_rpc_error: Optional[Web3RPCError] = None
        error = response["error"]

        # raise the error when the value is a string
        if error is None or not isinstance(error, dict):
            _raise_bad_response_format(
                response,
                'response["error"] must be a valid object as defined by the '
                "JSON-RPC 2.0 specification.",
            )

        # errors must include a message
        error_message = error.get("message")
        if not isinstance(error_message, str):
            _raise_bad_response_format(
                response, 'error["message"] is required and must be a string value.'
            )
        elif error_message == "transaction not found":
            transaction_hash = params[0]
            web3_rpc_error = TransactionNotFound(
                repr(error),
                rpc_response=response,
                user_message=(f"Transaction with hash {transaction_hash!r} not found."),
            )

        # errors must include an integer code
        code = error.get("code")
        if not isinstance(code, int):
            _raise_bad_response_format(
                response, 'error["code"] is required and must be an integer value.'
            )
        elif code == METHOD_NOT_FOUND:
            web3_rpc_error = MethodUnavailable(
                repr(error),
                rpc_response=response,
                user_message=(
                    "This method is not available. Check your node provider or your "
                    "client's API docs to see what methods are supported and / or "
                    "currently enabled."
                ),
            )
        elif any(
            # parse specific timeout messages
            timeout_str in error_message.lower()
            for timeout_str in KNOWN_REQUEST_TIMEOUT_MESSAGING
        ):
            web3_rpc_error = RequestTimedOut(
                repr(error),
                rpc_response=response,
                user_message=(
                    "The request timed out. Check the connection to your node and "
                    "try again."
                ),
            )

        if web3_rpc_error is None:
            # if no condition was met above, raise a more generic `Web3RPCError`
            web3_rpc_error = Web3RPCError(repr(error), rpc_response=response)

        response = apply_error_formatters(error_formatters, response)

        logger.error(web3_rpc_error.user_message)
        logger.debug(f"RPC error response: {response}")
        raise web3_rpc_error

    elif "result" not in response and not is_subscription_response:
        _raise_bad_response_format(response)


