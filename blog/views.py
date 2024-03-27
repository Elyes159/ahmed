from django.shortcuts import render

from blog.models import CompteSnapchat
import requests
from django.http import JsonResponse


def recuperer_donnees_snapchat(request):
    access_token = "eyJpc3MiOiJodHRwczpcL1wvYWNjb3VudHMuc25hcGNoYXQuY29tXC9hY2NvdW50c1wvb2F1dGgyXC90b2tlbiIsInR5cCI6IkpXVCIsImVuYyI6IkExMjhDQkMtSFMyNTYiLCJhbGciOiJkaXIiLCJraWQiOiJhY2Nlc3MtdG9rZW4tYTEyOGNiYy1oczI1Ni4wIn0..5eM3-mPT0X9kNjdi0XWoFQ.qU_eciD9PLlT3by_DI4GBMO7m09FYhO81oGpDAK_PU_39hq5-A0Y7JfwksCkMeASsconCJyxDeZHF8Dn5fER-UOO8TlV-gFjipoysbQ_RpLjyVFR5upSWyz6lIuc2Afpz1CVxE6ASRDNXVFK2xCjfARpVtpKQ2QU5oJxqW4OnfGIzrA-54rXPXddvaRmMWrsoe-UuCyDhg6mM0TlB_KZfLW2ov-QNPOjMpsmjW1lfK-IhnRhHqGMcxoPoczpLk_hbn5sJ2dP9wV-F4Mn_4OqcnQTpkDO719u1ClT2TxH2eWk8wa76mJbiJjHsTT5E_6zN4F2_EU4vuRvZ8JgHkajHORh4bKAYBEVfplfavGyolUFKdBL4Y6WbMLOFIvXAA0FfqSTAnxIPwaXXxkbMUkeWKrd3FcUyo774eng6bvvO-FfHgXlhOmvjuStt_QOYhwv3mFL9Bmd4SoVdYL0WB_l0gauVBlS7lqd5hJXyTvGm40OWLsVdgQD_DTfLCLH4YX8H1U2apmXXFOa8zpOIIMSFLuo5T9eTACGyshBHMwCxDX7s1NDCtw8lLpiOeOcUIezDFs9xbHNI4Q0sVmSepiRXbnRmr7Hw8uao4nGJPkNmpn9z63NTannONvBeryXn7csau5gTf8HYOe5okIJpNUe6qVoR1IHvzK-9HpuftEcqs1YFm8FJj2aq08vU4Z1B6paVGsLVhwp9bmkWjxdlB27g_AZdcZvG2o79uwwEhNDrtvAdigB81XhzR5EJWxG12zL7gIsqDL45dPqGyVNJ7yWaF80OqnLHrTq_65Mia_B6zEKANly-17ti9n97CGVBwlS.u4EE0XxBtGeqGcjCCX-YYw"
    url = "https://businessapi.snapchat.com/v1/organizations/fc439f0e-ae54-463f-a876-1f0fde1a4d62/public_profiles"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        request_status = data.get("request_status")
        
        if request_status == "SUCCESS":
            print("Aucune donnée de compte Snapchat n'a été renvoyée.")
            return JsonResponse({"message": "Aucune donnée de compte Snapchat n'a été renvoyée."})
        else:
            print("La requête a réussi mais n'a pas renvoyé de données de compte Snapchat.")
            return JsonResponse({"error": "La requête a réussi mais n'a pas renvoyé de données de compte Snapchat."})
    else:
        print("La requête GET a échoué avec le code :", response.status_code)
        return JsonResponse({"error": "La requête GET a échoué", "status_code": response.status_code})

