import requests

def autocomplete_place(input_text, api_key):
    endpoint = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
    params = {
        "input": input_text,
        "key": api_key,
        "components": "country:FR"
    }
    print (params)
    try:
        response = requests.get(endpoint, params=params)
        data = response.json()
        
        print (data)
        if 'predictions' in data:
            predictions = [prediction['description'] for prediction in data['predictions']]
            return predictions
        else:
            print("Aucune prédiction trouvée.")
            return []
    
    except Exception as e:
        print("Une erreur s'est produite:", e)
        return []

if __name__ == "__main__":
    api_key = 'AIzaSyBPmOKr6x00xyj0wJV1xuOUwZslnPXyOaU'
    input_text = input("Entrez votre recherche : ")
    places = autocomplete_place(input_text, api_key)
    print (places)
    if places:
        print("Résultats de l'autocomplétion :")
        for place in places:
            print(place)
