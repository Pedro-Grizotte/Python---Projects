from pathlib import Path

ROOT = Path(__file__).parent
IMGS = ROOT / 'images'
ICON = IMGS / 'icon.png'

# Sizing
BIG_FONT_SIZE = 40
FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MIN_WIDTH = 500

PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'

# QSS - Estilos do QT for Python 
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
import qdarkstyle

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

def setupStyle(app):
    # Aplica o style [dark] no projeto
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    # sobrepoem o QSS perdonalizado para estilização adicional
    app.setStyleSheet(app.styleSheet() + qss)

