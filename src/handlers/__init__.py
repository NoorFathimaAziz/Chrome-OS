# --------------- organization ---------------
from .organization.list import OrganizationList
from .organization.get import OrganizationGet
from .organization.add import OrganizationAdd
from .organization.update import OrganizationUpdate
from .organization.patch_update import OrganizationUpdatePatch
from .organization.delete import OrganizationDelete

# --------------- customers ----------------
from .customer.get import CustomerGet
from .customer.update import CustomerUpdate
from .customer.patch import CustomerPatch 

# -------------- roles -----------------
from .role.get import RoleGet
from .role.list import RoleList
from .role.add import RoleAdd
from .role.update import RoleUpdate
from .role.patch import RolePatch
from .role.delete import RoleDelete
from.role.list_next import List_Next_Role

# -------------- users -------------------
from .user.list import  UserListHandler
from .user.add import UserAdd
from .user.get import UserGet
from .user.update import UserUpdate
from .user.patch import UserPatch
from .user.delete import UserDelete
from .user.undelete import UserUndelete
from .user.makeadmin import MakeAdmin
from .user.alias.list import AliasList
from .user.alias.add import AliasAdd
from .user.alias.delete import AliasDelete
from .user.photo.get import PhotoGet
from .user.photo.update import PhotoUpdate
from .user.photo.patch import PhotoPatch
from .user.photo.delete import PhotoDelete 

#-------------------domain---------------------
from .domain.list import DomainList   
from .domain.add import DomainAdd
from .domain.get import DomainGet
from .domain.delete import DomainDelete 

#-------------------groups----------------------
from .group.list import GroupList
from .group.add import GroupAdd
from .group.get import GroupGet
from .group.update import GroupUpdate
from .group.patch import GroupPatch 
from .group.delete import GroupDelete
from .group.alias.list import AliasListGroup
from .group.alias.add import AliasAddGroup 
from .group.alias.delete import AliasDeleteGroup 

#------------------members-------------------------
from .member.list import MemberList
from .member.add import MemberAdd
from .member.get import MemberGet
from .member.update import MemberUpdate
from .member.patch import MemberPatch
from .member.delete import MemberDelete
from .member.hasmember import HasMember


# ----------------chromeos--------------------------
from .chromeos.list import ChromeList
from .chromeos.action import ActionHandler
from .chromeos.get import ChromeOSget
from .chromeos.update import UpdateChrome
from .chromeos.patch import PatchChrome
from .chromeos.move import MoveChromeOS


#------------------------mobdevices------------------
from .mobiledevices.action import ActionMobDevices
from .mobiledevices.delete import DelMobdevices
from .mobiledevices.get import GetMobdevices
from .mobiledevices.list import ListMobDevices


# -------------------Notifications ----------------------
from .notifications.delete import DeleteNotifi
from .notifications.update import Updatenotifi
from .notifications.get import GetNotifi
from .notifications.patch import Patchnotifi
from .notifications.list import ListNotifi


# -----------------privileges---------------------
from .privileges.list import Listpriv


# ----------------------RESOURCES-----------------------------
# ---------------------CALENDARS-------------------------------
from .resources.calendars.list import CalList
from .resources.calendars.insert import CalAdd
from .resources.calendars.get import CalGet
from .resources.calendars.delete import CalDel
from .resources.calendars.update import CalUpdate
from .resources.calendars.patch import CalPatch

#-----------------schemas---------------------------
from .schema.list import SchemaList
from .schema.add import SchemaAdd 
from .schema.get import SchemaGet
from .schema.update import SchemaUpdate
from .schema.patch import SchemaPatch
from .schema.delete import SchemaDelete 

#---------------roleAssignment-----------------------
from .roleassigment.list import RoleAssList
from .roleassigment.add import RoleAssAdd
from .roleassigment.get import RoleAssGet
from .roleassigment.delete import RoleAssDelete     
  
#----------------verification code---------------------
from .verification.list import verificationList
from .verification.generate import verificationGenerate
from .verification.invaild import verificationInvaild



# -------------POLICYSCHEMA----------------------
#----------------policy_schema--------------------------
from .policyschema.list import PolicySchemaList
from .policyschema.get import PolicySchemaGet
from .policyschema.update import PolicySchemaUpdate
