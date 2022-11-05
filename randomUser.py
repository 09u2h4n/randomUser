#Coded by Oğuz
import requests
from json import dumps, loads

class randomUser(object):
    def __init__(self):
        self.api_version = "/1.4"
        self.api_url = "https://randomuser.me/api"+self.api_version
        self.func__codes__ = self.__codes__()
        self.national_codes = self.func__codes__[0]
        self.gender_codes = self.func__codes__[1]
        self.file_formats = self.func__codes__[2]
        self.returning_formats = self.func__codes__[3]

    def __help__(self):
        return(
f"""Using randomuser's api.
Website url : https://randomuser.me/
Api url : https://randomuser.me/api/

Something went wrong?
>>You must connect to internet
>>Check the keywords and rest of them (Codes? Maybe)

Usage of __help__() function:
    Shows this text.

Usage of create_person function:
>>randomUser().create_person(params)
    params:

        gender_code : Default equals to "random" but you can put other 2 gender such as "male" or "female". 
            All gender codes {self.gender_codes}

        nationality : Default equals to "random" but you can put national code like "TR", "IN".
            Supporting nationalities: {self.national_codes}

        noinfo : Default equals to 'False' but you can put 'True' for if you only want the data, and don't care for seed, results, page, and api version data.

        format : Default equals to "json", just specify the format you would like downloaded-returned by using the format parameter. !For downloading you must use with download() parameter!
            Supporting file formats {self.file_formats}

        download : Default equals to 'False', just make 'True' for downloading the fake person's data. (The file's name will be 'person.(format)','person.json') and generally using with format() parameter.

        returning_format : Default equalts to "strings". For returning to terminal

        printing_encode : Default equalts to "utf8". If you want to change printing encode you have to use this parameter.
        """)

    def __codes__(self):
        national_codes = {
            "AU":"Australia", 
            "BR":"Brazil", 
            "CA":"Canada", 
            "CH":"Switzerland",
            "DE":"Germany", 
            "DK":"Denmark", 
            "ES":"Spain", 
            "FI":"Finland", 
            "FR":"France", 
            "GB":"United Kingdom", 
            "IE":"Ireland", 
            "IN":"India", 
            "IR":"Iran", 
            "MX":"Mexico", 
            "NL":"Netherlands", 
            "NO":"Norway", 
            "NZ":"New Zealand", 
            "RS":"Serbia", 
            "TR":"Turkey", 
            "UA":"Ukraine", 
            "US":"United States"
        }
        gender_codes = {"random":"random", "male":"male", "female":"female"}
        supporting_formats = ["JSON (default)", "PrettyJSON or pretty", "CSV", "YAML", "XML"]
        returning_formats = ["json", "strings", "bytes", "dict"]
        return [national_codes, gender_codes, supporting_formats, returning_formats]

    def create_person(self, gender_code="random", nationality="random",noinfo=False , format="json", download=False, printing_encode="utf8"):
        try:
            if noinfo:
                url = self.api_url+f"/?gender={gender_code}&nat={nationality}&noinfo={noinfo}&format={format}"
            else:
                url = self.api_url+f"/?gender={gender_code}&nat={nationality}&format={format}"
            res = requests.get(url=url)
            data = res.content
            if download:
                try:
                    print("Trying to download..")
                    if format not in ["CSV","csv","YAML","yaml","XML","xml"]:
                        format = "json"
                    with open(f"person.{format}","wb") as f:
                        f.write(data)
                        return("Downloaded..")
                except:
                    return("Something went wrong!, for help \"randomUser.__help__()\"") 
            else:
                return data.decode(f"{printing_encode}",errors="replace")
        except:
            return ("Something went wrong!, for help \"randomUser.__help__()\"")