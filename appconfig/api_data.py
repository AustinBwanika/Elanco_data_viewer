import requests
from datetime import datetime
ENDPOINT = "https://engineering-task.elancoapps.com/api"
from django.core.cache import cache

class ApiData:
    def __init__(self):
        self.data = []
        self.applications = []
        self.resources = []

    def get_data(self):

        cache_key = "api_data_raw"
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data

        try:
            response = requests.get(url=f"{ENDPOINT}/raw")
            response.raise_for_status()
            results = response.json()
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON from response.")
            return {"api_data": []}
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return {"api_data": []}

        for result in results:
            self.data.append( {
                "ConsumedQuantity": result["ConsumedQuantity"],
                "Cost": (result["Cost"]),
                "Date": datetime.strptime(result["Date"], "%d/%m/%Y").date(),
                "InstanceId": result["InstanceId"],
                "MeterCategory": result["MeterCategory"],
                "ResourceGroup": result["ResourceGroup"],
                "ResourceLocation": result["ResourceLocation"],
                "Tags": result["Tags"],
                "UnitOfMeasure": result["UnitOfMeasure"],
                "Location": result["Location"],
                "ServiceName": result["ServiceName"],
            })

            cache.set(cache_key,self.data,timeout=3600)

        print(self.data[0])
        return self.data

    def get_application_list(self):
        response = requests.get(url=f"{ENDPOINT}/applications")
        results = response.json()
        response.raise_for_status()

        for result in results:
            self.applications.append(result)
        return self.applications

    def get_specifc_application(self, application):
        # list = []
        # response = requests.get(url=f"{ENDPOINT}/applications/{application}")
        # results = response.json()
        # response.raise_for_status()

        try:
            response = requests.get(url=f"{ENDPOINT}/applications/{application}")
            response.raise_for_status()
            print("Status Code:", response.status_code)
            print("Response Text:", response.text)
            results = response.json()
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON from response.")
            return {"api_data": []}
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return {"api_data": []}

        for result in results:
            list.append({
                "ConsumedQuantity": result["ConsumedQuantity"],
                "Cost": result["Cost"],
                "Date": result["Date"],
                "InstanceId": result["InstanceId"],
                "MeterCategory": result["MeterCategory"],
                "ResourceGroup": result["ResourceGroup"],
                "ResourceLocation": result["ResourceLocation"],
                "Tags": result["Tags"],
                "UnitOfMeasure": result["UnitOfMeasure"],
                "Location": result["Location"],
                "ServiceName": result["ServiceName"],
            })

        return list

    def get_resource_list(self):
        response = requests.get(url=f"{ENDPOINT}/resources")
        results = response.json()
        response.raise_for_status()

        for result in results:
            self.resources.append(result)
        return self.resources

    def get_specific_resource(self, resource):
        # list = []
        # response = requests.get(url=f"{ENDPOINT}/resources/{resource}")
        # results = response.json()
        # response.raise_for_status()

        try:
            response = requests.get(url=f"{ENDPOINT}/resources/{resource}")
            response.raise_for_status()
            print("Status Code:", response.status_code)
            print("Response Text:", response.text)
            results = response.json()
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON from response.")
            return {"api_data": []}
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return {"api_data": []}





        for result in results:
            list.append({
                "ConsumedQuantity": result["ConsumedQuantity"],
                "Cost": result["Cost"],
                "Date": result["Date"],
                "InstanceId": result["InstanceId"],
                "MeterCategory": result["MeterCategory"],
                "ResourceGroup": result["ResourceGroup"],
                "ResourceLocation": result["ResourceLocation"],
                "Tags": result["Tags"],
                "UnitOfMeasure": result["UnitOfMeasure"],
                "Location": result["Location"],
                "ServiceName": result["ServiceName"],
            })

        return list

    def costs_map(self):
        list_of_data = self.get_data()
        hash_list = []
        for index, j in enumerate(list_of_data):
            cost = float(j.get("Cost", 0))
            map = {"ID": index, "Cost": cost}
            hash_list.append(map)

        return hash_list

    def dates_map(self):
        list_of_data = self.get_data()
        hash_list = []
        for index, j in enumerate(list_of_data):
            map = {"ID": index, "Date": j["Date"]}
            hash_list.append(map)

        return hash_list

    def location_map(self):
        list_of_data = self.get_data()
        hash_list = {}
        for item in list_of_data:
            location = item["Location"].lower()
            resource_group = item["ResourceGroup"].lower()

            hash_list.setdefault(location, {})

            hash_list[location][resource_group] = hash_list[location].get(resource_group, 0) + 1

        return hash_list

    def consumption_per_day(self):
        list_of_data = self.get_data()
        # map = {"Day": "29/11/20", "Total_Consumption": 0}
        cache_key = 'api_data_consumption_per_day'
        consumption = cache.get(cache_key)
        if consumption is not None:
            return consumption
        hash_list = {}
        for item in list_of_data:
            date = item["Date"]
            consumed_quantity = item["ConsumedQuantity"]

            hash_list.setdefault(date.strftime("%Y-%m-%d"), 0)

            hash_list[date.strftime("%Y-%m-%d")] += float(consumed_quantity)


        hash_list = sorted(hash_list.items())
        cache.set(cache_key, hash_list, timeout=3600)
        return hash_list



# api = ApiData()
# api.get_data()





# print(results)

# print("\n\n\n")
# # Retireve all the applications from the API
#
# app_response = requests.get(url=f"{ENDPOINT}/applications")
# app_results = app_response.json()
# app_response.raise_for_status()
# # print(app_results)
#
# # Retreives all occurences of the application within the API
# application = input("Enter the application name: ").lower()
# name_response = requests.get(url=f"{ENDPOINT}/applications/{application}")
# name_results = name_response.json()
# name_response.raise_for_status()
# # print(name_results)
#
#
# # Gives a list of all the resources within the API
# resources_response = requests.get(url=f"{ENDPOINT}/resources")
# resources_results = resources_response.json()
# resources_response.raise_for_status()
# print(resources_results)
#
#
# # Gives a list of all occurence of the inputted resource within the API
# resource = input("Enter the resource name: ")
# resource_response = requests.get(url=f"{ENDPOINT}/resources/{resource}")
# resource_results = resource_response.json()[0]["Cost"]
# resource_response.raise_for_status()
# print(resource_results)