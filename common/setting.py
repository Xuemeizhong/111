import  os

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
LOG_PATH =os.path.join(BASE_PATH,'log')
DATA_PATH =os.path.join(BASE_PATH,'data')
REPORT_PATH =os.path.join(BASE_PATH,'report')
CASE_PATH = os.path.join(BASE_PATH,'case')
REPORT_XML = os.path.join(REPORT_PATH,'xml')
REPORT_HTML = os.path.join(REPORT_PATH,'html')