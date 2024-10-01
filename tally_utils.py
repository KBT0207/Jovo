import pyautogui as pg
import time
from dotenv import load_dotenv
import os

load_dotenv(".env")

def wait_img_path(path:str):
    loc = None
    while loc == None:
        try:
            loc = pg.locateOnScreen(path,confidence=0.9)
        except:
            time.sleep(0.5)

def open_tally():
    pg.hotkey('win','d')
    time.sleep(1)
    pg.hotkey('win','r')
    time.sleep(1)
    pg.typewrite(r"C:\Program Files\TallyPrime\tally.exe")
    time.sleep(1)
    pg.press('enter')
    wait_img_path("img_tally/select_comp.png")

def select_comp(comp):
    pg.typewrite(comp,interval=0.1)
    time.sleep(1)
    pg.press('enter')
    wait_img_path("img_tally/user_pass.png")
    pg.typewrite(os.getenv("busy_user"),interval=0.1)
    time.sleep(1)
    pg.press('enter')
    pg.typewrite(os.getenv("busy_pass"),interval=0.1)
    time.sleep(1)
    pg.press('enter')
    wait_img_path("img_tally/getway_tally.png")

def display_vch():
    pg.press('d')
    time.sleep(1)
    pg.press('a')
    wait_img_path('img_tally/account_book.png')

def purchase_register(start_date:str,end_date:str):
    wait_img_path("img_tally/account_book.png")
    pg.press('p')
    time.sleep(1)
    pg.press('enter')
    wait_img_path("img_tally/list_of.png")
    pg.hotkey('alt','f2')
    pg.typewrite(start_date,interval=0.1)
    time.sleep(1)
    pg.press('enter')
    pg.typewrite(end_date,interval=0.1)
    time.sleep(1)
    pg.press('enter')

def format_register(satrt_date:str,end_date:str):
    pg.hotkey('ctrl','e')
    time.sleep(1)
    pg.press('c')


open_tally()
select_comp("20001")
display_vch()
purchase_register(start_date='01-04-2024',end_date='14-09-2024')
