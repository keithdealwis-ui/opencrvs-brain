---
title: "Event Observations"
source_url: "https://documentation.opencrvs.org/v1.6/technology/standards/fhir-documents/event-observations"
markdown_url: "https://documentation.opencrvs.org/v1.6/technology/standards/fhir-documents/event-observations.md"
version: "v1.6"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:3d7b906a433d258e53626f9e1ec081b0ccd3bb46292e496338d30523a9a00f77"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.6/technology/standards/fhir-documents/event-observations.md).

# Event Observations

### Requesting the FHIR Observations for a birth event

A number of other configurable and unidentifiable data points can be captured for the event lifecycle, such as; who was present at the birth, what was the birth weight etc. For this kind of data, we use [FHIR Observations](https://www.hl7.org/fhir/observation.html).

#### **URL**

To request all the [Observations](https://www.hl7.org/fhir/observation.html) associated with the event use the `birth-encounter` resource reference:

```
GET http://openhim-core:5001/fhir/Observation?encounter=Encounter/af7be33b-3e0c-4012-b894-c32d4bcc5100
```

#### **Request headers**

```
Content-Type: application/json
Authorization: Bearer <token>
```

#### **Observations payload**

Multiple FHIR Resources are returned in a [FHIR Bundle](https://www.hl7.org/fhir/bundle.html) containing an `entry` array.

```
{
  "resourceType": "Bundle",
  "id": "e4fad8cb-12b6-4deb-be72-cc8075c0692e",
  "meta": { "lastUpdated": "2020-07-04T10:56:50.398+00:00" },
  "type": "searchset",
  "total": 4,
  "link": [
    {
      "relation": "self",
      "url": "http://localhost:3447/fhir/Observation?encounter=Encounter/af7be33b-3e0c-4012-b894-c32d4bcc5100"
    }
  ],
  "entry": [
    {
      "fullUrl": "http://localhost:3447/fhir/Observation/fdbaa049-8da6-44b2-9780-e02ed70b3e73/_history/4db373f9-9b50-4c95-bfdf-f0009ef89bb5",
      "resource": {
        "resourceType": "Observation",
        "status": "final",
        "context": {
          "reference": "Encounter/af7be33b-3e0c-4012-b894-c32d4bcc5100"
        },
        "category": [
          {
            "coding": [
              {
                "system": "http://hl7.org/fhir/observation-category",
                "code": "procedure",
                "display": "Procedure"
              }
            ]
          }
        ],
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "73764-3",
              "display": "Birth attendant title"
            }
          ]
        },
        "id": "fdbaa049-8da6-44b2-9780-e02ed70b3e73",
        "valueString": "PHYSICIAN",
        "meta": {
          "lastUpdated": "2020-07-04T10:15:03.246+00:00",
          "versionId": "4db373f9-9b50-4c95-bfdf-f0009ef89bb5"
        }
      },
      "request": {
        "method": "PUT",
        "url": "Observation/fdbaa049-8da6-44b2-9780-e02ed70b3e73"
      }
    },
    {
      "fullUrl": "http://localhost:3447/fhir/Observation/fc2f1c18-cfee-44ec-bbb6-d3d1463a950c/_history/6e8b6116-c411-478a-a07b-24d67eefbef4",
      "resource": {
        "resourceType": "Observation",
        "status": "final",
        "context": {
          "reference": "Encounter/af7be33b-3e0c-4012-b894-c32d4bcc5100"
        },
        "category": [
          {
            "coding": [
              {
                "system": "http://hl7.org/fhir/observation-category",
                "code": "vital-signs",
                "display": "Vital Signs"
              }
            ]
          }
        ],
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "3141-9",
              "display": "Body weight Measured"
            }
          ]
        },
        "id": "fc2f1c18-cfee-44ec-bbb6-d3d1463a950c",
        "valueQuantity": {
          "value": 1.5,
          "unit": "kg",
          "system": "http://unitsofmeasure.org",
          "code": "kg"
        },
        "meta": {
          "lastUpdated": "2020-07-04T10:15:03.250+00:00",
          "versionId": "6e8b6116-c411-478a-a07b-24d67eefbef4"
        }
      },
      "request": {
        "method": "PUT",
        "url": "Observation/fc2f1c18-cfee-44ec-bbb6-d3d1463a950c"
      }
    },
    {
      "fullUrl": "http://localhost:3447/fhir/Observation/3f7bce83-2993-4741-a436-7b99035ab427/_history/87767bc5-d70a-415b-9435-0f744a1de592",
      "resource": {
        "resourceType": "Observation",
        "status": "final",
        "context": {
          "reference": "Encounter/af7be33b-3e0c-4012-b894-c32d4bcc5100"
        },
        "category": [
          {
            "coding": [
              {
                "system": "http://hl7.org/fhir/observation-category",
                "code": "procedure",
                "display": "Procedure"
              }
            ]
          }
        ],
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "57722-1",
              "display": "Birth plurality of Pregnancy"
            }
          ]
        },
        "id": "3f7bce83-2993-4741-a436-7b99035ab427",
        "valueQuantity": { "value": "SINGLE" },
        "meta": {
          "lastUpdated": "2020-07-04T10:15:03.254+00:00",
          "versionId": "87767bc5-d70a-415b-9435-0f744a1de592"
        }
      },
      "request": {
        "method": "PUT",
        "url": "Observation/3f7bce83-2993-4741-a436-7b99035ab427"
      }
    },
    {
      "fullUrl": "http://localhost:3447/fhir/Observation/3d4abe32-d7dc-42c8-93ab-54186a68088a/_history/47ac808e-3cde-4b80-9b5b-71ad50f89ac3",
      "resource": {
        "resourceType": "Observation",
        "status": "final",
        "context": {
          "reference": "Encounter/af7be33b-3e0c-4012-b894-c32d4bcc5100"
        },
        "category": [
          {
            "coding": [
              {
                "system": "http://hl7.org/fhir/observation-category",
                "code": "procedure",
                "display": "Procedure"
              }
            ]
          }
        ],
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "present-at-birth-reg",
              "display": "Present at birth registration"
            }
          ]
        },
        "id": "3d4abe32-d7dc-42c8-93ab-54186a68088a",
        "valueString": "BOTH_PARENTS",
        "meta": {
          "lastUpdated": "2020-07-04T10:15:03.257+00:00",
          "versionId": "47ac808e-3cde-4b80-9b5b-71ad50f89ac3"
        }
      },
      "request": {
        "method": "PUT",
        "url": "Observation/3d4abe32-d7dc-42c8-93ab-54186a68088a"
      }
    }
  ]
}
```

###


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.6/technology/standards/fhir-documents/event-observations.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
