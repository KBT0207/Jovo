import pyautogui as pg
import time
import os
from dotenv import load_dotenv
from datetime import datetime,timedelta,date
from logging_config import logger

logger.info("Starting the automation script")

load_dotenv(".env")

current_date = datetime.now().date()
start_date = date(current_date.year, 4, 1)

start_date = start_date.strftime('%d-%m-%Y')
today_date = current_date.strftime('%d-%m-%Y')

comp_list = ['COMP0003']

def open_busy():
    logger.info(f"Busy Opening.... {open_busy}")
    busy_url = r"D:\UserProfile\Desktop\Busy 21.lnk"
    pg.hotkey('win', 'r')
    time.sleep(1)
    pg.typewrite(busy_url)
    time.sleep(1)
    pg.press('enter')

    security_check = None
    while security_check == None:
        try:
            security_check = pg.locateOnScreen(r'D:\Busy\img\security_check.png', confidence=0.9)
            time.sleep(1)
            pg.press('enter')
            time.sleep(1)
        except:
            time.sleep(3)

    open_comapny = None
    while open_comapny == None:
        try:
            open_comapny = pg.locateOnScreen(r'D:\Busy\img\open_company.png', confidence=0.9)
            pg.press('enter')
        except:
            time.sleep(3)

    select_comapny = None
    while select_comapny == None:
        try:
            select_comapny = pg.locateOnScreen(r'D:\Busy\img\comapny_list.png',confidence=0.9)
        except:
            time.sleep(3)
    logger.info("Busy Open Succsesfully")

def company_open(comp):
    pg.typewrite(comp,interval=0.3)
    time.sleep(1)
    pg.press('tab')
    time.sleep(1)
    pg.press('enter')
    logger.info(f"Open {comp} Succsessfully ")

    user_pass = None
    while user_pass == None:
        try:
            user_pass = pg.locateOnScreen(r'D:\Busy\img\user_pass.png',confidence=0.9)
            time.sleep(1)
        except:
            time.sleep(1)



    pg.typewrite(os.getenv("busy_user"),interval=1)
    time.sleep(1)  
    pg.press('enter')
    time.sleep(1)
    pg.typewrite(os.getenv('busy_pass'),interval=1)  
    time.sleep(1)
    pg.press('f2')
  
    open_dashboard = None
    while open_dashboard == None:
        try:
            open_dashboard = pg.locateOnScreen(r'D:\Busy\img\open_dashboard.png',confidence=0.9)
            logger.info(f'Succsesfully Logged In{comp}')
        except:
            time.sleep(3)

def transaction_tab():
    transaction = None
    while transaction == None:
        try:
            transaction = pg.locateOnScreen(r'D:\Busy\img\transaction.png',confidence=0.9)
            time.sleep(1)
            pg.moveTo(transaction,duration=0.2)
            time.sleep(1)
            pg.click(transaction)
            time.sleep(1)
            logger.info('Transaction Tab Opened')
        except:
            time.sleep(1)

def list_voucher_wait(image_path):
    loc = None
    while loc == None:
        try:
            loc = pg.locateOnScreen(image_path,confidence=0.9)
        except:
            time.sleep(1)

def purchase():
    try:
        purchase= pg.locateOnScreen(r'D:\Busy\img\purchase_unselected.png',confidence=0.9)
        pg.moveTo(purchase)
        time.sleep(1)
        pg.click(purchase)
        time.sleep(1)
        pg.press('l')
        time.sleep(1)
        pg.press('enter')
        logger.info('Purchase Vch Open Succsesfully')
    except:
        try:
            pg.locateOnScreen(r'D:\Busy\img\purchase_sel.png',confidence=0.9)
            pg.moveTo()
            time.sleep(1)
            pg.click()
            time.sleep(1)
            pg.press('l')
            time.sleep(1)
            pg.press('enter')
            logger.info('Purchase Vch Open Succsesfully')
        except:
            try:
                pg.locateOnScreen(r'D:\Busy\img\purchase_sel_down.png',confidence=0.9)
                pg.moveTo()
                time.sleep(1)
                pg.doubleClick()
                time.sleep(1)
                pg.press('l')
                time.sleep(1)
                pg.press('enter')
                logger.info('Purchase Vch Open Succsesfully')
            except:
                try:
                    pg.locateOnScreen(r'D:\Busy\img\purchase_unsel_down.png',confidence=0.9)
                    pg.moveTo()
                    time.sleep(1)
                    pg.doubleClick()
                    time.sleep(1)
                    pg.press('l')
                    time.sleep(1)
                    pg.press('enter')
                    logger.info('Purchase Vch Open Succsesfully')
                except:
                    logger.info('Purchase Vch Error')
                    pass

def purchase_order():
    try:
        purchase_order = pg.locateOnScreen(r'D:\Busy\img\po_unselected.png',confidence=0.9)
        pg.moveTo(purchase_order)
        time.sleep(1)
        pg.click(purchase_order)
        time.sleep(1)
        pg.press('l')
        time.sleep(1)
        pg.press('enter')
        logger.info('Purchase Order Vch Open Succsesfully')
    except:
        try:
            pg.locateOnScreen(r'D:\Busy\img\po_selected.png',confidence=0.9)
            pg.moveTo()
            time.sleep(1)
            pg.click()
            time.sleep(1)
            pg.press('l')
            time.sleep(1)
            pg.press('enter')
            logger.info('Purchase Order Vch Open Succsesfully')
        except:
            try:
                pg.locateOnScreen(r'D:\Busy\img\po_unselected.png',confidence=0.9)
                pg.moveTo()
                time.sleep(1)
                pg.doubleClick()
                time.sleep(1)
                pg.press('l')
                time.sleep(1)
                pg.press('enter')
                logger.info('Purchase Order Vch Open Succsesfully')
            except:
                try:
                    pg.locateOnScreen(r'D:\Busy\img\po_unselected_down.png',confidence=0.9)
                    pg.moveTo()
                    time.sleep(1)
                    pg.doubleClick()
                    time.sleep(1)
                    pg.press('l')
                    time.sleep(1)
                    pg.press('enter')
                    logger.info('Purchase Order Vch Open Succsesfully')
                except:
                    logger.info('Purchase Order Vch Error ')
                    pass

def formate_vch():
    list_voucher_wait(r'D:\Busy\img\list_of.png')
    time.sleep(1)
    pg.typewrite('New',interval=0.1)   #Formate Select
    time.sleep(0.5) 
    pg.press('enter')
    time.sleep(0.5)
    pg.typewrite('<<-ALL->>',interval=0.1) #master_series
    pg.press('enter')
    time.sleep(0.5)
    pg.typewrite('<<-ALL->>',interval=0.1) #vch_Series_group_series
    pg.press('enter')
    time.sleep(0.5)
    pg.typewrite("<<-ALL->>",interval=0.1)
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(1)
    pg.typewrite(start_date)
    time.sleep(1)
    pg.press('enter')
    pg.typewrite(today_date)
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.typewrite('Name',interval=0.1)
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.typewrite('Name',interval=0.1)
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.press('y')
    time.sleep(1)
    pg.press('enter')  
    time.sleep(1)
    pg.press('y')
    time.sleep(1)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')  
    time.sleep(0.5)
    pg.press('n')
    time.sleep(1)
    pg.press('f2')
            
def export_data(report):
    loc = None
    while loc == None:
        try:
            loc = pg.locateOnScreen(r'img/data_complete100%.png',confidence=0.9)
        except:
            time.sleep(1)

    pg.hotkey('alt','e')

    export_data = None
    while export_data == None:
        try:
            export_data = pg.locateOnScreen(r'D:\Busy\img\export_Report_data.png',confidence=0.9)
        except:
            time.sleep(1)

    pg.typewrite('Microsoft Excel',interval=0.2)
    time.sleep(1)
    pg.press('enter')

    base_dir = r'D:\Busy'  #Base Directory 
    busy_export_data_dir = os.path.join(base_dir, 'busy_export_data', today_date) #join path
    os.makedirs(busy_export_data_dir, exist_ok=True) #folder creations
    report_path = os.path.join(busy_export_data_dir, f'{report}_{today_date}.xlsx') # report path

    pg.typewrite(report_path, interval=0.3)
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.press('f2')
    time.sleep(2)
    logger.info(f"{report} Data Exporting.. {today_date}")
    try:
        overwrite = pg.locateOnScreen(r'D:\Busy\img\file_exits.png',confidence=0.9)
        if overwrite:
            time.sleep(1)
            pg.click(overwrite)
            logger.info(f"{report} Overwrite Data Exporting.. {today_date}")
    except:
        pass


    export = None
    while export == None:
        try:
            export = pg.locateOnScreen(r'D:\Busy\img\exported_completed.png',confidence=0.9)
            pg.press('n')
            time.sleep(1)
            pg.press('esc')
            logger.info(f'{report} Succsesfully Exported {today_date}')
        except:
            time.sleep(1)
    pg.press('esc',presses=3,interval=1)
    
def change_company():
    comp = None
    while comp == None:
        try:
            comp = pg.locateOnScreen(r'D:\Busy\img\close_comapny.png',confidence=0.9)
            if comp:
                time.sleep(1)
                pg.press('y')
        except:
            time.sleep(1)
            pg.press("esc")

    open_comp = None
    while open_comp == None:
        try:
            open_comp = pg.locateOnScreen(r'D:\Busy\img\open_company.png',confidence=0.9) 
            time.sleep(1)
            pg.press('enter')
        except:
            time.sleep(1)
            pg.press('down')

    comp_list = None
    while comp_list == None:
        try:
            comp_list = pg.locateOnScreen(r'D:\Busy\img\comapny_list.png',confidence=0.9)
            time.sleep(1)
        except:
            time.sleep(1)


l1 = {'purchase':purchase,'purchase_order':purchase_order}

def main():
    open_busy()
    for i in comp_list:
        company_open(comp=i)
        transaction_tab()
        for report,method in l1.items():
            method()
            formate_vch()
            export_data(report)



main()