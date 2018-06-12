SELECT CreatedDate,LeadSource,Company,AnnualRevenue,NumberOfEmployees,
FROM Lead
WHERE LeadSource LIKE '%Google%' AND CreatedDate > YESTERDAY
LIMIT 20

SELECT LeadSource,CreatedDate,CreatedById,Rating,State,Website,Pardot_Drip_Program__c,Company,AnnualRevenue,Title,PostalCode,NumberOfEmployees,Persona__c,Market__c,Industries__c,Industry,Oppty_Created__c,ConvertedDate,OwnerId,PhotoUrl,Status,SQL_Date__c,SRL_Reason__c,Unqualified_Reason__c,User_Type__c
  FROM Lead
  WHERE CreatedDate >= THIS_YEAR
GROUP BY LeadSource

2017-01-01T00:00:00.000Z

String[]  VIPTITLES = new String []{'CEO','CFO','CMO','CTO','CIO','COO','VP','DIRECTOR','VIP'};
String[]  ORGANIC = new String []{'Bing Natural','Google Natural','Web','Yahoo! Natural','Yahoo Natural'}
String[]  TACTICAL = new String []{'Email','Lead Nurturing','Tactical'}
String[]  EVENT = new String []{'conf','Reception','Connect Owners','DSE','HITEC','ACI'}

String[]  PAID = new String []{'Bing','Bing Paid','Facebook','Google Ad','Google Paid','Incoming','LinkedIn','Yahoo Paid'}
Boolean first = true;
query = 'Select LeadSource FROM Lead';
for(String pd : PAID){
    if(!first){
        query = query + ' OR';
    } else {
        query = query + ' WHERE';
    }
    query = query + ' Lead.LeadSource LIKE \'%' + pd + '%\'';
    first = false;
}


YESTERDAY	Starts 00:00:00 the day before and continues for 24 hours.	SELECT Id FROM Account WHERE CreatedDate = YESTERDAY
TODAY	Starts 00:00:00 of the current day and continues for 24 hours.	SELECT Id FROM Account WHERE CreatedDate > TODAY
TOMORROW	Starts 00:00:00 after the current day and continues for 24 hours.	SELECT Id FROM Opportunity WHERE CloseDate = TOMORROW
LAST_WEEK	Starts 00:00:00 on the first day of the week before the most recent first day of the week and continues for seven full days. Your locale determines the first day of the week.	SELECT Id FROM Account WHERE CreatedDate > LAST_WEEK
THIS_WEEK	Starts 00:00:00 on the most recent first day of the week before the current day and continues for seven full days. Your locale determines the first day of the week.	SELECT Id FROM Account WHERE CreatedDate < THIS_WEEK
NEXT_WEEK	Starts 00:00:00 on the most recent first day of the week after the current day and continues for seven full days. Your locale determines the first day of the week.	SELECT Id FROM Opportunity WHERE CloseDate = NEXT_WEEK
LAST_MONTH	Starts 00:00:00 on the first day of the month before the current day and continues for all the days of that month.	SELECT Id FROM Opportunity WHERE CloseDate > LAST_MONTH
THIS_MONTH	Starts 00:00:00 on the first day of the month that the current day is in and continues for all the days of that month.	SELECT Id FROM Account WHERE CreatedDate < THIS_MONTH
NEXT_MONTH	Starts 00:00:00 on the first day of the month after the month that the current day is in and continues for all the days of that month.	SELECT Id FROM Opportunity WHERE CloseDate = NEXT_MONTH
LAST_90_DAYS	Starts 00:00:00 of the current day and continues for the past 90 days.	SELECT Id FROM Account WHERE CreatedDate = LAST_90_DAYS
NEXT_90_DAYS	Starts 00:00:00 of the current day and continues for the next 90 days.	SELECT Id FROM Opportunity WHERE CloseDate > NEXT_90_DAYS
LAST_N_DAYS:n	For the number n provided, starts 00:00:00 of the current day and continues for the past n days.	SELECT Id FROM Account WHERE CreatedDate = LAST_N_DAYS:365
NEXT_N_DAYS:n	For the number n provided, starts 00:00:00 of the current day and continues for the next n days.	SELECT Id FROM Opportunity WHERE CloseDate > NEXT_N_DAYS:15
NEXT_N_WEEKS:n	For the number n provided, starts 00:00:00 of the first day of the next week and continues for the next n weeks.	SELECT Id FROM Opportunity WHERE CloseDate > NEXT_N_WEEKS:4
LAST_N_WEEKS:n	For the number n provided, starts 00:00:00 of the last day of the previous week and continues for the past n weeks.	SELECT Id FROM Account WHERE CreatedDate = LAST_N_WEEKS:52
NEXT_N_MONTHS:n	For the number n provided, starts 00:00:00 of the first day of the next month and continues for the next n months.	SELECT Id FROM Opportunity WHERE CloseDate > NEXT_N_MONTHS:2
LAST_N_MONTHS:n	For the number n provided, starts 00:00:00 of the last day of the previous month and continues for the past n months.	SELECT Id FROM Account WHERE CreatedDate = LAST_N_MONTHS:12
THIS_QUARTER	Starts 00:00:00 of the current quarter and continues to the end of the current quarter.	SELECT Id FROM Account WHERE CreatedDate = THIS_QUARTER
LAST_QUARTER	Starts 00:00:00 of the previous quarter and continues to the end of that quarter.	SELECT Id FROM Account WHERE CreatedDate > LAST_QUARTER
NEXT_QUARTER	Starts 00:00:00 of the next quarter and continues to the end of that quarter.	SELECT Id FROM Account WHERE CreatedDate < NEXT_QUARTER
NEXT_N_QUARTERS:n	Starts 00:00:00 of the next quarter and continues to the end of the nth quarter.	SELECT Id FROM Account WHERE CreatedDate < NEXT_N_QUARTERS:2
LAST_N_QUARTERS:n	Starts 00:00:00 of the previous quarter and continues to the end of the previous nth quarter.	SELECT Id FROM Account WHERE CreatedDate > LAST_N_QUARTERS:2
THIS_YEAR	Starts 00:00:00 on January 1 of the current year and continues through the end of December 31 of the current year.	SELECT Id FROM Opportunity WHERE CloseDate = THIS_YEAR
LAST_YEAR	Starts 00:00:00 on January 1 of the previous year and continues through the end of December 31 of that year.	SELECT Id FROM Opportunity WHERE CloseDate > LAST_YEAR
NEXT_YEAR	Starts 00:00:00 on January 1 of the following year and continues through the end of December 31 of that year.	SELECT Id FROM Opportunity WHERE CloseDate < NEXT_YEAR
NEXT_N_YEARS:n	Starts 00:00:00 on January 1 of the following year and continues through the end of December 31 of the nth year.	SELECT Id FROM Opportunity WHERE CloseDate < NEXT_N_YEARS:5
LAST_N_YEARS:n	Starts 00:00:00 on January 1 of the previous year and continues through the end of December 31 of the previous nth year.	SELECT Id FROM Opportunity WHERE CloseDate > LAST_N_YEARS:5
THIS_FISCAL_QUARTER	Starts 00:00:00 on the first day of the current fiscal quarter and continues through the end of the last day of the fiscal quarter. The fiscal year is defined on the Fiscal Year page in Setup.	SELECT Id FROM Account WHERE CreatedDate = THIS_FISCAL_QUARTER
LAST_FISCAL_QUARTER	Starts 00:00:00 on the first day of the last fiscal quarter and continues through the end of the last day of that fiscal quarter. The fiscal year is defined on the Fiscal Year page in Setup.	SELECT Id FROM Account WHERE CreatedDate > LAST_FISCAL_QUARTER
NEXT_FISCAL_QUARTER	Starts 00:00:00 on the first day of the next fiscal quarter and continues through the end of the last day of that fiscal quarter. The fiscal year is defined on the Fiscal Year page in Setup.	SELECT Id FROM Account WHERE CreatedDate < NEXT_FISCAL_QUARTER
NEXT_N_FISCAL_​QUARTERS:n	Starts 00:00:00 on the first day of the next fiscal quarter and continues through the end of the last day of the nth fiscal quarter. The fiscal year is defined on the Fiscal Year page in Setup.	SELECT Id FROM Account WHERE CreatedDate < NEXT_N_FISCAL_QUARTERS:6
LAST_N_FISCAL_​QUARTERS:n	Starts 00:00:00 on the first day of the last fiscal quarter and continues through the end of the last day of the previous nth fiscal quarter. The fiscal year is defined on the Fiscal Year page in Setup.	SELECT Id FROM Account WHERE CreatedDate > LAST_N_FISCAL_QUARTERS:6
THIS_FISCAL_YEAR	Starts 00:00:00 on the first day of the current fiscal year and continues through the end of the last day of the fiscal year. The fiscal year is defined on the Fiscal Year page in Setup.	SELECT Id FROM Opportunity WHERE CloseDate = THIS_FISCAL_YEAR
LAST_FISCAL_YEAR	Starts 00:00:00 on the first day of the last fiscal year and continues through the end of the last day of that fiscal year. The fiscal year is defined on the Fiscal Year page in Setup.	SELECT Id FROM Opportunity WHERE CloseDate > LAST_FISCAL_YEAR
NEXT_FISCAL_YEAR	Starts 00:00:00 on the first day of the next fiscal year and continues through the end of the last day of that fiscal year. The fiscal year is defined on the Fiscal Year page in Setup.	SELECT Id FROM Opportunity WHERE CloseDate < NEXT_FISCAL_YEAR
NEXT_N_FISCAL_​YEARS:n	Starts 00:00:00 on the first day of the next fiscal year and continues through the end of the last day of the nth fiscal year. The fiscal year is defined on the Fiscal Year page in Setup.	SELECT Id FROM Opportunity WHERE CloseDate < NEXT_N_FISCAL_YEARS:3
LAST_N_FISCAL_​YEARS:n
