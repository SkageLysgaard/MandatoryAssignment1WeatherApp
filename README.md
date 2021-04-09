# MandatoryAssignment1WeatherApp
1st mandatory assignment in INF142
People in the team:
Skage Lysgard
Sondre Sylte 
Åsmund Groven
Tuva Kvalsøren



STORAGE.py fungerer som serveren vår, og kjører værstasjon-simulasjonene i tre forskjellige tråder, parallelt ved hjelp av threading. 
I værstasjonene blir simulert data lagt til i de respektive csv-filene på formated:
weatherData = {
        "LOCATION" : location,
        "MONTH" : month,
        "TEMPERATURE" : temperature,
        "RAIN" : rain 
    }
Værstasjonene er koblet til serveren med UDP-protokoll. 

Klienten vår er FMI.py, som kobles til serveren med TCP, der brukeren velger by, og serveren printer data fra valgt by sin csv.fil, der dataen er lagret.  Dataen er også lagret i mongoDB, men vi valgte og ikke bruke dette.
OBS : Dataen fra de forskjellige byene kommer fra hver sin simulasjon. Vi kunne selfølgelig brukt en stasjon som simulerte all dataen til de tre byene og sendt det rett til STORAGE.py. Men dersom man skulle videreutvikle stasjonen, vil man ikke kunne endre på "måleenheter" til en spesifikk by. Derfor laget vi en stasjon for hver by slik at dette vil være mulig i fremtiden uten og lage store problemer. 
NB: Man må kjøre simulasjonene manuelt i terminale for at det skal legge inn data i csv-filene. Dataen lagres med enkelt-parantes, noe vi egentlig ikke vil, fordi da fungerer det ikke å bruke json.loads() (som gjør om objectet til et dictionary, slik at vi kan sende den til mongoDB gjennom collections.insert_one(dictionary)) på dictionarisene når vi iterere gjennom de. Vi har prøvd ulike løsninger, men virker som om det er veldig vanskelig å få til. Om vi hadde hatt mer tid, hadde vi selvfølgelig funnet en annen måte å gjøre dette på. 
Derfor har vi allerede lagt inn data i de ulike csv filene og endre enkeltparantesene til dobbeltparantes manuelt. 

I tillegg til å lagre og hente fra csv-filer, har vi en mongoDB-database vi sender data til på dict-format.

Vi har valgt å bruke matplotlib.pyplot kombinert med user-input i terminalen som vår GUI. Brukeren vil kunne skrive inn valgt by, og få data respektivt, der data er navn, tid og graf over temperatur og regn. Begrunnelse for at dette er et GUI er fordi brukeren kan selv velge hvilken data han/hun vil ha (User Interface) fra hvilken by, og få ut dette som en graf (graphic).

For å kjøre programmet må du:
 1.Starte serverer med "python STORAGE.py" i en terminal (ikke i anaconda). 
 2.Starte "FMI.py" i et annet terminalvindu
 3.Skrive ønsket by i FMI.py - Deretter få grafen
 4.Om du vil få en annen by må du close FMI.py med CTRL+C i terminalen og samme i STORAGE.py.
 5.Deretter kjøre server og FMI på nytt og repetere stegene. (dette er fordi vi ikke fikk while loopen til å fungere)      
