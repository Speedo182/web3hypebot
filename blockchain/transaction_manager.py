# blockchain/transaction_manager.py

from solana.rpc.api import Client
from solana.system_program import TransferParams, transfer
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.transaction import Transaction

class TransactionManager:
    def __init__(self, client: Client):
        self.client = client

    def send_transaction(self, sender_keypair: Keypair, receiver_pubkey: PublicKey, amount: int):
        # Get the recent blockhash
        recent_blockhash = self.client.get_recent_blockhash()["result"]["value"]["blockhash"]

        # Create a transaction
        transaction = Transaction()
        transaction.add(transfer(
            TransferParams(
                from_pubkey=sender_keypair.public_key(),
                to_pubkey=receiver_pubkey,
                lamports=amount
            )
        ))

        # Assign the blockhash to the transaction
        transaction.recent_blockhash = recent_blockhash

        # Sign the transaction with the sender's keypair
        transaction.sign(sender_keypair)

        try:
            # Send the transaction
            response = self.client.send_transaction(transaction)
            return response
        except Exception as e:
            print(f"Transaction failed: {e}")
            return None
        def airdrop_tokens(self, recipient_pubkey: PublicKey, amount: int):
        try:
            response = self.client.request_airdrop(
                wallet_address=recipient_pubkey,
                lamports=amount,
                commitment="finalized"
            )
            return response
        except Exception as e:
            print(f"Airdrop failed: {e}")
            return None

    def check_transaction_status(self, signature):
        # Check the status of a transaction using its signature
        try:
            status = self.client.get_confirmed_transaction(signature)["result"]
            if status:
                return status["meta"]["status"]
            return "Transaction not found or pending"
        except Exception as e:
            print(f"Error checking transaction status: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Initialize Solana RPC client
    solana_client = Client("https://api.mainnet-beta.solana.com")

    # Initialize the transaction manager with the client
    tx_manager = TransactionManager(solana_client)

    # Example: Sending SOL from one account to another
    # This requires the sender's Keypair object and the receiver's public key
    sender = Keypair()  # Assume this is already generated or loaded
    receiver = PublicKey('RECEIVER_PUBLIC_KEY')  # Replace with actual receiver public key
    tx_signature = tx_manager.send_transaction(sender, receiver, 10000000)  # Sending 0.01 SOL

    if tx_signature:
        print(f"Transaction submitted with signature: {tx_signature}")

    # Checking the status of the transaction
    status = tx_manager.check_transaction_status(tx_signature)
    print(f"Transaction status: {status}")

        # Checking airdrop status
    airdrop_signature = tx_manager.airdrop_tokens(receiver, 100000000)  # Airdropping 0.1 SOL
    if airdrop_signature:
        print(f"Airdrop transaction submitted with signature: {airdrop_signature}")
        # Checking the status of the airdrop transaction
        airdrop_status = tx_manager.check_transaction_status(airdrop_signature)
        print(f"Airdrop transaction status: {airdrop_status}")
    else:
        print("Airdrop transaction failed.")

# End of transaction_manager.py

# Note: The example usage here is for demonstration purposes. In a real-world scenario,
# proper error handling, validation, and secure management of keys are crucial.

# This completes the 'transaction_manager.py' file.
