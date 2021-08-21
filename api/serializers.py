from rest_framework import serializers
from .models import Metar

class MetarSerializer(serializers.ModelSerializer):
    last_observation = serializers.SerializerMethodField(read_only=True)
    wind = serializers.SerializerMethodField(read_only=True)
    temperature = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Metar
        fields = ["station","last_observation","temperature","wind"]
    
    def get_last_observation(self,obj):
        """Convert UTC to GTM+6"""
        last_created = str(obj.last_observation)
        gmt_time = int(last_created[11:13])+6
        last_observation = last_created[:10]+" at "+str(gmt_time)+last_created[13:19]+ " GMT"
        return last_observation

    def get_wind(self,obj):
        windData = obj.wind

        if(len(windData) ==7):
            windMessage = "Wind direction is "+windData[0:3]+", velocity is "+windData[3:5]+" knots"
        elif (len(windData)>7 and windData.find("G")== -1):
            windMessage = "Wind direction is "+windData[0:4]+", velocity is "+windData[4:6]+" knots"
        else:
            windMessage = "Wind is blowing from "+windData[0:3]+" velocity is "+windData[3:5]+" knots with "+windData[6:8]+"-knot gusts"
        
        wind = windMessage
        return wind

    def get_temperature(self,obj):
        temp = obj.temperature

        if(temp[0]=="M"):
            tempValue = int(temp[1:3])
            cToF = -(tempValue*(9/5))+32
            tempMessage = "-"+str(tempValue)+"C "+"( "+str(cToF)+"F )"
        else:
            tempValue = int(temp[0:2])
            cToF = int((tempValue*(9/5))+32)
            tempMessage = str(tempValue)+"C "+"( "+str(cToF)+"F )"

        temperature = tempMessage
        return temperature