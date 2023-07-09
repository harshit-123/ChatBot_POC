from django.urls import path
from api.views import CustomTrainModel, PDFFileUploadView, chatInterface, chatInterfaceDB, trainModelDB

urlpatterns = [
    path('trainModel/', CustomTrainModel.as_view(), name="Train_custom_model1"),
    path('trainModelDB/', trainModelDB.as_view(), name="trainModelDB"),
    path('postPdf/', PDFFileUploadView.as_view(), name="Train_custom_model"),
    path('chatInterface/', chatInterface, name="chatInterface"),
    path('chatInterfaceDB/', chatInterfaceDB, name="chatInterfaceDB"),
]