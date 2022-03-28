// YouToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token is ERC20 {
    constructor(uint256 initialSupply,string memory tokenName, string memory tokenSymbole) ERC20(tokenName,tokenSymbole) {
        _mint(msg.sender, initialSupply);
    }
}