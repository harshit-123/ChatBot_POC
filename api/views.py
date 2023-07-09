from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import CustomTrainModelSerializer, CustomTrainSerializer, CustomTrainDBSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework import generics
from core.models import UploadPDF
from api.models import TrainModel
import os
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI 
from django.conf import settings
# db
import mysql.connector as sql
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor

os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

max_input_size = 4096
num_outputs = 512
max_chunk_overlap = 20
chunk_size_limit = 600
directory_path = 'media/pdf'

# Create your views here.
def chatInterface(request):
    return render(request, 'chatInterface.html')


def chatInterfaceDB(request):
    return render(request, 'dbchatbot.html')


class trainModelDB(APIView):
    def post(self, request, format=None):
        seriallizer = CustomTrainDBSerializer(data = request.data)
        print("djkasjdkasjda==>", request.data)
        if seriallizer.is_valid():
            return self.train_model_db(seriallizer, request.data['input_text'])
        return Response(seriallizer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def train_model_db(self, serializer, input_text):
        serializer.save()
        # Connect to the database and execute the SQL script
        conn = sqlite3.connect('bikestrorenew.db')
        with open('./bikestrore_newdb.sql', 'r',encoding='cp1252', errors='replace') as f:
            sql_script = f.read()
        conn.executescript(sql_script)
        conn.close()

        # Create the agent executor
        db = SQLDatabase.from_uri("sqlite:///./bikestrorenew.db")
        toolkit = SQLDatabaseToolkit(db=db)
        agent_executor = create_sql_agent(
            llm=OpenAI(temperature=0),
            toolkit=toolkit,
            verbose=True
        )
        query = input_text
        # Run the query using the agent executor
        result = agent_executor.run(query)
        return Response({"input_text": query, "response": result}, status=status.HTTP_200_OK)


class CustomTrainModel(APIView):
    def post(self, request, format=None):
        """
        Handles the creation of a new user.
        Expects a POST request with user data in the request body.
        """
        try:
            seriallizer = CustomTrainSerializer(data = request.data)
            print("djkasjdkasjda==>", request.data)
            if seriallizer.is_valid():
                return self.train_model(seriallizer, request.data['input_text'])
            return Response(seriallizer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message": "Something Went Wrong"}, status=status.HTTP_400_BAD_REQUEST)
    
    def train_model(self, serializer, input_text):
        serializer.save()
        prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
        llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))
        documents = SimpleDirectoryReader(directory_path).load_data()
        index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
        index.save_to_disk('index.json')
        index = GPTSimpleVectorIndex.load_from_disk('index.json')
        response = index.query(input_text, response_mode="compact")
        return Response({"input_text": input_text, "response": response.response}, status=status.HTTP_200_OK)

    def trainModel(self, path):
        os.environ["OPENAI_API_KEY"] = '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'
        self.construct_index(path)

    def construct_index(self, directory_path):
        max_input_size = 4096
        num_outputs = 512
        max_chunk_overlap = 20
        chunk_size_limit = 600
        prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

        llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

        documents = SimpleDirectoryReader(directory_path).load_data()

        index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

        index.save_to_disk('index.json')

        print("index==>", index)
        self.chatbot("how many projects i have done it now?")
        return index
    
    def chatbot(self, input_text):
        print("input_text==>", input_text)
        index = GPTSimpleVectorIndex.load_from_disk('index.json')
        response = index.query(input_text, response_mode="compact")
        print("response===>", response.response)
        return response.response


class PDFFileUploadView(generics.CreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset = UploadPDF.objects.all()
    serializer_class = CustomTrainModelSerializer

