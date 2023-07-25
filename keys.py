import json
import gspread
import pandas as pd

credentials = json.load(
    open("/Users/sophiechance/Documents/CourseKey/syncs/google_credentials.json")
)
gc = gspread.service_account_from_dict(credentials)


def get_keys():
    id_wb = gc.open_by_url(
        "https://docs.google.com/spreadsheets/d/1NzExg0HSoyrpTSkd9A49EOB4XAWZCh00w9An5p3rKa0/edit#gid=726799529"
    )
    key_list = id_wb.worksheet("Keys").get_all_records()
    key_dict = {d["Key"]: d["Value"] for d in key_list}

    client_success_payload = key_dict["cs_payload"]
    maxio_api_key = key_dict["maxio_key"]
    click_up_apikey = key_dict["click_up_key"]
    hubspot_arr_sync_apikey = key_dict["hubspot_key"]
    mysql_grow_pass = key_dict["grow_pass"]


    return (
        client_success_payload,
        maxio_api_key,
        click_up_apikey,
        hubspot_arr_sync_apikey,
        mysql_grow_pass
    )