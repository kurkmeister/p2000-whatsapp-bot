import pandas as pd
from geocode import get_coordinates_from_string
from send_message import send_body_message, send_location_message
import time
import json


# import capcodes from json file
with open("capcodes-json.json", "r") as file:
    capcodes = json.load(file)

def parse_url_and_clean(city='Amsterdam'):

    # url to parse
    url = 'http://p2000.brandweer-berkel-enschot.nl/LiveMonitor.aspx'

    ###
    # Get tables from URL, and format into table with columns:
    # Index, Capcode, Datumtijd, Messsage
    # 2,	2029568,	30-09-23 23:17:35,	P 2 BAD-02 Liftopsluiting Binnenkadijk Amsterd...

    tables = pd.read_html(url)
    tables[2]
    # select first 10 rows, but skip first row. second row is the header
    df = tables[2][1:]
    # set first row as header
    df.columns = tables[2].iloc[1]
    # drop first row
    df = df.drop(df.index[0])

    # get last 6 characters of the last column and set as new column, only if they are digits
    df['incident'] = df['Message'].str[-6:].str.extract('(\d+)', expand=False)


    # make new df with only rows that contain 'Amsterdam'

    df_amsterdam = df[df['Message'].str.contains(city, case=False)]

    if df_amsterdam.empty:
        print(f'No new incidents in {city}')
        send_body_message('🚨🚨🚨🚨🚨🚨🚨')
        time.sleep(0.9)
        send_body_message(f'Geen recente P2000 meldingen in {city}')
        time.sleep(0.9)
        send_body_message('_Einde bericht_')
        exit()

    number_of_incidents = 3

    # get all messages from the last three incident numbers
    last_three = df_amsterdam[df_amsterdam['incident'].isin(df_amsterdam['incident'].unique()[-number_of_incidents:])]

    # merge rows with the same incident number, keeping the capcodes, and first time and message
    last_three = last_three.groupby('incident').agg({'Capcode': lambda x: x.tolist(), 'Datumtijd': 'first', 'Message': 'first'}).reset_index()

    # turn the dataframe into a list
    last_three = last_three.values.tolist()

    return last_three

def format_list(last_three, city='Amsterdam'):
    # replace the capcodes with the corresponding names, if they do not exist, replace with 'onbekend'
    for row in last_three:
        row[1] = [capcodes.get(item, '‼️ Code onbekend') for item in row[1]]
    # print the list


    # turn the list into a formatted string for a telegram bot message
    last_three_formatted = [
        f'{row[2]}: Incident {row[0]}\n{row[1]}\n{row[3]}\n' for row in last_three
        ]

    send_body_message('🚨🚨🚨🚨🚨🚨🚨')
    time.sleep(0.9)
    send_body_message(f"P2000 meldingen\nRegio {city}")
    time.sleep(0.9)
    for row in last_three:
        time_only = row[2].split(' ')[1]
        messages = '\n'.join(row[1])
        # body = f'{time}\nIncident {row[0]}\n{row[3]}\n{messages}\n'
        body = f'*Tijd*: {time_only}\n*Bericht*: {row[3]}\n*Eenheden opgeroepen*\n{messages}\n'
        print(body)
        coordinates, label, location_type = get_coordinates_from_string(row[3])
        send_body_message(body)
        time.sleep(1.5)
        send_location_message(coordinates, label, f'Accurracy: {location_type}')
        time.sleep(3)
    send_body_message('_Einde bericht_')


if __name__ == '__main__':
    last_three = parse_url_and_clean()
    format_list(last_three)

def run_p2000_bot(city='Amsterdam'):
    last_three = parse_url_and_clean(city)
    format_list(last_three, city)