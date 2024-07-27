 



# Elasticsearch

**Read, Update, Append data from or to Indices**

Elasticsearch is a search engine based on the Lucene library. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents.

CloudFabrix RDA provides out of the box integration for Elasticsearch through it's API interface. As part of the integration, it provides an ability to query the data from Elasticsearch indice(s), update or append the data into an Elasticsearch indice. Below Elasticsearch distributions are supported.

*   Elasticsearch Commercial & Open-source versions
*   Opendistro & Opensearch from AWS versions

**Elasticsearch Permissions:** Below permissions are required as a prerequisite.

*   read: To read, search/filter the data from indices
*   write: To create, update & append data into indices (optional)

## ****1\. Adding Elasticsearch as Datasource/Extension in RDA Studio:****

Elasticsearch or any other datasource/extension's configuration is configured in RDA's user interface. Login into RDA's user interface using a browser.

**https://\[rda-ip-address\]:9998**

Info

Default username and password of standalone **RDA Studio** is **rdademo** and **rdademo1234**

Under **Notebook**, click on **CFXDX Python 3** box ![Elasticsearch_RDA_Studio](https://bot-docs.cloudfabrix.io/images/rda_integrations/elasticsearch/elasticsearch_launcher2.png)

In the **Notebook** command box, type **botadmin()** and **alt (or option) + Enter** to open datasource administration menu.

Click on **Add** menu and under **Type** drop down, select **elasticsearch\_v2**

Note

Elasticsearch extension type **elasticsearch** is deprecated, please use **elasticsearch\_v2** instead.

![Elasticsearch_RDA_Datasource](https://bot-docs.cloudfabrix.io/images/rda_integrations/elasticsearch/elasticsearch_elasticsearchv2.png)

*   **Type**: Datasource/Extension type. In this context, it is **elasticsearch\_v2**
    
*   **name**: Datasource/Extension label which should be unique within the RDA
    
*   **Hostname**: Elasticsearch's IP Address or DNS name
    
*   **URL Prefix**: Use this option when Elasticsearch is behind a load balancer and it has additional path to the root (ex: /elasticsearch) - Optional
    
*   **Username**: Username that has read/write permissions to Elasticsearch indices (optional)
    
*   **Password**: User account's password (optional)
    
*   **HTTP(s) Port**: default is 9200, but can be changed to 443 or to other port
    
*   **Protocol**: API integration over HTTP/HTTPs protocol
    
*   **Timeout(seconds)**: HTTP response timeout in seconds, default value is 30 seconds
    

For the details on Elasticsearch (v2) inventory data collection bots, refer [CloudFabrix RDA Bot Documentation](https://bot-docs.cloudfabrix.io/Extensions/extensions_D_E/#extension-elasticsearch_v2 "CloudFabrix RDA Bot Documentation")

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!