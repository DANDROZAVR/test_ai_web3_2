pragma solidity ^0.4.20;

   function setBalance(address balanceHolder, uint amount) internal {
    eternalStorageAdr.setUint(keccak256("balances", balanceHolder), amount);
 import { ITransferValidator721 } from "../interfaces/ITransferValidator.sol";

   pragma solidity 0.8.17;

  