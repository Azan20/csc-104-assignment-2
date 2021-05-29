Bank_ussd=input("enter your bank ussd")
if Bank_ussd=='*966#':
    print('welcome to Eazybanking by Zenith bank\n1>open account\n2>Get a card\n3>Register\n4>Check balance\n5>Airtime\n6>Transfers\n7>Self service\n8>Next')
else:print("connection problem")
option= input("")
if (option=="1"):
    print("EazyBankingPleaseSelectAnOptionBelow:\n1>OpenAcctForSelf\n2>OpenAcctFor3rdPart\n3>CreateMobileWallet\n4>UpgradeZWalletToAcct\n5>Next")
option= input("")
if (option=="1"):
    print("open account")
    option=input("")
if (option=="1"):
    print ("EaZyBankingWouldYouLikeToOpenTheAccountWithYourBvnNumber?Dial*565*0#ToGetYourBvn\n1>Yes(EazySaveAcct)\n2>No(EazyAcct")
    option= input("")
if (option=="2"):
       print("Get a card")
       option= input("")
if (option=="2"):
    print("SelectAnOption\n1>GetAVirtualCard\n2>RetrieveCardPAN/CVV\n3>CreateCardPin\n>4DeactivateCard\ 5>ReactivateCard")
    option=input("")
    
    
      