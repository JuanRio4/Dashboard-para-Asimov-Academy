import sys
from streamlit.web import cli as stcli

sys.argv=['streamlit','run','Script.py']
sys.exit(stcli.main())
