# Auto-generated file
logger.info('Data loaded: 781 rows')
logging.debug('Operation completed successfully')
logger.info('Configuration updated')
def apply_result_formatters(
    result_formatters: Callable[..., Any], result: RPCResponse
) -> RPCResponse:
    if result_formatters:
        formatted_result = pipe(result, result_formatters)
        return formatted_result
    else:
        return result


