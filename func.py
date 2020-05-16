import io
import json
import logging
import requests
from fdk import response


def handler(ctx, data: io.BytesIO = None):
    # name = "World"
    try:
        body = json.loads(data.getvalue())
        deviceToken = body.get("name")
        serverToken = "AAAAOSxh1Ys:APA91bE1Q4hdRXG7KKXvMmdiMSb1aM5CbJS2Fw3RG9-yTrCjs8ta7JbCg_Gf55YzJkkFrABg53NezTNko0CXaqW2oVvOJEyF2DE7zUoCwm2KubTp6mFJjHRbgoPNxG4pvNruFEn_y0iC"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "key=" + serverToken,
        }
        to_body = {
            "notification": {
                "title": "Corona alert",
                "body": "Hi you have possibility of contacting someone who has corona",
            },
            "to": deviceToken,
            "priority": "high",
            #   'data': dataPayLoad,
        }
        response = requests.post(
            "https://fcm.googleapis.com/fcm/send",
            headers=headers,
            data=json.dumps(body),
        )

    except (Exception, ValueError) as ex:
        logging.getLogger().info("error parsing json payload: " + str(ex))

    logging.getLogger().info("Inside Python Hello World function")
    return response.Response(
        ctx,
        response_data=json.dumps({"message": "Successful"}),
        headers={"Content-Type": "application/json"},
    )
