import datetime

PROJECT= {
    "name":"Zebra Converter",
    "description": "Convert open source currency provider from currency to another"}

PROVIDERS = {
    "BCE-daily":{
        "sender":"European Central Bank",
        "url":"http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"}
}

SERVER_PATH= {
    "root":"/home/CubeB87",
    "project":"mysite",
    "temp":"temp",
}

EXCHANGERATEDEMO = {
    "date": datetime.date(2023,2,20),
    "rates" :
    {
		'USD' :1.0768,
		'JPY' :161.88,
		'BGN' :1.9558,
		'CZK' :25.460,
		'DKK' :7.4546,
		'GBP' :0.85605,
		'HUF' :389.13,
		'PLN' :4.3400,
		'RON' :4.9771,
		'SEK' :11.2655,
		'CHF' :0.9491,
		'ISK' :149.10,
		'NOK' :11.3555,
		'TRY' :33.1951,
		'AUD' :1.6517,
		'BRL' :5.3551,
		'CAD' :1.4518,
		'CNY' :7.7461,
		'HKD' :8.4236,
		'IDR' :16837.38,
		'ILS' :3.8864,
		'INR' :89.3815,
		'KRW' :1435.09,
		'MXN' :18.3536,
		'MYR' :5.1476,
		'NZD' :1.7648,
		'PHP' :60.258,
		'SGD' :1.4500,
		'THB' :38.829,
		'ZAR' :20.3375,
            }
    }

COVER_HTML = {
    "Logo" : """<pre>
                ██████                                                        
        ██      ██  ░░██  ██                                                  
      ██  ██    ██  ░░████  ██                                                
      ██  ██    ██░░░░██    ██░░                                              
      ██    ██  ████████    ██                                                
        ██  ████    ██    ██  ██                                              
          ▓▓  ██  ▓▓    ██░░  ██▓▓                                            
          ██  ██  ██      ▓▓░░██░░░░                                          
          ██  ██  ██      ██████  ██                                          
        ▒▒                  ██    ██▒▒                                        
        ██                  ██░░██  ██                                        
        ██  ██    ██          ████    ██                                      
        ██  ██    ██            ██░░▓▓██                                      
        ██            ██          ████  ██                                    
        ████            ██      ██  ██░░██                                    
      ████          ██    ██  ██      ██░░██                                  
      ██              ██  ██        ██  ▓▓██        ██████▒▒████              
      ██████████      ██░░██      ██      ██████████  ██    ██  ██            
    ██░░░░░░░░░░██  ░░░░██      ██      ██  ██  ██      ██    ██  ██          
    ██░░░░░░░░░░░░██░░██░░            ██    ██    ██    ██    ██    ████      
    ██░░██░░▒▒░░░░████  ██░░        ▒▒      ██    ▓▓    ██    ██    ██░░▓▓    
    ██░░░░░░░░░░░░██    ██░░                ██    ██    ██    ██    ██  ██    
      ██▒▒▒▒▒▒▒▒▒▒██      ████████          ██    ██    ██    ██    ██    ██  
        ▓▓▓▓▓▓▓▓▓▓        ██░░            ▒▒      ██    ██    ██    ██    ██  
                          ██░░      ██          ██    ██    ██      ██  ██    
                          ██▓▓██▓▓▓▓        ██                    ▓▓██  ██    
                          ██░░              ██    ▓▓    ▒▒      ▒▒  ██  ██    
                          ██░░        ██    ██    ██    ██    ██    ██        
                          ██▓▓▓▓▓▓▓▓▓▓    ▓▓      ██    ██          ██        
                            ██░░                ██    ██      ██    ██        
                            ██    ██      ██░░░░░░░░░░░░░░░░██      ██        
                            ██░░  ████    ██████████████████░░      ██        
                              ██  ██  ██  ██          ██░░░░██████  ██        
                              ██████  ██▓▓██          ██████░░██░░    ██      
                              ██  ██  ██  ██            ██░░░░████░░████      
                              ██████  ██████            ██░░████  ██    ██    
                              ██  ██  ██  ██              ▓▓░░██    ▓▓  ██    
                              ██  ██  ██  ██      ░░      ██░░██    ██░░██    
                              ██░░██  ██░░██              ██░░██    ██░░██    
                              ██▓▓██  ██▓▓██              ██▓▓██    ██████    
                              ██████  ██████              ████▓▓    ██████    
                                                                              
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓    ▓▓░░▒▒▒▒▓▓▓▓░░▒▒▒▒▓▓  ▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓
▓▓▓▓    ▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓
</pre>
""",

"copyright_text": """
<pre>
Copyright 2024, Bonacorsi Giorgio

Copying and distribution of this file, with or without modification, are permitted in any medium without royalty, 
provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.,

</pre>
""",

"Guide":"""
<br>
[END POINTS]<br>
<br>
BCE daily provider:<br>
	/getconversion/bce-daily/[insert your reference currency]        exemple: /getconversion/bce-daily/USD <br>
<br>
"""
}