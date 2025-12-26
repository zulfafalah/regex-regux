import os
import pdfplumber
import re

file_path ="pdf/"
files = [x for x in os.listdir(file_path) if x.endswith(".pdf")]
for file in files:
    print('-------------------------')
    print(f'Processing file: {file}')
    pdf = pdfplumber.open(f'pdf/{file}')
    page = pdf.pages[0]
    text = page.extract_text()  

    order_id = re.search(r'Purchase\s+Order\s+.*?\n\s*(\d{5,6})', text).group(1)
    purchase_order_no = re.search(r'Purchase\s+Order\s+.*?\n\s*\d{5,6}\s+(\d{10})', text).group(1)
    customer_name = re.search(r'Purchase\s+Order\s+([A-Z\s]+PT)', text).group(1)
    customer_address = re.search(r'Send\s+To\s*:\s*\n(.+?\n.+?\n.+?)(?:\n\n|\nNPWP)', text).group(1)
    npwp = re.search(r'NPWP\s*:\s*(\d+)', text).group(1)
    telephone = re.search(r'Telephone\s*:\s*([\d\s]+)', text).group(1)

    if len(telephone) < 5:
        telephone = re.search(r'Telephone\s*:\s*([\d\s\-/]+?)(?=\s+Delivery)', text).group(1)

    contact = re.search(r'Contact\s*:\s*([A-Z]+)', text).group(1)
    payment = re.search(r'Payment\s*:\s*([A-Z0-9]+)', text).group(1)
    po_date = re.search(r'PO\s+Date\s*:\s*(\d{2}\.\d{2}\.\d{4})', text).group(1)
    delivery = re.search(r'Delivery\s*:\s*(\d{2}\.\d{2}\.\d{4})', text).group(1)
    currency = re.search(r'Currency\s*:\s*([A-Z]+)', text).group(1)
    expiry_date = re.search(r'Expiry\s+Date\s*:\s*(\d{2}\.\d{2}\.\d{4})', text).group(1)
    note = re.search(r'Note\s*:\s*(.+?)(?=\n|$)', text).group(1).strip()
    prepared_by = re.search(r'Prepare\s+By\s*:*([^\n]+)', text).group(1).strip().replace(':', '')
    phone_number = (m := re.search(r'Phone\s+Number\s*:\s*(\d+)', text)) and m.group(1).strip()
    total_qty = re.search(r'Total Quantity+\s:+\s(\d+.\d+\s)', text).group(1).strip()
    total = re.search(r'Total+\s:(\d+.\d+.\d+)\s', text).group(1).strip()
    ppn_bm = re.search(r'PPN-BM+\s:+\s(\d+)\s', text).group(1).strip()
    ppn = re.search(r'PPN\s*:\s*([\d.]+)', text).group(1).strip()
    purchasing_group = re.search(r'Puchasing\s+Group\s*:\s*(.*?)\s+Planned', text).group(1).strip()
    planned_delv_cost = re.search(r'Delv.\sCost\s:\s(\d+)\s', text).group(1).strip()
    total_include_tax = re.search(r'Total\sInclude\sTax\s:(\d+.\d+.\d+)\s', text).group(1).strip()


    header_data = {
        "order_id": order_id,
        "purchase_order_no": purchase_order_no,
        "customer_name": customer_name,
        "customer_address": customer_address,
        "npwp": npwp,
        "telephone": telephone,
        "contact": contact,
        "payment": payment,
        "po_date": po_date,
        "delivery": delivery,
        "currency": currency,
        "expiry_date": expiry_date,
        "note": note,
        "prepared_by": prepared_by,
        "phone_number": phone_number,
        "total_qty": total_qty,
        "total": total,
        "ppn_bm": ppn_bm,
        "ppn": ppn,
        "purchasing_group": purchasing_group,
        "planned_delv_cost": planned_delv_cost,
        "total_include_tax": total_include_tax
    }

    
    # Pattern for get item data
    item_pattern = r'(\d{8})\s+([A-Z\s\d/]+?)\s+([\d,]+)\s*\n\s*(\d{5})\s+(\d+)\s+(EA)\s+(\d+)\s+(\d+)\s+(\d+)\s+([\d,]+)\s*\n\s*(PF\d+)Country of Origin\s*:\s*\w+\s+([\d,]+)'
    items = []
    matches = re.finditer(item_pattern, text, re.MULTILINE)
    
    for match in matches:
        article = match.group(1)
        description = match.group(2).strip()
        purc_price = match.group(3)  # Harga per unit (Purc/Unt)
        item_no = match.group(4)
        qty = match.group(5)
        uom = match.group(6)  # Unit of Measure (EA)
        discount_1st = match.group(7)  # Discount 1st
        discount_2nd = match.group(8)  # Discount 2nd
        discount_3rd = match.group(9)  # Discount 3rd
        total = match.group(10)  # Total
        sku = match.group(11)  # SKU (PF...)
        price_per_unit = match.group(12)  # Price/Unt (harga setelah discount)
        
        item_data = {
            "no": item_no,
            "article_sku": article + sku,
            "description": description,
            "qty": qty,
            "uom": uom,
            "discount_1st": discount_1st,
            "discount_2nd": discount_2nd,
            "discount_3rd": discount_3rd,
            "purc_price": purc_price,
            "price_per_unit": price_per_unit,
            "total": total
        }
        items.append(item_data)

    print(header_data) 
    
