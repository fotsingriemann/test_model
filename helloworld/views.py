from helloworld import settings
from statsmodels.tsa.arima.model import ARIMAResults # type: ignore
import mpu # type: ignore
import os
from django.http import HttpResponse, JsonResponse, Http404 # type: ignore
from openlocationcode import openlocationcode # type: ignore
import time


def Application(latitude, longitude):

    

#     test de la position 
    file_path = os.path.join(settings.BASE_DIR, 'static', 'model')


    pluscodes = list(map(lambda x : x.split("_")[1],os.listdir(file_path)))
    
    resultat_final = {
        plus: [] for plus in pluscodes
    }

    
    for dirs, pluscode in zip(os.listdir(file_path),pluscodes) :
        resultat = {
            "distance" : 0.0,
            "distance_ref" : 0.0,
            "HPH" : 0.0,
            "CPB" : 0.0,
            "resultat" : 0.0
        }
        
        results_longitude = ARIMAResults.load(f'{file_path}/{dirs}/{"longitude"}')
        results_latitude = ARIMAResults.load(f'{file_path}/{dirs}/{"latitude"}')
        results_heure_parking = ARIMAResults.load(f'{file_path}/{dirs}/{"heure_de_parking"}')
        
        latitude_given_by_model = results_latitude.forecast()
        longitude_given_by_model = results_longitude.forecast()
        heure_given_by_model = results_heure_parking.forecast()

        print(latitude_given_by_model)

        current_time = time.localtime()
        formatted_time = time.strftime("%H", current_time)

        # if( abs(int(formatted_time) - heure_given_by_model[0]) == 0 ): #packet ignition on
        reference = openlocationcode.decode(openlocationcode.encode(latitude_given_by_model[0], longitude_given_by_model[0], 8))

        distance_ref = mpu.haversine_distance((reference.latitudeCenter, reference.longitudeCenter), (reference.latitudeLo, reference.longitudeLo)) * 100
        distance = mpu.haversine_distance((latitude_given_by_model[0], longitude_given_by_model[0]), (latitude, longitude))
        
        if( abs(int(formatted_time) - heure_given_by_model[0]) <= 100 ):
            if(distance <= distance_ref ) :
                resultat.update({
                    "distance" :distance,
                    "distance_ref" : distance_ref,
                "HPH": heure_given_by_model[0],
                "CPB": abs(int(formatted_time) - heure_given_by_model[0]),
                "resultat": "Vous etes au environ de chez vous au environ de votre heure habituel de parking Merci de votre discipline"
                
                })
                

            else:

                resultat.update({
                    "distance" :distance,
                    "distance_ref" : distance_ref,
                "HPH": heure_given_by_model[0],
                "CPB": abs(int(formatted_time) - heure_given_by_model[0]),
                "resultat": "Vous etes loin de votre zone de parking habituel a cette heure, vous risquer donc de ne pas parker a temps. Y a t-il un probleme ?"
                
                })
            resultat_final[pluscode] = resultat
        

    return resultat_final
            
         
    
        

def model_testing(request, latitude, longitude):
    if request.method == 'GET':
        # Convertir les paramètres capturés en float
        latitude = float(latitude)
        longitude = float(longitude)

        result = Application(latitude, longitude)

        return JsonResponse(result, status=500, safe=False)
