# MandatoryAssignment1WeatherApp
1st mandatory assignment in INF142
People in the team:
Skage Lysgard
Sondre Sylte 
Åsmund Groven
Tuva Kvalsøren



STORAGE.py fungerer som serveren vår, og kjører værstasjon-simulasjonene i tre forskjellige tråder, parallelt ved hjelp av threading. 
I værstasjonene blir simulert data lagt til i de respektive txt-filene på formated 'Location, Month, Temperature, Rain'. 
Værstasjonene er koblet til serveren med UDP-protokoll. 

Klienten vår er FMI.py, som kobles til serveren med TCP, der brukeren velger by, og serveren printer data fra valgt by sin txt-fil i terminalen. 

I tillegg til å lagre og hente fra txt-filer, har vi en mongoDB-database vi sender data til på dict-format. Da henter serveren data direkte fra databasen, og printer i terminalen, istedet for å hente fra tekstfilene. 


