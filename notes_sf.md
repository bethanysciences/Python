POWER BI  
-----------------------
http://community.powerbi.com/t5/Developer/Access-Power-BI-API-with-Python/td-p/189165

MISC  
-----------------------  
Customer  Support
0         0       Never 
0         1       Never (since ~2017)
1         1       Current customer, paying for support.
1         0       Former

SOQL
-----------------------  
```SQL
SELECT CloseDate,CreatedDate,ForecastCategory,LeadSource,Name,Opp_Lead_Source__c,Owner_Role_POD__c,QcvTotalSoftware2__c,StageName FROM Opportunity

SELECT
Name,CreatedDate,CloseDate,ForecastCategory,LeadSource,Opp_Lead_Source__c,Owner_Role_POD__c,StageName,QcvTotalSoftware2__c FROM Opportunity ORDER BY CreatedDate DESC NULLS FIRST LIMIT 10
```

STREAM
-----------------------  
https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/intro_stream.htm
https://github.com/robertmrk/aiosfstream
https://docs.python.org/3/library/asyncio.html

NODE  
-----------------------
https://www.npmjs.com/package/jsforce_downloader

PYTHON
-----------------------
https://github.com/simple-salesforce/simple-salesforce
$ pip3 install simple-salesforce

`from simple_salesforce import Salesforce`

REST  
-----------------------  
curl https://login.salesforce.com/services/Soap/u/33.0 -H \"Content-Type: text/xml; charset=UTF-8\" -H \"SOAPAction: login\" -d @sf_login.txt
