from abc import ABC , abstractmethod
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
class CommonView(ABC):
    @abstractmethod
    def handle(self , request , HttpRequest):
        pass

    