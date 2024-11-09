from sqlalchemy import Column, String, Integer, Float, Date, Numeric
from .base import TimeStampedModel

class BusyPurchase(TimeStampedModel):
    __tablename__ = 'busy_rm_purchase'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    vch_bill_no = Column(String(50), nullable=False)  # Added length (50)
    particulars = Column(String(100), nullable=False)  # Added length (100)
    item_details = Column(String(200), nullable=False)  # Added length (200)
    material_centre = Column(String(100), nullable=False)  # Added length (100)
    qty = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)  # Added length (50)
    price = Column(Float, nullable=False)
    amount = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    invoice_amt = Column(Float, nullable=False)
    grn_no = Column(String(50), nullable=False)  # Added length (50)
    types = Column(String(50), nullable=False)  # Added length (50)
    narration = Column(String(255), nullable=True)  # Added length (255)


class BusyPurchaseOrder(TimeStampedModel):
    __tablename__ = 'busy_rm_purchase_order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    vch_bill_no = Column(String(50), nullable=False)  # Added length (50)
    particulars = Column(String(100), nullable=False)  # Added length (100)
    item_details = Column(String(200), nullable=False)  # Added length (200)
    material_centre = Column(String(100), nullable=False)  # Added length (100)
    qty = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)  # Added length (50)
    price = Column(Float, nullable=False)
    amount = Column(Float, nullable=False)
    gst_amount = Column(Float, nullable=False)
    po_value = Column(Float, nullable=False)
    requesting_dept = Column(String(100), nullable=False)  # Added length (100)
    po_officer = Column(String(100), nullable=False)  # Added length (100)


class BusyMrfp(TimeStampedModel):
    __tablename__ = 'busy_rm_mrfp'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    vch_bill_no = Column(String(50), nullable=True)  
    particulars = Column(String(255), nullable=True) 
    item_details = Column(String(255), nullable=True) 
    batch_no = Column(String(50), nullable=True) 
    batch_qty = Column(String(50),nullable=True)
    mfg_date = Column(String(50),nullable=True)
    exp_date = Column(String(50),nullable=True)
    material_centre = Column(String(100), nullable=True) 
    qty = Column(Numeric(10, 2), nullable=True)
    unit = Column(String(5), nullable=True) 
    narration = Column(String(255), nullable=True)
    tax_rate = Column(String(50),nullable=True)
    cgst = Column(String(50),nullable=True)
    sgst = Column(String(50),nullable=True)
    igst = Column(String(50),nullable=True)
    price = Column(Numeric(10, 2), nullable=True)
    amount = Column(Numeric(10, 2), nullable=True)
    gr_no = Column(String(50), nullable=True)
    gr_date = Column(Date, nullable=True)



class BusyMitp(TimeStampedModel):
    __tablename__ = 'busy_rm_mitp'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    vch_bill_no = Column(String(50), nullable=True)  # Added length (50)
    account_group = Column(String(50),nullable=False)
    particulars = Column(String(255), nullable=True)  # Added length (255)
    product_group = Column(String(50),nullable=False)
    item_details = Column(String(255), nullable=True)  # Added length (255)
    batch_no = Column(String(50), nullable=True) 
    batch_qty = Column(String(50),nullable=True)
    mfg_date = Column(String(50),nullable=True)
    exp_date = Column(String(50),nullable=True)
    material_centre = Column(String(100), nullable=True)  # Added length (100)
    qty = Column(Numeric(10, 2), nullable=True)
    unit = Column(String(5), nullable=True)  # Added length (5)
    price = Column(Numeric(10,2), nullable=True)  # Added length (50)
    amount = Column(Numeric(10, 2), nullable=True)
    tax_rate = Column(String(50),nullable=True)
    cgst_amt = Column(String(50),nullable=True)
    sgst_amt = Column(String(50),nullable=True)
    igst_amt = Column(String(50),nullable=True)
    narration = Column(String(255), nullable=True)
    sales_order_no = Column(String(50),nullable=True)
    salesman = Column(String(50),nullable=True)
    territory = Column(String(50),nullable=True)
    



class BusyStockTransfer(TimeStampedModel):
    __tablename__ = 'busy_rm_stock_transfer'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Added id field for consistency
    date = Column(String(50), nullable=False)  # Added length (50)
    vch_bill_no = Column(String(50), nullable=False)  # Added length (50)
    from_location = Column(String(100), nullable=False)  # Added length (100)
    to_location = Column(String(100), nullable=False)  # Added length (100)
    item_details = Column(String(255), nullable=False)  # Added length (255)
    qty = Column(Float, nullable=False)
    batch_no = Column(String(50), nullable=False)  # Added length (50)
    batch_narration = Column(String(255), nullable=True)  # Added length (255)
    unit = Column(String(5), nullable=False)  # Added length (5)
    narration = Column(String(255), nullable=True)  # Added length (255)
    purchase_invoice_no = Column(String(50), nullable=True)  # Added length (50)
    price = Column(Float, nullable=False)
    amount = Column(Float, nullable=False)


class StockJournal(TimeStampedModel):
    __tablename__ = 'busy_rm_stock_journal'

    # Define the columns
    id = Column(Integer, primary_key=True)  # Automatically increments to give each record a unique ID
    date = Column(Date, nullable=False)
    vch_bill_no = Column(String(50), nullable=False)  # Added length (50)
    material_centre = Column(String(100), nullable=True)  # Added length (100)
    item_details = Column(String(255), nullable=True)  # Added length (255)
    batch_no = Column(String(50), nullable=True)  # Added length (50)
    qty_generated = Column(Float, nullable=True)
    unit_main = Column(String(50), nullable=True)  # Added length (50)
    price = Column(Float, nullable=True)
    amount = Column(Float, nullable=True)
    qty_consumed = Column(Float, nullable=True)
    unit_consumed = Column(String(50), nullable=True)  # Added length (50)
    price_consumed = Column(Float, nullable=True)
    amount_consumed = Column(Float, nullable=True)
    narration = Column(String(255), nullable=True)  # Added length (255)
    grn_no = Column(String(50), nullable=True)  # Added length (50)
    pur_inv_no = Column(String(50), nullable=True)  # Added length (50)
