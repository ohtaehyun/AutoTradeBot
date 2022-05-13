from binance.client import Client

class BinanceInfoSingleton:
    __instance: None

    def get_public(self):
        return self.public_key

    def get_private(self):
        return self.private_key

    def set_public(self,public_key):
        self.public_key = public_key

    def set_private(self,private_key):
        self.private_key = private_key
    
    def set_client(self):
        self.binance_client = Client(self.public_key,self.private_key)

    def get_client(self):
        if hasattr(self,"binance_client"):
            return self.binance_client
        else:
            return None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls,*args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance