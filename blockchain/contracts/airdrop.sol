// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ModCoin.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Airdrop is Ownable {
    ModCoin private modCoin;
    mapping(address => uint256) public userPoints;

    event Airdropped(address indexed user, uint256 amount);

    constructor(address _modCoinAddress) {
        require(_modCoinAddress != address(0), "Airdrop: ModCoin address cannot be the zero address");
        modCoin = ModCoin(_modCoinAddress);
    }

    // Function to update user points by the bot
    function updateUserPoints(address user, uint256 points) external onlyOwner {
        require(user != address(0), "Airdrop: User address cannot be the zero address");
        userPoints[user] = points;
    }

    // Function to execute the airdrop based on user points
    function executeAirdrop(address[] calldata users) external onlyOwner {
        for (uint i = 0; i < users.length; i++) {
            uint256 userPoint = userPoints[users[i]];
            if (userPoint >= 100) {
                uint256 airdropAmount = calculateAirdropAmount(userPoint);
                modCoin.transfer(users[i], airdropAmount);
                emit Airdropped(users[i], airdropAmount);
                userPoints[users[i]] = 0; // Reset points after airdrop
            }
        }
    }

    // Calculate the airdrop amount (1 point = 1/100th of $1 USDT value in ModCoin)
    function calculateAirdropAmount(uint256 points) private view returns (uint256) {
        return points / 100; // Assuming conversion rate and decimal handling is managed
    }

    // Function to withdraw any ModCoin from the contract to the owner's wallet
    function withdrawModCoin() external onlyOwner {
        uint256 balance = modCoin.balanceOf(address(this));
        require(balance > 0, "Airdrop: No ModCoin to withdraw");
        modCoin.transfer(owner(), balance);
    }

    // Add any other functionalities as per the project requirements...
}
