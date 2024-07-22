#ESERCIZIO FINALE
#PARTE 1 = TEMPO:40 MINUTI -- REALE: 45 MINUTI
#PARTE 2= TEMPO: 30 MINUTI -- REALE: 20 MINUTI
#PARTE 3= TEMPO: 30 MINUTI -- REALE: 25 MINUTI
#PARTE 4= TEMPO: ????????? -- REALE: 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def genera_dati():
    media_visitatori = 2000
    deviazione_standard = 500
    visitatori = np.random.normal(media_visitatori, deviazione_standard, size=365)           # Genera 365 valori casuali con media 2000 e deviazione standard 500  

    serie = pd.date_range(start='2023-01-01', periods= 365)                             # Crea una serie temporale 
    visitorori_serie = pd.Series(visitatori, index=serie)
    print(visitorori_serie)                                                               # Visualizza i primi 5 valori per verifica

    trend = np.linspace(0, 1000, 365)                                                      #creazione di un trend 
    aggiungi_trend = visitorori_serie + trend
    print(aggiungi_trend)

    return visitorori_serie,serie

def creazione_dataframe(serie,visitatori_serie):
    df_visitatori = pd.DataFrame({"Data":serie, "Numero di Visitatori": visitatori_serie})      #creazione del dataframe
    print(df_visitatori)
    return df_visitatori

def analisi_dei_dati(df_visitatori):
    media_visitatori = df_visitatori.resample('ME').mean()  
    print("Media divisa per mesi ")                                                 #raggruppo i dati per mese ed eseguo la media
    print(media_visitatori)

    deviazione_standard = df_visitatori.resample('ME').std()                                #raggruppo i dati per mese ed eseguo la deviazione standard
    print("Deviazione standard per mesi")
    print(deviazione_standard)
    
    return media_visitatori, deviazione_standard


def visualizza_dati(df_visitatori):
    plt.figure(figsize=(12,6))                                              #larghezza 12 pollici e altezza 6
    plt.plot(df_visitatori.index,df_visitatori["Numero di Visitatori"], label= "Numero di Visitatori giornalieri")
    plt.xlabel("Data")                                                      #asse x
    plt.ylabel("Numero di Visitatori")                                      #asse y
    plt.title("Visulizzazione dei dati")                                    #aggiunge un titolo
    plt.legend()                                                            #aggiunge un etichetta
    plt.show()                                                              #mostra output








visitatori_serie,serie= genera_dati()
df_visitatori = creazione_dataframe(visitatori_serie,serie)
media_visitatori = analisi_dei_dati(df_visitatori)
grafico = visualizza_dati(df_visitatori)







