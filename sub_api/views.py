from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class SubjectApiView(APIView):
    def post(self,request):
        data = request.data
        print(data)
        highestEducation = data['highestEducation']
        if(highestEducation == '9' or highestEducation == '10'):
            return Response({
            'success':True,
            'result': {
                'subjectChooser' : "That's great!!! Please enter your favourite subject? [[EXT:BUTTON|Maths|Biology|Chemistry|Physics|Computer Science|Economics|English|Geography|History|Civics|Sports]]",
            },
            'resetList' : [],
            'errorMessageKey' : 'Error_Response'
        })
        elif(highestEducation == '11' or highestEducation == '12'):
            return Response({
            'success':True,
            'result': {
                'subjectChooser' : "That's great!!! Please enter your favourite subject? [[EXT:BUTTON|Maths|Biology|Chemistry|Physics|Computer Science|Economics|English|Geography|History|Civics|Sports]]",
                },
                'resetList' : [],
                'errorMessageKey' : 'Error_Response'
    })
