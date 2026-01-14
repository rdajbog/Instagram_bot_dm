# Instagram_bot_dm
Acest proiect reprezinta un bot Python automatizat pentru Instagram, conceput sa trimita mesaje directe programate zilnic, optional, catre mai multi utilizatori. Conceptul este destinat firmelor de marketing pentru promovarea produselor si este dezvoltat in scop educational, demonstrand integrarea cu API-uri externe,gestionarea autentificarii securizate (inclusiv 2FA daca este cazul), programarea task-urilor si evitarea limitarilor de rata.


Functionalitati Principale: 
Trimite DM-uri catre o lista de utilizatori din fisierul CSV, cu esalonare pentru a evita detectarea ca spam.
Verificare raspunsuri: Analizeaza mesajele primite si trimite un mesaj daca raspunsul contine cuvinte cheie predefinite (ex: "da", "interesat").
Gestionare securizata: Suporta autentificare cu 2FA automata (via pyotp), proxy rotativ pentru anonimitate si salvarea sesiunilor pentru eficienta.
Log in si erori: inregistreaza toate actiunile si erorile intr-un fisier log pentru debugging in caz ca e nevoie.
Limbajul : Python 3.x
Biblioteci: instagrapi (pentru interactiune cu Instagram API), APScheduler (programare cron/mesaj), pyotp (intra in 2FA al contului si sa logheaza), pandas (gestionare CSV), fake_useragent si urllib (proxy si agentii utiliztorului pe langa proxy).

Proiectul inca poate fi imbunatatit si planific sa fac asta in viitor. Printre prioritati se numara imbunatatirea securitatii (ex: criptarea credentialelor suplimentara) si transformarea intregului proiect intr-unul accesibil printr-un program cu interfata grafica, cum ar fi folosind biblioteci precum Tkinter sau PyQt, pentru a-l face mai user-friendly si mai usor de configurat fara linie de comanda.

Daca doriti acces la codul complet al acestui proiect (inclusiv implementarea botului pe Instagram), va rog sa ma contactati direct prin email sau prin mesaje private pe GitHub. Codul nu este disponibil public pentru a pastra confidentialitatea si a evita potentiale probleme legate de termenii de serviciu ai platformelor implicate. Multumesc pentru interes!


<img width="286" height="88" alt="image" src="https://github.com/user-attachments/assets/64ed219f-c44b-4250-81f9-773e7c975c7a" />
<img width="1542" height="53" alt="Untitled design" src="https://github.com/user-attachments/assets/e0c247c3-c158-4a4a-8f99-ee7b0366078d" />
<img width="1436" height="948" alt="Untitled design (1)" src="https://github.com/user-attachments/assets/7124d105-fc7d-45a5-bcfe-29b277ff1256" />
