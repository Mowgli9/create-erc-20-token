from scripts.helpful_script import getAccount
from brownie import Token
from web3 import Web3


hom_much_token_you_want_to_creat = 1000000 # 1 million 
token_name = "Token"
token_symbole = "TKN"

def deploy():
    account = getAccount() # get an account => {helpful_script}
    totalsupply  = Web3.toWei(hom_much_token_you_want_to_creat,"ether") # convert to wei
    # deploy the contract we passing parameters for constructor
    deployedContract = Token.deploy(totalsupply,token_name,token_symbole,{"from":account})
    print(f"Succefully deployed ! now you're the owner of {token_name}")
    balance = Web3.fromWei(deployedContract.balanceOf(account.address),'ether')
    print(f"and you have {balance} of it ")


def main():
    deploy()