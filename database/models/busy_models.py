from sqlalchemy import Column, String, Integer, Float, Date, Numeric
from .base import TimeStampedModel

class BusyPurchase(TimeStampedModel):
    __tablename__ = 'busy_rm_purchase'

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
                f"invoice_amt={self.invoice_amt}, grn_no={self.grn_no}, types={self.types}, "
                f"narration={self.narration})>")

class BusyPurchaseOrder(TimeStampedModel):
    __tablename__ = 'busy_rm_purchase_order'

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

class BusyMrfp(TimeStampedModel):
    __tablename__ = 'busy_rm_mrfp'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    vch_bill_no = Column(String(50))
    particulars = Column(String(255))
    item_details = Column(String(255))
    material_centre = Column(String(100))
    qty = Column(Numeric(10, 2))
    unit = Column(String(5))
    batch_no = Column(String(50))
    price = Column(Numeric(10,2))
    amount = Column(Numeric(10, 2))

    def __repr__(self):
        return (
            f"<BusyMrfp(id={self.id}, date={self.date}, vch_bill_no='{self.vch_bill_no}', "
            f"particulars='{self.particulars}', item_details='{self.item_details}', "
            f"material_centre='{self.material_centre}', qty={self.qty}, unit='{self.unit}', "
            f"batch_no='{self.batch_no}', price={self.price}, amount={self.amount})>"
            )
