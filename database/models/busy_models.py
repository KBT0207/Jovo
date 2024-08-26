from sqlalchemy import Column, String, Integer, Float, Date
from .base import TimeStampedModel

class Purchase(TimeStampedModel):
    __tablename__ = 'busy_purchase'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    vch_bill_no = Column(String(50), nullable=False)
    particulars = Column(String(100), nullable=False)
    item_details = Column(String(200), nullable=False)
    material_centre = Column(String(100), nullable=False)
    qty = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    amount = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    invoice_amt = Column(Float, nullable=False)
    grn_no = Column(String(50), nullable=False)
    types = Column(String(50), nullable=False)
    narration = Column(String(255), nullable=True)

    def __repr__(self):
        return (f"<PurchaseRecord(id={self.id}, date={self.date}, vch_bill_no={self.vch_bill_no}, "
                f"particulars={self.particulars}, item_details={self.item_details}, "
                f"material_centre={self.material_centre}, qty={self.qty}, unit={self.unit}, "
                f"price={self.price}, amount={self.amount}, tax={self.tax}, "
                f"invoice_amt={self.invoice_amt}, grn_no={self.grn_no}, type={self.type}, "
                f"narration={self.narration})>")

class PurchaseOrder(TimeStampedModel):
    __tablename__ = 'busy_purchase_order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    vch_bill_no = Column(String(50), nullable=False)
    particulars = Column(String(100), nullable=False)
    item_details = Column(String(200), nullable=False)
    material_centre = Column(String(100), nullable=False)
    qty = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    amount = Column(Float, nullable=False)
    gst_amount = Column(Float, nullable=False)
    po_value = Column(Float, nullable=False)
    requesting_dept = Column(String(100), nullable=False)
    po_officer = Column(String(100), nullable=False)

    def __repr__(self):
        return (f"<PurchaseOrder(id={self.id}, date={self.date}, vch_bill_no={self.vch_bill_no}, "
                f"particulars={self.particulars}, item_details={self.item_details}, "
                f"material_centre={self.material_centre}, qty={self.qty}, unit={self.unit}, "
                f"price={self.price}, amount={self.amount}, gst_amount={self.gst_amount}, "
                f"po_value={self.po_value}, requesting_dept={self.requesting_dept}, "
                f"po_officer={self.po_officer})>")
