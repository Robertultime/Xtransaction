import smartpy as sp

#importation de la librairy fa2 permettant de générer des tokens fongibles ou non fongibles
fa2 = sp.io.import_template("fa2_lib.py")
testing = sp.io.import_template("fa2_lib_testing.py")

#Permet de stocker sous forme de json les métadatas concernant le produit
def make_metadata(serieSize,
                 name,
                 description,
                 brand,
                 thumbnailUri,
                 home,
                 inceptionDate,
                 inceptionPriceEUR
                 ):
    return sp.big_map(
        l={
            #serieSize: indique le nombre de produit créé pour la série
            "serieSize": sp.utils.bytes_of_string("%d" % serieSize), 

            #nom: indique le nom du produit               
            "name": sp.utils.bytes_of_string(name),
            "description": sp.utils.bytes_of_string(description),

            #brand: donne la marque du produit
            "brand":sp.utils.bytes_of_string(brand),

            #thumbnailUri: image du produit stocké sur le protocole ipfs
            "thumbnailUri": sp.utils.bytes_of_string(thumbnailUri),

            #home: redirige vers le site web de la marque concernant le produit
            "home":sp.utils.bytes_of_string(home),

            #inceptionDate: date de lancement du produit
            "inceptionDate":sp.utils.bytes_of_string(inceptionDate),
            
            #inceptionPriceEUR: donne le prix du produit en euro à son lancement, 
            "inceptionPriceEUR":sp.utils.bytes_of_string("%d" % inceptionPriceEUR)
        }
    )

if "templates" not in __name__:

    #creation des comptes de test
    admin = sp.test_account("Administrator")
    alice = sp.test_account("Alice")
    serieSize = 12
    name = "Sac Plume fourre-tout 45 chimères Pégase"

    TOKEN_METADATA = []
    ledger={}

    #creation des tokens pour chaque produits de la série
    for id in range(serieSize):
        token= fa2.make_metadata(name=name+" "+str(id), decimals=1, symbol="Tok"+str(id))
        TOKEN_METADATA.append(token)
        ledger[id] = alice.address
    
    #adresse des métadatas concernant la série, stocké sur ipfs
    METADATA = sp.utils.metadata_of_url("ipfs://QmSmXTAHscg9Wrfr3S1qMa1hAhPFtmKpfFosW5dNuLMeAF")


    def _pre_minter(base_class=fa2.Fa2Nft, policy=None):
        token_metadata = TOKEN_METADATA
        return base_class(
            metadata=METADATA,
            token_metadata=token_metadata,
            ledger=ledger,
            policy=policy,
        )

    # Standard features
    for _Fa2 in [fa2.Fa2Nft]:
        testing.test_core_interfaces(_pre_minter(_Fa2))
