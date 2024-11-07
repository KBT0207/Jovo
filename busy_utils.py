import pyautogui as pg
import time
import os
from dotenv import load_dotenv
from datetime import datetime
from logging_config import logger
from crud_database import process_files

pg.FAILSAFE = False


logger.info("Starting the automation script")

load_dotenv(".env")

current_date = datetime.now().date()
start_date = datetime(current_date.year, 11, 7).strftime('%d-%m-%Y')
today_date = current_date.strftime('%d-%m-%Y')


comp_list = ['COMP0003']

def open_busy():
    logger.info(f"Busy Opening....")
    busy_url = r"D:\UserProfile\Desktop\Busy 21.lnk"
    pg.hotkey('win', 'r')
    time.sleep(1)
    pg.typewrite(busy_url)
    time.sleep(1)
    pg.press('enter')

    security_check = None
    while security_check == None:
        try:
            security_check = pg.locateOnScreen('img/security_check.png', confidence=0.9)
            time.sleep(1)
            pg.press('enter')
            time.sleep(1)
        except:
            time.sleep(3)

    open_comapny = None
    while open_comapny == None:
        try:
            open_comapny = pg.locateOnScreen('img/open_company.png', confidence=0.9)
            pg.press('enter')
        except:
            time.sleep(3)

    select_comapny = None
    while select_comapny == None:
        try:
            select_comapny = pg.locateOnScreen('img/comapny_list.png',confidence=0.9)
        except:
            time.sleep(3)
    logger.info("Busy Open Succsesfully")

def company_open(comp):
    pg.typewrite(comp,interval=0.3)
    time.sleep(1)
    pg.press('tab')
    time.sleep(1)
    pg.press('enter')
    logger.info(f"Open Company {comp} Succsessfully ")

    user_pass = None
    while user_pass == None:
        try:
            user_pass = pg.locateOnScreen('img/user_pass.png',confidence=0.9)
            time.sleep(1)
        except:
            time.sleep(1)



    pg.typewrite(os.getenv("busy_user"),interval=0.1)
    time.sleep(1)  
    pg.press('enter')
    time.sleep(1)
    pg.typewrite(os.getenv('busy_pass'),interval=0.1)  
    time.sleep(1)
    pg.press('f2')
  
    open_dashboard = None
    while open_dashboard == None:
        try:
            open_dashboard = pg.locateOnScreen('img/open_dashboard.png',confidence=0.9)
            logger.info(f'Succsesfully Logged In {comp}')
        except:
            time.sleep(3)

def transaction_tab():
    transaction = None
    while transaction == None:
        try:
            transaction = pg.locateOnScreen('img/transaction.png',confidence=0.9)
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
        purchase= pg.locateOnScreen('img/purchase_unselected.png',confidence=0.9)
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
            pg.locateOnScreen('img/purchase_sel.png',confidence=0.9)
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
                pg.locateOnScreen('img/purchase_sel_down.png',confidence=0.9)
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
                    pg.locateOnScreen('img/purchase_unsel_down.png',confidence=0.9)
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
        purchase_order = pg.locateOnScreen('img/po_unselected.png',confidence=0.9)
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
            pg.locateOnScreen('img/po_selected.png',confidence=0.9)
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
                pg.locateOnScreen('img/po_unselected.png',confidence=0.9)
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
                    pg.locateOnScreen('img/po_unselected_down.png',confidence=0.9)
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

def mrfp_voucher():
    try:
        purchase_order = pg.locateOnScreen('img/mrfp_unselected.png',confidence=0.9)
        pg.moveTo(purchase_order)
        time.sleep(1)
        pg.click(purchase_order)
        time.sleep(1)
        pg.press('l')
        time.sleep(1)
        pg.press('enter')
        logger.info('MRFP Vch Open Succsesfully')
    except:
        try:
            pg.locateOnScreen('img/mrfp_unselected_down.png',confidence=0.9)
            pg.moveTo()
            time.sleep(1)
            pg.click()
            time.sleep(1)
            pg.press('l')
            time.sleep(1)
            pg.press('enter')
            logger.info('MRFP Vch Open Succsesfully')
        except:
            try:
                pg.locateOnScreen('img/mrfp_selected.png',confidence=0.9)
                pg.moveTo()
                time.sleep(1)
                pg.doubleClick()
                time.sleep(1)
                pg.press('l')
                time.sleep(1)
                pg.press('enter')
                logger.info('MRFP Vch Open Succsesfully')
            except:
                try:
                    pg.locateOnScreen('img/mrfp_sel_down.png',confidence=0.9)
                    pg.moveTo()
                    time.sleep(1)
                    pg.doubleClick()
                    time.sleep(1)
                    pg.press('l')
                    time.sleep(1)
                    pg.press('enter')
                    logger.info('MRFP Vch Open Succsesfully')
                except:
                    logger.info('MRFP Vch Error ')
                    pass

def mitp_voucher():
    try:
        mitp = pg.locateOnScreen('img/mitp_unselected.png',confidence=0.9)
        pg.moveTo(mitp)
        time.sleep(1)
        pg.click(mitp)
        time.sleep(1)
        pg.press('l')
        time.sleep(1)
        pg.press('enter')
        logger.info('MITP Vch Open Succsesfully')
    except:
        try:
            pg.locateOnScreen('img/mitp_selected.png',confidence=0.9)
            pg.moveTo()
            time.sleep(1)
            pg.click()
            time.sleep(1)
            pg.press('l')
            time.sleep(1)
            pg.press('enter')
            logger.info('MRFP Vch Open Succsesfully')
        except:
            try:
                pg.locateOnScreen('img/mitp_unselected_down.png',confidence=0.9)
                pg.moveTo()
                time.sleep(1)
                pg.doubleClick()
                time.sleep(1)
                pg.press('l')
                time.sleep(1)
                pg.press('enter')
                logger.info('MRFP Vch Open Succsesfully')
            except:
                try:
                    pg.locateOnScreen('img/mitp_sel_down.png',confidence=0.9)
                    pg.moveTo()
                    time.sleep(1)
                    pg.doubleClick()
                    time.sleep(1)
                    pg.press('l')
                    time.sleep(1)
                    pg.press('enter')
                    logger.info('MITP Vch Open Succsesfully')
                except:
                    logger.info('MITP Vch Error ')
                    pass

def stock_transfer():
    try:
        stck = pg.locateOnScreen('img/stck_unselected.png',confidence=0.9)
        pg.moveTo(stck)
        time.sleep(1)
        pg.click(stck)
        time.sleep(1)
        pg.press('l')
        time.sleep(1)
        pg.press('enter')
        logger.info('StockTransfer Vch Open Succsesfully')
    except:
        try:
            pg.locateOnScreen('img/stck_selected.png',confidence=0.9)
            pg.moveTo()
            time.sleep(1)
            pg.click()
            time.sleep(1)
            pg.press('l')
            time.sleep(1)
            pg.press('enter')
            logger.info('StockTransfer Vch Open Succsesfully')
        except:
            try:
                pg.locateOnScreen('img/stck_sel_down.png',confidence=0.9)
                pg.moveTo()
                time.sleep(1)
                pg.doubleClick()
                time.sleep(1)
                pg.press('l')
                time.sleep(1)
                pg.press('enter')
                logger.info('StockTransfer Vch Open Succsesfully')
            except:
                try:
                    unselected = pg.locateOnScreen('img/stck_unselected_down.png',confidence=0.9)
                    print(unselected)
                    pg.moveTo(unselected)
                    # time.sleep(1)
                    pg.click(unselected)
                    time.sleep(1)
                    pg.click(unselected)
                    time.sleep(1)
                    pg.press('l')
                    time.sleep(1)
                    pg.press('enter')
                    logger.info('Stcok Vch Open Succsesfully')
                except:
                    logger.info('StockTransfer Vch Error ')
                    pass

def stock_journal():
    try:
        stj = pg.locateOnScreen('img/stj_unselected.png',confidence=0.9)
        pg.moveTo(stj)
        time.sleep(1)
        pg.click(stj)
        time.sleep(1)
        pg.press('l')
        time.sleep(1)
        pg.press('enter')
        logger.info('StockJornal Vch Open Succsesfully')
    except:
        try:
            pg.locateOnScreen('img/stj_selected.png',confidence=0.9)
            pg.moveTo()
            time.sleep(1)
            pg.click()
            time.sleep(1)
            pg.press('l')
            time.sleep(1)
            pg.press('enter')
            logger.info('StockJornal Vch Open Succsesfully')
        except:
            try:
                pg.locateOnScreen('img/stj_unselected_down.png',confidence=0.9)
                pg.moveTo()
                time.sleep(1)
                pg.doubleClick()
                time.sleep(1)
                pg.press('l')
                time.sleep(1)
                pg.press('enter')
                logger.info('StockJornal Vch Open Succsesfully')
            except:
                try:
                    unselected = pg.locateOnScreen('img/stj_unselected.png',confidence=0.9)
                    print(unselected)
                    pg.moveTo(unselected)
                    # time.sleep(1)
                    pg.click(unselected)
                    time.sleep(1)
                    pg.click(unselected)
                    time.sleep(1)
                    pg.press('l')
                    time.sleep(1)
                    pg.press('enter')
                    logger.info('Stcok Jornal Open Succsesfully')
                except:
                    logger.info('StockJournal Vch Error ')
                    pass

def formate_vch(start_date: str, end_date: str, report_type: str = None):
    list_voucher_wait('img/list_of.png')
    time.sleep(1)
    pg.typewrite('New', interval=0.1)  # Formate Select
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.typewrite('<<-ALL->>', interval=0.1)  # master_series
    pg.press('enter')
    time.sleep(0.5)
    pg.typewrite('<<-ALL->>', interval=0.1)  # vch_Series_group_series
    pg.press('enter')
    time.sleep(0.5)
    pg.typewrite("<<-ALL->>", interval=0.1)
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(1)
    pg.typewrite(start_date)
    time.sleep(1)
    pg.press('enter')
    pg.typewrite(end_date)
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.typewrite('Name', interval=0.1)
    time.sleep(1)
    pg.press('enter')

    # Handle report-specific logic
    if report_type == 'purchase':
        handle_purchase_report()
    elif report_type == 'purchase_order':
        handle_purchase_order_report()
    elif report_type == 'mrfp':
        handle_mrfp_report()
    elif report_type == 'mitp':
        handle_mitp_report()
    elif report_type == 'stock_transfer':
        handle_stock_transfer_report()
    elif report_type == 'stock_jornal':
        handle_stock_journal_report()

def handle_purchase_report():
    time.sleep(0.5)
    pg.typewrite('Name')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('y')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('y')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('f2')

def handle_purchase_order_report():
    time.sleep(0.5)
    pg.typewrite('Name')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('y')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('y')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('f2')

def handle_mrfp_report():
    time.sleep(0.5)
    pg.typewrite('Name')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('y')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('y')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('f2')

def handle_mitp_report():
    time.sleep(0.5)
    pg.typewrite('Name')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('y')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('y')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('f2')

def handle_stock_transfer_report():
    time.sleep(0.5)
    pg.press('y')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('f2')

def handle_stock_journal_report():
    time.sleep(0.5)
    pg.press('y')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('y')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.5)
    pg.press('n')
    time.sleep(0.5)
    pg.press('enter')
    pg.press('f2')

def export_data(report:str, comp:str,start_date:str, end_date:str,today_date:str):
    loc = None
    while loc == None:
        try:
            loc = pg.locateOnScreen('img/data_complete100%.png',confidence=0.9)
        except:
            time.sleep(1)

    pg.hotkey('alt','e')

    export_data = None
    while export_data == None:
        try:
            export_data = pg.locateOnScreen('img/export_Report_data.png',confidence=0.9)
        except:
            time.sleep(1)

    pg.typewrite('Microsoft Excel',interval=0.2)
    time.sleep(1)
    pg.press('enter')

    base_dir = r"D:/UserProfile/Desktop/data"
    busy_export_data_dir = os.path.join(base_dir, 'busy_export_data', comp)
    date_dir = os.path.join(busy_export_data_dir,report)
    os.makedirs(date_dir, exist_ok=True)
    report_path = os.path.join(date_dir, f'{comp}_{report}_{start_date} to {end_date} {today_date}.xlsx')

    pg.typewrite(report_path, interval=0.3)
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.press('f2')
    time.sleep(2)
    logger.info(f"{report} Data Exporting.. {start_date} to {end_date}")
    try:
        overwrite = pg.locateOnScreen('img/file_exits.png',confidence=0.9)
        if overwrite:
            time.sleep(1)
            pg.click(overwrite)
            logger.info(f"{report} Overwrite Data Exporting.. {start_date} to {end_date}")
    except:
        pass


    export = None
    while export == None:
        try:
            export = pg.locateOnScreen('img/exported_completed.png',confidence=0.9)
            pg.press('n')
            time.sleep(1)
            pg.press('esc')
            logger.info(f'{report} Succsesfully Exported {start_date} to {end_date}')
        except:
            time.sleep(1)
    pg.press('esc',presses=3,interval=1)
    
def change_company():

    comp = None
    while comp == None:
        try:
            comp = pg.locateOnScreen('img/close_comapny.png', confidence=0.9)
            if comp:
                time.sleep(1)
                pg.press('y')
        except:
            time.sleep(1)
            pg.press("esc")

    open_comp = None
    while open_comp == None:
        try:
            time.sleep(1)
            open_comp = pg.locateOnScreen('img/open_company.png', confidence=0.9) 
            pg.press('enter')
        except:
            pg.press('down')

    comp_list = None
    while comp_list == None:
        try:
            comp_list = pg.locateOnScreen('img/comapny_list.png', confidence=0.9)
        except:
            time.sleep(0.5)



voucher_list = {'purchase': purchase,'purchase-order': purchase_order,'mrfp': mrfp_voucher, 'mitp':mitp_voucher,"stock-transfer":stock_transfer,'stock-journal':stock_journal}

def main():
    open_busy()
    for i in comp_list:
        company_open(comp=i)
        transaction_tab()
        for report, method in voucher_list.items():
            if callable (method):
                try:
                    method()
                    formate_vch(start_date,today_date,report_type=report)
                    export_data(start_date=start_date,end_date=today_date,report=report,comp=i,today_date=today_date)
                except Exception as e:
                    print(f"Error processing {report} for company {i}: {e}")
                    continue
        change_company()
    process_files(r"D:\UserProfile\Desktop\data")
        
main()

