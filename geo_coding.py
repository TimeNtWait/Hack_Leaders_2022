import geocoder
API_KEY_tomtom = "CEJC7uEFOsHPWyIJ8bLt6QkTGGDyEIVG"
API_KEY_here = "jjsxVCLxh6Qw9OgZqJvWcUqDnetjN6DrNRkez-dR5P8"  #Leaders2022
# g = geocoder.tomtom('аллея. Долгопрудная, д. 1, к. 71, Москва', key=API_KEY_tomtom)
# print(g.json)
# g = geocoder.here('аллея. Долгопрудная, д. 1, к. 71, Москва', app_code="jjsxVCLxh6Qw9OgZqJvWcUqDnetjN6DrNRkez-dR5P8", app_id="6bJcIX7zqUyA7B0VuX0O")
# print(g.json)

# g = geocoder.osm('New York city')
# g = geocoder.osm('Москва, Ленинградский проспект 72', key="pk.e3708a8348ad1254ff06a6389c33b093")
g = geocoder.osm('п.Первомайское д Жуковка д 7 75/100, Москва', key="pk.e3708a8348ad1254ff06a6389c33b093")
print(g.json)

#
# import requests
# import json
# import time
# import zipfile
# import io
# from bs4 import BeautifulSoup
#
#
# # Org ID: org980004931 Roles: Org admin Email: time.nt.wait@gmail.com
# # User ID: HERE-817caa0b-042b-4628-9eb5-3b3a95b2a083
# API_KEY = "jjsxVCLxh6Qw9OgZqJvWcUqDnetjN6DrNRkez-dR5P8"  #Leaders2022
# # org980004931
# class BatchGEOCoding:
#
#     SERVICE_URL = "https://batch.geocoder.ls.hereapi.com/6.2/jobs"
#     jobId = None
#
#     def __init__(self, apikey):
#         self.apikey = apikey
#
#     def start(self, filename, indelim=";", outdelim=";"):
#         file = open(filename, 'rb')
#
#         params = {
#             "action": "run",
#             "apiKey": self.apikey,
#             "politicalview": "RUS",
#             "gen": 9,
#             "maxresults": "1",
#             "header": "true",
#             "indelim": indelim,
#             "outdelim": outdelim,
#             "outcols": "displayLatitude,displayLongitude,locationLabel,houseNumber,street,district,city,postalCode,county,state,country",
#             "outputcombined": "true",
#         }
#
#         response = requests.post(self.SERVICE_URL, params=params, data=file)
#         self.__stats(response)
#         file.close()
#
#     def status(self, jobId=None):
#
#         if jobId is not None:
#             self.jobId = jobId
#         print(jobId)
#         statusUrl = self.SERVICE_URL + "/" + self.jobId
#
#         params = {
#             "action": "status",
#             "apiKey": self.apikey,
#         }
#
#         response = requests.get(statusUrl, params=params)
#         self.__stats(response)
#
#
#     def create_file(self, src_filename, target_filename=None):
#         if not target_filename:
#             name_filename, ext_filename = src_filename.split(".")
#             print(name_filename, ext_filename)
#             target_filename = f"{name_filename}_.{ext_filename}"
#         print(target_filename)
#         # recId;searchText
#
#     def result(self, jobId=None):
#
#         if jobId is not None:
#             self.jobId = jobId
#
#         print("Requesting result data ...")
#
#         resultUrl = self.SERVICE_URL + "/" + self.jobId + "/result"
#
#         params = {
#             "apiKey": self.apikey
#         }
#
#         response = requests.get(resultUrl, params=params, stream=True)
#
#         if (response.ok):
#             zipResult = zipfile.ZipFile(io.BytesIO(response.content))
#             zipResult.extractall()
#             print("File saved successfully")
#
#         else:
#             print("Error")
#             print(response.text)
#
#     def __stats(self, response):
#         print(response.text)
#         print(response.ok)
#         print(response.content)
#         if (response.ok):
#             parsedXMLResponse = BeautifulSoup(response.text, "lxml")
#             self.jobId = parsedXMLResponse.find('requestid').get_text()
#
#             for stat in parsedXMLResponse.find('response').findChildren():
#                 if (len(stat.findChildren()) == 0):
#                     print("{name}: {data}".format(name=stat.name, data=stat.get_text()))
#
#         else:
#             print(response.text)
#
# geo_batch = BatchGEOCoding(apikey=API_KEY)
# PATH = "datasets/"
# # geo_batch.create_file(PATH + "Реестр домов_v10.csv")
#
# test_file = "test_here_com.csv"
# geo_batch.start(filename = PATH+test_file, indelim=";", outdelim=";")
#
# geo_batch.result()
# # with open(filename, 'rb') as file:
# #     file
#
# print(1+2)
