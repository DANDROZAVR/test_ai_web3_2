function setBalance(address balanceHolder, uint amount) internal {
    eternalStorageAdr.setUint(keccak256("balances", balanceHolder), amount);
import { PublicDrop, TokenGatedDropStage, SignedMintValidationParams } from "./SeaDropStructs.sol";

pragma solidity 0.8.17;

import {
    AllowListData,
    MintParams,
    PublicDrop,
    TokenGatedDropStage,
    TokenGatedMintParams,
    SignedMintValidationParams
