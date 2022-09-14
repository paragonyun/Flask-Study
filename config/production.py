## 서버 환경 담당
from config.default import *

SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'pybo.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xf4\xe7\xd7\x00\xe6\xfc:n\x0c\x171\x164\xc2\x040'

