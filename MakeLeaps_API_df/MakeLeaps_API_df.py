### ML api ###
import pandas as pd 
import requests

d = {"grant_type" : "client_credentials"}
h = {"Accept": "application/json", "Accept-Language": "en_US"}

auth_url = "https://api.makeleaps.com/user/oauth2/token/"
cid = "{Client Id}"
secret = "{Client Secret}"

r = requests.post(auth_url, auth=(cid, secret), headers=h, data=d).json()
access_token = r['access_token']
h["Authorization"] = f'Bearer {access_token}'

import time
def getRecord(url,page_num):    
    queries = f"?page={page_num}"
    #     if page_num % 100 == 0:
    #         print(f"sleeping as n_get reached {page_num}")
    #         time.sleep(40)
    print(f"retrieving page {page_num}")
    g = requests.get(url+queries, headers=h).json()
    if g['meta']['status'] != 200:
        print(f"error at page {page_num} with status {g['meta']['status']}")
        return "error"
    else:
        data = pd.DataFrame(g['response'])
        return data

def load_df(kind):
    g_url = f'https://api.makeleaps.com/api/partner/{MakeLeaps_ID}/{kind}/'
    g_r = requests.get(g_url, headers=h).json()
    df = pd.DataFrame(g_r['response'])
    n_retrieve = -(-g_r['meta']['count'] // 20)
    
    print(f"downloading {kind}s across {n_retrieve} pages and {g_r['meta']['count']} records")
    for i in range(2,n_retrieve + 1):
        data = getRecord(g_url,i)
        if type(data) != str:
            df = df.append(data)
    return df.reset_index()
 
client_df = load_df("client").drop(["index"],axis=1)
client_df.to_csv(f"ML_client.csv",index=False)
document_df = load_df("document")
document_df.to_csv(f"ML_document.csv",index=False)

def expandLineItems(d_row):
    t_df = pd.DataFrame(d_row.lineitems)
    cols = t_df.columns.to_list()
    t_df["document_number"] = d_row.document_number
    return t_df[["document_number"]+cols]

lineitem_df = expandLineItems(document_df.iloc[0,:]).iloc[0:0]
for i in range(len(document_df)):
    t_df = expandLineItems(document_df.iloc[i,:])
    lineitem_df = pd.concat([lineitem_df,t_df])
    print(f"{i+1}/{len(document_df)} done")

lineitem_df = lineitem_df.rename_axis('index').reset_index()  
lineitem_df.to_csv(f"ML_document_lineitem.csv",index=False)
