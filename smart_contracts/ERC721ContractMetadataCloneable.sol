 contract ERC721SeaDropCloneable is
    ERC721ContractMetadataCloneable,
    INonFungibleSeaDropToken,
    ERC721SeaDropStructsErrorsAndEvents,
    ReentrancyGuardUpgradeable
