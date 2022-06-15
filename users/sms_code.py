import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sms.v20210111 import sms_client, models
def send_message(mobile,code):
    try:
        SecretId = "AKIDpX4SeecVDn8G9nCMGvKVR8amiSxCE1cz"
        SecretKey = "A8sMbaMtBDzWmna8TcXDiyzlIZaMs89w"
        cred = credential.Credential(SecretId, SecretKey)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "sms.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = sms_client.SmsClient(cred, "ap-guangzhou", clientProfile)

        req = models.SendSmsRequest()
        params = {
            "PhoneNumberSet": [ mobile ],
            # "PhoneNumberSet": [ "+8615707514490" ],
            "SmsSdkAppId": "1400639080",
            "SignName": "Challengdeep",
            "TemplateId": "1413727",
            "TemplateParamSet": [ code, "5" ]
        }
        req.from_json_string(json.dumps(params))

        resp = client.SendSms(req)
        # print(resp.to_json_string())
        return resp.to_json_string(),True

    except TencentCloudSDKException as err:
        print(err)
        return err,False
if __name__ == '__main__':
    mobile, code = ("+86157075144901","11")
    data,coden = send_message(mobile, code)
    print(coden)