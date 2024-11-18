from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, country_code: str=None, **kwargs):
        self.spark = None
        self.update(country_code)

    def update(self, country_code: str="RU", **kwargs):
        prophecy_spark = self.spark
        self.country_code = country_code
        pass
