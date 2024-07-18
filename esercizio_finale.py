#OBBIETTIVO: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un daatset
#di clienti della compagnia di telecomunicazioni. L'esercizio mira a costruire un modello predittivo
#di base per la churn e scoprire correlazioni tra vari attributi del cliente e la loro fedeltà.

import pandas as pd
import numpy as np


id_cliente = np.random.randint(0,10000,size=100)
età = np.random.randint(20,70,size=100)
durata_allenamento = ["1 mese","2 mesi","3 mesi","4 mesi","5 mesi","6 mesi","7 mesi","8 mesi","9 mesi","10 mesi","11 mesi","12 mesi"]
tariffa_mensile = [10,20,30,40,50]
dati_consumati = np.random.randint(0,30,size= 100)
servizio_clienti_contatti = np.random.randint(0,20,size = 100)
churn = ["sì","no"]




class Telecomunicazioni:
    def __init__(self,id_cliente,età,durata_allenamento,tariffa_mensile,dati_consumati,servizio_clienti_contatti,churn):
        self.id_cliente = id_cliente
        self.età = età
        self.durata_allenamento = durata_allenamento
        self.tariffa_mensile = tariffa_mensile
        self.dati_consumati = dati_consumati
        self.servizio_clienti_contatti = servizio_clienti_contatti
        self.churn = churn
       
    def crea(self):
        data = {"id_cliente": id_cliente,
                "età": età,
                "durata_allenamento":np.random.choice(durata_allenamento,size=100),
                "tariffa_mensile": np.random.choice(tariffa_mensile,size=100),
                "dati_consumati": dati_consumati,
                "servizio_clienti_contatti": servizio_clienti_contatti,
                "churn": np.random.choice(churn,size=100)
        }
        self.df = pd.DataFrame(data)
        print(self.df)
        return self.df
    
    def file(self):
        self.df.to_csv("Esercizio_finale.csv")
    
    def info(self):
        informazioni = self.df.info()
        print (informazioni)
        return informazioni
    
    def describe(self):
        descrizione = self.df.describe()
        print(descrizione)
        return descrizione
    
    def value_counts(self):
        valore = self.df.value_counts()
        print(valore)
        return valore
    
    def righe_mancanti(self):
        self.controllo_righe = True
        self.df_righe_mancanti = self.df[self.df.isnull().any(axis=1)]
        if len(self.df_righe_mancanti)>0:
            print(self.df_righe_mancanti)
        else:
            print("Nessuna riga mancante")
    
    
    def aggiungi_colonne(self):                                                                  
        self.df['Costp_per_GB'] = self.df['tariffa_mensile'] / self.df['dati_consumati'] 
        print(self.df)
        return self.df
    
    def relazioni(self):
        gruppo1 = self.df.groupby("churn").agg("età")
        gruppo2 = self.df.groupby("churn").agg("durata_allenamento")
        gruppo3= self.df.groupby("churn").agg("tariffa_mensile")
        print(gruppo1)
        print(gruppo2)
        print(gruppo3)
                         
    def correlazioni(self):
        selezione_variabili = ['età', 'dati_consumati', 'tariffa_mensile']
        correlazioni_variabili = self.df[selezione_variabili]
        correlazioni_variabili = correlazioni_variabili.corr()
        print (correlazioni_variabili)

    
    def convertire_colonna(self):
        convertita = self.df['churn'] = self.df['churn'].map({'no': 0, 'sì': 1})
        print(convertita)
        return convertita
        
    def normalizzazione(self):
        numeric_columns = ["età","tariffa_mensile", "dati_consumati"]             
        self.df[numeric_columns] = (self.df[numeric_columns] - self.df[numeric_columns].min()) / (self.df[numeric_columns].max() - self.df[numeric_columns].min()) 
        print(self.df)







self = Telecomunicazioni
Telecomunicazioni.crea(self)
Telecomunicazioni.file(self)
Telecomunicazioni.info(self)
Telecomunicazioni.describe(self)
Telecomunicazioni.value_counts(self)
Telecomunicazioni.righe_mancanti(self)
Telecomunicazioni.aggiungi_colonne(self)
Telecomunicazioni.relazioni(self)
Telecomunicazioni.correlazioni(self)
Telecomunicazioni.convertire_colonna(self)
Telecomunicazioni.normalizzazione(self)
