# Instagram_bot_dm
Acest proiect reprezintă un bot Python automatizat pentru Instagram, conceput să trimită mesaje directe programate zilnic, opțional, către mai mulți utilizatori. Conceptul este destinat firmelor de marketing pentru promovarea produselor și este dezvoltat în scop educațional, demonstrând integrarea cu API-uri externe.


Funcționalități Principale: 
Trimite DM-uri către o listă de utilizatori din fișierul CSV, cu esalonare pentru a evita detectarea ca spam.
Verificare răspunsuri: Analizează mesajele primite și trimite un mesaj dacă răspunsul conține cuvinte cheie predefinite (ex: "da", "interesat").
Gestionare securizată: Suportă autentificare cu 2FA automată (via pyotp), proxy rotativ pentru anonimitate și salvarea sesiunilor pentru eficiență.
Log in și erori: inregistrează toate acțiunile și erorile într-un fișier log pentru debugging in caz ca e nevoie.
Limbajul : Python 3.x
Biblioteci: instagrapi (pentru interactiune cu Instagram API), APScheduler (programare cron/mesaj), pyotp (intra in 2FA al contului si sa logheaza), pandas (gestionare CSV), fake_useragent și urllib (proxy si agentii utiliztorului pe langa proxy).

Dacă doriți acces la codul complet al acestui proiect (inclusiv implementarea botului pe Instagram), va rog să mă contactați direct prin email sau prin mesaje private pe GitHub. Codul nu este disponibil public pentru a păstra confidențialitatea și a evita potențiale probleme legate de termenii de serviciu ai platformelor implicate. Multumesc pentru interes!

<img width="1542" height="53" alt="image1" src="https://github.com/user-attachments/assets/968d3cdd-01c6-4bac-98ae-1246ee371192" />
<img width="286" height="88" alt="image" src="https://github.com/user-attachments/assets/10e36427-4826-4efb-be19-39ecf667e64d" />
<img width="1437" height="934" alt="image" src="https://github.com/user-attachments/assets/4e20cf6b-72a3-4bd1-b95d-b3aa82c72e58" />
