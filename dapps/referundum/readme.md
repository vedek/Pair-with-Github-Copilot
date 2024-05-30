# Referendum dApp

A decentralized application (dApp) for creating and voting on proposals using Ethereum blockchain.

## Features
- Create proposals.
- Vote on proposals.
- View the winning proposal.

## Prerequisites

- Node.js and npm installed.
- MetaMask extension installed and configured.
- Solidity compiler (solc) installed.

## Smart Contract

1. Deploy the Solidity smart contract on an Ethereum test network (e.g., Rinkeby).

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Referendum {
    struct Proposal {
        string description;
        uint voteCount;
    }

    struct Voter {
        bool voted;
        uint proposalIndex;
    }

    address public chairperson;
    Proposal[] public proposals;
    mapping(address => Voter) public voters;

    constructor(string[] memory proposalNames) {
        chairperson = msg.sender;
        for (uint i = 0; i < proposalNames.length; i++) {
            proposals.push(Proposal({
                description: proposalNames[i],
                voteCount: 0
            }));
        }
    }

    modifier onlyChairperson() {
        require(msg.sender == chairperson, "Only chairperson can call this function.");
        _;
    }

    function giveRightToVote(address voter) public onlyChairperson {
        require(!voters[voter].voted, "The voter already voted.");
        voters[voter].voted = false;
    }

    function vote(uint proposalIndex) public {
        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "Already voted.");
        require(proposalIndex < proposals.length, "Invalid proposal index.");
        
        sender.voted = true;
        sender.proposalIndex = proposalIndex;

        proposals[proposalIndex].voteCount += 1;
    }

    function winningProposal() public view returns (uint winningProposalIndex) {
        uint winningVoteCount = 0;
        for (uint i = 0; i < proposals.length; i++) {
            if (proposals[i].voteCount > winningVoteCount) {
                winningVoteCount = proposals[i].voteCount;
                winningProposalIndex = i;
            }
        }
    }

    function winnerName() public view returns (string memory winnerName_) {
        winnerName_ = proposals[winningProposal()].description;
    }
}
