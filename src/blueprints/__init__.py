from .home import home_bl
from .organizations import org_bl
from .customer import cus_bl
from .role import role_bl
from .user import user_bl
from .chromeos import chrome_bl
from .mobdevices import mobdevices_bl
from .notifications import notifi_bl
from .domain import domain_bl
from .group import group_bl
from .member import member_bl
from .privileges import priv_bl
from .resources.calendars import cal_bl



# POLICY_SCHEMAS:
from .schemas import schema_bl
from .roleassigment import roleass_bl
from .verification import verification_bl
from .policy_schema import policyschema_bl





def reg_blueprints(app):
    app.register_blueprint(home_bl, url_prefix='/')
    app.register_blueprint(org_bl, url_prefix='/organization')
    app.register_blueprint(cus_bl,url_prefix='/customer')
    app.register_blueprint(role_bl,url_prefix='/role')
    app.register_blueprint(chrome_bl,url_prefix = '/chrome')
    app.register_blueprint(mobdevices_bl,url_prefix = '/mobdevices')
    app.register_blueprint(notifi_bl,url_prefix = '/notifi')
    app.register_blueprint(user_bl,url_prefix='/user') 
    app.register_blueprint(domain_bl,url_prefix='/domain') 
    app.register_blueprint(group_bl,url_prefix='/group') 
    app.register_blueprint(member_bl,url_prefix='/member')
    app.register_blueprint(priv_bl,url_prefix='/priv')
    app.register_blueprint(cal_bl,url_prefix = '/calendar')


# POLICY_SCHEMA
    app.register_blueprint(schema_bl,url_prefix='/schema')
    app.register_blueprint(roleass_bl,url_prefix='/roleass') 
    app.register_blueprint(verification_bl,url_prefix='/verification')
    app.register_blueprint(policyschema_bl,url_prefix='/policy_schema')
    
