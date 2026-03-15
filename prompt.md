# Esposizione all'IA del Mercato del Lavoro Italiano

Analisi dell'esposizione all'intelligenza artificiale di 813 professioni
italiane classificate secondo ISTAT CP2021.

## Metodologia

Ogni professione e' stata valutata su una scala 0-10 utilizzando Claude (Anthropic),
integrando il framework 'observed exposure' di Anthropic Research.

| Punteggio | Significato | Esempi |
|-----------|-------------|--------|
| 0-1 | Minima | Muratore, giardiniere, sommozzatore |
| 2-3 | Bassa | Elettricista, idraulico, vigile del fuoco |
| 4-5 | Moderata | Infermiere, poliziotto, veterinario |
| 6-7 | Alta | Insegnante, dirigente, commercialista |
| 8-9 | Molto alta | Sviluppatore software, traduttore, analista dati |
| 10 | Massima | Addetto inserimento dati, operatore telemarketing |

## Statistiche aggregate

- **Professioni totali:** 813
- **Professioni con score:** 813
- **Media esposizione:** 4.6/10

### Distribuzione per punteggio

- **1/10:** 33 professioni
- **2/10:** 116 professioni
- **3/10:** 140 professioni
- **4/10:** 70 professioni
- **5/10:** 135 professioni
- **6/10:** 175 professioni
- **7/10:** 106 professioni
- **8/10:** 32 professioni
- **9/10:** 5 professioni
- **10/10:** 1 professioni

### Media esposizione per Grande Gruppo

| GG | Nome | Prof. | Media |
|----|------|-------|-------|
| 1 | LEGISLATORI, IMPRENDITORI E ALTA DIRIGENZA | 73 | 5.8 |
| 2 | PROFESSIONI INTELLETTUALI, SCIENTIFICHE E DI ELEVA | 179 | 6.2 |
| 3 | PROFESSIONI TECNICHE | 164 | 5.5 |
| 4 | PROFESSIONI ESECUTIVE NEL LAVORO D'UFFICIO | 30 | 7.2 |
| 5 | PROFESSIONI QUALIFICATE NELLE ATTIVITÀ COMMERCIALI | 62 | 3.9 |
| 6 | ARTIGIANI, OPERAI SPECIALIZZATI E AGRICOLTORI | 170 | 2.4 |
| 7 | CONDUTTORI DI IMPIANTI, OPERAI DI MACCHINARI FISSI | 104 | 3.5 |
| 8 | PROFESSIONI NON QUALIFICATE | 28 | 2.2 |
| 9 | FORZE ARMATE | 3 | 3.3 |

### Ripartizione per fascia

| Fascia | Professioni | % |
|--------|-------------|---|
| Minima (0-1) | 33 | 4.1% |
| Bassa (2-3) | 256 | 31.5% |
| Moderata (4-5) | 205 | 25.2% |
| Alta (6-7) | 281 | 34.6% |
| Molto alta (8-10) | 38 | 4.7% |

## Tabella completa

| Codice | Professione | GG | Esposizione | Rationale |
|--------|-------------|-----|-------------|-----------|
| 4.1.2.2.0 | Addetti all'immissione dati | 4 | 10 | L'immissione dati e le operazioni di elaborazione sono completamente digitali, r |
| 2.1.1.3.2 | Statistici e analisti di dati | 2 | 9 | Questa professione è quasi interamente lavoro intellettuale digitale focalizzato |
| 2.7.1.1.1 | Analisti e progettisti di software | 2 | 9 | Gli analisti e progettisti di software operano quasi interamente in ambiti digit |
| 3.1.2.1.0 | Tecnici programmatori | 3 | 9 | I tecnici programmatori operano quasi interamente in domini digitali—scrittura d |
| 4.1.2.1.0 | Addetti alla videoscrittura, dattilograf | 4 | 9 | Questa professione consiste quasi interamente in lavoro digitale: trascrizione,  |
| 4.1.2.3.0 | Addetti alle macchine per la redazione,  | 4 | 9 | Questa professione riguarda l'elaborazione routinaria di documenti digitali, la  |
| 2.1.1.3.1 | Matematici | 2 | 8 | I matematici operano quasi interamente in domini digitali—sviluppando teorie, ri |
| 2.2.2.2.0 | Cartografi, fotogrammetristi e specialis | 2 | 8 | Questa professione è quasi interamente digitale, coinvolgendo acquisizione, anal |
| 2.5.1.4.1 | Specialisti in contabilità | 2 | 8 | Gli specialisti in contabilità svolgono lavoro prevalentemente digitale e basato |
| 2.5.1.4.2 | Fiscalisti e tributaristi | 2 | 8 | I fiscalisti e tributaristi svolgono prevalentemente lavoro intellettuale digita |
| 2.5.1.5.4 | Analisti di mercato | 2 | 8 | Gli analisti di mercato operano quasi interamente con dati digitali, conducendo  |
| 2.5.4.1.3 | Redattori di testi per la pubblicità | 2 | 8 | I redattori di testi pubblicitari operano quasi interamente in domini digitali—s |
| 2.5.4.1.4 | Redattori di testi tecnici | 2 | 8 | I redattori di testi tecnici producono contenuti completamente digitali (manuali |
| 2.5.4.3.0 | Interpreti e traduttori di livello eleva | 2 | 8 | Gli interpreti e traduttori di livello elevato operano prevalentemente in domini |
| 2.5.4.4.2 | Revisori di testi | 2 | 8 | La revisione di testi è un compito essenzialmente digitale e linguistico, ambiti |
| 2.6.2.1.1 | Ricercatori e tecnici laureati nelle sci | 2 | 8 | Questa professione comporta ricerca, sperimentazione e lavoro intellettuale quas |
| 2.7.1.1.2 | Analisti di sistema | 2 | 8 | Gli analisti di sistema operano quasi interamente in domini digitali—progettando |
| 2.7.1.1.3 | Analisti e progettisti di applicazioni w | 2 | 8 | Gli analisti e progettisti di applicazioni web operano quasi interamente in domi |
| 2.7.2.1.1 | Specialisti in reti e comunicazioni info | 2 | 8 | La professione è quasi interamente lavoro intellettuale digitale: analisi, proge |
| 2.7.2.1.2 | Analisti e progettisti di basi dati | 2 | 8 | Gli analisti e progettisti di basi dati operano quasi interamente in ambiti digi |
| 2.7.2.1.3 | Amministratori di sistemi | 2 | 8 | Gli amministratori di sistemi svolgono lavoro prevalentemente digitale: configur |
| 3.1.1.3.0 | Tecnici statistici | 3 | 8 | I tecnici statistici svolgono principalmente lavoro digitale: acquisizione dati, |
| 3.1.2.2.0 | Tecnici esperti in applicazioni | 3 | 8 | Questa professione riguarda principalmente lavoro digitale—installazione, config |
| 3.1.2.3.0 | Tecnici web | 3 | 8 | I tecnici web svolgono lavoro quasi interamente digitale—sviluppo, configurazion |
| 3.1.2.4.0 | Tecnici gestori di basi di dati | 3 | 8 | Gli amministratori di basi di dati svolgono lavoro quasi interamente digitale—ge |
| 3.1.2.5.0 | Tecnici gestori di reti e di sistemi tel | 3 | 8 | I tecnici gestori di reti e sistemi telematici svolgono lavoro prevalentemente d |
| 3.1.3.7.1 | Disegnatori tecnici | 3 | 8 | I disegnatori tecnici operano quasi interamente in ambienti digitali, creando di |
| 3.3.1.2.1 | Contabili | 3 | 8 | Il lavoro contabile è prevalentemente digitale e basato su elaborazione routinar |
| 3.3.2.5.0 | Agenti di borsa e cambio, tecnici dell'i | 3 | 8 | Gli agenti di borsa svolgono lavoro prevalentemente digitale: analisi dati di me |
| 3.4.4.1.1 | Grafici | 3 | 8 | I grafici lavorano quasi interamente in ambienti digitali, creando contenuti vis |
| 4.1.1.3.0 | Addetti al protocollo e allo smistamento | 4 | 8 | La professione consiste principalmente nell'elaborazione routinaria di documenti |
| 4.2.2.3.0 | Centralinisti | 4 | 8 | I centralinisti svolgono elaborazione routinaria di informazioni digitali—riceve |
| 4.2.2.4.0 | Addetti all'informazione nei Call Center | 4 | 8 | Gli addetti all'informazione nei call center svolgono lavoro quasi interamente d |
| 4.3.2.1.0 | Addetti alla contabilità | 4 | 8 | Gli addetti alla contabilità svolgono lavoro quasi interamente digitale: inserim |
| 4.3.2.2.0 | Addetti alle buste paga | 4 | 8 | Gli addetti alle buste paga svolgono attività quasi interamente digitali: raccol |
| 4.3.2.4.0 | Addetti ai servizi statistici | 4 | 8 | Gli addetti ai servizi statistici svolgono principalmente compiti digitali: racc |
| 4.3.2.5.0 | Addetti agli uffici interni di cassa | 4 | 8 | Gli addetti agli uffici interni di cassa svolgono operazioni finanziarie routina |
| 4.4.2.1.0 | Addetti ad archivi, schedari e professio | 4 | 8 | Questa professione riguarda la classificazione, l'archiviazione e l'organizzazio |
| 1.1.2.4.2 | Dirigenti tecnici e professionali | 1 | 7 | I dirigenti tecnici e professionali nella pubblica amministrazione supervisionan |
| 1.2.1.6.3 | Imprenditori e amministratori di grandi  | 1 | 7 | Questi dirigenti guidano grandi aziende nei settori IT e telecomunicazioni, pren |
| 1.2.1.7.0 | Imprenditori e amministratori di grandi  | 1 | 7 | Questi dirigenti senior nei settori bancario, assicurativo e immobiliare operano |
| 1.2.2.6.3 | Direttori e dirigenti generali di aziend | 1 | 7 | Questi sono dirigenti senior che gestiscono aziende di servizi informatici e tel |
| 1.2.3.1.0 | Direttori e dirigenti della finanza ed a | 1 | 7 | I direttori e dirigenti della finanza e amministrazione operano prevalentemente  |
| 1.2.3.3.0 | Direttori e dirigenti delle vendite e co | 1 | 7 | I direttori delle vendite e marketing svolgono lavoro prevalentemente cognitivo— |
| 1.2.3.4.0 | Direttori e dirigenti della comunicazion | 1 | 7 | Questo ruolo comporta pianificazione strategica, creazione di contenuti, comunic |
| 1.2.3.6.0 | Direttori e dirigenti dei servizi inform | 1 | 7 | I direttori dei servizi informatici svolgono lavoro prevalentemente digitale nel |
| 1.2.3.7.0 | Direttori e dirigenti della ricerca e sv | 1 | 7 | I direttori della ricerca e sviluppo gestiscono lavoro prevalentemente basato su |
| 1.3.1.6.3 | Imprenditori e responsabili di piccole a | 1 | 7 | Sono imprenditori e responsabili di piccole aziende nei settori IT e telecomunic |
| 2.1.1.1.1 | Fisici | 2 | 7 | I fisici conducono ricerche, sviluppano teorie e risolvono problemi principalmen |
| 2.1.1.1.2 | Astronomi ed astrofisici | 2 | 7 | Gli astronomi e gli astrofisici svolgono lavoro altamente digitale: l'analisi de |
| 2.1.1.4.3 | Geofisici | 2 | 7 | I geofisici svolgono ricerca basata su dati e computazione: analisi di dati sism |
| 2.1.1.4.4 | Meteorologi | 2 | 7 | I meteorologi operano principalmente con raccolta, elaborazione e analisi di dat |
| 2.1.1.4.5 | Idrologi | 2 | 7 | Gli idrologi svolgono lavoro prevalentemente intellettuale basato su analisi dat |
| 2.2.1.1.1 | Ingegneri meccanici | 2 | 7 | Gli ingegneri meccanici svolgono lavoro prevalentemente intellettuale: progettaz |
| 2.2.1.1.2 | Ingegneri navali | 2 | 7 | Gli ingegneri navali svolgono lavoro prevalentemente basato sulla conoscenza: pr |
| 2.2.1.1.3 | Ingegneri aerospaziali e astronautici | 2 | 7 | Gli ingegneri aerospaziali svolgono lavoro prevalentemente intellettuale: proget |
| 2.2.1.3.0 | Ingegneri elettrotecnici | 2 | 7 | Gli ingegneri elettrotecnici svolgono lavoro prevalentemente intellettuale—proge |
| 2.2.1.4.1 | Ingegneri elettronici | 2 | 7 | Gli ingegneri elettronici svolgono lavoro prevalentemente intellettuale—progetta |
| 2.2.1.4.2 | Ingegneri progettisti di hardware | 2 | 7 | Gli ingegneri progettisti di hardware svolgono principalmente lavoro digitale—pr |
| 2.2.1.4.3 | Ingegneri in telecomunicazioni | 2 | 7 | Gli ingegneri in telecomunicazioni svolgono lavoro prevalentemente intellettuale |
| 2.2.1.4.4 | ingegneri della automazione | 2 | 7 | Gli ingegneri dell'automazione svolgono lavoro prevalentemente intellettuale: pr |
| 2.2.1.5.2 | Ingegneri dei materiali | 2 | 7 | Gli ingegneri dei materiali conducono ricerche, progettano processi e sviluppano |
| 2.2.1.7.0 | Ingegneri industriali e gestionali | 2 | 7 | Gli ingegneri industriali e gestionali operano prevalentemente con sistemi digit |
| 2.2.1.8.0 | Ingegneri biomedici e bioingegneri | 2 | 7 | Gli ingegneri biomedici conducono ricerche, progettazione e sviluppo di disposit |
| 2.2.2.1.1 | Architetti | 2 | 7 | Gli architetti svolgono lavoro prevalentemente digitale—progettazione CAD, model |
| 2.3.1.1.2 | Biochimici | 2 | 7 | I biochimici svolgono ricerca, analisi dati e lavoro di laboratorio sempre più d |
| 2.3.1.1.3 | Biofisici | 2 | 7 | I biofisici conducono ricerche, analisi dati e sperimentazioni di laboratorio—la |
| 2.3.1.1.4 | Biotecnologi | 2 | 7 | I biotecnologi svolgono ricerca, analisi dati e sperimentazione di laboratorio—l |
| 2.4.1.7.3 | Epidemiologi | 2 | 7 | Gli epidemiologi svolgono principalmente lavoro intellettuale digitale: analisi  |
| 2.5.1.2.0 | Specialisti della gestione e del control | 2 | 7 | Questa professione comporta principalmente lavoro digitale e basato sulla conosc |
| 2.5.1.3.1 | Specialisti in risorse umane | 2 | 7 | Gli specialisti in risorse umane svolgono lavoro prevalentemente intellettuale—s |
| 2.5.1.3.2 | Specialisti dell'organizzazione del lavo | 2 | 7 | Gli specialisti dell'organizzazione del lavoro svolgono principalmente compiti d |
| 2.5.1.4.3 | Specialisti in attività finanziarie | 2 | 7 | Gli specialisti in attività finanziarie svolgono principalmente lavoro intellett |
| 2.5.1.5.1 | Specialisti nell'acquisizione di beni e  | 2 | 7 | Questa professione comporta l'analisi delle condizioni di mercato, il confronto  |
| 2.5.1.5.3 | Specialisti nella commercializzazione ne | 2 | 7 | Questa professione si concentra su compiti prevalentemente digitali e intellettu |
| 2.5.1.6.0 | Specialisti delle relazioni pubbliche, d | 2 | 7 | Gli specialisti di relazioni pubbliche svolgono principalmente lavoro basato su  |
| 2.5.2.1.0 | Avvocati | 2 | 7 | Il lavoro degli avvocati è prevalentemente digitale e basato sulla conoscenza: r |
| 2.5.2.2.1 | Esperti legali in imprese | 2 | 7 | Gli esperti legali in impresa svolgono principalmente lavoro intellettuale digit |
| 2.5.2.2.2 | Esperi legali in enti pubblici | 2 | 7 | Gli esperti legali in enti pubblici svolgono lavoro prevalentemente intellettual |
| 2.5.3.1.1 | Specialisti dei sistemi economici | 2 | 7 | Gli specialisti dei sistemi economici conducono ricerche, analisi e sviluppo di  |
| 2.5.3.1.2 | Specialisti dell'economia aziendale | 2 | 7 | Gli specialisti dell'economia aziendale svolgono lavoro prevalentemente intellet |
| 2.5.3.2.2 | Antropologi | 2 | 7 | Gli antropologi svolgono principalmente lavoro intellettuale—ricerca, analisi, s |
| 2.5.3.2.3 | Geografi | 2 | 7 | I geografi svolgono lavoro prevalentemente intellettuale—ricerca, analisi, inter |
| 2.5.3.4.1 | Storici | 2 | 7 | Gli storici svolgono principalmente lavoro intellettuale digitale: ricerca, anal |
| 2.5.3.4.3 | Specialisti in scienza politica | 2 | 7 | Gli specialisti in scienza politica svolgono lavoro prevalentemente intellettual |
| 2.5.3.4.4 | Filosofi | 2 | 7 | I filosofi conducono ricerche, scrittura e analisi completamente basate su conos |
| 2.5.4.1.1 | Scrittori e poeti | 2 | 7 | Gli scrittori e i poeti producono opere completamente digitalizzabili (testo) ch |
| 2.5.4.1.2 | Dialoghisti e parolieri | 2 | 7 | I dialoghisti e parolieri producono contenuti creativi completamente digitali (c |
| 2.5.4.2.0 | Giornalisti | 2 | 7 | Il giornalismo è prevalentemente lavoro intellettuale condotto in ambienti digit |
| 2.5.4.4.1 | Linguisti e filologi | 2 | 7 | I linguisti e filologi operano principalmente con testi digitali, dati linguisti |
| 2.5.4.5.1 | Archivisti e conservatori di documenti d | 2 | 7 | La professione è incentrata su attività prevalentemente digitali e intellettuali |
| 2.5.5.1.2 | Disegnatori artistici e illustratori | 2 | 7 | I disegnatori artistici e illustratori operano prevalentemente in domini digital |
| 2.5.5.1.3 | Disegnatori di moda | 2 | 7 | I disegnatori di moda operano prevalentemente in ambiti digitali—schizzi, disegn |
| 2.5.5.1.4 | Creatori artistici a fini commerciali (e | 2 | 7 | I creatori artistici commerciali producono principalmente elaborati digitali (bo |
| 2.5.5.2.4 | Sceneggiatori | 2 | 7 | Gli sceneggiatori operano principalmente in domini digitali (sceneggiature, narr |
| 2.5.5.4.1 | Compositori | 2 | 7 | I compositori lavorano prevalentemente in ambiti digitali (software di notazione |
| 2.6.1.1.1 | Docenti universitari in scienze matemati | 2 | 7 | I docenti universitari in scienze matematiche e dell'informatica svolgono princi |
| 2.6.1.1.2 | Docenti universitari in scienze fisiche | 2 | 7 | I docenti universitari di scienze fisiche svolgono lavoro prevalentemente digita |
| 2.6.1.3.2 | Docenti universitari in scienze ingegner | 2 | 7 | I docenti universitari in scienze ingegneristiche svolgono prevalentemente lavor |
| 2.6.1.6.0 | Docenti universitari in scienze economic | 2 | 7 | I docenti universitari in scienze economiche e statistiche svolgono principalmen |
| 2.6.2.1.2 | Ricercatori e tecnici laureati nelle sci | 2 | 7 | Questa professione comporta un lavoro prevalentemente intellettuale e basato su  |
| 2.6.2.3.2 | Ricercatori e tecnici laureati nelle sci | 2 | 7 | Questo ruolo comporta progettazione della ricerca, analisi dei dati, modellazion |
| 2.6.2.6.0 | Ricercatori e tecnici laureati nelle sci | 2 | 7 | Questa professione comporta principalmente lavoro intellettuale digitale: analis |
| 2.6.2.7.1 | Ricercatori e tecnici laureati nelle sci | 2 | 7 | La professione è incentrata su attività di ricerca, analisi giuridica e scrittur |
| 2.6.2.7.2 | Ricercatori e tecnici laureati nelle sci | 2 | 7 | Questa professione comporta principalmente lavoro intellettuale e basato su atti |
| 2.6.3.2.4 | Docenti di scienze dell'informazione nel | 2 | 7 | I docenti di scienze dell'informazione insegnano contenuti prevalentemente digit |
| 2.6.5.3.1 | Docenti della formazione e dell'aggiorna | 2 | 7 | I formatori professionali operano principalmente in ambiti digitali e di knowled |
| 2.7.2.1.4 | Specialisti in sicurezza informatica | 2 | 7 | Gli specialisti in sicurezza informatica svolgono lavoro prevalentemente digital |
| 3.1.2.7.0 | Tecnici dei sistemi informativi geografi | 3 | 7 | I tecnici GIS operano principalmente con dati digitali, analisi spaziale e carto |
| 3.1.3.7.3 | Rilevatori e disegnatori di prospezioni | 3 | 7 | Questa professione comporta la creazione di disegni tecnici e mappe dettagliate  |
| 3.1.7.1.0 | Fotografi e professioni assimilate | 3 | 7 | La fotografia è sempre più digitale, con strumenti AI che automatizzano porzioni |
| 3.1.7.2.3 | Tecnici del montaggio audio-video-cinema | 3 | 7 | La professione riguarda principalmente lavoro digitale—montaggio, elaborazione e |
| 3.3.1.1.1 | Segretari amministrativi e tecnici degli | 3 | 7 | Questa professione è principalmente basata su lavoro informativo e digitale: ric |
| 3.3.1.1.2 | Assistenti di archivio e di biblioteca | 3 | 7 | Gli assistenti di archivio e biblioteca svolgono principalmente lavoro basato su |
| 3.3.1.2.2 | Economi e tesorieri | 3 | 7 | Gli economi e tesorieri svolgono principalmente compiti finanziari digitali: ela |
| 3.3.1.3.1 | Tecnici dell'acquisizione delle informaz | 3 | 7 | I tecnici dell'acquisizione delle informazioni svolgono lavoro prevalentemente d |
| 3.3.1.3.2 | Intervistatori e rilevatori professional | 3 | 7 | Gli intervistatori e rilevatori professionali conducono raccolta dati strutturat |
| 3.3.1.4.0 | Corrispondenti in lingue estere e profes | 3 | 7 | La professione si concentra su compiti prevalentemente digitali e linguistici: r |
| 3.3.1.5.0 | Tecnici dell'organizzazione e della gest | 3 | 7 | Queste professioni applicano tecniche di analisi ai processi produttivi, alla pr |
| 3.3.2.1.0 | Tecnici della gestione finanziaria | 3 | 7 | I tecnici della gestione finanziaria svolgono principalmente lavoro digitale: an |
| 3.3.2.2.0 | Tecnici del lavoro bancario | 3 | 7 | I tecnici del lavoro bancario svolgono principalmente compiti digitali: elaboraz |
| 3.3.2.6.1 | Tecnici dei contratti di scambio, a prem | 3 | 7 | La professione è principalmente basata su lavoro digitale: redazione di contratt |
| 3.3.2.6.2 | Tecnici della locazione finanziaria | 3 | 7 | I tecnici della locazione finanziaria svolgono principalmente lavoro cognitivo d |
| 3.3.3.1.0 | Approvvigionatori e responsabili acquist | 3 | 7 | Le professioni di approvvigionamento e acquisti sono prevalentemente basate su l |
| 3.3.3.5.0 | Tecnici del marketing | 3 | 7 | I tecnici del marketing svolgono lavoro prevalentemente digitale e basato sulla  |
| 3.3.3.6.1 | Tecnici della pubblicità | 3 | 7 | I tecnici della pubblicità operano principalmente con strumenti digitali, analis |
| 3.3.3.6.2 | Tecnici delle pubbliche relazioni | 3 | 7 | I tecnici delle pubbliche relazioni operano prevalentemente con creazione di con |
| 3.4.3.1.1 | Annunciatori della radio e della televis | 3 | 7 | Gli annunciatori di radio e televisione svolgono principalmente lavoro digitale— |
| 4.1.1.1.0 | Addetti a funzioni di segreteria | 4 | 7 | Le professioni di segreteria sono prevalentemente digitali e basate su conoscenz |
| 4.1.1.2.0 | Addetti agli affari generali | 4 | 7 | Questa professione comprende principalmente compiti amministrativi digitali (ela |
| 4.1.1.4.0 | Addetti alla gestione del personale | 4 | 7 | Questa professione comporta principalmente compiti amministrativi e digitali: el |
| 4.2.1.1.0 | Addetti agli sportelli assicurativi, ban | 4 | 7 | Gli addetti agli sportelli bancari e assicurativi svolgono principalmente compit |
| 4.2.1.2.0 | Addetti agli sportelli dei servizi posta | 4 | 7 | Gli addetti agli sportelli postali svolgono principalmente lavoro transazionale  |
| 4.2.1.3.0 | Addetti agli sportelli per l'esazione di | 4 | 7 | La professione comporta principalmente compiti amministrativi e digitali: elabor |
| 4.2.1.5.0 | Addetti alla vendita di biglietti | 4 | 7 | Il lavoro di vendita di biglietti è prevalentemente digitale e transazionale: il |
| 4.2.1.6.0 | Addetti agli sportelli delle agenzie di  | 4 | 7 | Gli addetti agli sportelli di agenzie di viaggio svolgono principalmente compiti |
| 4.3.1.1.0 | Addetti alla gestione degli acquisti di  | 4 | 7 | Questa professione di gestione degli acquisti è prevalentemente lavoro digitale  |
| 4.3.1.3.0 | Addetti alla gestione amministrativa dei | 4 | 7 | La professione si concentra su compiti amministrativi prevalentemente digitali:  |
| 4.3.2.3.0 | Addetti alle operazioni finanziarie per  | 4 | 7 | La professione comporta principalmente compiti digitali e amministrativi: operaz |
| 4.4.1.1.0 | Personale addetto a compiti di controllo | 4 | 7 | Questa professione comporta verifiche documentali routinarie, controlli di confo |
| 4.4.1.2.0 | Addetti al controllo della documentazion | 4 | 7 | Questa professione riguarda il controllo della documentazione di viaggio e l'ide |
| 5.1.2.4.0 | Cassieri di esercizi commerciali | 5 | 7 | I cassieri svolgono principalmente lavoro digitale: elaborazione pagamenti, regi |
| 5.1.2.5.2 | Venditori a distanza | 5 | 7 | Il lavoro di vendita a distanza è prevalentemente digitale e basato su informazi |
| 5.5.4.2.0 | Addetti di agenzie per il disbrigo di pr | 5 | 7 | La professione comporta lavoro amministrativo e documentale significativo—ricerc |
| 1.1.2.3.1 | Direttori generali, dipartimentali ed eq | 1 | 6 | Questi direttori generali della pubblica amministrazione svolgono principalmente |
| 1.1.2.3.2 | Rettori di università, direttori di isti | 1 | 6 | I rettori e direttori di enti di ricerca svolgono principalmente lavoro intellet |
| 1.1.2.3.3 | Direttori generali ed equiparati nella s | 1 | 6 | I direttori generali sanitari svolgono principalmente lavoro cognitivo: pianific |
| 1.1.2.3.4 | Direttori generali ed equiparati nelle r | 1 | 6 | I direttori generali negli enti locali svolgono principalmente lavoro cognitivo: |
| 1.1.2.4.1 | Dirigenti amministrativi | 1 | 6 | I dirigenti amministrativi svolgono principalmente lavoro cognitivo: gestione di |
| 1.1.2.4.4 | Dirigenti delle professioni sanitarie | 1 | 6 | I dirigenti delle professioni sanitarie svolgono principalmente lavoro cognitivo |
| 1.1.2.4.5 | Dirigenti scolastici ed equiparati | 1 | 6 | I dirigenti scolastici svolgono principalmente lavoro cognitivo: pianificazione  |
| 1.1.2.4.6 | Segretari comunali e provinciali | 1 | 6 | I segretari comunali e provinciali svolgono prevalentemente lavoro amministrativ |
| 1.1.4.1.1 | Dirigenti di partiti e movimenti politic | 1 | 6 | I dirigenti di partiti politici svolgono lavoro prevalentemente cognitivo—formul |
| 1.1.4.1.2 | Dirigenti di sindacati e altre organizza | 1 | 6 | I dirigenti sindacali svolgono principalmente lavoro intellettuale: sviluppo di  |
| 1.1.4.2.0 | Dirigenti di associazioni umanitarie, cu | 1 | 6 | Questi dirigenti gestiscono organizzazioni attraverso pianificazione strategica, |
| 1.2.1.2.1 | Imprenditori e amministratori di grandi  | 1 | 6 | Questi dirigenti senior nel settore manifatturiero ed estrattivo operano a livel |
| 1.2.1.2.2 | Imprenditori e amministratori di grandi  | 1 | 6 | Si tratta di dirigenti senior che gestiscono grandi aziende di servizi pubblici  |
| 1.2.1.3.0 | Imprenditori e amministratori di grandi  | 1 | 6 | Gli imprenditori e amministratori di grandi aziende di costruzioni svolgono lavo |
| 1.2.1.4.1 | Imprenditori e amministratori di grandi  | 1 | 6 | Questi imprenditori e amministratori nel settore automotive affrontano un'esposi |
| 1.2.1.4.2 | Imprenditori e amministratori di grandi  | 1 | 6 | Questi imprenditori e amministratori di grandi aziende commerciali affrontano un |
| 1.2.1.5.0 | Imprenditori e amministratori di grandi  | 1 | 6 | Si tratta di dirigenti senior che gestiscono grandi imprese nel settore alberghi |
| 1.2.1.6.1 | Imprenditori e amministratori di grandi  | 1 | 6 | Questi sono dirigenti e imprenditori di grandi aziende nel settore trasporti e m |
| 1.2.1.6.2 | Imprenditori e amministratori di grandi  | 1 | 6 | Questi sono dirigenti senior che gestiscono grandi aziende nei settori editorial |
| 1.2.1.8.0 | Imprenditori e amministratori di grandi  | 1 | 6 | Si tratta di imprenditori e dirigenti senior che gestiscono grandi aziende nei s |
| 1.2.1.9.1 | Imprenditori e amministratori di grandi  | 1 | 6 | Questi dirigenti di alto livello in istituti educativi privati svolgono principa |
| 1.2.1.9.2 | Imprenditori e amministratori di grandi  | 1 | 6 | Gli imprenditori e amministratori di grandi strutture sanitarie e socio-assisten |
| 1.2.1.9.3 | Imprenditori e amministratori di grandi  | 1 | 6 | Questi sono dirigenti e imprenditori senior che gestiscono grandi aziende nel se |
| 1.2.2.2.1 | Direttori e dirigenti generali di aziend | 1 | 6 | Questi dirigenti generali di aziende manifatturiere e estrattive svolgono princi |
| 1.2.2.2.2 | Direttori e dirigenti generali di aziend | 1 | 6 | Si tratta di dirigenti senior che gestiscono aziende di servizi pubblici e gesti |
| 1.2.2.3.0 | Direttori e dirigenti generali di aziend | 1 | 6 | I direttori e dirigenti generali di aziende nelle costruzioni svolgono principal |
| 1.2.2.4.1 | Direttori e dirigenti generali di aziend | 1 | 6 | Sono dirigenti senior nel commercio e riparazione di autoveicoli, responsabili d |
| 1.2.2.4.2 | Direttori e dirigenti generali di aziend | 1 | 6 | I direttori e dirigenti nel commercio svolgono lavoro prevalentemente cognitivo: |
| 1.2.2.5.0 | Direttori e dirigenti generali di aziend | 1 | 6 | I direttori e dirigenti generali nel settore alloggio e ristorazione svolgono un |
| 1.2.2.6.1 | Direttori e dirigenti generali di aziend | 1 | 6 | I direttori e dirigenti generali nel settore trasporti e magazzinaggio svolgono  |
| 1.2.2.6.2 | Direttori e dirigenti generali di aziend | 1 | 6 | Si tratta di dirigenti senior in settori editoriali, cinematografici, televisivi |
| 1.2.2.7.0 | Direttori e dirigenti generali di banche | 1 | 6 | Questi dirigenti senior operano prevalentemente in ambiti digitali e informativi |
| 1.2.2.8.0 | Direttori e dirigenti generali di aziend | 1 | 6 | Si tratta di dirigenti senior che gestiscono aziende di servizi nei settori prof |
| 1.2.2.9.0 | Direttori e dirigenti generali di aziend | 1 | 6 | Si tratta di ruoli dirigenziali nel settore sportivo, dell'intrattenimento e cul |
| 1.2.3.2.0 | Direttori e dirigenti dell'organizzazion | 1 | 6 | I direttori delle risorse umane svolgono prevalentemente lavoro basato sulla con |
| 1.2.3.5.0 | Direttori e dirigenti dell'approvvigiona | 1 | 6 | Questo ruolo comporta pianificazione strategica, negoziazione con fornitori, ges |
| 1.2.3.8.0 | Direttori e dirigenti della pianificazio | 1 | 6 | Questo ruolo riguarda la pianificazione strategica, l'analisi delle politiche e  |
| 1.3.1.6.2 | Imprenditori e responsabili di piccole a | 1 | 6 | Questi piccoli imprenditori nei settori editoriale, cinematografico, radiofonico |
| 1.3.1.7.0 | Imprenditori e responsabili di piccoli i | 1 | 6 | Questi imprenditori di piccoli istituti finanziari, assicurativi e immobiliari o |
| 1.3.1.8.0 | Imprenditori e responsabili di piccole a | 1 | 6 | Gli imprenditori di piccole aziende nei servizi affrontano un'esposizione modera |
| 1.3.1.9.1 | Imprenditori e responsabili di piccole a | 1 | 6 | Gli imprenditori di piccole aziende nel settore educativo svolgono lavoro preval |
| 2.1.1.2.1 | Chimici e professioni assimilate | 2 | 6 | I chimici conducono ricerche, analisi e esperimenti che beneficiano sempre più d |
| 2.1.1.2.2 | Chimici informatori e divulgatori | 2 | 6 | Gli informatori chimici e divulgatori scientifici svolgono lavoro prevalentement |
| 2.1.1.4.1 | Geologi | 2 | 6 | I geologi conducono ricerche e analisi sulla struttura fisica della Terra, rocce |
| 2.1.1.4.2 | Paleontologi | 2 | 6 | I paleontologi conducono ricerche analizzando materiale fossile e ricostruendo l |
| 2.2.1.1.4 | Ingegneri energetici e nucleari | 2 | 6 | Gli ingegneri energetici e nucleari svolgono un mix di lavoro intellettuale (ric |
| 2.2.1.2.1 | Ingegneri metallurgici | 2 | 6 | Gli ingegneri metallurgici conducono ricerche, applicano conoscenze tecniche e s |
| 2.2.1.2.2 | Ingegneri minerari | 2 | 6 | Gli ingegneri minerari svolgono un mix di lavoro intellettuale (ricerca geologic |
| 2.2.1.5.1 | Ingegneri chimici e petroliferi | 2 | 6 | Gli ingegneri chimici e petroliferi svolgono un mix di lavoro intellettuale (pro |
| 2.2.1.6.1 | Ingegneri edili e ambientali | 2 | 6 | Gli ingegneri edili e ambientali svolgono un mix di lavoro intellettuale (proget |
| 2.2.1.6.2 | Ingegneri idraulici | 2 | 6 | Gli ingegneri idraulici svolgono lavoro prevalentemente intellettuale che compre |
| 2.2.2.1.2 | Pianificatori, paesaggisti e specialisti | 2 | 6 | La professione comporta lavoro prevalentemente intellettuale—ricerca, analisi, p |
| 2.3.1.1.1 | Biologi e professioni assimilate | 2 | 6 | I biologi conducono ricerche, analisi di laboratorio e interpretazione di dati—l |
| 2.3.1.1.5 | Botanici | 2 | 6 | I botanici svolgono ricerca combinando lavoro di laboratorio, analisi dati e oss |
| 2.3.1.1.6 | Zoologi | 2 | 6 | Gli zoologi conducono ricerche combinando lavoro sul campo, analisi di laborator |
| 2.3.1.1.7 | Ecologi | 2 | 6 | Gli ecologi svolgono ricerche, analizzano dati e redigono relazioni scientifiche |
| 2.3.1.1.8 | Tecnologi alimentari | 2 | 6 | I tecnologi alimentari svolgono ricerca, analisi e certificazione principalmente |
| 2.3.1.2.1 | Farmacologi e assimilati | 2 | 6 | I farmacologi svolgono ricerca, analizzano dati e redigono rapporti scientifici— |
| 2.3.1.2.2 | Microbiologi | 2 | 6 | I microbiologi conducono ricerche, esperimenti e analisi sempre più digitalizzat |
| 2.3.1.5.0 | Farmacisti | 2 | 6 | I farmacisti svolgono un mix di lavoro conoscitivo (formulazione farmacologica,  |
| 2.4.1.2.0 | Specialisti in terapie mediche | 2 | 6 | Gli specialisti in terapie mediche svolgono attività mista di ricerca e applicaz |
| 2.4.1.4.0 | Laboratoristi e patologi clinici | 2 | 6 | I laboratoristi e patologi clinici svolgono lavoro ad alta intensità di conoscen |
| 2.4.1.6.0 | Specialisti in diagnostica per immagini  | 2 | 6 | Gli specialisti in diagnostica per immagini e radioterapia svolgono lavoro medic |
| 2.4.1.7.1 | Dietologi e igienisti | 2 | 6 | I dietologi e igienisti svolgono un mix di lavoro intellettuale (valutazione nut |
| 2.4.1.7.2 | Specialisti in medicina sociale e del la | 2 | 6 | Gli specialisti in medicina sociale e del lavoro svolgono attività ad alta inten |
| 2.5.1.1.1 | Specialisti della gestione nella Pubblic | 2 | 6 | Sono ruoli di lavoro intellettuale nella pubblica amministrazione che coinvolgon |
| 2.5.1.1.2 | Specialisti del controllo nella Pubblica | 2 | 6 | Gli specialisti del controllo nella PA svolgono lavoro prevalentemente cognitivo |
| 2.5.1.5.2 | Specialisti nella commercializzazione di | 2 | 6 | La professione comporta un lavoro prevalentemente intellettuale—analisi di merca |
| 2.5.2.3.0 | Notai | 2 | 6 | I notai svolgono lavoro prevalentemente intellettuale—redazione di atti, interpr |
| 2.5.2.4.0 | Magistrati | 2 | 6 | I magistrati svolgono lavoro prevalentemente intellettuale—analisi legale, valut |
| 2.5.3.2.1 | Esperti nello studio, nella gestione e n | 2 | 6 | Queste sono professioni ad alta intensità di conoscenza che coinvolgono ricerca, |
| 2.5.3.2.4 | Archeologi | 2 | 6 | Gli archeologi svolgono lavoro prevalentemente intellettuale—analisi, documentaz |
| 2.5.3.3.2 | Psicologi dello sviluppo e dell'educazio | 2 | 6 | Gli psicologi dello sviluppo e dell'educazione svolgono un lavoro prevalentement |
| 2.5.3.3.3 | Psicologi del lavoro e delle organizzazi | 2 | 6 | Gli psicologi del lavoro e delle organizzazioni svolgono lavoro prevalentemente  |
| 2.5.3.4.2 | Esperti d'arte | 2 | 6 | Gli esperti d'arte svolgono lavoro prevalentemente intellettuale—ricerca, analis |
| 2.5.3.5.0 | Pedagogisti | 2 | 6 | I pedagogisti svolgono lavoro prevalentemente intellettuale—valutazione dei biso |
| 2.5.4.5.2 | Bibliotecari | 2 | 6 | I bibliotecari svolgono lavoro prevalentemente intellettuale—indicizzazione, cat |
| 2.5.5.2.1 | Registi | 2 | 6 | I registi operano principalmente nella concezione creativa e nel processo decisi |
| 2.5.5.2.3 | Direttori artistici | 2 | 6 | I direttori artistici svolgono lavoro prevalentemente intellettuale—concettualiz |
| 2.5.5.2.5 | Scenografi | 2 | 6 | Gli scenografi combinano lavoro creativo di progettazione (sempre più supportato |
| 2.6.1.1.3 | Docenti universitari in scienze chimiche | 2 | 6 | I docenti universitari in scienze chimiche e farmaceutiche svolgono un mix di la |
| 2.6.1.1.4 | Docenti universitari in scienze della te | 2 | 6 | I docenti universitari in scienze della terra svolgono un mix di lavoro intellet |
| 2.6.1.2.1 | Docenti universitari in scienze biologic | 2 | 6 | I docenti universitari in scienze biologiche svolgono un mix di lavoro intellett |
| 2.6.1.2.2 | Docenti universitari in scienze agrarie, | 2 | 6 | I docenti universitari in scienze agrarie hanno un'esposizione elevata poiché il |
| 2.6.1.2.3 | Docenti universitari in scienze mediche | 2 | 6 | I docenti universitari in scienze mediche svolgono un mix di attività di ricerca |
| 2.6.1.3.1 | Docenti universitari in scienze ingegner | 2 | 6 | I docenti universitari in scienze ingegneristiche civili e dell'architettura svo |
| 2.6.1.4.0 | Docenti universitari in scienze dell'ant | 2 | 6 | I docenti universitari in discipline umanistiche svolgono un mix di lavoro intel |
| 2.6.1.5.1 | Docenti universitari in scienze storiche | 2 | 6 | I docenti universitari in scienze storiche e filosofiche svolgono ricerca, inseg |
| 2.6.1.5.2 | Docenti universitari in scienze pedagogi | 2 | 6 | I docenti universitari in scienze pedagogiche e psicologiche svolgono un mix di  |
| 2.6.1.7.1 | Docenti universitari in scienze giuridic | 2 | 6 | I docenti universitari di discipline giuridiche svolgono lavoro prevalentemente  |
| 2.6.1.7.2 | Docenti universitari in scienze politich | 2 | 6 | I docenti universitari in scienze politiche e sociali svolgono un mix di attivit |
| 2.6.2.1.3 | Ricercatori e tecnici laureati nelle sci | 2 | 6 | Questa professione combina lavoro sperimentale in laboratorio, progettazione di  |
| 2.6.2.1.4 | Ricercatori e tecnici laureati nelle sci | 2 | 6 | Questo ruolo combina attività di ricerca teorica e sperimentale (progettazione,  |
| 2.6.2.2.1 | Ricercatori e tecnici laureati nelle sci | 2 | 6 | La professione comporta un significativo lavoro intellettuale—progettazione dell |
| 2.6.2.2.2 | Ricercatori e tecnici laureati nelle sci | 2 | 6 | Questa professione combina ricerca teorica, progettazione sperimentale, lavoro d |
| 2.6.2.2.3 | Ricercatori e tecnici laureati nelle sci | 2 | 6 | Questa professione combina attività di ricerca e analisi (progettazione, elabora |
| 2.6.2.3.1 | Ricercatori e tecnici laureati nelle sci | 2 | 6 | Questa professione combina lavoro intellettuale digitale (progettazione della ri |
| 2.6.2.4.0 | Ricercatori e tecnici laureati nelle sci | 2 | 6 | La professione comporta principalmente lavoro intellettuale—ricerca, analisi, sc |
| 2.6.2.5.1 | Ricercatori e tecnici laureati nelle sci | 2 | 6 | La professione comporta principalmente lavoro intellettuale—progettazione della  |
| 2.6.2.5.2 | Ricercatori e tecnici laureati nelle sci | 2 | 6 | Questa professione comporta progettazione della ricerca, analisi dei dati, revis |
| 2.6.3.2.1 | Docenti di scienze matematiche, fisiche  | 2 | 6 | L'insegnamento di matematica, fisica e chimica comporta un lavoro prevalentement |
| 2.6.3.2.2 | Docenti di scienze della vita e della sa | 2 | 6 | Gli insegnanti di scienze della vita e della salute svolgono prevalentemente lav |
| 2.6.3.2.3 | Docenti di discipline tecnico-ingegneris | 2 | 6 | L'insegnamento di discipline tecnico-ingegneristiche comprende lavoro intellettu |
| 2.6.3.2.5 | Docenti di scienze letterarie, artistich | 2 | 6 | Gli insegnanti di scienze letterarie, artistiche, storiche, filosofiche e psicol |
| 2.6.3.2.6 | Docenti di scienze giuridiche, economich | 2 | 6 | Gli insegnanti di scienze giuridiche, economiche e sociali svolgono prevalenteme |
| 2.6.3.3.1 | Docenti di discipline umanistiche nella  | 2 | 6 | Gli insegnanti di discipline umanistiche nella scuola secondaria inferiore svolg |
| 2.6.3.3.2 | Docenti di discipline tecniche e scienti | 2 | 6 | Gli insegnanti di discipline tecniche e scientifiche nella scuola secondaria inf |
| 2.6.4.1.0 | Docenti di scuola primaria | 2 | 6 | L'insegnamento nella scuola primaria è prevalentemente basato su conoscenze e se |
| 2.6.5.2.0 | Ispettori scolastici e professioni assim | 2 | 6 | Gli ispettori scolastici svolgono lavoro prevalentemente intellettuale: analisi  |
| 2.6.5.3.2 | Esperti della progettazione formativa e  | 2 | 6 | Questa professione comporta la progettazione di curricula, il coordinamento di a |
| 2.6.5.4.0 | Consiglieri dell'orientamento | 2 | 6 | I consiglieri dell'orientamento svolgono principalmente lavoro basato sulla cono |
| 2.6.5.5.1 | Insegnanti di arti figurative | 2 | 6 | Questi insegnanti di arti figurative svolgono lezioni prevalentemente in presenz |
| 2.6.5.5.5 | Insegnanti di lingue | 2 | 6 | Gli insegnanti di lingue svolgono un lavoro intrinsecamente interattivo e relazi |
| 3.1.1.1.1 | Tecnici geologici | 3 | 6 | I tecnici geologici svolgono un mix di lavoro in campo (rilevamenti, monitoraggi |
| 3.1.1.2.0 | Tecnici chimici | 3 | 6 | I tecnici chimici svolgono analisi di laboratorio, controllo qualità e lavoro te |
| 3.1.2.6.2 | Tecnici delle trasmissioni radio-televis | 3 | 6 | I tecnici delle trasmissioni radio-televisive svolgono un mix di lavoro tecnico  |
| 3.1.3.1.0 | Tecnici meccanici | 3 | 6 | I tecnici meccanici svolgono un mix di lavoro tecnico-cognitivo (progettazione C |
| 3.1.3.4.0 | Tecnici elettronici | 3 | 6 | I tecnici elettronici svolgono attività di progettazione, installazione, manuten |
| 3.1.3.5.0 | Tecnici delle costruzioni civili e profe | 3 | 6 | I tecnici delle costruzioni civili svolgono un mix di lavoro tecnico-cognitivo ( |
| 3.1.3.6.0 | Tecnici del risparmio energetico e delle | 3 | 6 | La professione combina lavoro tecnico-cognitivo (analisi energetica, verifica pr |
| 3.1.3.7.2 | Disegnatori tessili | 3 | 6 | I disegnatori tessili svolgono principalmente lavoro digitale utilizzando softwa |
| 3.1.4.1.2 | Tecnici della conduzione e del controllo | 3 | 6 | Gli operatori di impianti chimici lavorano principalmente con sistemi di control |
| 3.1.4.2.1 | Tecnici della produzione di energia term | 3 | 6 | Questi tecnici svolgono attività miste di monitoraggio, gestione di sistemi di c |
| 3.1.5.3.0 | Tecnici della produzione manifatturiera | 3 | 6 | I tecnici della produzione manifatturiera svolgono un mix di lavoro tecnico-cogn |
| 3.1.5.5.0 | Tecnici della produzione di servizi | 3 | 6 | I tecnici della produzione di servizi svolgono lavoro prevalentemente cognitivo  |
| 3.1.6.2.1 | Piloti e ufficiali di aeromobili | 3 | 6 | Piloti e ufficiali di aeromobili svolgono un mix di compiti automatizzabili digi |
| 3.1.6.2.3 | Tecnici aerospaziali | 3 | 6 | I tecnici aerospaziali svolgono un mix di lavoro tecnico-cognitivo (installazion |
| 3.1.6.3.1 | Controllori di volo | 3 | 6 | I controllori di volo svolgono lavoro prevalentemente cognitivo basato su monito |
| 3.1.6.3.2 | Tecnici del traffico aeroportuale | 3 | 6 | I tecnici del traffico aeroportuale svolgono attività di coordinamento operativo |
| 3.1.6.4.0 | Tecnici dell'organizzazione del traffico | 3 | 6 | I tecnici dell'organizzazione del traffico ferroviario svolgono principalmente l |
| 3.1.7.2.1 | Tecnici degli apparati audio-video e del | 3 | 6 | Questa professione comporta un lavoro tecnico e creativo sostanzialmente digital |
| 3.1.7.2.2 | Tecnici del suono | 3 | 6 | I tecnici del suono operano prevalentemente con apparati digitali e software aud |
| 3.1.7.3.0 | Tecnici di apparati medicali e per la di | 3 | 6 | I tecnici di apparati medicali svolgono un mix di lavoro tecnico-cognitivo (diag |
| 3.1.8.2.0 | Tecnici della sicurezza sul lavoro | 3 | 6 | I tecnici della sicurezza sul lavoro svolgono un mix di attività conoscitive (va |
| 3.2.1.3.2 | Tecnici sanitari di laboratorio biomedic | 3 | 6 | I tecnici di laboratorio biomedico svolgono lavoro prevalentemente digitale e an |
| 3.2.1.5.3 | Ergonomo | 3 | 6 | L'ergonomo svolge lavoro prevalentemente cognitivo di analisi, valutazione e pro |
| 3.2.2.3.1 | Tecnici di laboratorio biochimico | 3 | 6 | I tecnici di laboratorio biochimico svolgono lavoro prevalentemente analitico e  |
| 3.2.2.3.4 | Tecnico biologo | 3 | 6 | Il lavoro del tecnico biologo è prevalentemente basato su conoscenze e procedure |
| 3.3.1.2.3 | Amministratore di stabili e condomini | 3 | 6 | Gli amministratori di stabili svolgono un mix di lavoro amministrativo (gestione |
| 3.3.2.3.0 | Agenti assicurativi | 3 | 6 | Gli agenti assicurativi svolgono un mix di lavoro conoscitivo (valutazione del r |
| 3.3.2.4.0 | Periti, valutatori di rischio e liquidat | 3 | 6 | Questa professione comporta un lavoro prevalentemente cognitivo—raccolta dati, v |
| 3.3.3.2.0 | Responsabili di magazzino e della distri | 3 | 6 | I responsabili di magazzino svolgono un mix di compiti digitali e fisici: la ges |
| 3.3.3.3.2 | Periti commerciali | 3 | 6 | I periti commerciali svolgono valutazioni che beneficiano sempre più di strument |
| 3.3.3.4.0 | Tecnici della vendita e della distribuzi | 3 | 6 | I tecnici della vendita e della distribuzione svolgono un mix di lavoro conoscit |
| 3.3.4.1.0 | Spedizionieri e tecnici dell'organizzazi | 3 | 6 | Gli spedizionieri e tecnici dell'organizzazione commerciale svolgono lavoro prev |
| 3.3.4.2.0 | Agenti di commercio | 3 | 6 | Gli agenti di commercio svolgono un mix di lavoro digitale e interpersonale: la  |
| 3.3.4.3.0 | Agenti concessionari | 3 | 6 | Gli agenti concessionari promuovono e vendono prodotti di marca in un territorio |
| 3.3.4.4.0 | Agenti di pubblicità | 3 | 6 | Gli agenti di pubblicità svolgono un mix di lavoro conoscitivo (gestione relazio |
| 3.3.4.5.0 | Agenti e periti immobiliari | 3 | 6 | Gli agenti e periti immobiliari svolgono un mix di lavoro conoscitivo (valutazio |
| 3.3.4.6.0 | Rappresentanti di commercio | 3 | 6 | I rappresentanti di commercio svolgono un mix di lavoro digitale e interpersonal |
| 3.3.4.7.0 | Agenti e rappresentanti di artisti ed at | 3 | 6 | Gli agenti e rappresentanti di artisti e atleti svolgono un mix di lavoro conosc |
| 3.4.1.2.1 | Organizzatori di fiere, esposizioni ed e | 3 | 6 | Gli organizzatori di fiere svolgono un mix di lavoro coordinativo digitale e fis |
| 3.4.1.4.0 | Agenti di viaggio | 3 | 6 | Gli agenti di viaggio svolgono lavoro prevalentemente cognitivo: ricerca destina |
| 3.4.2.2.1 | Insegnanti nella formazione professional | 3 | 6 | Gli insegnanti di formazione professionale insegnano competenze tecniche pratich |
| 3.4.2.5.2 | Osservatori sportivi | 3 | 6 | Gli osservatori sportivi svolgono un mix di osservazione diretta (partite, allen |
| 3.4.3.2.0 | Tecnici dell'organizzazione della produz | 3 | 6 | Questa professione organizza e coordina i flussi di lavoro per produzioni radiot |
| 3.4.4.2.2 | Tecnici delle biblioteche | 3 | 6 | I tecnici delle biblioteche svolgono compiti misti tra digitale e fisico: catalo |
| 3.4.4.3.3 | Periti calligrafi | 3 | 6 | L'analisi della calligrafia e l'autenticazione richiedono un lavoro prevalenteme |
| 3.4.5.3.0 | Tecnici dei servizi per l'impiego | 3 | 6 | I tecnici dei servizi per l'impiego svolgono principalmente lavoro basato su con |
| 3.4.6.1.0 | Tecnici dei servizi giudiziari | 3 | 6 | I tecnici dei servizi giudiziari svolgono principalmente lavoro amministrativo e |
| 3.4.6.5.0 | Controllori fiscali | 3 | 6 | I controllori fiscali svolgono lavoro ad alta intensità di conoscenza, coinvolge |
| 3.4.6.6.1 | Tecnici dei servizi pubblici di concessi | 3 | 6 | La professione comporta l'esame di domande, la verifica di condizioni e l'elabor |
| 3.4.6.6.2 | Tecnici dei servizi pubblici per il rila | 3 | 6 | La professione comporta l'esame di domande, la verifica di condizioni e il rilas |
| 4.2.1.4.0 | Addetti agli sportelli delle agenzie di  | 4 | 6 | La professione comporta compiti amministrativi e di registrazione significativi  |
| 4.2.2.1.0 | Addetti all'accoglienza e all'informazio | 4 | 6 | Questa professione combina compiti informativi e amministrativi (compilazione mo |
| 4.3.1.2.0 | Addetti alla gestione dei magazzini e pr | 4 | 6 | Le professioni di gestione magazzino combinano compiti digitali e fisici. Le att |
| 4.4.2.2.0 | Addetti a biblioteche e professioni assi | 4 | 6 | Il personale bibliotecario svolge un mix di compiti fisici (collocazione, gestio |
| 5.1.3.4.0 | Addetti all'informazione e all'assistenz | 5 | 6 | Questa professione riguarda l'informazione e l'assistenza ai clienti, sempre più |
| 5.4.1.2.1 | Allibratori | 5 | 6 | Le attività principali dell'allibratore—accettazione scommesse, registrazione, c |
| 5.4.1.2.3 | Ricevitori | 5 | 6 | I ricevitori svolgono attività miste di gestione del denaro, interazione con cli |
| 5.5.4.1.0 | Esercenti di agenzie per il disbrigo di  | 5 | 6 | Gli esercenti di agenzie per il disbrigo di pratiche gestiscono attività amminis |
| 6.3.4.1.0 | Operatori delle attività poligrafiche di | 6 | 6 | Le operazioni di prestampa coinvolgono lavoro sostanzialmente digitale (impagina |
| 7.2.8.1.0 | Addetti a macchine confezionatrici e al  | 7 | 6 | Questa professione riguarda la conduzione e il monitoraggio di macchinari per il |
| 8.1.2.2.0 | Lettori di contatori, collettori di mone | 8 | 6 | Questa professione combina lavoro di campo (lettura contatori, raccolta monete,  |
| 8.1.3.2.0 | Personale non qualificato addetto all'im | 8 | 6 | Questa professione comprende principalmente compiti fisici di magazzino e imball |
| 1.1.1.1.1 | Membri di organismi di governo e di asse | 1 | 5 | I ruoli legislativi ed esecutivi comportano un lavoro intellettuale significativ |
| 1.1.1.1.2 | Membri di autorità indipendenti con pote | 1 | 5 | I membri di autorità indipendenti svolgono lavoro ad alta intensità di conoscenz |
| 1.1.1.3.0 | Membri di organismi di governo e di asse | 1 | 5 | Questo ruolo comporta decisioni legislative e normative, formulazione di politic |
| 1.1.2.1.0 | Ambasciatori, ministri plenipotenziari e | 1 | 5 | Gli ambasciatori e i dirigenti diplomatici svolgono un mix di lavoro intellettua |
| 1.1.2.2.1 | Prefetti, vice prefetti e alti dirigenti | 1 | 5 | I prefetti e gli alti dirigenti della carriera prefettizia svolgono attività di  |
| 1.1.2.2.2 | Responsabili della sicurezza pubblica | 1 | 5 | Questi ruoli di alta dirigenza della sicurezza pubblica comportano decisioni str |
| 1.1.2.3.5 | Sovrintendenti al patrimonio culturale n | 1 | 5 | Questa professione comporta un lavoro prevalentemente intellettuale—implementazi |
| 1.1.2.4.3 | Dirigenti nella sanità | 1 | 5 | I dirigenti sanitari svolgono un lavoro prevalentemente di coordinamento e gesti |
| 1.1.3.1.0 | Magistrati con funzioni direttive superi | 1 | 5 | I magistrati con funzioni direttive svolgono un mix di lavoro intellettuale (ana |
| 1.2.1.1.0 | Imprenditori e amministratori di grandi  | 1 | 5 | Si tratta di dirigenti senior che gestiscono grandi imprese agricole, forestali  |
| 1.2.2.1.0 | Direttori e dirigenti generali di aziend | 1 | 5 | Questi sono ruoli di alta dirigenza in aziende del settore primario (agricoltura |
| 1.3.1.2.1 | Imprenditori e responsabili di piccole a | 1 | 5 | Gli imprenditori di piccole aziende manifatturiere ed estrattive svolgono attivi |
| 1.3.1.2.2 | Imprenditori e responsabili di piccole a | 1 | 5 | Questi imprenditori e responsabili di piccole aziende nel settore utilities e ge |
| 1.3.1.3.0 | Imprenditori e responsabili di piccole a | 1 | 5 | I piccoli imprenditori edili svolgono un mix di lavoro cognitivo (pianificazione |
| 1.3.1.4.0 | Imprenditori e responsabili di piccole a | 1 | 5 | Gli imprenditori di piccole aziende commerciali svolgono attività miste di piani |
| 1.3.1.5.0 | Imprenditori e responsabili di piccoli a | 1 | 5 | Gli imprenditori di piccoli alberghi e esercizi di ristorazione gestiscono compi |
| 1.3.1.6.1 | Imprenditori e responsabili di piccole a | 1 | 5 | Questi imprenditori di piccole aziende nei trasporti e magazzinaggio svolgono un |
| 1.3.1.9.2 | Imprenditori e responsabili di piccole a | 1 | 5 | Questi imprenditori e responsabili di piccole aziende nei servizi sanitari e soc |
| 1.3.1.9.3 | Imprenditori e responsabili di piccole a | 1 | 5 | Questi imprenditori di piccole aziende nel settore sportivo, ricreativo e dell'i |
| 2.3.1.3.0 | Agronomi e forestali | 2 | 5 | Gli agronomi e forestali svolgono un mix di ricerca sul campo, analisi dati e la |
| 2.3.1.4.0 | Medici veterinari | 2 | 5 | I medici veterinari svolgono un mix di lavoro intellettuale (diagnosi, pianifica |
| 2.4.1.1.0 | Medici generici | 2 | 5 | I medici generici svolgono un mix di lavoro intellettuale (diagnosi, pianificazi |
| 2.4.1.3.0 | Specialisti in terapie chirurgiche | 2 | 5 | Gli specialisti in terapie chirurgiche affrontano un'esposizione moderata all'IA |
| 2.5.1.1.3 | Specialisti in pubblica sicurezza | 2 | 5 | Gli specialisti in pubblica sicurezza svolgono attività di pianificazione strate |
| 2.5.3.3.1 | Psicologi clinici e psicoterapeuti | 2 | 5 | Gli psicologi clinici e psicoterapeuti svolgono lavoro ad alta intensità di cono |
| 2.5.4.5.3 | Curatori e conservatori di musei | 2 | 5 | I curatori e conservatori di musei svolgono un mix di lavoro intellettuale (rice |
| 2.5.5.3.1 | Coreografi | 2 | 5 | I coreografi combinano la concezione creativa (sempre più supportata da AI per l |
| 2.5.5.6.2 | Specialisti nella conservazione dei beni | 2 | 5 | Questa professione combina lavoro specializzato (diagnostica, tecniche di conser |
| 2.5.6.1.0 | Specialisti in discipline religiose e te | 2 | 5 | Questa professione combina lavoro intellettuale (ricerca teologica, studio della |
| 2.6.3.1.1 | Docenti di discipline artistiche nelle a | 2 | 5 | Gli insegnanti di discipline artistiche combinano lavoro intellettuale (progetta |
| 2.6.3.1.2 | Docenti di discipline musicali nei conse | 2 | 5 | L'insegnamento della musica nei conservatori richiede interazione umana in tempo |
| 2.6.4.2.0 | Docenti di scuola pre-primaria | 2 | 5 | L'insegnamento nella scuola pre-primaria combina compiti di pianificazione e val |
| 2.6.5.1.0 | Specialisti nell'educazione e nella form | 2 | 5 | Questa professione combina un lavoro intellettuale significativo (progettazione  |
| 2.6.5.5.3 | Insegnanti di canto | 2 | 5 | L'insegnamento del canto richiede interazione umana significativa in tempo reale |
| 2.6.5.5.4 | Insegnanti di strumenti musicali | 2 | 5 | L'insegnamento di strumenti musicali comporta componenti interpersonali e fisich |
| 3.1.1.1.2 | Tecnici fisici e nucleari | 3 | 5 | I tecnici nucleari e fisici svolgono attività miste di monitoraggio apparecchiat |
| 3.1.2.6.1 | Tecnici per le telecomunicazioni | 3 | 5 | I tecnici per le telecomunicazioni svolgono un mix di lavoro fisico (installazio |
| 3.1.3.2.1 | Tecnici dei prodotti ceramici | 3 | 5 | I tecnici dei prodotti ceramici svolgono un mix di lavoro tecnico-cognitivo (sup |
| 3.1.3.2.2 | Tecnici minerari | 3 | 5 | I tecnici minerari svolgono un mix di rilevazioni geologiche in campo, valutazio |
| 3.1.3.2.3 | Tecnici metallurgici | 3 | 5 | I tecnici metallurgici svolgono un mix di lavoro tecnico-conoscitivo (ricerca su |
| 3.1.3.3.0 | Elettrotecnici | 3 | 5 | Gli elettrotecnici svolgono un mix di lavoro tecnico-cognitivo (progettazione ci |
| 3.1.4.1.1 | Tecnici della conduzione e del controllo | 3 | 5 | Questo ruolo comporta il monitoraggio e il controllo di sistemi automatizzati pe |
| 3.1.4.1.3 | Tecnici della conduzione e del controllo | 3 | 5 | Questo ruolo comporta il monitoraggio e il controllo di sistemi automatizzati di |
| 3.1.4.1.4 | Tecnici della conduzione e del controllo | 3 | 5 | Questa professione comporta il monitoraggio e il controllo di sistemi automatizz |
| 3.1.4.1.5 | Tecnici della conduzione e del controllo | 3 | 5 | Questo ruolo comporta il monitoraggio e il controllo di catene di montaggio auto |
| 3.1.4.2.2 | Tecnici dell'esercizio di reti idriche e | 3 | 5 | Questa professione combina lavoro tecnico-cognitivo (monitoraggio sistemi, anali |
| 3.1.4.2.3 | Tecnici dell'esercizio di reti di distri | 3 | 5 | Questa professione combina lavoro tecnico-cognitivo (monitoraggio sistemi, anali |
| 3.1.5.2.0 | Tecnici della gestione di cantieri edili | 3 | 5 | I tecnici di cantiere svolgono attività miste di supervisione fisica in loco, co |
| 3.1.5.4.2 | Tecnici della produzione alimentare | 3 | 5 | I tecnici della produzione alimentare svolgono attività di supervisione tecnica, |
| 3.1.6.1.1 | Comandanti navali | 3 | 5 | I comandanti navali svolgono un mix di navigazione tecnica (sempre più automatiz |
| 3.1.6.1.2 | Ufficiali e assistenti di bordo | 3 | 5 | Gli ufficiali di bordo svolgono attività di monitoraggio tecnico, gestione delle |
| 3.1.6.1.3 | Piloti navali | 3 | 5 | I piloti navali operano in ambienti marittimi complessi richiedendo presenza fis |
| 3.1.6.2.2 | Tecnici avionici | 3 | 5 | I tecnici avionici svolgono un mix di lavoro tecnico-cognitivo (diagnostica, tar |
| 3.1.6.5.0 | Tecnici dell'organizzazione del traffico | 3 | 5 | I tecnici dell'organizzazione del traffico portuale svolgono compiti di supervis |
| 3.1.8.1.0 | Tecnici della sicurezza degli impianti | 3 | 5 | Questa professione combina lavoro tecnico-cognitivo (progettazione di sistemi, v |
| 3.1.8.3.1 | Tecnici del controllo ambientale | 3 | 5 | I tecnici del controllo ambientale svolgono attività miste di monitoraggio sul c |
| 3.1.8.3.2 | Tecnici della raccolta e trattamento dei | 3 | 5 | Questa professione combina lavoro tecnico-cognitivo con presenza operativa sul c |
| 3.2.1.1.1 | Professioni sanitarie infermieristiche | 3 | 5 | L'infermieristica combina lavoro cognitivo (pianificazione dell'assistenza, valu |
| 3.2.1.2.3 | Logopedisti | 3 | 5 | I logopedisti svolgono un mix di lavoro cognitivo e interazione diretta con i pa |
| 3.2.1.2.4 | Ortottisti - assistenti di oftalmologia | 3 | 5 | Gli ortottisti svolgono una combinazione di valutazione clinica, interazione con |
| 3.2.1.2.5 | Terapisti della neuro e psicomotricità d | 3 | 5 | La professione richiede valutazione clinica diretta, interventi terapeutici prat |
| 3.2.1.2.7 | Educatori professionali | 3 | 5 | Il lavoro dell'educatore professionale è fondamentalmente relazionale e interper |
| 3.2.1.2.8 | Terapisti occupazionali | 3 | 5 | I terapisti occupazionali svolgono un mix di lavoro cognitivo (valutazione, prog |
| 3.2.1.3.1 | Tecnici audiometristi | 3 | 5 | I tecnici audiometristi svolgono un mix di compiti tecnico-clinici: esecuzione d |
| 3.2.1.3.3 | Tecnici sanitari di radiologia medica | 3 | 5 | I tecnici sanitari di radiologia medica svolgono compiti tecnici e procedurali c |
| 3.2.1.3.4 | Tecnici di neurofisiopatologia | 3 | 5 | I tecnici di neurofisiopatologia svolgono un lavoro misto tra competenze tecnich |
| 3.2.1.4.1 | Tecnici ortopedici | 3 | 5 | I tecnici ortopedici svolgono un mix di lavoro tecnico e manuale: progettazione, |
| 3.2.1.4.2 | Tecnici audioprotesisti | 3 | 5 | I tecnici audioprotesisti svolgono un mix di lavoro tecnico e manuale. Le attivi |
| 3.2.1.4.3 | Igienisti dentali | 3 | 5 | Gli igienisti dentali svolgono un mix di procedure cliniche (ablazione del tarta |
| 3.2.1.4.4 | Tecnici della fisiopatologia cardiocirco | 3 | 5 | Questa professione comporta l'operazione e la manutenzione di apparecchiature ca |
| 3.2.1.4.5 | Dietisti | 3 | 5 | I dietisti svolgono un mix di lavoro conoscitivo (analisi nutrizionale, formulaz |
| 3.2.1.5.1 | Tecnici della prevenzione nell'ambiente  | 3 | 5 | Questa professione combina ispezioni sul campo, documentazione normativa e valut |
| 3.2.1.5.2 | Assistenti sanitari | 3 | 5 | Gli assistenti sanitari svolgono un mix di lavoro conoscitivo (analisi epidemiol |
| 3.2.1.6.1 | Ottici e ottici optometristi | 3 | 5 | Gli ottici svolgono un mix di lavoro tecnico-conoscitivo (esame visivo, prescriz |
| 3.2.1.6.2 | Odontotecnici | 3 | 5 | Gli odontotecnici svolgono un mix di lavoro tecnico e artigianale manuale. Sebbe |
| 3.2.2.1.1 | Tecnici agronomi | 3 | 5 | I tecnici agronomi svolgono un mix di lavoro tecnico sul campo (monitoraggio col |
| 3.2.2.3.2 | Tecnici dei prodotti alimentari | 3 | 5 | I tecnici dei prodotti alimentari svolgono analisi di laboratorio, test di quali |
| 3.2.2.3.3 | Tecnici di laboratorio veterinario | 3 | 5 | I tecnici di laboratorio veterinario svolgono un mix di lavoro manuale (prelievo |
| 3.3.3.3.1 | Commissari e aggiudicatori d'asta | 3 | 5 | I commissari d'asta svolgono un mix di lavoro cognitivo (valutazione, analisi di |
| 3.4.1.1.0 | Tecnici delle attività ricettive e profe | 3 | 5 | Questa professione combina lavoro di conoscenza (marketing turistico, analisi te |
| 3.4.1.2.2 | Organizzatori di convegni e ricevimenti | 3 | 5 | Gli organizzatori di convegni svolgono un mix di compiti digitali e interpersona |
| 3.4.2.1.1 | Istruttori di volo | 3 | 5 | Gli istruttori di volo combinano la trasmissione di conoscenze teoriche (che l'I |
| 3.4.2.1.3 | Istruttori di nautica | 3 | 5 | Gli istruttori di nautica svolgono insegnamento teorico e pratico sulla guida di |
| 3.4.2.3.0 | Istruttori di tecniche in campo artistic | 3 | 5 | Questa professione comporta l'insegnamento di tecniche artistiche attraverso ist |
| 3.4.2.5.1 | Organizzatori di eventi e di strutture s | 3 | 5 | Gli organizzatori di eventi e strutture sportive svolgono un mix di lavoro ammin |
| 3.4.4.1.2 | Allestitori di scena | 3 | 5 | Gli allestitori di scena combinano lavoro di costruzione fisica con compiti di p |
| 3.4.4.2.1 | Tecnici dei musei | 3 | 5 | I tecnici dei musei svolgono un mix di lavoro fisico (manipolazione di reperti,  |
| 3.4.4.3.1 | Stimatori di opere d'arte | 3 | 5 | Gli stimatori di opere d'arte combinano lavoro specializzato (ricerca, analisi,  |
| 3.4.4.3.2 | Periti filatelici e numismatici | 3 | 5 | I periti filatelici e numismatici svolgono un lavoro misto tra analisi storico-a |
| 3.4.5.1.0 | Assistenti sociali | 3 | 5 | Gli assistenti sociali svolgono un mix di lavoro conoscitivo (valutazione dei ca |
| 3.4.5.2.0 | Tecnici del reinserimento e dell'integra | 3 | 5 | Questa professione comporta un lavoro sostanziale di interazione interpersonale, |
| 3.4.5.4.0 | Tecnici dei servizi di sicurezza privati | 3 | 5 | I professionisti della sicurezza privata svolgono un mix di sorveglianza fisica, |
| 3.4.6.2.0 | Ufficiali della Polizia di Stato | 3 | 5 | Gli ufficiali di polizia svolgono un mix di lavoro sul campo (pattugliamenti, ar |
| 3.4.6.4.0 | Ufficiali della guardia di finanza | 3 | 5 | Gli ufficiali della guardia di finanza svolgono attività miste tra lavoro cognit |
| 4.2.2.2.0 | Addetti all'accoglienza nei servizi di a | 4 | 5 | Questo ruolo combina compiti digitali e interpersonali: la gestione delle prenot |
| 4.4.1.3.0 | Addetti allo smistamento e al recapito d | 4 | 5 | Questa professione combina compiti digitali e fisici: lo smistamento della posta |
| 5.1.1.1.0 | Esercenti delle vendite all'ingrosso | 5 | 5 | Gli esercenti delle vendite all'ingrosso svolgono attività miste tra gestione st |
| 5.1.1.2.1 | Esercenti delle vendite al minuto in neg | 5 | 5 | I commercianti al dettaglio combinano lavoro fisico e interpersonale significati |
| 5.1.1.3.0 | Esercenti di distributori di carburanti  | 5 | 5 | Questa professione combina operazioni commerciali fisiche (distribuzione carbura |
| 5.1.2.1.0 | Commessi delle vendite all'ingrosso | 5 | 5 | I commessi delle vendite all'ingrosso svolgono un mix di compiti fisici (gestion |
| 5.1.2.2.0 | Commessi delle vendite al minuto | 5 | 5 | I commessi delle vendite al minuto svolgono un mix di lavoro interpersonale rivo |
| 5.1.2.3.0 | Addetti ad attività organizzative delle  | 5 | 5 | Questo ruolo combina compiti organizzativi e amministrativi (raccolta ordini, ge |
| 5.1.2.5.1 | Venditori a domicilio | 5 | 5 | La vendita porta a porta richiede interazione interpersonale significativa e pre |
| 5.1.3.2.0 | Dimostratori e professioni assimilate | 5 | 5 | I dimostratori svolgono un mix di attività interpersonali (spiegazione caratteri |
| 5.2.1.1.0 | Esercenti nelle attività ricettive | 5 | 5 | Gli esercenti nelle attività ricettive svolgono compiti amministrativi e strateg |
| 5.2.2.5.1 | Esercenti di ristoranti, fast food, pizz | 5 | 5 | Gli esercenti di ristorazione combinano compiti gestionali e amministrativi sign |
| 5.4.1.1.1 | Esercenti di cinema e teatri | 5 | 5 | Gli esercenti di cinema e teatri combinano compiti di gestione strategica (piani |
| 5.4.1.1.5 | Esercenti di sale scommesse | 5 | 5 | Gli esercenti di sale scommesse combinano compiti di gestione aziendale (strateg |
| 5.6.1.8.0 | Esercenti di garage ed autorimesse | 5 | 5 | Gli esercenti di garage e autorimesse svolgono attività miste tra gestione fisic |
| 6.2.4.2.0 | Manutentori e riparatori di apparati ele | 6 | 5 | Questa professione richiede lavoro manuale specializzato e presenza fisica per r |
| 6.2.4.6.0 | Installatori, manutentori e riparatori d | 6 | 5 | Questa professione comporta l'installazione, la manutenzione e la riparazione fi |
| 6.3.4.2.0 | Stampatori offset e alla rotativa | 6 | 5 | Gli stampatori offset e alla rotativa svolgono un mix di operazioni fisiche su m |
| 6.5.3.3.1 | Modellisti di capi di abbigliamento | 6 | 5 | I modellisti combinano lavoro digitale e manuale: traducono i disegni in cartamo |
| 7.1.4.2.0 | Operatori di impianti per la preparazion | 7 | 5 | Questa professione comporta la conduzione di macchinari industriali e reattori c |
| 7.1.5.1.1 | Conduttori di impianti per la raffinazio | 7 | 5 | Questa professione comporta la conduzione e il monitoraggio di impianti industri |
| 7.1.5.2.0 | Operatori di macchinari e di impianti pe | 7 | 5 | Questa professione comporta la conduzione di impianti chimici e il monitoraggio  |
| 7.1.5.3.1 | Operatori di macchinari per la produzion | 7 | 5 | Questo ruolo comporta la conduzione e il monitoraggio di macchinari per la produ |
| 7.1.6.1.0 | Conduttori di caldaie a vapore e di moto | 7 | 5 | Questa professione comporta il monitoraggio e il controllo di caldaie industrial |
| 7.1.7.1.0 | Operatori di catene di montaggio automat | 7 | 5 | Questa professione riguarda il monitoraggio e il controllo di linee di montaggio |
| 7.1.8.2.0 | Conduttori di forni e di impianti per il | 7 | 5 | Questo ruolo comporta la conduzione di forni e impianti per il trattamento termi |
| 7.2.1.1.0 | Conduttori di macchine utensili automati | 7 | 5 | Questi operatori conducono macchine utensili industriali sempre più automatizzat |
| 7.2.2.2.0 | Conduttori di macchinari per la fabbrica | 7 | 5 | Questa professione comporta la conduzione di macchinari fissi per la produzione  |
| 7.2.3.1.0 | Conduttori di macchinari per la confezio | 7 | 5 | Questa professione riguarda la conduzione di macchinari specializzati per la fab |
| 7.2.3.2.0 | Conduttori di macchinari per la fabbrica | 7 | 5 | Questa professione riguarda la conduzione di macchinari per la lavorazione della |
| 7.2.3.3.0 | Conduttori di macchinari per la fabbrica | 7 | 5 | Questa professione comporta la conduzione di macchinari industriali per la lavor |
| 7.2.5.1.0 | Conduttori di macchinari per tipografia  | 7 | 5 | La professione richiede la conduzione di macchinari per la stampa e la lavorazio |
| 7.2.5.2.0 | Conduttori di macchinari per la fabbrica | 7 | 5 | Questa professione riguarda la conduzione di macchinari fissi per la fabbricazio |
| 7.2.6.1.0 | Addetti a macchinari per la filatura e l | 7 | 5 | Questa professione riguarda la conduzione di macchinari automatici per filatura  |
| 7.2.6.2.0 | Addetti a telai meccanici e a macchinari | 7 | 5 | Questa professione riguarda la conduzione di macchinari tessili automatizzati, l |
| 7.2.6.3.0 | Operai addetti a macchinari industriali  | 7 | 5 | Questa professione riguarda la conduzione di macchinari industriali per la produ |
| 7.2.6.4.0 | Addetti ai macchinari per il trattamento | 7 | 5 | Questa professione riguarda la conduzione di macchinari automatici per il tratta |
| 7.2.7.3.0 | Assemblatori e cablatori di apparecchiat | 7 | 5 | La professione comporta il montaggio e il cablaggio di componenti elettronici su |
| 7.3.2.7.0 | Conduttori di macchinari per la lavorazi | 7 | 5 | Questa professione riguarda la conduzione di macchinari industriali per la lavor |
| 7.3.2.9.0 | Conduttori di macchinari per la produzio | 7 | 5 | Questa professione comporta la conduzione di macchinari industriali per la produ |
| 7.4.2.1.0 | Autisti di taxi, conduttori di automobil | 7 | 5 | Gli autisti di taxi e conducenti di veicoli per passeggeri affrontano un'esposiz |
| 1.1.1.2.0 | Membri di organismi di governo e di asse | 1 | 4 | I legislatori regionali e i funzionari delle province autonome svolgono un mix d |
| 1.1.1.4.0 | Membri di organismi di governo e di asse | 1 | 4 | Questo ruolo comporta deliberazione legislativa, formulazione di politiche e sup |
| 1.3.1.1.0 | Imprenditori e responsabili di piccole a | 1 | 4 | Questi imprenditori agricoli svolgono un mix di pianificazione strategica, gesti |
| 2.4.1.5.0 | Dentisti e odontostomatologi | 2 | 4 | L'odontoiatria è una professione essenzialmente clinica e manuale che richiede m |
| 2.4.1.8.0 | Anestesisti e rianimatori | 2 | 4 | Gli anestesisti e rianimatori svolgono attività cliniche critiche che richiedono |
| 2.5.5.2.2 | Attori | 2 | 4 | La recitazione è radicata nella performance umana dal vivo, nell'autenticità emo |
| 2.5.5.4.4 | Cantanti | 2 | 4 | Il lavoro principale dei cantanti—l'esecuzione vocale e l'interpretazione artist |
| 2.5.5.6.1 | Restauratori dei beni culturali | 2 | 4 | Il restauro dei beni culturali è fondamentalmente un mestiere artigianale che ri |
| 2.6.3.1.3 | Docenti di arte drammatica e danza nelle | 2 | 4 | Gli insegnanti di arte drammatica e danza svolgono un'attività fondamentalmente  |
| 2.6.5.5.2 | Insegnanti di danza | 2 | 4 | L'insegnamento della danza è fondamentalmente radicato nella dimostrazione fisic |
| 3.1.5.1.0 | Tecnici di produzione in miniere e cave | 3 | 4 | I tecnici di produzione in miniere e cave svolgono attività di supervisione in l |
| 3.1.5.4.1 | Tecnici della preparazione alimentare | 3 | 4 | I tecnici della preparazione alimentare svolgono un mix di lavoro manuale (cottu |
| 3.2.1.1.2 | Professioni sanitarie ostetriche | 3 | 4 | L'ostetricia è radicata nel lavoro clinico pratico che richiede la presenza uman |
| 3.2.1.2.2 | Fisioterapisti e assimilati | 3 | 4 | I fisioterapisti svolgono principalmente lavoro clinico pratico e in presenza, r |
| 3.2.1.2.6 | Tecnici della riabilitazione psichiatric | 3 | 4 | I tecnici della riabilitazione psichiatrica svolgono principalmente lavoro inter |
| 3.2.2.1.2 | Tecnici forestali | 3 | 4 | I tecnici forestali svolgono un mix di lavoro sul campo (sopralluoghi, valutazio |
| 3.2.2.2.0 | Zootecnici | 3 | 4 | Gli zootecnici svolgono un mix di lavoro tecnico-conoscitivo (genetica animale,  |
| 3.4.1.3.0 | Animatori turistici e professioni assimi | 3 | 4 | Gli animatori turistici combinano presenza fisica, interazione interpersonale in |
| 3.4.1.5.2 | Guide turistiche | 3 | 4 | Le guide turistiche svolgono principalmente lavoro in presenza, in tempo reale,  |
| 3.4.2.1.2 | Istruttori di guida automobilistica | 3 | 4 | Gli istruttori di guida combinano la trasmissione di conoscenze teoriche (che l' |
| 3.4.2.4.0 | Istruttori di discipline sportive non ag | 3 | 4 | Gli istruttori di discipline sportive non agonistiche dipendono fortemente dalla |
| 3.4.2.6.1 | Allenatori e tecnici sportivi | 3 | 4 | Gli allenatori e tecnici sportivi dipendono fortemente dalla presenza fisica, da |
| 3.4.3.1.2 | Presentatori di performance artistiche e | 3 | 4 | Questa professione richiede performance dal vivo e interazione in tempo reale co |
| 3.4.4.4.0 | Tecnici del restauro | 3 | 4 | I tecnici del restauro svolgono un mix di lavoro manuale (preparazione materiali |
| 3.4.6.3.1 | Tecnici dei servizi di sicurezza dei vig | 3 | 4 | Questo ruolo comporta l'organizzazione e il coordinamento delle attività della p |
| 3.4.6.3.3 | Tecnici dei servizi di sicurezza del cor | 3 | 4 | I tecnici dei servizi di sicurezza del corpo forestale svolgono attività miste t |
| 5.1.1.2.2 | Esercenti delle vendite al minuto nei me | 5 | 4 | Questa professione richiede interazione diretta con i clienti, gestione fisica d |
| 5.1.3.1.0 | Indossatori, modelli e professioni assim | 5 | 4 | Le indossatrici e i modelli svolgono principalmente lavoro fisico e in presenza, |
| 5.2.2.1.0 | Cuochi in alberghi e ristoranti | 5 | 4 | Il lavoro dei cuochi è radicato in compiti fisici e in tempo reale: preparazione |
| 5.2.3.1.2 | Assistenti di viaggio e crociera | 5 | 4 | Gli assistenti di viaggio e crociera svolgono compiti misti di servizio al clien |
| 5.2.3.1.3 | Assistenti congressuali e fieristici | 5 | 4 | Gli assistenti congressuali e fieristici svolgono principalmente attività di ser |
| 5.2.3.2.0 | Accompagnatori turistici | 5 | 4 | Gli accompagnatori turistici svolgono principalmente lavoro in presenza, in temp |
| 5.4.1.1.2 | Esercenti di locali notturni | 5 | 4 | Gli esercenti di locali notturni svolgono un mix di attività che richiedono pres |
| 5.4.1.1.3 | Esercenti di attività ricreative | 5 | 4 | Questa professione combina gestione operativa e fisica (gestione di strutture, s |
| 5.4.1.1.4 | Esercenti di attività sportive | 5 | 4 | Gli esercenti di attività sportive combinano lavoro fisico (supervisione degli i |
| 5.5.5.1.0 | Esercenti di agenzie di pompe funebri | 5 | 4 | Gli esercenti di pompe funebri combinano compiti di gestione aziendale (programm |
| 5.6.1.3.2 | Agenti della Guardia di Finanza | 5 | 4 | Gli agenti della Guardia di Finanza svolgono un mix di attività di controllo fis |
| 6.2.2.3.1 | Attrezzisti di macchine utensili | 6 | 4 | Questa professione comporta lavoro manuale specializzato nella preparazione e ge |
| 6.2.3.6.0 | Meccanici collaudatori | 6 | 4 | I collaudatori meccanici svolgono verifiche e misurazioni su motori, macchine e  |
| 6.2.4.4.0 | Installatori e riparatori di apparati di | 6 | 4 | Questa professione richiede un lavoro prevalentemente manuale e fisico—installaz |
| 6.3.1.1.0 | Meccanici di precisione | 6 | 4 | La meccanica di precisione richiede lavoro manuale specializzato, destrezza moto |
| 6.3.1.2.0 | Meccanici e riparatori di protesi, di or | 6 | 4 | Questa professione comporta artigianato specializzato manuale—progettazione, fab |
| 6.3.1.5.1 | Addetti alla produzione di lenti e occhi | 6 | 4 | Questa professione comporta lavoro manuale e tecnico specializzato nella produzi |
| 6.3.1.5.2 | Addetti alla produzione di apparecchi ot | 6 | 4 | Questa professione comporta lavoro manuale specializzato nella produzione di app |
| 6.3.4.5.0 | Rilegatori e rifinitori post stampa | 6 | 4 | La rilegatura e la finitura di libri è principalmente lavoro manuale e fisico ch |
| 6.5.1.4.0 | Degustatori e classificatori di prodotti | 6 | 4 | Questa professione si basa fondamentalmente sulla percezione sensoriale umana (g |
| 7.1.2.3.0 | Operatori di impianti per il trattamento | 7 | 4 | Questa professione riguarda la conduzione di forni e impianti per i trattamenti  |
| 7.1.3.2.2 | Conduttori di impianti per la lavorazion | 7 | 4 | I conduttori di impianti vetrieri svolgono lavori prevalentemente fisici e di mo |
| 7.1.4.1.0 | Conduttori di impianti per la fabbricazi | 7 | 4 | Questa professione riguarda la conduzione di impianti industriali per la fabbric |
| 7.1.4.3.0 | Operatori di impianti per la fabbricazio | 7 | 4 | Gli operatori di impianti cartieri svolgono lavoro prevalentemente fisico e mecc |
| 7.1.5.1.2 | Conduttori di impianti per la stazzatura | 7 | 4 | Questa professione riguarda la conduzione di impianti fissi per la lavorazione d |
| 7.1.5.3.2 | Operatori di macchinari per la produzion | 7 | 4 | Questa professione comporta la conduzione e il controllo di macchinari per la pr |
| 7.1.8.1.0 | Conduttori di mulini e impastatrici | 7 | 4 | Questa professione riguarda la conduzione di macchinari industriali fissi per ma |
| 7.2.1.2.0 | Conduttori di macchinari per la produzio | 7 | 4 | Questa professione riguarda la conduzione e la sorveglianza di macchinari per la |
| 7.2.4.1.0 | Addetti a macchinari per la produzione i | 7 | 4 | Questa professione riguarda la conduzione e il monitoraggio di macchinari per la |
| 7.2.6.5.0 | Addetti a macchinari per la stampa dei t | 7 | 4 | Questa professione riguarda la conduzione di macchinari automatici per la stampa |
| 7.2.6.6.2 | Addetti a macchinari per la produzione i | 7 | 4 | Questa professione riguarda la conduzione di macchinari per la produzione in ser |
| 7.2.6.7.0 | Addetti a macchinari per la produzione i | 7 | 4 | Questa professione comporta la conduzione di macchinari automatici per la produz |
| 7.2.6.9.0 | Altri operai addetti a macchinari dell'i | 7 | 4 | Questa professione riguarda la conduzione e il monitoraggio di macchinari automa |
| 7.3.2.1.0 | Conduttori di macchinari per la lavorazi | 7 | 4 | Questo ruolo comporta la conduzione di macchinari per la lavorazione e conservaz |
| 7.3.2.3.3 | Conduttori di macchinari industriali per | 7 | 4 | Questa professione comporta la conduzione di macchinari industriali per la produ |
| 7.3.2.4.1 | Conduttori di macchinari per la cernita  | 7 | 4 | Questo ruolo comporta l'operazione di macchinari industriali per la cernita e la |
| 7.3.2.5.0 | Conduttori di macchinari per la produzio | 7 | 4 | Questa professione riguarda la conduzione di macchinari industriali nella produz |
| 7.3.2.8.1 | Addetti a macchinari industriali per la  | 7 | 4 | Questa professione comporta la conduzione di macchinari industriali per la produ |
| 7.3.2.8.2 | Addetti a macchinari industriali per la  | 7 | 4 | Questa professione riguarda la conduzione di macchinari industriali per la produ |
| 7.3.2.8.3 | Addetti a macchinari industriali per la  | 7 | 4 | Questa professione comporta la conduzione di macchinari industriali per la disti |
| 7.4.1.1.0 | Conduttori di convogli ferroviari | 7 | 4 | I macchinisti ferroviari operano macchinari complessi che richiedono presenza fi |
| 7.4.1.2.0 | Operatori di verifica, circolazione e fo | 7 | 4 | Questa professione combina operazioni fisiche (accoppiamento/disaccoppiamento ca |
| 8.1.3.3.0 | Addetti alle consegne di merci | 8 | 4 | Gli addetti alle consegne svolgono compiti principalmente fisici—ritiro, traspor |
| 9.2.1.1.0 | Sergenti, sovraintendenti e marescialli  | 9 | 4 | I sottufficiali delle forze armate (sergenti, marescialli, sovraintendenti) svol |
| 2.5.5.1.1 | Pittori e scultori | 2 | 3 | Pittori e scultori dipendono fondamentalmente dalla creazione fisica—coordinamen |
| 2.5.5.4.2 | Direttori d'orchestra e coro | 2 | 3 | I direttori d'orchestra e coro svolgono un lavoro radicato nell'interazione uman |
| 2.5.5.5.1 | Artisti delle forme di cultura popolare | 2 | 3 | Questa professione comporta performance artistiche dal vivo e intrattenimento di |
| 2.5.5.5.2 | Artisti di varietà | 2 | 3 | Gli artisti di varietà eseguono spettacoli dal vivo che richiedono presenza fisi |
| 3.2.1.2.1 | Podologi | 3 | 3 | I podologi svolgono lavoro clinico manuale che richiede l'esame fisico diretto e |
| 3.2.1.7.0 | Tecnici della medicina popolare | 3 | 3 | Questi professionisti forniscono servizi terapeutici e di benessere principalmen |
| 3.4.2.2.2 | Maestri di arti e mestieri | 3 | 3 | Si tratta principalmente di ruoli di insegnamento artigianale e di mestieri che  |
| 3.4.2.6.2 | Arbitri e giudici di gara | 3 | 3 | Gli arbitri e i giudici di gara svolgono compiti fondamentalmente legati alla pr |
| 3.4.3.3.0 | Intrattenitori | 3 | 3 | I professionisti dell'intrattenimento dipendono fondamentalmente dall'esibizione |
| 3.4.5.5.0 | Tecnici delle attività religiose e di cu | 3 | 3 | Questa professione comporta principalmente attività interpersonali, spirituali e |
| 3.4.6.3.2 | Tecnici dei servizi di sicurezza dei vig | 3 | 3 | Questo ruolo comporta l'organizzazione e il coordinamento delle attività di prev |
| 5.1.2.6.0 | Addetti ai distributori di carburanti ed | 5 | 3 | Questa professione è principalmente fisica e interpersonale: assistenza ai clien |
| 5.1.3.3.0 | Vetrinisti e professioni assimilate | 5 | 3 | I vetrinisti e visual merchandiser svolgono principalmente lavoro fisico e creat |
| 5.2.2.2.1 | Addetti alla preparazione e alla cottura | 5 | 3 | Questa professione comporta principalmente lavoro manuale e pratico: preparazion |
| 5.2.2.2.2 | Addetti alla preparazione, alla cottura  | 5 | 3 | Questa professione comporta principalmente attività fisiche—preparazione di cibi |
| 5.2.2.2.3 | Addetti al banco nei servizi di ristoraz | 5 | 3 | Questa professione è radicata nel lavoro di servizio fisico e in tempo reale: se |
| 5.2.2.3.1 | Camerieri di albergo | 5 | 3 | I camerieri d'albergo svolgono principalmente lavoro fisico e manuale: pulizia c |
| 5.2.2.3.2 | Camerieri di ristorante | 5 | 3 | I camerieri di ristorante svolgono principalmente compiti interpersonali e fisic |
| 5.2.2.4.0 | Baristi e professioni assimilate | 5 | 3 | I baristi e professioni assimilate sono radicati nel lavoro di servizio fisico e |
| 5.2.2.5.2 | Esercenti di attività di ristorazione ne | 5 | 3 | Questa professione riguarda piccole attività di ristorazione nei mercati e in po |
| 5.2.3.1.1 | Assistenti di volo | 5 | 3 | Gli assistenti di volo svolgono principalmente lavoro interpersonale e fisico in |
| 5.3.1.1.0 | Professioni qualificate nei servizi sani | 5 | 3 | Questa categoria comprende ruoli di supporto sanitario e assistenza sociale radi |
| 5.4.1.2.2 | Croupiers | 5 | 3 | I croupier svolgono lavoro intrinsecamente fisico e in tempo reale, richiedendo  |
| 5.4.1.3.0 | Astrologi, preveggenti, chiromanti e pro | 5 | 3 | Questa professione si basa fondamentalmente sull'interazione faccia a faccia, su |
| 5.5.1.3.0 | Massaggiatori ed operatori termali | 5 | 3 | Questa professione è principalmente lavoro manuale e fisico che richiede contatt |
| 5.5.3.1.0 | Addestratori di animali | 5 | 3 | L'addestramento di animali è una professione essenzialmente pratica e fisica che |
| 5.5.3.2.0 | Custodi e allevatori di animali domestic | 5 | 3 | Questa professione comporta principalmente lavoro manuale e fisico: cura degli a |
| 5.5.5.2.0 | Addetti alle agenzie di pompe funebri | 5 | 3 | Questa professione comporta principalmente lavoro fisico e manuale in ambienti i |
| 5.6.1.1.0 | Personale di guardiania territoriale | 5 | 3 | Questa professione comporta sorveglianza territoriale, controllo normativo e pre |
| 5.6.1.2.0 | Vigili urbani | 5 | 3 | I vigili urbani svolgono principalmente lavoro fisico e interpersonale: pattugli |
| 5.6.1.3.1 | Agenti della Polizia di Stato | 5 | 3 | Gli agenti di polizia svolgono lavoro intrinsecamente fisico e in tempo reale, r |
| 5.6.1.3.3 | Agenti del Corpo Forestale | 5 | 3 | Gli agenti del Corpo Forestale svolgono principalmente attività sul campo che ri |
| 5.6.1.5.0 | Agenti di istituti di pena e rieducazion | 5 | 3 | Gli agenti di custodia carceraria svolgono principalmente sorveglianza fisica, c |
| 5.6.1.6.0 | Guardie private di sicurezza | 5 | 3 | Le guardie private svolgono principalmente lavoro di sorveglianza e vigilanza ba |
| 6.2.1.8.2 | Stampatori e piegatori di lamiere | 6 | 3 | Gli stampatori e piegatori di lamiere svolgono principalmente lavoro fisico e ma |
| 6.2.2.2.0 | Costruttori di utensili, modellatori e t | 6 | 3 | Questa professione comporta lavoro manuale e semi-manuale specializzato—tracciat |
| 6.2.3.1.1 | Meccanici motoristi e riparatori di veic | 6 | 3 | I meccanici motoristi svolgono principalmente lavoro manuale e fisico che richie |
| 6.2.3.2.0 | Meccanici, riparatori e manutentori di a | 6 | 3 | I meccanici aeronautici svolgono lavoro specializzato prevalentemente manuale, r |
| 6.2.3.3.1 | Riparatori e manutentori di macchinari e | 6 | 3 | Questa professione comporta lavoro manuale di riparazione e manutenzione di macc |
| 6.2.3.3.2 | Installatori e montatori di macchinari e | 6 | 3 | Questa professione comporta principalmente lavoro manuale e di assemblaggio in a |
| 6.2.3.5.1 | Riparatori e manutentori di apparecchi e | 6 | 3 | Questa professione riguarda la riparazione e la manutenzione di impianti termoid |
| 6.2.3.5.2 | Installatori e montatori di apparecchi e | 6 | 3 | Questa professione comporta principalmente lavoro manuale e pratico: installazio |
| 6.2.3.7.0 | Verniciatori artigianali ed industriali | 6 | 3 | I verniciatori artigianali e industriali svolgono lavoro prevalentemente manuale |
| 6.2.3.8.2 | Meccanici e motoristi navali | 6 | 3 | I meccanici e motoristi navali svolgono lavori di manutenzione e riparazione dei |
| 6.2.4.1.1 | Installatori e riparatori di impianti el | 6 | 3 | Questa professione è principalmente lavoro manuale e pratico che richiede presen |
| 6.2.4.1.2 | Riparatori di apparecchi elettrici e di  | 6 | 3 | Questa professione comporta riparazione e manutenzione manuale di elettrodomesti |
| 6.2.4.1.3 | Elettromeccanici | 6 | 3 | Gli elettromeccanici svolgono principalmente lavoro manuale specializzato, costr |
| 6.2.4.1.4 | Installatori e riparatori di apparati di | 6 | 3 | Questa professione comporta lavoro manuale, installazione, riparazione e manuten |
| 6.2.4.1.5 | Elettrauto | 6 | 3 | Il lavoro dell'elettrauto è principalmente manuale e fisico, richiedendo manipol |
| 6.2.4.3.0 | Riparatori di apparecchi radio televisiv | 6 | 3 | I riparatori di apparecchi radio-televisivi svolgono principalmente lavoro manua |
| 6.3.1.4.0 | Addetti alla costruzione e riparazione d | 6 | 3 | La costruzione e riparazione di orologi è un mestiere artigianale che richiede d |
| 6.3.1.6.1 | Orafi | 6 | 3 | Gli orafi e gli artigiani gioiellieri svolgono lavori artigianali altamente spec |
| 6.3.2.2.2 | Tagliatori, molatori e levigatori del ve | 6 | 3 | I tagliatori, molatori e levigatori del vetro svolgono principalmente lavoro man |
| 6.3.2.4.0 | Pittori e decoratori su vetro e ceramica | 6 | 3 | Questa professione comprende lavoro manuale e artistico altamente specializzato  |
| 6.3.4.4.2 | Litografi, serigrafisti e incisori tipog | 6 | 3 | Questa professione comporta tecniche specializzate manuali e chimiche per la cre |
| 6.4.1.1.0 | Agricoltori e operai agricoli specializz | 6 | 3 | Questa professione comporta principalmente lavoro fisico e manuale in ambienti e |
| 6.4.1.2.0 | Agricoltori e operai agricoli specializz | 6 | 3 | Questa professione comprende principalmente lavoro agricolo manuale e fisico—pot |
| 6.4.1.3.2 | Agricoltori e operai agricoli specializz | 6 | 3 | Questa professione riguarda il lavoro agricolo specializzato in ambienti control |
| 6.4.1.4.0 | Agricoltori e operai agricoli specializz | 6 | 3 | Gli agricoltori e operai agricoli specializzati in colture miste svolgono princi |
| 6.4.2.3.0 | Allevatori e operai specializzati degli  | 6 | 3 | L'allevamento di suini è un'attività fondamentalmente fisica che richiede presen |
| 6.4.2.6.0 | Allevatori e operai specializzati degli  | 6 | 3 | Questa professione comporta allevamento manuale, manutenzione degli ambienti e m |
| 6.4.2.9.0 | Altri allevatori e operai specializzati  | 6 | 3 | Questa professione comporta principalmente lavoro fisico e manuale: allevamento, |
| 6.4.3.1.0 | Allevatori e agricoltori | 6 | 3 | Gli allevatori e agricoltori svolgono lavoro prevalentemente manuale e fisico in |
| 6.4.5.1.0 | Acquacoltori | 6 | 3 | Gli acquacoltori svolgono principalmente lavori fisici e pratici: monitoraggio d |
| 6.5.1.1.4 | Addetti alla conservazione di carni e pe | 6 | 3 | Questa professione comporta principalmente lavoro manuale e fisico in ambienti d |
| 6.5.1.3.1 | Pasticcieri e cioccolatai | 6 | 3 | I pasticcieri e cioccolatai svolgono principalmente lavoro manuale e artigianale |
| 6.5.1.3.3 | Conservieri | 6 | 3 | I conservieri svolgono principalmente lavoro manuale e artigianale, gelatinizzan |
| 6.5.1.6.0 | Operai specializzati della preparazione  | 6 | 3 | Questa professione comporta principalmente lavoro manuale e fisico—selezione, es |
| 6.5.2.1.1 | Stagionatori ed operai specializzati del | 6 | 3 | Questa professione comporta principalmente lavoro manuale e fisico: taglio e lav |
| 6.5.3.1.0 | Preparatori di fibre | 6 | 3 | La preparazione delle fibre è un processo manifatturiero fondamentalmente fisico |
| 6.5.3.2.1 | Tessitori | 6 | 3 | La tessitura è fondamentalmente un'occupazione artigianale che richiede destrezz |
| 6.5.3.3.2 | Tagliatori di capi di abbigliamento | 6 | 3 | I tagliatori di capi di abbigliamento svolgono un lavoro prevalentemente manuale |
| 6.5.3.4.1 | Modellisti di pellicceria e di capi in p | 6 | 3 | La professione comporta la creazione di cartamodelli per capi in pelle e pellicc |
| 6.5.3.4.4 | Pellicciai e sarti in pelle | 6 | 3 | La professione richiede progettazione, taglio e confezione di capi in pelle o pe |
| 6.5.3.5.1 | Confezionatori e rifinitori di biancheri | 6 | 3 | Questa professione comporta principalmente lavoro manuale e artigianale—taglio,  |
| 6.5.3.5.2 | Confezionatori e rifinitori di biancheri | 6 | 3 | Questa professione comprende la produzione artigianale di biancheria per la casa |
| 6.5.3.6.1 | Confezionatori di tende e drappeggi | 6 | 3 | Questa professione comporta principalmente lavoro manuale e fisico: taglio, cuci |
| 6.5.3.7.0 | Artigiani e addetti alle tintolavanderie | 6 | 3 | Questa professione comporta principalmente lavoro fisico e manuale nelle lavande |
| 6.5.4.1.0 | Conciatori di pelli e di pellicce | 6 | 3 | La concia di pelli e pellicce è un mestiere artigianale fondamentalmente manuale |
| 6.5.4.2.1 | Modellisti di calzature | 6 | 3 | I modellisti di calzature svolgono un lavoro artigianale altamente specializzato |
| 6.5.4.2.2 | Tagliatori di calzature | 6 | 3 | I tagliatori di calzature svolgono lavoro manuale specializzato che richiede abi |
| 6.5.4.3.1 | Modellisti di pelletteria | 6 | 3 | I modellisti di pelletteria svolgono un lavoro artigianale altamente specializza |
| 6.5.4.3.2 | Tagliatori di pelletteria | 6 | 3 | I tagliatori di pelletteria svolgono lavoro principalmente manuale e artigianale |
| 6.5.5.1.0 | Macchinisti ed attrezzisti di scena | 6 | 3 | I macchinisti e attrezzisti di scena svolgono principalmente lavoro fisico e man |
| 7.1.1.1.0 | Conduttori di macchinari in miniere e ca | 7 | 3 | Questa professione comporta l'operazione di macchinari pesanti in miniere e cave |
| 7.1.1.2.0 | Conduttori di impianti per il primo trat | 7 | 3 | Questa professione riguarda la conduzione di macchinari fissi per il trattamento |
| 7.1.1.3.1 | Trivellatori di pozzi | 7 | 3 | I trivellatori di pozzi svolgono lavoro fisico altamente specializzato in ambien |
| 7.1.1.3.2 | Conduttori di sonde e perforatrici da pr | 7 | 3 | Questa professione comporta l'operazione di attrezzature specializzate di perfor |
| 7.1.2.1.1 | Operatori di altoforno | 7 | 3 | Gli operatori di altoforno svolgono lavoro prevalentemente fisico e meccanico in |
| 7.1.2.2.2 | Operatori di laminatoi | 7 | 3 | Gli operatori di laminatoi svolgono principalmente lavoro fisico e di sorveglian |
| 7.1.2.4.1 | Conduttori di macchine per la trafila di | 7 | 3 | Questa professione riguarda la conduzione di macchine per la trafilatura dei met |
| 7.1.2.4.2 | Conduttori di macchine per l'estrusione  | 7 | 3 | Questa professione comporta l'operazione di macchinari specializzati per l'estru |
| 7.1.2.5.1 | Operatori di impianti termici per la pro | 7 | 3 | Questa professione riguarda la conduzione di impianti termici e macchinari per l |
| 7.1.2.5.2 | Operatori di impianti elettrochimici per | 7 | 3 | Questo ruolo riguarda la conduzione di impianti elettrochimici per la produzione |
| 7.1.3.1.0 | Conduttori di impianti per dosare, misce | 7 | 3 | Questa professione riguarda la conduzione di impianti fissi per miscelare, dosar |
| 7.1.3.2.1 | Conduttori di forni per la produzione de | 7 | 3 | I conduttori di forni per la produzione del vetro svolgono principalmente lavoro |
| 7.1.3.3.1 | Conduttori di impianti per la formatura  | 7 | 3 | Questa professione riguarda la conduzione di impianti e macchinari per la produz |
| 7.1.3.3.2 | Conduttori di forni per la produzione di | 7 | 3 | Questa professione riguarda la conduzione di forni industriali e attrezzature di |
| 7.1.3.4.1 | Conduttori di impianti per la formatura  | 7 | 3 | Questa professione riguarda la conduzione di impianti fissi per la produzione di |
| 7.1.3.4.2 | Conduttori di forni per la produzione di | 7 | 3 | Questa professione riguarda la conduzione di forni e macchinari per la produzion |
| 7.1.6.2.1 | Operatori di impianti di recupero e rici | 7 | 3 | Questa professione comporta la conduzione e il monitoraggio di macchinari e impi |
| 7.1.6.2.2 | Operatori di impianti per la depurazione | 7 | 3 | Questo ruolo comporta la gestione e il controllo di impianti di trattamento e di |
| 7.2.1.3.0 | Conduttori di macchinari per la produzio | 7 | 3 | Questa professione riguarda la conduzione e la sorveglianza di macchinari per la |
| 7.2.2.1.0 | Finitori di metalli e conduttori di impi | 7 | 3 | Questa professione riguarda la conduzione di impianti industriali per la finitur |
| 7.2.5.3.0 | Conduttori di macchinari per rilegatura  | 7 | 3 | Questa professione riguarda la conduzione di macchinari industriali per la rileg |
| 7.2.6.6.1 | Addetti a macchinari industriali per la  | 7 | 3 | Questo ruolo riguarda la conduzione di macchinari automatici per la lavorazione  |
| 7.2.7.1.0 | Assemblatori in serie di parti di macchi | 7 | 3 | Gli assemblatori svolgono principalmente lavori manuali e fisici utilizzando att |
| 7.2.7.2.0 | Assemblatori e cablatori di apparecchiat | 7 | 3 | Questa professione comporta il montaggio manuale e il cablaggio di componenti el |
| 7.2.7.4.0 | Assemblatori in serie di articoli in met | 7 | 3 | Gli assemblatori svolgono principalmente compiti manuali e fisici che richiedono |
| 7.2.7.5.0 | Assemblatori in serie di articoli in leg | 7 | 3 | Questa professione comporta lavoro manuale di assemblaggio su linee di produzion |
| 7.2.7.6.0 | Assemblatori in serie di articoli in car | 7 | 3 | Questa professione comporta lavoro di assemblaggio su linee semiautomatiche con  |
| 7.2.7.9.0 | Assemblatori in serie di articoli indust | 7 | 3 | Questa professione comporta lavoro di assemblaggio su linee semiautomatiche con  |
| 7.3.1.1.0 | Addetti agli impianti fissi in agricoltu | 7 | 3 | Questa professione riguarda la conduzione di impianti e macchinari fissi per il  |
| 7.3.1.3.0 | Addetti alla refrigerazione, trattamento | 7 | 3 | Questa professione riguarda la conduzione di impianti industriali per il trattam |
| 7.3.2.2.0 | Conduttori di apparecchi per la lavorazi | 7 | 3 | Questo ruolo riguarda la conduzione di macchinari fissi per la lavorazione indus |
| 7.3.2.3.1 | Conduttori di macchinari industriali per | 7 | 3 | Questa professione riguarda la conduzione di macchinari industriali per la lavor |
| 7.3.2.3.2 | Conduttori di macchinari industriali per | 7 | 3 | Questa professione riguarda la conduzione di macchinari industriali per la lavor |
| 7.3.2.4.2 | Conduttori di macchinari per la conserva | 7 | 3 | Questa professione riguarda la conduzione di macchinari industriali per la lavor |
| 7.3.2.4.3 | Conduttori di macchinari per la conserva | 7 | 3 | Questa professione riguarda la conduzione di macchinari industriali per il tratt |
| 7.3.2.4.4 | Conduttori di macchinari per la produzio | 7 | 3 | Questa professione riguarda la conduzione di macchinari industriali per la produ |
| 7.3.2.6.1 | Conduttori di macchinari per la preparaz | 7 | 3 | Questo ruolo comporta la conduzione di macchinari industriali per la lavorazione |
| 7.3.2.6.2 | Conduttori di macchinari per la preparaz | 7 | 3 | Questa professione riguarda la conduzione di macchinari industriali per la produ |
| 7.3.2.8.4 | Addetti a macchinari industriali per la  | 7 | 3 | Questo ruolo comporta la conduzione di macchinari industriali per la produzione  |
| 7.4.1.3.0 | Manovratori di impianti a fune | 7 | 3 | La professione riguarda il controllo e l'azionamento di impianti a fune (funivie |
| 7.4.2.2.0 | Conduttori di autobus, di tram e di filo | 7 | 3 | I conducenti di autobus, tram e filobus svolgono lavoro principalmente fisico ch |
| 7.4.2.3.0 | Conduttori di mezzi pesanti e camion | 7 | 3 | I conducenti di mezzi pesanti svolgono principalmente compiti fisici che richied |
| 7.4.3.1.0 | Conduttori di trattori agricoli | 7 | 3 | La guida di trattori e macchinari agricoli è un lavoro fondamentalmente manuale  |
| 7.4.4.1.0 | Conduttori di macchinari per il moviment | 7 | 3 | Questa professione comporta l'operazione di macchinari pesanti per il movimento  |
| 7.4.4.2.1 | Conduttori di macchinari mobili per la p | 7 | 3 | Questa professione comporta l'utilizzo di macchinari pesanti per perforazione in |
| 7.4.4.2.2 | Conduttori di macchinari mobili per la p | 7 | 3 | Questa professione comporta l'operazione di macchinari pesanti per la perforazio |
| 7.4.4.3.0 | Conduttori di gru e di apparecchi di sol | 7 | 3 | I conduttori di gru svolgono lavoro prevalentemente fisico e operativo in tempo  |
| 7.4.5.2.0 | Conduttori di caldaie ed altre attrezzat | 7 | 3 | Questa professione riguarda la conduzione e la manutenzione di caldaie, turbine  |
| 8.1.2.1.0 | Uscieri e professioni assimilate | 8 | 3 | Gli uscieri e professioni assimilate sono ruoli principalmente fisici e interper |
| 8.1.5.1.0 | Bidelli e professioni assimilate | 8 | 3 | I bidelli svolgono principalmente compiti fisici e interpersonali: pulizia, manu |
| 8.1.6.1.2 | Personale non qualificato addetto ai ser | 8 | 3 | Questo ruolo richiede la presenza fisica presso gli impianti, il monitoraggio in |
| 8.1.6.1.3 | Personale non qualificato addetto ai ser | 8 | 3 | Questo ruolo richiede presenza fisica, monitoraggio in tempo reale e consapevole |
| 8.2.1.1.0 | Personale non qualificato nei servizi ri | 8 | 3 | Questa professione richiede principalmente presenza fisica, interazione con i cl |
| 8.4.3.1.0 | Personale non qualificato delle attività | 8 | 3 | Questa professione comprende principalmente compiti manuali e fisici in ambienti |
| 9.1.1.1.0 | Ufficiali delle forze armate | 9 | 3 | Le responsabilità fondamentali degli ufficiali militari—decisioni strategiche, a |
| 9.3.1.1.0 | Truppa delle forze armate | 9 | 3 | Il personale delle forze armate svolge compiti principalmente fisici, operativi  |
| 2.5.5.3.2 | Ballerini | 2 | 2 | I ballerini eseguono lavoro corporeo dal vivo che richiede presenza fisica, inte |
| 2.5.5.4.3 | Strumentisti | 2 | 2 | Gli strumentisti eseguono musica dal vivo richiedendo abilità fisica in tempo re |
| 3.4.1.5.1 | Guide ed accompagnatori naturalistici e  | 3 | 2 | Questa professione è radicata nella presenza fisica, nell'interazione umana in t |
| 3.4.2.7.0 | Atleti | 3 | 2 | Il lavoro principale degli atleti è la prestazione fisica in competizioni sporti |
| 5.5.1.1.0 | Acconciatori | 5 | 2 | L'acconciatura è un servizio principalmente manuale che richiede presenza fisica |
| 5.5.1.2.0 | Estetisti e truccatori | 5 | 2 | Gli estetisti e i truccatori svolgono lavoro prevalentemente manuale e fisico ch |
| 5.5.2.1.0 | Personale di compagnia e personale quali | 5 | 2 | Questa professione comporta principalmente lavoro interpersonale e di presenza f |
| 5.5.2.2.0 | Addetti alla sorveglianza di bambini e p | 5 | 2 | Questa professione richiede sorveglianza diretta e assistenza ai bambini in ambi |
| 5.5.2.3.0 | Addetti all'assistenza personale | 5 | 2 | Gli addetti all'assistenza personale svolgono principalmente lavoro manuale e fi |
| 5.6.1.4.1 | Vigili del fuoco | 5 | 2 | I vigili del fuoco svolgono un lavoro fondamentalmente fisico e di risposta alle |
| 5.6.1.4.2 | Personale delle squadre antincendio | 5 | 2 | Il lavoro di prevenzione e lotta agli incendi è intrinsecamente fisico, in tempo |
| 5.6.1.7.0 | Bagnini e professioni assimilate | 5 | 2 | I bagnini e le professioni assimilate sono radicati nella presenza fisica, nel g |
| 6.1.1.1.0 | Brillatori e artificieri in cave e minie | 6 | 2 | Questa professione comporta lavoro altamente specializzato e manuale in ambienti |
| 6.1.1.2.0 | Tagliatori e levigatori di pietre, scalp | 6 | 2 | Questa professione comporta principalmente lavoro manuale specializzato, giudizi |
| 6.1.2.2.1 | Casseronisti/Cassonisti | 6 | 2 | I casseronisti svolgono principalmente lavori di assemblaggio e disassemblaggio  |
| 6.1.2.5.1 | Armatori di gallerie e pozzi | 6 | 2 | Questa professione riguarda la costruzione e il rinforzo fisico di strutture sot |
| 6.1.2.5.2 | Armatori di ferrovie | 6 | 2 | Gli armatori di ferrovie svolgono lavoro prevalentemente fisico e manuale in amb |
| 6.1.3.2.4 | Parchettisti e posatori di pavimenti e r | 6 | 2 | Questa professione comporta lavoro manuale e fisico altamente specializzato: pos |
| 6.1.3.4.0 | Installatori di impianti di isolamento e | 6 | 2 | Questa professione comporta l'installazione manuale di materiali isolanti e fono |
| 6.1.3.5.0 | Vetrai | 6 | 2 | L'installazione e il taglio del vetro è un mestiere artigianale fondamentalmente |
| 6.1.3.6.1 | Idraulici nelle costruzioni civili | 6 | 2 | Gli idraulici nelle costruzioni civili svolgono lavoro prevalentemente manuale e |
| 6.1.3.6.2 | Installatori di impianti termici nelle c | 6 | 2 | Questa professione comporta principalmente lavoro manuale e fisico di installazi |
| 6.1.3.7.0 | Elettricisti ed installatori di impianti | 6 | 2 | Gli elettricisti negli impianti civili svolgono lavoro prevalentemente manuale e |
| 6.1.3.8.0 | Installatori di infissi e serramenti | 6 | 2 | Questa professione comporta principalmente lavoro fisico e manuale per l'install |
| 6.1.4.1.2 | Decoratori e stuccatori edili | 6 | 2 | Questa professione comporta lavoro manuale altamente specializzato e artigianale |
| 6.1.5.1.0 | Operai addetti ai servizi di igiene e pu | 6 | 2 | Questa professione comporta principalmente lavoro manuale e fisico in ambienti i |
| 6.1.5.2.0 | Operai addetti alla manutenzione degli i | 6 | 2 | Questa professione comporta lavoro manuale e pratico in ambienti imprevedibili e |
| 6.2.1.1.1 | Fonditori | 6 | 2 | Il lavoro di fonditore è intrinsecamente manuale e fisico, richiedendo la manipo |
| 6.2.1.1.2 | Formatori e animisti | 6 | 2 | Questa professione riguarda la lavorazione specializzata dei metalli e le operaz |
| 6.2.1.2.0 | Saldatori e tagliatori a fiamma | 6 | 2 | I saldatori e tagliatori a fiamma svolgono lavoro manuale altamente specializzat |
| 6.2.1.3.1 | Lattonieri e calderai | 6 | 2 | I lattonieri e calderai svolgono lavori artigianali specializzati che richiedono |
| 6.2.1.3.2 | Tracciatori | 6 | 2 | I tracciatori svolgono lavoro manuale e fisico altamente specializzato—marcatura |
| 6.2.1.4.0 | Carpentieri e montatori di carpenteria m | 6 | 2 | La carpenteria metallica e il montaggio sono lavori prevalentemente manuali che  |
| 6.2.1.5.0 | Attrezzatori e montatori di cavi metalli | 6 | 2 | Questa professione comporta l'installazione fisica e il montaggio di cavi metall |
| 6.2.1.7.0 | Saldatori elettrici e a norme ASME | 6 | 2 | I saldatori elettrici svolgono un lavoro altamente specializzato, manuale e fisi |
| 6.2.1.8.1 | Carrozzieri | 6 | 2 | I carrozzieri svolgono lavoro manuale altamente specializzato che richiede compe |
| 6.2.2.1.1 | Fabbri | 6 | 2 | I fabbri e gli artigiani metallici svolgono lavoro manuale altamente specializza |
| 6.2.2.1.2 | Fucinatori e forgiatori | 6 | 2 | I fucinatori e forgiatori sono artigiani specializzati che trasformano i metalli |
| 6.2.2.3.2 | Aggiustatori meccanici | 6 | 2 | Gli aggiustatori meccanici svolgono lavoro manuale specializzato che richiede pr |
| 6.2.3.1.2 | Gommisti | 6 | 2 | I gommisti svolgono lavoro prevalentemente manuale e fisico che richiede destrez |
| 6.2.3.1.3 | Meccanici di biciclette e veicoli assimi | 6 | 2 | I meccanici di biciclette svolgono lavoro manuale altamente specializzato che ri |
| 6.2.3.4.1 | Frigoristi industriali | 6 | 2 | I frigoristi industriali svolgono lavoro altamente specializzato e manuale, rich |
| 6.2.3.4.2 | Frigoristi navali | 6 | 2 | I frigoristi navali svolgono lavoro altamente specializzato e manuale, richieden |
| 6.2.3.8.1 | Attrezzisti navali | 6 | 2 | Gli attrezzisti navali svolgono lavori di manutenzione e riparazione meccanica a |
| 6.2.4.5.0 | Installatori, manutentori e riparatori d | 6 | 2 | Questa professione comporta principalmente lavoro manuale e pratico di installaz |
| 6.3.1.3.1 | Accordatori di strumenti musicali | 6 | 2 | L'accordatura di strumenti musicali è un mestiere artigianale che richiede compe |
| 6.3.1.3.2 | Addetti alla costruzione e riparazione d | 6 | 2 | Questa professione richiede un lavoro artigianale altamente specializzato che di |
| 6.3.1.6.2 | Addetti alla lavorazione di pietre prezi | 6 | 2 | Questa professione richiede artigianato manuale altamente specializzato con cont |
| 6.3.1.6.3 | Addetti alla lavorazione di bigiotteria | 6 | 2 | Questa professione comporta la lavorazione artigianale di bigiotteria, richieden |
| 6.3.2.1.1 | Vasai e terracottai | 6 | 2 | Questa professione artigianale richiede lavoro manuale altamente specializzato—m |
| 6.3.2.1.2 | Ceramisti | 6 | 2 | I ceramisti svolgono lavoro artigianale altamente specializzato che richiede abi |
| 6.3.2.2.1 | Soffiatori e modellatori del vetro | 6 | 2 | La soffiatura e modellazione del vetro è un'attività artigianale che richiede ma |
| 6.3.2.3.0 | Incisori ed acquafortisti su vetro | 6 | 2 | Questa professione richiede artigianato manuale specializzato con abilità fisica |
| 6.3.3.1.1 | Cartapestai | 6 | 2 | I cartapestai svolgono un lavoro artigianale altamente specializzato che richied |
| 6.3.3.1.2 | Incisori e intarsiatori su legno | 6 | 2 | Questa professione comporta un artigianato altamente specializzato che richiede  |
| 6.3.3.2.1 | Artigiani di prodotti tessili artistici  | 6 | 2 | Questa professione comporta un lavoro artigianale manuale che richiede destrezza |
| 6.3.3.2.2 | Artigiani di prodotti artistici in pelle | 6 | 2 | Questa professione comporta lavoro artigianale manuale di cuoio e pelle, che ric |
| 6.3.4.3.0 | Zincografi, stereotipisti ed elettrotipi | 6 | 2 | Questa professione comporta processi manuali e chimici specializzati per la crea |
| 6.3.4.4.1 | Artigiani acquafortisti | 6 | 2 | Gli acquafortisti svolgono un lavoro manuale altamente specializzato che richied |
| 6.4.1.3.1 | Agricoltori e operai agricoli specializz | 6 | 2 | Questa professione è radicata nel lavoro manuale e fisico in ambienti naturali i |
| 6.4.2.1.0 | Allevatori e operai specializzati degli  | 6 | 2 | Questa professione comporta principalmente lavoro fisico e manuale in ambienti a |
| 6.4.2.2.0 | Allevatori e operai specializzati degli  | 6 | 2 | L'allevamento di ovini e caprini è un'attività intrinsecamente manuale che richi |
| 6.4.2.4.0 | Allevatori e operai specializzati degli  | 6 | 2 | L'allevamento avicolo è un'attività essenzialmente manuale e fisica che richiede |
| 6.4.2.5.0 | Allevatore di bestiame misto | 6 | 2 | L'allevamento di bestiame misto è un'occupazione fondamentalmente fisica e prati |
| 6.5.1.1.1 | Macellai e abbattitori di animali | 6 | 2 | I macellai e gli abbattitori di animali svolgono un lavoro altamente specializza |
| 6.5.1.1.2 | Norcini | 6 | 2 | I norcini svolgono lavoro manuale e fisico altamente specializzato—trinciatura,  |
| 6.5.1.1.3 | Pesciaioli | 6 | 2 | I pesciaioli svolgono principalmente attività manuali e fisiche (pulizia, filett |
| 6.5.1.2.1 | Panettieri | 6 | 2 | I panettieri svolgono un lavoro altamente manuale e artigianale che richiede giu |
| 6.5.1.2.2 | Pastai | 6 | 2 | I pastai svolgono un lavoro altamente specializzato e manuale—impastare farine,  |
| 6.5.1.3.2 | Gelatai | 6 | 2 | I gelatai svolgono principalmente lavoro manuale e fisico che richiede giudizio  |
| 6.5.1.5.0 | Artigiani ed operai specializzati delle  | 6 | 2 | Questa professione comporta la trasformazione artigianale del latte—produzione d |
| 6.5.2.1.2 | Curvatori, sagomatori ed operai speciali | 6 | 2 | Questa professione comporta lavoro manuale specializzato—curvatura, sagomatura e |
| 6.5.2.2.1 | Attrezzisti di falegnameria | 6 | 2 | Gli attrezzisti di falegnameria svolgono lavoro artigianale altamente specializz |
| 6.5.2.2.2 | Falegnami | 6 | 2 | I falegnami svolgono lavoro artigianale altamente specializzato che richiede com |
| 6.5.2.2.3 | Montatori di mobili | 6 | 2 | I montatori di mobili svolgono lavoro prevalentemente manuale e pratico, richied |
| 6.5.2.3.2 | Cordai e intrecciatori di fibre | 6 | 2 | Questa professione comporta principalmente lavoro manuale e pratico con material |
| 6.5.2.3.3 | Lavoranti in giunco e canna | 6 | 2 | Questa professione comporta un lavoro manuale e artigianale altamente specializz |
| 6.5.2.3.4 | Lavoranti in sughero e spugna | 6 | 2 | I lavoranti in sughero e spugna svolgono principalmente attività manuali e artig |
| 6.5.3.2.2 | Maglieristi | 6 | 2 | I maglieristi svolgono lavoro manuale altamente specializzato e artigianale—rifi |
| 6.5.3.2.3 | Tintori e addetti al trattamento chimico | 6 | 2 | Questa professione comporta il trattamento chimico e la tintura manuale dei tess |
| 6.5.3.3.3 | Confezionatori di capi di abbigliamento | 6 | 2 | I confezionatori di capi di abbigliamento svolgono lavoro artigianale altamente  |
| 6.5.3.3.4 | Sarti | 6 | 2 | I sarti svolgono un lavoro manuale altamente specializzato che richiede coordina |
| 6.5.3.3.5 | Cappellai | 6 | 2 | I cappellai svolgono un lavoro artigianale altamente specializzato che richiede  |
| 6.5.3.4.2 | Tagliatori di pellicceria e di capi in p | 6 | 2 | Questa professione comporta lavoro manuale specializzato—taglio di capi in pelle |
| 6.5.3.4.3 | Confezionatori di pellicceria e di capi  | 6 | 2 | Questa professione comporta lavoro artigianale manuale in laboratori semi-artigi |
| 6.5.3.5.3 | Merlettai e ricamatrici a mano | 6 | 2 | Le merlettaie e ricamatrici a mano svolgono lavoro artigianale altamente special |
| 6.5.3.5.4 | Bottonai | 6 | 2 | I bottonai svolgono lavoro manuale e artigianale altamente specializzato che coi |
| 6.5.3.6.2 | Modellisti di poltrone e divani | 6 | 2 | Questa professione comporta il trasferimento di disegni su dime e sagome per sch |
| 6.5.3.6.3 | Tagliatori di imbottiture e rivestimenti | 6 | 2 | Questa professione comporta il taglio di imbottiture e rivestimenti per mobili u |
| 6.5.3.6.4 | Confezionatori di poltrone e divani | 6 | 2 | Questa professione comporta lavoro manuale e fisico nella tappezzeria e nell'ass |
| 6.5.3.6.5 | Tappezzieri di poltrone, divani e assimi | 6 | 2 | Si tratta di lavoro artigianale prevalentemente manuale che richiede presenza fi |
| 6.5.3.6.6 | Materassai | 6 | 2 | I materassai svolgono lavoro artigianale altamente specializzato che richiede ab |
| 6.5.4.2.3 | Confezionatori di calzature | 6 | 2 | La confezione e la rifinitura di calzature è un lavoro fondamentalmente manuale  |
| 6.5.4.2.4 | Calzolai, sellai e cuoiai | 6 | 2 | Questa professione comporta principalmente lavoro artigianale manuale—taglio, cu |
| 6.5.4.3.3 | Confezionatori di pelletteria | 6 | 2 | La confezione di pelletteria è un lavoro artigianale che richiede destrezza manu |
| 6.5.4.3.4 | Pellettieri | 6 | 2 | I pellettieri svolgono lavoro manuale altamente specializzato—taglio, cucitura,  |
| 7.1.2.1.2 | Operatori di colata | 7 | 2 | Gli operatori di colata svolgono lavoro altamente fisico e in tempo reale in amb |
| 7.1.2.2.1 | Operatori di forni di seconda fusione | 7 | 2 | Questa professione riguarda la conduzione di forni industriali e il caricamento  |
| 7.3.1.2.0 | Addetti agli impianti per la trasformazi | 7 | 2 | Questa professione riguarda la conduzione di macchinari fisici in un impianto di |
| 7.4.3.2.1 | Conduttori di macchine raccoglitrici, tr | 7 | 2 | Questa professione riguarda la guida di macchinari agricoli in condizioni estern |
| 7.4.3.2.2 | Conduttori di mietitrebbiatrici | 7 | 2 | La guida di mietitrebbiatrici richiede un'operazione manuale qualificata in ambi |
| 7.4.3.2.3 | Conduttori di macchine per la raccolta d | 7 | 2 | Questa professione comporta l'operazione di macchinari agricoli in ambienti este |
| 7.4.3.3.0 | Conduttori di macchine forestali | 7 | 2 | Gli operatori di macchine forestali svolgono lavoro altamente fisico e manuale i |
| 7.4.4.4.0 | Conduttori di carrelli elevatori | 7 | 2 | I carrellisti svolgono principalmente lavoro fisico in tempo reale in ambienti d |
| 7.4.5.1.0 | Marinai di coperta | 7 | 2 | I marinai di coperta svolgono lavoro prevalentemente fisico e manuale in ambient |
| 7.4.5.3.0 | Conduttori di barche e battelli a motore | 7 | 2 | La professione richiede il controllo fisico in tempo reale di imbarcazioni in am |
| 8.1.1.1.0 | Venditori ambulanti di beni | 8 | 2 | Il lavoro dei venditori ambulanti è intrinsecamente fisico e interpersonale, ric |
| 8.1.1.2.0 | Venditori ambulanti di servizi | 8 | 2 | I venditori ambulanti di servizi svolgono lavori prevalentemente manuali e artig |
| 8.1.3.1.0 | Facchini, addetti allo spostamento merci | 8 | 2 | Questa professione comporta principalmente lavoro manuale—carico, scarico e movi |
| 8.1.4.1.0 | Personale non qualificato addetto alla p | 8 | 2 | Questa professione comporta principalmente lavoro manuale e fisico in ambienti i |
| 8.1.4.2.0 | Personale non qualificato nei servizi di | 8 | 2 | Questa professione comporta principalmente compiti manuali e fisici in un ambien |
| 8.1.4.3.0 | Personale non qualificato addetto ai ser | 8 | 2 | Questa professione comporta principalmente lavoro manuale e fisico in ambienti f |
| 8.1.4.5.0 | Operatori ecologici e altri raccoglitori | 8 | 2 | La raccolta e la separazione dei rifiuti è un lavoro prevalentemente manuale e f |
| 8.1.5.2.0 | Portantini e professioni assimilate | 8 | 2 | I portantini e professioni assimilate svolgono principalmente lavoro fisico e ma |
| 8.1.6.1.1 | Personale non qualificato addetto ai ser | 8 | 2 | Questo ruolo è fondamentalmente fisico e interpersonale, richiedendo una presenz |
| 8.2.2.1.0 | Collaboratori domestici e professioni as | 8 | 2 | Il lavoro domestico è intrinsecamente manuale e pratico, richiedendo una presenz |
| 2.5.5.5.3 | Acrobati e artisti circensi | 2 | 1 | Gli acrobati e gli artisti circensi eseguono performance dal vivo che richiedono |
| 6.1.1.3.0 | Coltivatori di saline | 6 | 1 | I coltivatori di saline svolgono lavoro prevalentemente manuale e all'aperto in  |
| 6.1.2.1.0 | Muratori in pietra e mattoni | 6 | 1 | La muratura in pietra e mattoni è un lavoro essenzialmente manuale e fisico che  |
| 6.1.2.2.2 | Muratori e formatori in calcestruzzo | 6 | 1 | Questa professione comporta lavoro manuale e fisico in ambienti di cantiere impr |
| 6.1.2.3.0 | Carpentieri e falegnami edili | 6 | 1 | I carpentieri e falegnami edili svolgono lavoro altamente specializzato e manual |
| 6.1.2.4.0 | Ponteggiatori | 6 | 1 | I ponteggiatori svolgono lavoro fisico altamente specializzato che richiede pres |
| 6.1.2.6.1 | Asfaltisti | 6 | 1 | Gli asfaltisti svolgono lavoro manuale altamente specializzato che richiede pres |
| 6.1.2.6.2 | Lastricatori e pavimentatori stradali | 6 | 1 | I lastricatori e pavimentatori stradali svolgono lavoro quasi interamente manual |
| 6.1.2.7.0 | Montatori di manufatti prefabbricati e d | 6 | 1 | Questa professione comporta l'assemblaggio e l'installazione fisica di component |
| 6.1.3.1.0 | Copritetti e impermeabilizzatori di sola | 6 | 1 | Questa professione comporta lavoro fisico altamente specializzato su tetti e fac |
| 6.1.3.2.1 | Posatori di pavimenti | 6 | 1 | I posatori di pavimenti svolgono lavoro manuale altamente specializzato che rich |
| 6.1.3.2.2 | Rifinitori di pavimenti | 6 | 1 | I rifinitori di pavimenti svolgono lavori manuali altamente specializzati che ri |
| 6.1.3.2.3 | Piastrellisti e rivestimentisti in pietr | 6 | 1 | Questa professione comporta lavoro manuale altamente specializzato che richiede  |
| 6.1.3.3.0 | Intonacatori | 6 | 1 | Gli intonacatori svolgono lavoro manuale altamente specializzato che richiede pr |
| 6.1.4.1.1 | Pittori edili | 6 | 1 | I pittori edili svolgono lavoro manuale altamente specializzato che richiede pre |
| 6.1.4.2.0 | Pulitori di facciate | 6 | 1 | La pulizia di facciate è un'occupazione fondamentalmente fisica che richiede ai  |
| 6.2.1.6.0 | Sommozzatori e lavoratori subacquei | 6 | 1 | I sommozzatori e lavoratori subacquei svolgono lavori fisici altamente specializ |
| 6.4.4.1.1 | Abbattitori di alberi e rimboschitori | 6 | 1 | Questa professione comprende lavoro manuale intensivo e specializzato in ambient |
| 6.4.4.1.2 | Sugherai e raccoglitori di resine | 6 | 1 | I sugherai e raccoglitori di resine svolgono lavoro manuale altamente specializz |
| 6.4.5.2.0 | Pescatori della pesca costiera e in acqu | 6 | 1 | La pesca costiera e in acque interne è un'attività intrinsecamente manuale che r |
| 6.4.5.3.0 | Pescatori d'alto mare | 6 | 1 | La pesca d'alto mare è un'occupazione intrinsecamente fisica che richiede presen |
| 6.4.5.4.0 | Cacciatori | 6 | 1 | La caccia è un'attività intrinsecamente fisica e all'aperto che richiede navigaz |
| 6.5.2.3.1 | Impagliatori e lavoranti in vimini e set | 6 | 1 | Questa professione artigianale richiede abilità manuale specializzata con materi |
| 7.4.2.4.0 | Conduttori di veicoli a trazione animale | 7 | 1 | Questa professione riguarda la guida di veicoli a trazione animale in ambienti f |
| 8.1.4.4.0 | Addetti al lavaggio veicoli | 8 | 1 | Il lavaggio dei veicoli è un'attività prevalentemente manuale e fisica che richi |
| 8.3.1.1.0 | Braccianti agricoli | 8 | 1 | I braccianti agricoli svolgono lavori principalmente manuali e fisici in ambient |
| 8.3.1.2.0 | Personale non qualificato addetto alla m | 8 | 1 | Questa professione comporta lavoro completamente manuale e fisico in ambienti es |
| 8.3.2.1.0 | Personale forestale non qualificato | 8 | 1 | Questa professione comporta lavoro manuale e fisico in ambienti forestali all'ap |
| 8.3.2.2.0 | Personale non qualificato addetto alla c | 8 | 1 | Questa professione comporta lavoro manuale e fisico prevalentemente in ambienti  |
| 8.3.2.3.0 | Personale non qualificato addetto alla p | 8 | 1 | Questa professione comporta lavoro manuale e fisico in ambienti esterni impreved |
| 8.4.1.1.0 | Manovali ed altro personale non qualific | 8 | 1 | Questa professione comporta lavoro manuale e fisico quasi esclusivamente nelle m |
| 8.4.2.1.0 | Manovali e personale non qualificato del | 8 | 1 | Questa professione comporta lavoro manuale e fisico quasi esclusivamente in ambi |
| 8.4.2.2.0 | Manovali e personale non qualificato del | 8 | 1 | Questa professione comporta lavoro manuale quasi interamente fisico in ambienti  |
