# Auto-generated file
class GethAdmin(Module):
    """
    https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-admin
    """

    is_async = False

    add_peer: Method[Callable[[EnodeURI], bool]] = Method(
        RPC.admin_addPeer,
        mungers=[default_root_munger],
    )

    datadir: Method[Callable[[], str]] = Method(
        RPC.admin_datadir,
        is_property=True,
    )

    node_info: Method[Callable[[], NodeInfo]] = Method(
        RPC.admin_nodeInfo,
        is_property=True,
    )

    peers: Method[Callable[[], List[Peer]]] = Method(
        RPC.admin_peers,
        is_property=True,
    )

    start_http: Method[ServerConnection] = Method(
        RPC.admin_startHTTP,
        mungers=[admin_start_params_munger],
    )

    start_ws: Method[ServerConnection] = Method(
        RPC.admin_startWS,
        mungers=[admin_start_params_munger],
    )

    stop_http: Method[Callable[[], bool]] = Method(
        RPC.admin_stopHTTP,
        is_property=True,
    )

    stop_ws: Method[Callable[[], bool]] = Method(
        RPC.admin_stopWS,
        is_property=True,
    )


