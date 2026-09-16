---
title: "Record Search clients"
source_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/apis-requiring-oauth-credentials/record-search-clients"
markdown_url: "https://documentation.opencrvs.org/v1.9/technology/interoperability/apis-requiring-oauth-credentials/record-search-clients.md"
version: "v1.9"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:42dc418694afe7cf3074309c746d1e0e38c87d0dedae1923617891303e2230fb"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.9/technology/interoperability/apis-requiring-oauth-credentials/record-search-clients.md).

# Record Search clients

Perform an advanced search of civil registration records from a trusted, external e-Gov service

The Record Search client can perform an advanced search of civil registration records. Use this to help support social protection systems, check the existence of civil registration records or check citizen demographics.

<figure><img src="https://3485090019-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRziAMaeBMeyiTg5hfFq5%2Fuploads%2Fgit-blob-cc2b3c00e48904f6ad6edc9366c6b85b238fc3de%2FScreenshot%202023-01-11%20at%2017.17.45.png?alt=media" alt=""><figcaption></figcaption></figure>

To stop abuse of such a powerful API, all results returned are audited as having been downloaded by the client. System Administrators should be careful to ensure that citizen data is not exposed to untrustworthy individuals by using this API.

{% hint style="danger" %}
All client behaviour is audited and is ultimately the personal responsibility of the National System Administrator of OpenCRVS that created the client. Protect citizen data and do not expose it unnecessarily as you may be in breach of local laws.
{% endhint %}

{% hint style="info" %}
A daily limit of 2000 Record Search requests per client, per day is hardcoded into OpenCRVS Core. Any subsequent requests will fail.
{% endhint %}

**Submitting a Record Search**

To submit an Record Search, your client must first request an [authorization token ](/v1.9/technology/interoperability/apis-requiring-oauth-credentials/authenticate-a-client.md)using your `client_id` and `client_secret`.

#### Record Search Requests

With the token as an authorization header, the following example request will submit a record search. It utilises queries that are used buy the OpenCRVS GUI and an example integration using the [Digital Convergence Initiative](https://standards.spdci.org/standards/standards-for-interoperability-interfaces/common-standards-for-interoperability-interfaces/) standard [middleware](https://github.com/opencrvs/dci-crvs-api).

```


Content-Type: application/json
Authorization: Bearer {{token}}

// Example code from social protection system example middleware 
// https://github.com/opencrvs/dci-crvs-api

export const OPENCRVS_EVENTS_URL =
  process.env.OPENCRVS_EVENTS_URL ??
  new URL('events', OPENCRVS_GATEWAY_URL).toString()

const client = createClient(OPENCRVS_EVENTS_URL, `Bearer ${token}`)
  const searchQuery = buildSearchParameters(searchRequest.search_criteria, {
    pageSize,
    pageNumber
  })

  try {
    const { results, total } = await client.event.search.query(searchQuery)

    return {
      registrations: results,
      responseFinishedTimestamp: new Date(),
      originalRequest: searchRequest,
      pageNumber,
      pageSize,
      totalItems: total
    }
  } catch (e: any) {
    const status = e?.meta?.response?.status

    console.error('Error during search query:', e)

    if (status === 401) {
      throw new AuthorizationError('Invalid authorization token')
    }

    throw new ValidationError(
      `Search query failed: ${e.message || 'Unknown error'}`
    )
  }

function buildSearchParameters(
  criteria: SearchCriteria,
  { pageSize, pageNumber }: { pageSize: number; pageNumber: number }
): SearchQuery {
  const parameters = {
    limit: pageSize,
    offset: (pageNumber - 1) * pageSize,
    query: {},
    sort: criteria.sort?.map((sortItem) => ({
      field: sortItem.attribute_name,
      direction: sortItem.sort_order
    }))
  } satisfies SearchQuery

  if (isExpressionQuery(criteria)) {
    parameters.query = {
      type: 'and',
      clauses: [
        {
          eventType: criteria.reg_event_type,
          status: { type: 'exact', term: 'REGISTERED' },
          ...criteria.query.value.expression.query
        }
      ]
    }
  }

  if (isRegistrationNumberQuery(criteria)) {
    parameters.query = {
      type: 'and',
      clauses: [
        {
          eventType: criteria.reg_event_type,
          status: { type: 'exact', term: 'REGISTERED' },
          'legalStatuses.REGISTERED.registrationNumber': {
            type: 'exact',
            term: criteria.query.value
          }
        }
      ]
    }
  }

  if (isNationalIdQuery(criteria)) {
    const nidField =
      criteria.reg_event_type === 'birth' ? 'child.nid' : 'deceased.nid'
    parameters.query = {
      type: 'and',
      clauses: [
        {
          eventType: criteria.reg_event_type,
          status: { type: 'exact', term: 'REGISTERED' },
          data: {
            [nidField]: {
              type: 'exact',
              term: criteria.query.value
            }
          }
        }
      ]
    }
  }

  if (isPredicateQuery(criteria)) {
    const clauses: Array<Record<string, any>> = []
    for (const item of criteria.query) {
      clauses.push(mapPredicateExpression(item.expression1))
      if (item.expression2 !== undefined) {
        clauses.push(mapPredicateExpression(item.expression2))
      }
    }
    parameters.query = {
      type: 'and',
      clauses: [
        {
          eventType: criteria.reg_event_type,
          status: 'REGISTERED',
          ...Object.assign({}, ...clauses)
        }
      ]
    }
  }

  return parameters
}
```

We recommend that you use the Advanced Search feature in the OpenCRVS application and monitor the payload that is sent to the Gateway using the Chrome Developer Tools "Network" tab, in order to understand how these parameters are formatted. The table below lists all possible parameters with a description and example where we feel further explanation is helpful.

#### Record Search Results

After a search has completed and if you search for any record returned, you will see that in Record Audit, an entry shows that this client has accessed the personally identifiable citizen data on the record.

<figure><img src="https://3485090019-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRziAMaeBMeyiTg5hfFq5%2Fuploads%2Fgit-blob-47ed83856d11cdcfd1ebeb2f7327f45726c5c600%2FScreenshot%202023-01-16%20at%2011.49.25.png?alt=media" alt=""><figcaption></figcaption></figure>

```
{
  "results": [
    {
      "id": "00000000-0000-0000-0000-000000000000",
      "type": "string",
      "status": "CREATED",
      "legalStatuses": {
        "DECLARED": {
          "createdAt": "0029-03-30T21:00Z",
          "createdBy": "string",
          "createdAtLocation": "00000000-0000-0000-0000-000000000000",
          "createdByUserType": "user",
          "acceptedAt": "4967-02-21T23:32:46Z",
          "createdByRole": "string",
          "createdBySignature": "string"
        },
        "REGISTERED": {
          "createdAt": "4115-02-22T10:01:56Z",
          "createdBy": "string",
          "createdAtLocation": "a2CC06AF-1ed0-16f3-a2Ff-ffD071b5a0fb",
          "createdByUserType": "user",
          "acceptedAt": "1356-11-05T23:31Z",
          "createdByRole": "string",
          "createdBySignature": "string",
          "registrationNumber": "string"
        }
      },
      "createdAt": "2397-11-30T23:52:10.0541149825157802403912327647707242224719807421894381681357562151736869882654670Z",
      "dateOfEvent": "9600-02-29",
      "placeOfEvent": "ffffffff-ffff-ffff-ffff-ffffffffffff",
      "createdBy": "string",
      "createdByUserType": "user",
      "updatedByUserRole": "string",
      "createdAtLocation": "00000000-0000-0000-0000-000000000000",
      "createdBySignature": "string",
      "updatedAtLocation": "ffffffff-ffff-ffff-ffff-ffffffffffff",
      "updatedAt": "6072-02-29T23:09:36Z",
      "assignedTo": "string",
      "updatedBy": "string",
      "trackingId": "string",
      "potentialDuplicates": [
        {
          "id": "ffffffff-ffff-ffff-ffff-ffffffffffff",
          "trackingId": "string"
        }
      ],
      "flags": [
        "print_certificate:rejected",
        "string"
      ],
      "declaration": {
        "additionalProp1": [],
        "additionalProp2": [],
        "additionalProp3": []
      }
    }
  ],
  "total": 0
}
```

For full API details, refer to the [Swagger documentation](https://api.opencrvs.org/develop/events/).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.9/technology/interoperability/apis-requiring-oauth-credentials/record-search-clients.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
