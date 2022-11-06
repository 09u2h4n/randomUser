# randomUser
This is a randomUser module, it provides to create a random and fake user informations with cool utilities.

# Basic Usage
```python
# returns random user info
randomUser.create_person()
```

# Parameters
1) [gender_code](#gender_code)
2) [nationality]
3) [noinfo]
4) [format]
5) [download] 
6) [returning_format]
7) [printing_encode]

# Usage with parameters
### gender_code
```python
# gender_code : Default equals to "random" but you can put other 2 gender such as "male" or "female". Codes = ("random":"random", "male":"male", "female":"female")
randomUser.create_person(gender_code="male")
```
Output:
```
{"results":[{"gender":"male","name":{"title":"Mr","first":"Ricky","last":"Davidson"},"location":{"street":{"number":2862,"name":"Hogan St"},"city":"Savannah","state":"New York","country":"United States","postcode":27786,"coordinates":{"latitude":"87.6258","longitude":"111.0923"},"timezone":{"offset":"+9:00","description":"Tokyo, Seoul, Osaka, Sapporo, Yakutsk"}},"email":"ricky.davidson@example.com","login":{"uuid":"3d45ca3c-40fc-46c0-9e95-72b77918b669","username":"tinymeercat414","password":"austin31","salt":"Xpc8XyXa","md5":"8c78ecfbbefa93d5c938b16d9b5698ea","sha1":"d325d7227758c969a637646959d14fdb7086eed5","sha256":"5a273c849a45c09d3b12170f3eca46378ba914bdc11fd1c0c1a3f4b314bcf07d"},"dob":{"date":"1969-09-28T05:25:54.348Z","age":53},"registered":{"date":"2004-11-13T22:46:15.432Z","age":17},"phone":"(545) 257-4463","cell":"(619) 386-9410","id":{"name":"SSN","value":"516-23-7052"},"picture":{"large":"https://randomuser.me/api/portraits/men/72.jpg","medium":"https://randomuser.me/api/portraits/med/men/72.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/72.jpg"},"nat":"US"}],"info":{"seed":"96f4cd9219a8457b","results":1,"page":1,"version":"1.4"}}
```


