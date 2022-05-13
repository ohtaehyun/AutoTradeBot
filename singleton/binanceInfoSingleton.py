class BinanceInfoSingleton:
    __instance: None
    public_key:None
    private_key:None

    def get_public(self):
        return self.public_key

    def get_private(self):
        return self.private_key

    def set_public(self,public_key):
        self.public_key = public_key

    def set_private(self,private_key):
        self.private_key =private_key

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls,*args, **kargs):
        try:
            cls.__instance = cls(*args, **kargs)
            cls.instance = cls.__getInstance
            return cls.__instance
        except Exception as ex:
            print(ex)