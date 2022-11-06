# randomUser
This is a randomUser module, it provides to create a random and fake user informations with cool utilities.

# Basic Usage
```python
# returns random user info
print(randomUser.create_person())
```

# Parameters
1) [gender_code](#gender_code)
2) [nationality](#nationality)
3) [noinfo](#noinfo)
4) [format](#format-and-download)
5) [download](**download**)
6) [printing_encode](#printing_encode)

# Usage with parameters
### gender_code
```python
# gender_code : Default equals to "random" but you can put other 2 gender such as "male" or "female". Codes = ("random":"random", "male":"male", "female":"female")
print(randomUser.create_person(gender_code="male"))
```
Output:
```
{"results":[{"gender":"male","name":{"title":"Mr","first":"Ricky","last":"Davidson"},"location":{"street":{"number":2862,"name":"Hogan St"},"city":"Savannah","state":"New York","country":"United States","postcode":27786,"coordinates":{"latitude":"87.6258","longitude":"111.0923"},"timezone":{"offset":"+9:00","description":"Tokyo, Seoul, Osaka, Sapporo, Yakutsk"}},"email":"ricky.davidson@example.com","login":{"uuid":"3d45ca3c-40fc-46c0-9e95-72b77918b669","username":"tinymeercat414","password":"austin31","salt":"Xpc8XyXa","md5":"8c78ecfbbefa93d5c938b16d9b5698ea","sha1":"d325d7227758c969a637646959d14fdb7086eed5","sha256":"5a273c849a45c09d3b12170f3eca46378ba914bdc11fd1c0c1a3f4b314bcf07d"},"dob":{"date":"1969-09-28T05:25:54.348Z","age":53},"registered":{"date":"2004-11-13T22:46:15.432Z","age":17},"phone":"(545) 257-4463","cell":"(619) 386-9410","id":{"name":"SSN","value":"516-23-7052"},"picture":{"large":"https://randomuser.me/api/portraits/men/72.jpg","medium":"https://randomuser.me/api/portraits/med/men/72.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/72.jpg"},"nat":"US"}],"info":{"seed":"96f4cd9219a8457b","results":1,"page":1,"version":"1.4"}}
```

### nationality
```
nationality : Default equals to "random" but you can put national code like "TR", "IN". Codes = "AU":"Australia", "BR":"Brazil", "CA":"Canada", "CH":"Switzerland", "DE":"Germany", "DK":"Denmark", "ES":"Spain", "FI":"Finland", "FR":"France", "GB":"United Kingdom", "IE":"Ireland", "IN":"India", "IR":"Iran", "MX":"Mexico", "NL":"Netherlands", "NO":"Norway", "NZ":"New Zealand", "RS":"Serbia", "TR":"Turkey", "UA":"Ukraine", "US":"United States"
```
```python
print(randomUser.create_person(nationality="US"))
```
Output:
```
{"results":[{"gender":"male","name":{"title":"Mr","first":"Ruben","last":"Ross"},"location":{"street":{"number":9716,"name":"Lakeshore Rd"},"city":"Ontario","state":"Arizona","country":"United States","postcode":25027,"coordinates":{"latitude":"86.7816","longitude":"-45.2377"},"timezone":{"offset":"+9:30","description":"Adelaide, Darwin"}},"email":"ruben.ross@example.com","login":{"uuid":"dcef6a02-42cc-4750-8ef0-8027177204d7","username":"yellowbird597","password":"taco","salt":"qhXXEwbH","md5":"a2e9e36d984c50cfab60cb50a4fe15f6","sha1":"6ace2c3b8f298259daec0b51cc5864c4137514a8","sha256":"3656dab83c2ccd94eb90714a49599994ef01357ca26435ce7dd8fc94e65ca0f8"},"dob":{"date":"1947-07-25T04:40:24.471Z","age":75},"registered":{"date":"2005-09-01T06:47:33.146Z","age":17},"phone":"(244) 302-8446","cell":"(385) 539-7299","id":{"name":"SSN","value":"721-43-0518"},"picture":{"large":"https://randomuser.me/api/portraits/men/45.jpg","medium":"https://randomuser.me/api/portraits/med/men/45.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/45.jpg"},"nat":"US"}],"info":{"seed":"3e3e2342ec6d62d6","results":1,"page":1,"version":"1.4"}}
```

### noinfo 
```python
# noinfo : Default equals to 'False' but you can put 'True' for if you only want the data, and don't care for seed, results, page, and api version data.
print(randomUser.create_person(noinfo=True))
```
Output: There is no seed, results, page, and api version data informations.
```
{"results":[{"gender":"female","name":{"title":"Mademoiselle","first":"Cindy","last":"Marchand"},"location":{"street":{"number":8147,"name":"Place de L'Abbé-Jean-Lebeuf"},"city":"Spiez","state":"Bern","country":"Switzerland","postcode":7687,"coordinates":{"latitude":"-56.9745","longitude":"137.2696"},"timezone":{"offset":"-3:00","description":"Brazil, Buenos Aires, Georgetown"}},"email":"cindy.marchand@example.com","login":{"uuid":"3935d3d3-e3ff-4ecb-9a97-bf36d2b30df7","username":"lazypeacock962","password":"mars","salt":"m076VTwP","md5":"0baaa8e3090f1cd45248879aa69b7565","sha1":"30b4310809c24a27bfc207614277c61269c5a90e","sha256":"47caf5a85298d5518c28312f2f135d014286925d84f5c99db2ad1f768ac75863"},"dob":{"date":"1958-10-22T16:53:56.263Z","age":64},"registered":{"date":"2009-12-30T03:53:04.822Z","age":12},"phone":"076 089 44 00","cell":"079 536 59 98","id":{"name":"AVS","value":"756.0343.5906.58"},"picture":{"large":"https://randomuser.me/api/portraits/women/80.jpg","medium":"https://randomuser.me/api/portraits/med/women/80.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/80.jpg"},"nat":"CH"}]}
```

### format and download
```python
# format : Default equals to "json", just specify the format you would like downloaded-returned by using the format parameter. !For downloading you must use with download() parameter!
# Supporting file formats "json", "strings", "bytes", "dict"
print(randomUser.create_person(format="csv"))
```
Output:
```
gender,name.title,name.first,name.last,location.street.number,location.street.name,location.city,location.state,location.country,location.postcode,location.coordinates.latitude,location.coordinates.longitude,location.timezone.offset,location.timezone.description,email,login.uuid,login.username,login.password,login.salt,login.md5,login.sha1,login.sha256,dob.date,dob.age,registered.date,registered.age,phone,cell,id.name,id.value,picture.large,picture.medium,picture.thumbnail,nat
female,Ms,Shubha,Nagane,2500,College St,Jalgaon,Uttar Pradesh,India,52075,11.0960,60.6897,+6:00,"Almaty, Dhaka, Colombo",shubha.nagane@example.com,c8ec336f-7e89-49c7-abec-08dcc76198b1,smallbird605,testerer,4HLJXBAQ,cf03b7ad8c04543966c14a4912c3f18f,a6cb6f52cc39c754b0bbeb2259b34e89924cf2fb,f56eb303cf4484e6e1c82f4f39ba037dce4ce2f8105d1f3d086ce04ba9662a8a,1990-10-11T10:05:53.148Z,32,2017-06-10T14:19:41.066Z,5,8305570316,9368258681,UIDAI,435592458886,https://randomuser.me/api/portraits/women/74.jpg,https://randomuser.me/api/portraits/med/women/74.jpg,https://randomuser.me/api/portraits/thumb/women/74.jpg,IN
```

And if you want to download use **"download"** parameter.

```python
# download : Default equals to 'False', just make 'True' for downloading the fake person's data. (The file's name will be 'person.(format)','person.json') and generally using with format() parameter.
print(randomUser.create_person(format="csv", download=True))
```
Output:
```
Trying to download..
Downloaded..
```
Downloaded file [csv_file](./img/person.csv)

### printing_encode 
```python
# printing_encode : Default equalts to "utf8". If you want to change printing encode you have to use this parameter.
print(randomUser.create_person(printing_encode="ascii"))
```
Output:
```
{"results":[{"gender":"male","name":{"title":"Mr","first":"����������","last":"������������"},"location":{"street":{"number":1674,"name":"��������"},"city":"������������","state":"����������","country":"Iran","postcode":53576,"coordinates":{"latitude":"4.8290","longitude":"-151.8642"},"timezone":{"offset":"+1:00","description":"Brussels, Copenhagen, Madrid, Paris"}},"email":"shyn.slry@example.com","login":{"uuid":"8472f0a7-4c5f-4f85-8c12-e1e577449820","username":"beautifuldog889","password":"rudy","salt":"tUu97Iva","md5":"da42c7ab20ce5e83ecdf95f8a42e6e49","sha1":"089985d60202b35487655d7d91fda61d3e1c2b8e","sha256":"cabf250c6ae20b61915854361a6557e8da1be3ffcd7d6a495e5ec667420d146a"},"dob":{"date":"1949-09-24T19:25:37.935Z","age":73},"registered":{"date":"2020-11-23T11:34:35.526Z","age":1},"phone":"044-22651020","cell":"0933-808-4621","id":{"name":"","value":null},"picture":{"large":"https://randomuser.me/api/portraits/men/36.jpg","medium":"https://randomuser.me/api/portraits/med/men/36.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/36.jpg"},"nat":"IR"}],"info":{"seed":"1e3195c6fd3257ab","results":1,"page":1,"version":"1.4"}}
```
