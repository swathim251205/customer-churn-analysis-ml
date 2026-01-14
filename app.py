# app.py
from multipage import MultiPage   
from app_pages.dashboard import dashboard_body

app = MultiPage(app_name="Dashboard App")  
app.add_page("Insurance", dashboard_body)

app.run()

