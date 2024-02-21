import requests
import datetime
import xml.etree.ElementTree as ET
import os
from constants import PROVIDERS,PROJECT, SERVER_PATH

def isSameCurrency(currency1, currency2):
    if currency1 == currency2:
        return True

class CurrencyCollection:

    def __init__(self,ExchanveValue):
        self.ExchanveValue = ExchanveValue

    def converterRatesEUR(self, currencyTarget):

        data = {
        "date": self.ExchanveValue["date"],
        "rates" :
            {
            }}

        ### Exchange rate Currency from EUR

        if not currencyTarget == "EUR":
            rate_CurrencyTarget_vs_Eur = 1 /  self.ExchanveValue["rates"][currencyTarget]
        else: 
            currencyTarget = 1
        data["rates"]["EUR"]= rate_CurrencyTarget_vs_Eur

        ### Remplace collection values with target currency's rates
        for rate in self.ExchanveValue["rates"]:
            if not isSameCurrency(currencyTarget,rate):

                rate_Eur_vs_ThirdCurrency            = self.ExchanveValue["rates"][rate]
                rate_CurrencyTarget_vs_ThirdCurrency = rate_CurrencyTarget_vs_Eur * rate_Eur_vs_ThirdCurrency

                data["rates"][rate] = rate_CurrencyTarget_vs_ThirdCurrency

        return data

class Deserializer:
    
    def BCE_daily_format(self):

        exchangeRates = {
            "date": "",
            "rates" :
                {
                }}

        ### Get xml from BCE
        providerUrl=PROVIDERS["BCE-daily"]["url"]
        dataSource_string  = requests.get(providerUrl).text
        dataSource_xml  = ET.fromstring(dataSource_string)

        ### Get datatime
        date_string=dataSource_xml[2][0].attrib['time']
        date_format = "%Y-%m-%d"

        date_object = datetime.datetime.strptime(date_string, date_format)
        exchangeRates["date"]=date_object

        ### Deserializer rates
        for exchangeRate in dataSource_xml[2][0]:
            exchangeRates["rates"][exchangeRate.attrib['currency']]=float(exchangeRate.attrib["rate"])
        
        return exchangeRates
    
    def Route(self, ProviderChoose):
        
        if ProviderChoose == "BCE-daily":
            data=self.BCE_daily_format()
        
        return data

class Serializer:

    def __init__(self,exchangeRates,currencyTarget):
        self.exchangeRates=exchangeRates
        self.currencyTarget=currencyTarget

    def BCE_daily_format_xmlfile(self, xml_body):
        ### Path navigation
        path=SERVER_PATH["root"]
        if not SERVER_PATH["project"] == "":
            path= path+"/"+SERVER_PATH["project"]
        if not SERVER_PATH["temp"] == "":
            path= path+"/"+SERVER_PATH["temp"]
        
        print(os.getcwd())
        print (path)

        if not os.getcwd() == path:
            if not SERVER_PATH["project"] == "":
                os.chdir(SERVER_PATH["project"])
            if not SERVER_PATH["temp"] == "":
                os.chdir(SERVER_PATH["temp"])
        
        ### Create xml
        filename= f"{self.currencyTarget}fxref-daily.xml"
        file=open(filename, "wb")

        ### Write data in the xml file
        tree_xml=ET.ElementTree(xml_body)
        tree_xml.write(file, encoding='utf-8', xml_declaration=True)

        return filename

    def BCE_daily_format(self):

        ### Get xml from BCE
        providerUrl=PROVIDERS["BCE-daily"]["url"]
        dataSource_string  = requests.get(providerUrl).text
        dataSource_xml  = ET.fromstring(dataSource_string)

        ### remplace sender
        project_name=PROJECT["name"]
        original_sender=dataSource_xml[1][0].text
        dataSource_xml[1][0].text = f"{project_name} - {original_sender}"

        ### Remplace xml values with target currency's rates
        for exchangeRate in dataSource_xml[2][0]:
            if isSameCurrency(exchangeRate.attrib['currency'],self.currencyTarget):
                exchangeRate.set("currency",'EUR')
                exchangeRate.set("rate",str(self.exchangeRates["rates"]["EUR"]))
            
            else:
                exchangeRate.set("rate",str(self.exchangeRates["rates"][exchangeRate.attrib["currency"]]))
        
        filename=self.BCE_daily_format_xmlfile(dataSource_xml)
        
        return filename

    def Route(self, FormatChoose):
        
        if FormatChoose == "BCE-daily":
            data = self.BCE_daily_format(self.exchangeRates,self.currencyTarget)
        
        return data

class ZebraCLI:

    def Convert(currencyTarget,provider):
        original_currency_collection= Deserializer().Route(provider)
        new_currency_collection=CurrencyCollection(original_currency_collection).converterRatesEUR(currencyTarget)
        api_output=Serializer(new_currency_collection,currencyTarget).BCE_daily_format()

        return api_output
    
    def GetProvicerList():

        return PROVIDERS
