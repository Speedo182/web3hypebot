pragma solidity ^0.8.0;

import "./ModCoin.sol";
import "@solana/solana-program-library"; // Fictitious import for SPL compatibility, not real.

contract Airdrop {
    ModCoin public modCoin;
    address public owner;

    struct AirdropCampaign {
        address tokenAddress;
        uint256 amount;
        uint256 startTime;
        uint256 endTime;
        bool isActive;
    }

    AirdropCampaign[] public campaigns;

    event NewCampaign(address indexed token, uint256 amount, uint256 startTime, uint256 endTime);
    event Airdropped(address indexed recipient, address indexed token, uint256 amount);

    constructor(address _modCoinAddress) {
        modCoin = ModCoin(_modCoinAddress);
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this");
        _;
    }

    function startCampaign(address _tokenAddress, uint256 _amount, uint256 _duration) external onlyOwner {
        uint256 endTime = block.timestamp + _duration;
        campaigns.push(AirdropCampaign({
            tokenAddress: _tokenAddress,
            amount: _amount,
            startTime: block.timestamp,
            endTime: endTime,
            isActive: true
        }));
        emit NewCampaign(_tokenAddress, _amount, block.timestamp, endTime);
    }

    function executeAirdrop(uint256 _campaignIndex, address[] calldata _recipients) external onlyOwner {
        AirdropCampaign storage campaign = campaigns[_campaignIndex];
        require(campaign.isActive, "Campaign is not active");
        require(block.timestamp <= campaign.endTime, "Campaign has ended");
        require(_recipients.length > 0, "No recipients provided");

        uint256 amountPerRecipient = campaign.amount / _recipients.length;

        for (uint i = 0; i < _recipients.length; i++) {
            // Implement SPL token transfer if not ModCoin
            if (campaign.tokenAddress == address(modCoin)) {
                modCoin.transfer(_recipients[i], amountPerRecipient);
            } else {
                // Fictitious function to handle SPL token transfers, not real.
                SPLTransfer(campaign.tokenAddress, _recipients[i], amountPerRecipient);
            }
            emit Airdropped(_recipients[i], campaign.tokenAddress, amountPerRecipient);
        }
        campaign.isActive = false;
    }

    // Fictitious function for SPL token transfer
    function SPLTransfer(address token, address to, uint256 amount) private {
        // Implementation for SPL token transfer
        // Note: This part of the code is fictional as Solidity is not used for SPL token transfers.
    }

    // Function to withdraw ModCoin from the contract
    function withdrawModCoin(uint256 _amount) external onlyOwner {
        modCoin.transfer(owner, _amount);
    }
}
