import pandas as pd
import json
from datetime import datetime

#leitura dos respectivos csv
def readCsvEnergy():
    df = pd.read_csv('./src/GeradoresDeEnergia.csv')
    return df
def readCsvUser():
    df = pd.read_csv('./src/UserMetrics.csv')
    return df
def readCsvLogin():
    df = pd.read_csv('./src/User.csv')
    return df

#Energia Get
def getAll(user_id):
    user_id = int(user_id)
    energy_data = readCsvEnergy()
    user_metrics = readCsvUser()

    user_energy_data = energy_data[energy_data['IdUser'] == user_id]
    if user_energy_data.empty:
        return {"error": "No energy data found for the user."}
    
    user_metrics_data = user_metrics[user_metrics['IdUser'] == user_id]
    if user_metrics_data.empty:
        return {"error": "No user metrics found for the user."}
    user_data = user_energy_data.to_dict(orient='records')
    user_metrics_data = user_metrics_data.to_dict(orient='records')

    response_data = []
    
    for energy_record in user_data:
        
        month = str(energy_record['CreateMonth'])
        

        user_meta_for_month = next((metric for metric in user_metrics_data if metric['Month'] == month), None)
        
        if user_meta_for_month:

            combined_record = {**energy_record, 'Meta': user_meta_for_month['Meta']}
        else:

            combined_record = {**energy_record, 'Meta': 0}
        
        response_data.append(combined_record)
    
    return response_data

#Transforma o json em formato selhante ao csv (data frame) para concatenar ambos
def jsonToDataframe(json_data):
    df = pd.DataFrame(json_data, index=[0])
    return df

#Energia Post
def updateDataframe(new_data):
    df = readCsvEnergy()
    dataNow = datetime.now().strftime('%Y-%m')
    new_data["CreateMonth"] = dataNow
    new_df = jsonToDataframe(new_data)

    existing_record = df[(df['IdUser'] == new_data['IdUser']) & (df['CreateMonth'] == new_data['CreateMonth'])]

    if existing_record.empty:
        df = pd.concat([df, new_df], ignore_index=True)
    else:
        for column in ['Produzido', 'Gasto', 'Armazenado', 'Distribuido']:
            df.loc[(df['IdUser'] == new_data['IdUser']) & (df['CreateMonth'] == new_data['CreateMonth']), column] += float(new_data[column])
    df.to_csv('./src/GeradoresDeEnergia.csv', index=False)
    return df

#Post Login
def login(json):
    df = readCsvLogin()

    existing_record = df[(df['Nome'] == json['Nome']) & (df['Senha'] == json['Senha'])]
    if existing_record.empty:
        return False
    else:
        user_id = existing_record['Id'].values[0]
        return user_id

#Meta Post
def createMeta(json_data):
    df = readCsvUser()

    user_id = json_data['IdUser']
    month = json_data['Month']
    meta = json_data['Meta']

    existing_record = df[(df['IdUser'] == user_id) & (df['Month'] == month)]

    if existing_record.empty:
        new_record = {
            'IdUser': user_id,
            'Meta': meta,
            'Month': month
        }
        new_df = pd.DataFrame([new_record])
        df = pd.concat([df, new_df], ignore_index=True)
        message = 'Meta criada com sucesso!'
    else:
        df.loc[(df['IdUser'] == user_id) & (df['Month'] == month), 'Meta'] = meta
        message = 'Meta atualizada com sucesso!'
    
    df.to_csv('./src/UserMetrics.csv', index=False)
    return message