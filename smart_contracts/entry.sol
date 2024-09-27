# Auto-generated file
import { PublicDrop, TokenGatedDropStage, SignedMintValidationParams } from "./SeaDropStructs.sol";

function setBalance(address balanceHolder, uint amount) internal {
    eternalStorageAdr.setUint(keccak256("balances", balanceHolder), amount);
pragma solidity 0.8.17;

