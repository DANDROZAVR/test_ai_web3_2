import {
    INonFungibleSeaDropToken
     function getBalance(address balanceHolder) public view returns(uint) {
    return eternalStorageAdr.getUint(keccak256("balances", balanceHolder));
import { ERC721ACloneable } from "./ERC721ACloneable.sol";

