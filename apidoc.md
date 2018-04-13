|URL| headers|methods|
|--|--|--|
| /api/v1.1/login/ |  | POST |

**URL Params:  None**

**POST Data:**

```
{
         "id" : string,  
}
```

**RETURN Data:**

```
{
        "token" : string
}
```

**Status Code**

```
200      // 成功
```

***


|URL| headers|methods|
|--|--|--|
| /api/v1.1/postscore/ | 'token' : string  | POST |

**URL Params:  无**

**POST Data:**

```
{
         "id" : string,
         "score" : int,
}
```

**RETURN Data:**

```
{
        
}
```

**Status Code**

```
200      // 成功
401      // 验证失败
```

***

|URL| headers|methods|
|--|--|--|
| /api/v1.1/book/ | | POST |

**URL Params: 无**

**POST Data:**

```
{

}
```

**RETURN Data:**

```
{
        “board”: [
             {
                 "id": string,
                 "score": int,
                 "rank": int
             }
             ...
        ]
}
```

**Status Code**

```
200      // 成功
```

***


