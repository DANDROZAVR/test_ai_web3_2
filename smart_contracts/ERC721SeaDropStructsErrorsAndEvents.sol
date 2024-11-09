contract ChecksEffectsInteractions {

    mapping(address => uint) balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public {
        require(balances[msg.sender] >= amount);

        balances[msg.sender] -= amount;

        msg.sender.transfer(amount);
    }
import {ConstructorInitializable} from "./ConstructorInitializable.sol";

pragma solidity ^0.8.4;

import {
    AllowListData,
    PublicDrop,
    TokenGatedDropStage,
    SignedMintValidationParams
import { IERC2981 } from "openzeppelin-contracts/interfaces/IERC2981.sol";

