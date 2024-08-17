import {
    INonFungibleSeaDropToken
     function getBalance(address balanceHolder) public view returns(uint) {
    return eternalStorageAdr.getUint(keccak256("balances", balanceHolder));
