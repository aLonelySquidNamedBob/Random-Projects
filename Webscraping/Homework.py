import requests
from bs4 import BeautifulSoup
import pandas as pd
import platform
from datetime import datetime

# Setup and format date
now = datetime.now()
date = ' '
datel = now.strftime("%a %d %b %Y %H:%M:%S")
datel = datel.split(' ')
datel[1] = str(int(datel[1]))
date = date.join(datel)

# Setup OS and notification system
# Read CSV
osgroup = platform.system().lower()
if 'linux' in osgroup:
    from notify_run import Notify

    notify = Notify()
    linuxgroup = str(platform.uname()).lower()

    if 'arandomcomputer' in linuxgroup:
        df1 = pd.read_csv('~/Desktop/Homework.csv')
    else:
        df = pd.read_csv('Homework.csv')
else:
    import os

    df1 = pd.read_csv('C:\\Users\\nicop_ny6irwr\\OneDrive\\Desktop\\Homework.csv')

# Setup webscraping and login details
login_url = 'https://cas.kosmoseducation.com/login'
page_url = 'https://lfjm.kosmoseducation.com/sg.do?PROC=TRAVAIL_A_FAIRE&ACTION=AFFICHER_ELEVES_TAF&filtreAVenir=true'

login = {
    'username': 'Pullen.nicolas',
    'password': 'EhcrsCFl',
    'execution': '00c97539-d0ae-4490-9e84-9e5e000205c9_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuWmtaZnpwR0VqOWIwRUlzMUlNdlA0U0ltSUE1eXlpblIzYmZRMVpWMFF3OGN1VGF2WGlGS1d5czJZUEIxcHdUc0Z1Zm1TbmhqaFVRV0dvN0YxS2dPclNxVStZR3kvd2s5VzBVM0lGMXIxYkNydnJYazVjbnU5bFhTVTQ2SVE3RXNBZXAzMFNjeGZqZGZVR20yV0xheG1qQ3YyYksrOTFqWldTNzA0cDQwbTZ1WC9USFZndUN5SGJGMDBpdmlpT1RCTnQwV1BpUEdoQ2NDNHp1OWRjQXQ3bnhEVVdKWDB0cXlaQ0ZuSDBXcEJLNkdFRWVGN1hCbHN6QnNhVWR3bTIrczA0cFdXNTg5Tkl5YjFrSDJ6OHZ5bnZ0NXF1U2lHSWV0blVsSmVHb2o0NG8xVjh6MnNON2hpVjRCbk9PVVNkaE9NYmJTSm1sUjhxTDkyVHVYQUw5c3Z4WERxK2k4N2piQmtta21JaVpwKzNrcmtlcml6UzhLWFBzcnpZWUVBZFVVRjFZT1BnMnlhQ3VqcUFnQmQ0cGVTdlNFTS9idTRuWFp4WWs3cWZrVk1SVjNzQzJ2dWdwV01nS2UrdHhWMHFvd2M2bENva09qWGxGYzhZYmIyU3QyMUl3cGhuRHM4bzdmLzNvOFh4MWplUW9QMnBWMW9oMVA5QmhwekswSWI2MkVHbjZ2NTE5WjdYT2ZFMW9pOUZiOVlVNEI0a240SjVqRU1hVEQ3bWV4YUowT2R2WVhlNzJ5ZDdCaUdYTFJyUnZXY2lxQmFYNjVET2VTaFFDVUdmU2NxRHBBTWxWdE1NeWhaVkUxTzdZTlBmTk1NZnZyZ2laemdMa2tQWVl2MS9KTWtvWnMzN2xsT1JFdTdZU0ZrYXFjZ01SU0xMTThyVGVKQzJPTGI3dTY4QkNuVjEzbkpPT3R2dUIraHNsdXZmVXRvcjREVUlRQkRrUE5SSExmMEZuVVI4TElISWVuMEZiUjRBbnZQZmx0Mi9uVUhSaktTd1ByZVU1dldoaE1IZy9DVmxuSFg4UWRtRWtHWEZ3TWRwNWlhZHpaUU1vd1lhV0ZnRUxBQmlGY1JpbGx5WERBaWQ5Q3hERmVQR3NydktQWVovaGptdGUvdG5uTEJRcVN4SHh5RUxMMmZPL3VyS1MxVzhVNnhnZWZFN2lTdkxHS0g3NkpZcUNFOHBjc3NuK2thQzVad1VoenFZR0ZvM0pNWkRxMXNBN2JkSlY3cEtGS0tzYU9GMitJbEJOb1M4clNXd1phOEZaS0pTYnViT3NWMkwwcGVqTjZxNkw1aVpPVDlYRStSdXkvNWVXV0o1bE5EV3Q1MUlvM0pITkpGc252SHhpdTBFL2l1VWtzMWhaQW8vQkN3U2tFQXpWcnZKN0VxbDFJRTFQWnE0UW0wNDROMEhDMDZ5UzUzRzBReGk1NFN5VVZVekdISGFwTmZleDZVOTBuYytuSWl4ZjFlUUlKUWpBTTVRZXdoc1B5YXhCSEdSYStGemVZR01iUlVjR3dIRm04WUUzK0c5N2Nnb3dzNWl5VVZVTS9CV0NXNnArSiszWkRPbjFaMUFlVkVQR2l2U0xtK3lqaG96eURvZXlBZWdlNXVQMW5hVzBPQTNnYjFpV1MxTktzcU5ScXRIVzFtb0ozcVQzSGFvc25CMGY2MVQvVE9nMEM1K1A1bkoxbHlvd2lYWGU1ckE1T0JRQ201TWdic1hORlRvdUhhZFFaNnBUNGpJb2oySm9RTWE1T1N0bjRObDZ3Mi9UbWhrRG1YUzlmMzBVMDVJa0hmcDV1VVh6T0hLOWdLeVN6SUdFVS92MDY0OGdQRXlPb1A3NEVKM0JkMXRtV1V5WlkyY0RMQVlxOXNvY1YreThoWTN1RXA3ZzhZbkhJLzA3cEpwc3NZUVh5WlgxaG5DRkhidEh5d3lzdFJCdmxuQjY4Q3Nmd2dFMjROb3o1cndreEpOcFo4aDFkUGtBaDBaTlNrZFdDeXFhQUFJTWdCRGtKYUlEL0tlSGk3cklUclhjQ2E5UUIzY2w1ZU40aUc1UGlZTHVNOVR4amFldnN0VU5BTXRaRkVZd1RMNXBmZ2tOZXFzT1RXN20xRDVnQmNsYms4VFEyYjBsRER4MW5sZkNLZkpocWpoUU9ORGRJU3JpL2lYaUNNQ0hoQUVvb202aUxnQ3lETjJpeDVtTldXeGRwK2I0em5oVzltT09GeC8wWHlCSlMydzVnNmlraDJqRWZETlRhLzlVYzB5MWxMekUwL2p1TEsxNytGT2psVVBuVEhtZ1ZhU0xpOHhicTB0ck9oSWV2MGlMUW82c2FFZ0t0QnhudDdUU2VlUXQxbjVhVmFRVGxENTE5M1Q1bSs2aWJFUVZmMmNuOHlhNTNQRWRZL1F3TnNUdXBKd1FaSW5mU1RFOUo2VkJVVE83ODcwSVlYdEpob0ZTeUE3RFFOZmNnVVpOQ1ZXdGF3RkowcmcyeSs2dkpSeXVRZ1VqSms2MEdCZWx6SzJIckYyNjcxNVpybStKZUxaODdab1pVNnFaRkJmSGFnSnFxSW5LVWxMbkFpdnR5SmR2Uy9tRXR3MmxZd1Ird1d3cTVjaDlSbCs5VXErZCtpeEhidk0zc3c5clhMczJCVVp2KzhoOTR6bGttNmNST0NEYk13NStPSHFBaEtyUnJpMWovZzlFSkFNdXd5ZTY5bWk1ODVsNTgrWlNkWDBkcFVkdWFzQk9lQTNYUFNTaVcrZHVsMjUvTjh2YTBaZVVUbzBhR2ZWNWRNaU8xakovMWVkZWlQb3IrbmdoeVRoYlMybkFkRDBQcUNnVWFOS252OGxvS0FucVpwdzIxVFJMZ2lCMlZMS1IveG9ibnFqY1Btci9iMW5qRW1Uc3lzeDdLc0ZVcFlUMlZDZGt0N2V5ZHdkU3dncE5YS0oweEtQcU1NbGx5MWREbnYreEJpM2dnN1JEb04vbytuQTV3anBRV0dZOWVMaDBXY0Z4K2piOTYxTHRPdEsvRGowdnNjaGlZeWlaSEZraG5lMzVJVks2QlUxYWJSemt6OEx2ekVaeWsySmRQRGErbVNKZVVNYmF3R084dUJZM3VtbkMzT2lNRzkyczBhb0FZVVZ1ZURLajdIOERXMUJWdU1uckxkc2NHeFpRN2htZmpiVDlPd2xvWFEvQzBxL3ZJMEFhUkxuS0QrUzh1OHRjZjJzdWE4b3daT1B6N2pjbGdxQWNKbTljMnRGVmgrNnU5VGhUVXQyVFNIVmwwU3BiQzRtZG5Yak8yYzBZTEE3dHpnbVBCTGhaMFYrbzd4QkdWVWZhcTRyS09HWUFoN3k3eHJ6RzlWYUlUc0w4YUlSRHF0cGRQbEhXNUpNaURCczNJM1pBVksvUVd6Qk5GaWZSREZzcTlEQy9qaDdHZ0RSUWpUM0V2QWlORkxGSldRSDlPajZzNVFVSWwrRU5BeFJ2YjVVSzFkU1ZlY3BRQi8zMUtIdys0QXpsTkdTd3VnNU1tVC9jYVRxUTliVjdZRERxdE0zOWhHbWt6dFMxcklpR1NqWUtUemxIcVBTMFZ5U3Q0SjRoL1JDTGJaeC9wMkFnamxaT1BPVlA3Sk5pRlYrb2hzcUt0MERjRHRXOS9YUzdlY2lNUnpXRFFlQXpDNkJGRzcvK3pMaG04SkhOdlVnSm04UnorRTZwdTBFS2s5VnVkRk5YNjJwMjdjWk5wcmM4bnBpMC9NNG1qejhHVWt2YUNmVis5cEFGMksxWHp0T2ErWVdxcVdPV3ptU1VRK0ZkTklWdFpxRFZYM0c0TDhreFFoMHQwcU1mMVAzdzhzOWdWWmZwU2wrNlBIRDNSUzdwMVBONVR4RWF1YXZwVzI4a3RDRXQxWklha2FRNG5TUCs3eWRyM1dCaTFNUTBFYlMvZ3lTOENiR3BBbndocU1FaUVrZDdmR2JUc1FCU0ZjMkltYXFXcTNRUWZxMTZtOG5tRkhQQTdwUjBPb3BPandOeXFFcFhNalJzTExrSHRJZUgxNXpYcDQ4bHRXQ0h6Rmc5TUlYNTNHUGJvMGlTZm1ZclRQQU95UVpuYktYWGNZZ3BZaVNNc0Y0ZEgvWktVL29sVktpQUd2cHBwdnlWRmVqbkE1M25TVzBUOHhKcjZ5ODVSUTNTYWxzaHR0dDJ4MDMyK3pDL0FuRkNZU2Q3SmZRWlA0ZFh2eWZsei9CM3ZOQU14NVNyeXdOc2tRdFp5akx6N0tlMzVIOGw5Q0tqMDRGamVaRW5JeDNhbmNQNjdPV2JzSC9UcWpYVHZNczEwUmVhVjRkRzNRUngzZ2NwRGJXWFVvSzFZcDlvWitOK3NMSE5Rc2xhTFp2Y1o0dy9qaVEvMU1yQWJuUktRVTNzVjNOM0YvalAwS3psU2ZyVDZKdjFMSWp5VUxFeFNlVERjdTMrN2l3SzJSUjJSbUpzeVROQVQrU05SVkJhM0JVZm1ndlluK3BGeU1IQ05obkw3c0dKN1RXakhsa3U2azhObUFxSGNnOVNxQldTNXlIL0w2U3hxUTY1MERjaWdoNTlqR3ByR090M0pEZEZ5UTJob1ZZa01UVUpkc2ljdXpJaSsxTFloREdXT1ZEL3RhUU90eFNLbnJ0ZXZxL1V3RDZqdTMybnJ6SFJWbVhIeVBGOGlOenRSVjVSWEFhM1ptTVhTNW4vN1lOamJhTDl1SVhGRFl4SGNKMTVDZkptOWlSRk5URjJWZDhwaGx1c2VzYVBBMERGK290MUZwSXJEL2lMa2NWbUh6amFXZ1ZMdVA1aDdUSHJCN1ZiZHh0T3FxazRvM09hUEFEQ0t0eThQWTRUeU40b3Z0bDFMRjlENFRlYlcxNHR6WDhtbTNJRlpxUXJIcDZTK3NPUG5HOE5QQmh6a29QZTl1K28rNlN3cFZIWHlhYmtrOWNTdkFYMWtyNDRNejFuWVZIUHFyTkJpcUxKTjNxV1J6YjJIYis4bmkrdHVqalNEVDhhMytxYW81U2NBM3lCSlNXWGdPL2ZsVUZuNTliTnprNkdVVjVGZ0xOTW1kcjUrcVFHalllVXg4TjArT0F3RkZaZHZKVWtzY0ZYWFF4Vm83amRSNEdONU9PcTZZUUtOdW1JT3lBcm1DbVJPQWJ3U1NidXJOSFJKT1RWWXV4MUV4aEN5NGxFL0FyTmViTFVXZHRBSmFWSk9jcW93aFhsbDdMdHp4UDNoanV2TmRReHBySEMwNFUxWFEyYzE0RzJTRGp2SzZBZDVOaE1YRzErUTNWSzVCZ25nbjdmRW1MYmdROVN5S0JsM1JvcyszYkVLK3pvdysrZUpTcTd1TytURXZKVkorTTBHRlRYN2VEdW51T1pqb3FzOGNBTVFvbWtpdlFzTVpBcmdLWmlobVlmdE5xSXdTZk9FVTN1a0Q1aGFiUnFrOVZneEJzUkczMEFvdGZvc05kZ1M3dXNGZ2twMklKVGVISlpNVG42NDg0UW9sQzJrQlFjUDF3LzhMNmV3SE5VL0p1MHZtQjEwU0hUQktlTG1EUktDREZkTzJiNExHZ051TW5QTWZLcUlNeVJBQ0psNDVHN3dvcTd0Uk44cndOUVNhcWZBMmVqd1BBPT0uTkxWdVdRNDktWW1CM3FoV1V6ZnNhbjZVNE54VGxxTS1HNmxlR1VwRlRQUm5wdmV3bHE0UlB1UzFyUWsweVQ1Q0JFbmtHaGlWWS16ZjM0MzFyRkMwZnc=',
    '_eventId': 'submit',
    'geolocation': '',
    'submit': 'Confirm'
}

# Start virtual session
with requests.Session() as s:
    post = s.post(login_url, login)
    page = s.get(page_url)

# Find content
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find('ul', class_='timeline__list js-timeline__list')
homework_els = content.find_all('div', class_='panel')

dates = []
subjects = []
summaries = []
completed = []
hand_in_types = []
hand_in_type = ''

# Parse HTML
for homework_e in homework_els:
    complete = "Non fait"
    estimated_time_e = homework_e.find('span', class_='pull-right')
    subject_e = homework_e.find('p', class_='p-like b-like slug slug--xs')
    summary_e = homework_e.find('p', class_='p-like h-like--no-margin')
    due_date_e = homework_e.find('p', class_='p-like slug slug--xs text--slate')
    complete_e = homework_e.find('span', class_='icon icon--check-success')
    hand_in_e = homework_e.find('a', class_='btn')
    if None in (subject_e, summary_e, due_date_e, hand_in_e):
        continue
    if complete_e is not None:
        complete = "Fait"
    hand_in = hand_in_e.text.strip()
    if "Déclarer" not in hand_in:
        hand_in_type = 'En ligne'
    else:
        hand_in_type = "A l'ecole"
    subject = subject_e.text.replace(estimated_time_e.text.strip(), ' ').strip()
    summary = summary_e.text.replace('Exercices :', '').replace('\n', '').replace('  ', '').strip().capitalize()
    due_date = due_date_e.text.strip().capitalize()
    subjects.append(subject)
    dates.append(due_date)
    summaries.append(summary)
    completed.append(complete)
    hand_in_types.append(hand_in_type)

# Add date/time to the bottom of CSV
for i in range(2):
    summaries.append(' ')
    hand_in_types.append(' ')
    completed.append(' ')
    if i == 0:
        dates.append(' ')
        subjects.append(' ')
    else:
        dates.append('Last updated:')
        subjects.append(date)

# Save info to pandas dataframe
df2 = pd.DataFrame({
    'Date a rendre': dates,
    'Matiere': subjects,
    'Contenu': summaries,
    'Rendre': hand_in_types,
    'Fait': completed
})

# Check to see if changed
# Send notifications
# Save pandas dataframe as CSV
if df1.get('Contenu').to_string() == df2.get('Contenu').to_string() and df1.get('Fait').to_string() == df2.get('Fait').to_string():
    print(f'{date} Same')
    if 'linux' in osgroup:
        notify.send('Updated')
        if 'arandomcomputer' in linuxgroup:
            df2.to_csv('~/Desktop/Homework.csv', index=False)
        else:
            df2.to_csv('Homework.csv', index=False)
    else:
        os.system('cmd /c "curl https://notify.run/ty0NllFAqXc43wUs -d "Updated""')
        df2.to_csv('C:\\Users\\nicop_ny6irwr\\OneDrive\\Desktop\\Homework.csv', index=False)

else:
    if df1.get('Contenu').to_string().strip() == df2.get('Contenu').to_string().strip():
        print(f'{date} Changed  Saving...')
        if 'linux' in osgroup:
            notify.send('Changed')
            if 'arandomcomputer' in linuxgroup:
                df2.to_csv('~/Desktop/Homework.csv', index=False)
            else:
                df2.to_csv('Homework.csv', index=False)
        else:
            os.system('cmd /c "curl https://notify.run/ty0NllFAqXc43wUs -d "Changed""')
            df2.to_csv('C:\\Users\\nicop_ny6irwr\\OneDrive\\Desktop\\Homework.csv', index=False)
    else:
        print(f'{date} New work  Saving...')
        if 'linux' in osgroup:
            notify.send('New Homework')
            if 'arandomcomputer' in linuxgroup:
                df2.to_csv('~/Desktop/Homework.csv', index=False)
            else:
                df2.to_csv('Homework.csv', index=False)
        else:
            os.system('cmd /k "curl https://notify.run/ty0NllFAqXc43wUs -d "New Homework""')
            df2.to_csv('C:\\Users\\nicop_ny6irwr\\OneDrive\\Desktop\\Homework.csv', index=False)

