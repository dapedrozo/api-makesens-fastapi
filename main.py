from fastapi import FastAPI, Header
import httpx

app=FastAPI()

#FUNCTIONS CONTROLLER
token_ALL='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJUb2tlbl9QYXNvZWNvIiwic3ZyIjoibWFrZXNlbnMuYXdzLnRoaW5nZXIuaW8iLCJ1c3IiOiJNYWtlU2VucyJ9.MRZqkj8fnqXkzqf_EefhzXVQ6FYnL4iyNX-GraCKuhU'

token_f = lambda token:{'Content-Type': 'application/json','Authorization':f'Bearer {token}'}

async def requestAll(token):
    URL = "https://makesens.aws.thinger.io/v1/users/MakeSens/devices"
    headers=token_f(token)
    r = httpx.get(URL, headers=headers)
    return r.text

async def requestOne(id,token):
    URL = "https://makesens.aws.thinger.io/v1/users/MakeSens/devices/"
    headers=token_f(token)
    r = httpx.get(URL+id, headers=headers)
    return r.text

async def requestOneStats(id,token):
    URL = "https://makesens.aws.thinger.io/v1/users/MakeSens/devices/"
    END="/stats"
    headers=token_f(token)
    r = httpx.get(URL+id+END, headers=headers)
    return r.text

async def requestOneCallback(id,token):
    URL = "https://makesens.aws.thinger.io/v1/users/MakeSens/devices/"
    END="/callback"
    headers=token_f(token)
    r = httpx.get(URL+id+END, headers=headers)
    return r.text

async def requestOneProperties(id,token):
    URL = "https://makesens.aws.thinger.io/v1/users/MakeSens/devices/"
    END="/properties"
    headers=token_f(token)
    r = httpx.get(URL+id+END, headers=headers)
    return r.text

async def requestOneProperty(id,property,token):
    URL = "https://makesens.aws.thinger.io/v1/users/MakeSens/devices/"
    END="/properties/"
    headers=token_f(token)
    r = httpx.get(URL+id+END+property, headers=headers)
    return r.text

async def requestAllBuckets(token):
    URL = "https://makesens.aws.thinger.io/v1/users/MakeSens/buckets"
    headers=token_f(token)
    r = httpx.get(URL, headers=headers)
    return r.text

async def requestOneBuckets(bucket,token):
    URL = "https://makesens.aws.thinger.io/v1/users/MakeSens/buckets/"
    headers=token_f(token)
    r = httpx.get(URL+bucket, headers=headers)
    return r.text

async def requestOneBucketData(bucket,token):
    URL = "https://makesens.aws.thinger.io/v1/users/MakeSens/buckets/"
    END="/data"
    headers=token_f(token)
    r = httpx.get(URL+bucket+END, headers=headers)
    return r.text

async def requestAllDashboard(token):
    URL = "https://makesens.aws.thinger.io/v1/users/MakeSens/dashboards"
    headers=token_f(token)
    r = httpx.get(URL, headers=headers)
    return r.text

async def requestOneDashboard(dashboard,token):
    URL = "https://makesens.aws.thinger.io/v1/users/MakeSens/dashboards/"
    headers=token_f(token)
    r = httpx.get(URL+dashboard, headers=headers)
    return r.text

# DEVICES 
# RUTAS GET (LEECTURA)
@app.get('/devices')
async def f(token:str=Header(token_ALL)):
    r = await requestAll(token)
    return r

@app.get('/devices/{ID_DEVICES}')
async def f(ID_DEVICES:str,token:str=Header(token_ALL)):
    r = await requestOne(ID_DEVICES,token)
    return r

@app.get('/devices/{ID_DEVICES}/stats')
async def f(ID_DEVICES:str,token:str=Header(token_ALL)):
    r = await requestOneStats(ID_DEVICES,token)
    return r

@app.get('/devices/{ID_DEVICES}/callback')
async def f(ID_DEVICES:str,token:str=Header(token_ALL)):
    r = await requestOneCallback(ID_DEVICES,token)
    #r retorna unauthorized creo que es por el token que no tiene permiso de ver esto, eso dice
    #la documentacion
    return r

@app.get('/devices/{ID_DEVICES}/properties')
async def f(ID_DEVICES:str,token:str=Header(token_ALL)):
    r = await requestOneProperties(ID_DEVICES,token)
    #r retorna unauthorized creo que es por el token que no tiene permiso de ver esto, eso dice
    #la documentacion
    return r

@app.get('/devices/{ID_DEVICES}/properties/{PROPERTY}')
async def f(ID_DEVICES:str,PROPERTY:str,token:str=Header(token_ALL)):
    r = await requestOneProperty(ID_DEVICES,PROPERTY,token)
    #r retorna unauthorized creo que es por el token que no tiene permiso de ver esto, eso dice
    #la documentacion, ademas requiere una propiedad pero no se conoce ninguna
    return r

# BUCKETS
# RUTAS GET (LEECTURA)
@app.get('/buckets')
async def f(token:str=Header(token_ALL)):
    r = await requestAllBuckets(token)
    #r retorna unauthorized creo que es por el token que no tiene permiso de ver esto, eso dice
    #la documentacion
    return r

@app.get('/buckets/{bucket}')
async def f(bucket:str,token:str=Header(token_ALL)):
    r = await requestOneBuckets(bucket,token)
    #r retorna unauthorized creo que es por el token que no tiene permiso de ver esto, eso dice
    #la documentacion
    return r

@app.get('/buckets/{bucket}/data')
async def f(bucket:str,token:str=Header(token_ALL)):
    r = await requestOneBucketData(bucket,token)
    return r

# DASHBOARDS
# RUTAS GET (LEECTURA)
@app.get('/dashboards')
async def f(token:str=Header(token_ALL)):
    r = await requestAllDashboard(token)
    #r retorna unauthorized creo que es por el token que no tiene permiso de ver esto, eso dice
    #la documentacion
    return r

@app.get('/dashboards/{dashboard}')
async def f(dashboard:str,token:str=Header(token_ALL)):
    r = await requestOneDashboard(dashboard,token)
    #r retorna unauthorized creo que es por el token que no tiene permiso de ver esto, eso dice
    #la documentacion, ademas no se conoce ningun id de dashboard
    return r

# SE HACE LA ACLARACION DE QUE NO SE PUEDE IMPLEMENTAR LAS RUTAS POST ACTUALMENTE DEBIDO A DOS FACTORES
# PRIMERO: NO SE CONOCE LA ESTRUCTURA DEL JSON A ENVIAR PARA HACER CAMBIOS COMO TAL Y ESTO ES FUNDAMENTAL
# DADO A QUE SIN ENVIO DE PAQUETES NO SE PUEDE HACER UN METODO POST
# SEGUNDO: NO SE CONOCE ACTUALMENTE LOS PERMISOS DEL TOKEN EN CUESTION, CON LO CUAL SI EN CASI TODAS
# LAS VISTAS NO DEJA ACCEDER POR PERMISOS, SE CUESTIONA SI DESDE ESTE TOKEN SE PUEDA LLEGAR A REALIZAR
# ALGUN TIPO DE MODIFICACION YA SEA EN LOS DEVICES, LOS BUCKETS O LOS DASHBOARDS
# SIN EMBARGO SE ANEXAN LAS RUTAS A LAS CUALES SE DEBE HACER POST PARA UNA POSIBLE IMPLEMENTACION 
# A FUTURO

# RUTAS POST (DEVICES)
# https://makesens.aws.thinger. io/v3/users/MakeSens/devices/{ID_DEVICES}
# https://makesens.aws.thinger. io/v3/users/MakeSens/devices/{ID_DEVICES}/projects
# https://makesens.aws.thinger. io/v3/users/MakeSens/devices/{ID_DEVICES}/properties/{property}

# RUTA POST (PROPERTIES - DEVICES)
# https://makesens.aws.thinger. io/v3/users/MakeSens/devices/{ID_DEVICES}/properties

# RUTA POST (BUCKETS)
# https://makesens.aws.thinger. io/v1/users/MakeSens/buckets/{bucket}
# https://makesens.aws.thinger. io/v1/users/MakeSens/buckets/{bucket}/projects

# RUTA POST (DASHBOARDS)
# https://makesens.aws.thinger. io/v1/users/MakeSens/dashboards/{dashboard}