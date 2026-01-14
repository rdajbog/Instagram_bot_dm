import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from bot import RobotInstagram
import utils
import config
from datetime import timedelta, datetime
import time
import logging

def trimite_dm(robot, utilizatori):
    """functie pentru a trimite mesaje catre toti utilizatorii in fisier csv."""
    for idx, utilizator in enumerate(utilizatori):
        try:
            # INTARZIERE_LIMITA_RATA pentru protectie
            programare_dm.add_job(
                robot.trimite_dm_initial,
                'date',
                run_date=datetime.now() + timedelta(seconds=idx * config.INTARZIERE_LIMITA_RATA),
                args=[utilizator]
            )
            # programeaza urmarirea 1 zi mai tarziu pentru fiecare
            programare_dm.add_job(
                robot.trimite_urmarire,
                'date',
                run_date=datetime.now() + timedelta(days=1),
                args=[utilizator]
            )
            logging.info(f"Mesaj programat si urmarire pentru {utilizator}")
        except Exception as e:
            logging.error(f"Nu s-a putut programa pentru {utilizator}: {e}")

def main():
    robot = RobotInstagram()
    utilizatori = pd.read_csv('utilizatori_tinta.csv')['nume_utilizator'].tolist()

    global programare_dm  # face programare_dmul global pentru functia interna
    programare_dm = BackgroundScheduler()

    # Programeaza job-ul zilnic de dimineata la 7:00 AM
    programare_dm.add_job(
        trimite_dm,
        'cron',
        #hour=7,  # 7 dim
        minute='*',  # exact la minut
        args=[robot, utilizatori]  # trece robotul si utilizatori functiei
    )

    programare_dm.start()
    logging.info("programare_dm pornit. astept sarcini...")

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        programare_dm.shutdown()

if __name__ == "__main__":
    main()