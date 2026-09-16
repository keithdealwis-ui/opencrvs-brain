---
title: "Performance tests"
source_url: "https://documentation.opencrvs.org/v1.6/technology/architecture/performance-tests"
markdown_url: "https://documentation.opencrvs.org/v1.6/technology/architecture/performance-tests.md"
version: "v1.6"
retrieved_at: "2026-09-16T15:06:42Z"
content_hash: "sha256:f6b9c06a8f82cfe641b4799aa5fdbdeac29b79fe118c92a2e26cf77e60915efc"
---

> For the complete documentation index, see [llms.txt](https://documentation.opencrvs.org/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://documentation.opencrvs.org/v1.6/technology/architecture/performance-tests.md).

# Performance tests

Overview of results from performance tests conducted on OpenCRVS

OpenCRVS has been tested to ensure its performance and stability in a country that represents the upper-end of possible concurrent users and the number of birth declarations per year. Birth declaration submission was chosen as the focus of the performance tests because it is the most resource intensive operation of the software from the perspective of processing and storing data.&#x20;

The test, controlled by a performance testing framework [k6](https://k6.io/) by Grafana Labs, creates automated requests to the backend interface mimicking the actual birth declaration submission. A configured target value determines the number of requests per minute. The number of concurrent requests (Virtual Users) is dynamic and fluctuates based on request response times. New virtual users are added to meet the demand when the framework detects that the current target rate can not be reached with the current response times.

The target request rates were the following:

* 40 birth declarations per minute. Ran for 2 minutes.
* 60 birth declarations per minute. Ran for 2 minutes.
* 100 birth declarations per minute. Ran for 2 minutes.
* 150 birth declarations per minute. Ran for 2 minutes.
* 200 birth declarations per minute. Ran for 4 minutes.

The target rates were chosen based on a large reference country, Nigeria, where approximately seven million children are born every year. Based on this figure and the number of work days per year (250), we concluded that the approximate rate required for new birth declarations per minute is 60.

The infrastructure chosen for the test represents the recommended minimum server setup for the product. Our test setup includes three virtual private servers hosted on Digital Ocean with the following specification:

* 8 GB Memory
* 4 Intel vCPUs
* 160 GB Disk
* Ubuntu 20.04 (LTS) x64

The system achieved a request rate of 4 requests per second with minimal noticeable impact on response times, which is approximately four times the load required to support a country the size of Nigeria (population 206M).

**OpenCRVS v1.2.\* Test results**

The test was configured to run up to 15 VUs for 12 minutes 30 seconds. A total of 1 104 requests were made with a max throughput of 3.5 reqs/s.

The average response time of the system being tested was 1 894 ms and 1 104 requests were made at an average request rate of 2 requests per second.

The test had 2 different checks that were evaluated a total of 2 210 times, of which 2 failed. Overall the success rate was 99.91%.

The maximum response time was 4 779 ms at 13 VUs. The average response time at the same point in time was 3 651 ms, with 95% of requests taking less than 4 497 ms.

The test had an overall average request rate of 1.5 reqs/s peaking at 3.5 reqs/s while running 12 VUs.

The amount of data sent peaked at 13 VUs, sending 4 KB/s of data. Data received had its peak at 11 VUs with 2.39 KB/s being received.

There were requests to 3 unique URLs, with 1 104 different responses received. The slowest response had an average response time of 1 897 ms.

<figure><img src="https://content.gitbook.com/content/YTKQAa9NKqMdS5tq1TB3/blobs/AGRSbI7mFQZbREtpmZog/k6results.png" alt=""><figcaption></figcaption></figure>

**OpenCRVS v1.1.\* Test results**

1267 request were made in total, with no errors encountered during the test. With the highest request rate target of 200, the 95 percentile response time was 3.5 seconds, with an average request rate of 2.8 requests per second. During this target, an average of 12 requests were made concurrently.

![](https://content.gitbook.com/content/YTKQAa9NKqMdS5tq1TB3/blobs/cHuzYFF6fDtqxSI26lnL/Screenshot%202022-06-27%20at%2014.39.06.png)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://documentation.opencrvs.org/v1.6/technology/architecture/performance-tests.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
