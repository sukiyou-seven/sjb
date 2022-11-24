from models.app_user import *


class AppUserInc:
    def check_user(self, u, p):
        fil = {
            AppUser.username == u,
            AppUser.password == p
        }
        res = AppUser.fetch_one(filter=fil)
        print(res)
        try:
            if len(res) > 0:
                return {"token": res['openid']}
            else:
                return 'error'
        except:
            return 'error'
