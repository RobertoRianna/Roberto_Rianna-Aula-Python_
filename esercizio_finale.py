import modulo_esercizio_finale as ES1
#TEMPO SUDDIVISIONE ESERCIZIO
#PARTE 1 = PREVISTA:25 MINUTI/EFFETTIVA: 30 MINUTI
#PARTE 2 = PREVISTA =35 MINUTI/EFFETTIVA 30 MINUTI
#PARTE 3 = PREVISTA=45 MINUTI/EFFETTIVA 45 MINUTI
#PARTE 4 = PREVISTA=60 MINUTI/ EFFETTIVA 30 MINUTI
#DIVISIONE IN MODULO,CREAZIONE MENU = EFFETTIVA 20 MINUTI


def menù():                                                                                         
    controllo = True                                                                                 
    while controllo:                                                                                 
        print("Menù")
        print("Crea un dataframe (1) ")
        print("Salva il datafram su un file (2) ")
        print("Informazioni del dataframe (3) ")                                                             
        print("Descrizione del dataframe (4) ")
        print("Value counts (5) ")
        print("Controlla se ci sono righe vuote (6)")
        print("Aggiungi colonna: Costa per GB (7)")
        print("Controlla la relazione tra vari elementi (8)")
        print("Inìdentifica possibili correlazioni (9)")
        print("Converti la colonna churn in formato numerico (10)")
        print("Normalizzazione (11)")
        print("Exit (12) ")
        utente = input("Inserisci l'operazione da fare: ")                                        
        df = ES1.Telecomunicazioni(1,30,"1 mese",10,20,15,"sì")
        creazione = df.crea()
        salvattaggio = df.file()
        informazioni = df.info()
        descrizione = df.describe()
        valore = df.value_counts()
        righe = df.righe_mancanti()
        aggiungi = df.aggiungi_colonne()
        relazioni_val = df.relazioni()
        corr = df.correlazioni()
        convertitore = df.convertire_colonna()
        norma = df.normalizzazione()
        if utente == "1":
            print(creazione)
        elif utente == "2":
            try:
                print(salvattaggio)
            except:
                print("Errore sul file")
        elif utente == "3":
            try:
                print(informazioni)
            except:
                print("Dataframe non trovato")
        elif utente == "4":
            try:
                print(descrizione)
            except:
                print("dataframe non trovato")
        elif utente == "5":
            try:
                print(valore)
            except:
                print("dataframe non trovato") 
        elif utente == "6":
            try:
                print(righe)
            except:
                print("dataframe non trovato")  
        elif utente == "7":
            try:
                print(aggiungi)
            except:
                print("dataframe non trovato") 
        elif utente == "8":
            try:
                print(relazioni_val)
            except:
                print("dataframe non trovato")    
        elif utente == "9":
            try:
                print(corr)
            except:
                print("dataframe non trovato")  
        elif utente == "10":
            try:
                print(convertitore)
            except:
                print("dataframe non trovato") 
        elif utente =="11":
            try:
                print(norma)   
            except:
                print("Dataframe non trovato")  
        elif utente == "12":
            print("Arrivederci!")
            break
        else:
            print("Comando sbagliato!")

menù()

