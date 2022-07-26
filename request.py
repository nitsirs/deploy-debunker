import requests
import json
url = 'http://127.0.0.1:5000/webhook'
data = {
  "responseId": "response-id",
  "session": "projects/project-id/agent/sessions/session-id",
  "queryResult": {
    "queryText": "คนขับเกียร์ออโต้ขอเวลาอ่านสัก 5 นาที เพื่อชีวิตและความปลอดภัยบนท้องถนน",
    "parameters": {
      "param-name": "param-value"
    },
    "allRequiredParamsPresent": "true",
    "fulfillmentText": "Response configured for matched intent",
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            "Response configured for matched intent"
          ]
        }
      }
    ],
    "outputContexts": [
      {
        "name": "projects/project-id/agent/sessions/session-id/contexts/context-name",
        "lifespanCount": 5,
        "parameters": {
          "param-name": "param-value"
        }
      }
    ],
    "intent": {
      "name": "projects/project-id/agent/intents/intent-id",
      "displayName": "matched-intent-name"
    },
    "intentDetectionConfidence": 1,
    "diagnosticInfo": {},
    "languageCode": "en"
  },
  "originalDetectIntentRequest": {}
}

x = requests.post(url, data = json.dumps(data))

print(x.text)