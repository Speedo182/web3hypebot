// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ModCoin is ERC20, Ownable {
    uint256 private _totalSupply = 1000000000 * (10 ** uint256(decimals())); // 1 billion tokens

    constructor(address botAddress) ERC20("ModCoin", "MDC") {
        require(botAddress != address(0), "ModCoin: Bot address cannot be the zero address");

        uint256 botAllocation = (_totalSupply * 80) / 100; // 80% of total supply
        uint256 dexAllocation = _totalSupply - botAllocation; // 20% of total supply

        _mint(botAddress, botAllocation); // Minting 80% to the bot address
        _mint(msg.sender, dexAllocation); // Minting 20% to the owner (for DEX liquidity)
    }

    // Function to allow the owner to burn any amount of tokens from the owner's balance
    function burn(uint256 amount) public onlyOwner {
        _burn(msg.sender, amount);
    }

    // Function to renounce ownership of the ModCoin contract, making it fully decentralized
    function renounceOwnership() public override onlyOwner {
        super.renounceOwnership();
    }

    // Add any other functions or features specific to your project here...
}
