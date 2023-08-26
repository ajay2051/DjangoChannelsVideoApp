import random
import time
import json
import string


from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
from django.views.decorators.csrf import csrf_exempt

from .models import RoomMember

# Create your views here.


def get_token(request):
    appId = "ea2d3e7cff1840c6b1ccfeedfb77cf3d"
    appCertificate = "e7a6e8f300a4457b92c4c01a8286675c"
    channelName = request.GET.get("channel")
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = expirationTimeInSeconds + currentTimeStamp
    role = 1
    token = RtcTokenBuilder.buildTokenWithUid(
        appId, appCertificate, channelName, uid, role, privilegeExpiredTs
    )
    return JsonResponse({"token": token, "uid": uid}, safe=False)


def lobby(request):
    return render(request, "videochat/lobby.html")


def room(request):
    return render(request, "videochat/room.html")


@csrf_exempt
def createUser(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data["name"], uid=data["UID"], room_name=data["room_name"]
    )
    return JsonResponse(
        {"name": data["name"], "uid": data["UID"], "room_name": data["room_name"]},
        safe=False,
    )


def getMember(request):
    uid = request.GET.get("UID")
    room_name = request.GET.get("room_name")
    member = RoomMember.objects.get(uid=uid, room_name=room_name)
    return JsonResponse({"name": member.name}, safe=False)


@csrf_exempt
def deleteMember(request):
    """Delete User From Database After Leaving Chat"""
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data["name"], uid=data["UID"], room_name=data["room_name"]
    )
    member.delete()
    return JsonResponse({"Member Deleted"})


def generateUniqueCode(request):
    """Generates Unique Code to initiate video call"""
    code = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return JsonResponse({"Code":code})
    

