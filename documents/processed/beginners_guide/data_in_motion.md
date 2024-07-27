 



# Guide to Data In Motion in RDA Fabric

RDA Pipelines can exchange data even if they are running at different locations, as long as they all connected to same instance of RDA Fabric.

RDA Fabric uses [RDA Streams Using NATS](/Bots/rn/)
 for control path as well as as the default mechanism for data path. Any other streaming approach discussed in [section 3.2](#streaming_types)
 can also be used for data path. Multiple streaming approaches may be used at the same time.

* * *

## 1\. RDA Streams

*   Uses NATS Publish-Subscribe to move the data
*   Each Stream name is translated into a [NATS Subject](https://docs.nats.io/nats-concepts/subjects)
    .
*   Any Stream which is added to list of [Persistent Streams](#pstreams)
     it is automatically persisted in Opensearch.
*   Each subscriber can use a "group" parameter to identify consumer group. If multiple subscribers use same group name, only one of them will receive that specific batch of data.
*   Data can be routed to multiple subscribers by using a different group name for each of the subscribers.
*   Stream name `NULL` (case-insensitive), implies no data will be written or read from that stream.
*   RDA Streams do not have to be created in RDAF. First time a data is published or subscribed, streams come into existence.
*   List of RDA Streams used by RDA Fabric for it's own operations:

| Stream Name | Description |
| --- | --- |
| rda\_system\_feature\_usage | RDA Portal and Studio capture all usage metrics by feature.  <br>This report is accessible via left side menu **Analytics** |
| rda\_system\_deployment\_updates | Audit trail of changes to Service Blueprints |
| rda\_system\_gw\_endpoint\_metrics | RDA Event Gateway data ingestion metrics by ingestion endpoint |
| rda\_system\_worker\_trace\_summary | Pipeline execution statistics by Site, Bots etc. |
| rda\_worker\_resource\_usage | Resource usage metrics published by RDA Workers |
| rda\_system\_gw\_log\_archival\_updates | Log Archive metrics by RDA Event Gateway |
| rda\_system\_log\_replays | Audit trail of Log Archive replays |
| rda\_system\_worker\_traces | Detailed execution traces for each pipeline, published by RDA Workers |

All the above RDA Streams are also [Persistent Streams](#pstreams)

*   Example RDA [Service Map](#beginners_guide/#servicemap)
     showing data flow between pipelines using RDA Streams:

[![Servicemap](https://bot-docs.cloudfabrix.io/images/guide/servicemap.png)](/images/guide/servicemap.png)

**Related Bots**

*   [@rn:read-stream](/Bots/rn/#bot-rnread-stream)
    
*   [@rn:write-stream](/Bots/rn/#bot-rnwrite-stream)
    

**Related RDA Client CLI Commands**
```
     read-stream               Read messages from an RDA stream 
     read-stream-ack           Read messages from an RDA Stream with acknowledgements enabled 
     write-stream              Write data to the specified stream 
     write-stream-ack          Write data to the specified stream with acknowledgement enabled
 ```

## 2\. Bots to Manage Data Inflight

This section provides details about various bots to cleanup, re-shape, aggregate, enrich, mask, extract data as it progresses through the pipeline. RDA bots also can be used verify integrity of data to ensure it meets certain criteria.

### 2.1. Data Cleanup

Data cleanup means getting rid of unnecessary rows & columns, fixing the values, reformatting values on as needed basis.

Following are some of the bots that can be used for cleaning up of the data:

| Bot | Description |
| --- | --- |
| [@dm:dedup](/Bots/cfxdm/#bot-dmdedup) | Deduplicates data by using specified column values |
| [@dm:dropnull](/Bots/cfxdm/#bot-dmdropnul) | Drop rows if specified column have null values |
| [@dm:map](/Bots/cfxdm/#bot-dmmap) | Map values from one column to another, using optional mapping function and arguments |
| [@dm:map-multi-proc](/Bots/cfxdm/#bot-dmmap-multi-proc) | Same as @dm:map, but uses all available CPU core to do parallel processing |
| [@dm:eval](/Bots/cfxdm/#bot-dmeval) | Map values using evaluate function. Specify one of more column = 'expression' pairs |
| [@dm:eval-multi-proc](/Bots/cfxdm/#bot-dmeval-multi-proc) | Same as @dm:eval, but uses all available CPU core to do parallel processing |
| [\*dm:filter](/Bots/cfxdm/#bot-dmfilter) | Applies a CFXQL filter on input dataframe and returns rows that matches the filter |
| [\*dm:time-filter](/Bots/cfxdm/#bot-dmtime-filter) | Filter rows using one of the timestamp based column for a specific time range |
| [@#dm:filter-using-dict](/Bots/cfxdm/#bot-dmfilter-using-dict) | Applies a CFXQL filters specified in separate dictionary (saved dataset) and returns rows that matches the filters |
| [@dm:add-missing-columns](/Bots/cfxdm/#bot-dmadd-missing-columns) | Add columns to dataframe if they are not found. |
| [@dm:drop-null-columns](/Bots/cfxdm/#bot-dmdrop-null-columns) | Drop specified columns if they have certain percentage of null values |
| [@dm:mergecolumns](/Bots/cfxdm/#bot-dmmergecolumns) | Merge columns using 'include' regex and/or 'exclude' regex into a 'to' column |
| [@dm:fixcolumns](/Bots/cfxdm/#bot-dmfixcolumns) | Fix column names such that they contain only allowed characters |
| [@dm:fixnull](/Bots/cfxdm/#bot-dmfixnull) | Replace null values in a comma separated column list |
| [@dm:fixnull-regex](/Bots/cfxdm/#bot-dmfixnull-regex) | Replace null values in all columns that match the specified regular expression |
| [@dm:rename-columns](/Bots/cfxdm/#bot-dmrename-columns) | Rename specified column names using new\_column\_name = 'old\_column\_name' format |
| [@dm:replace-data](/Bots/cfxdm/#bot-dmreplace-data) | Replace data using regex pattern from list of comma separated columns |
| [@dm:selectcolumns](/Bots/cfxdm/#bot-dmselectcolumns) | Select columns using 'include' regex and/or 'exclude' regex |
| [@dm:to-type](/Bots/cfxdm/#bot-dmto-type) | Change data type to str or int or float for specified columns |
| [@dm:change-time-format](/Bots/cfxdm/#bot-dmchange-time-format) | Change timestamp from one format to another for all specified columns |

### 2.2 Data Re-shaping

RDA [cfxdm](/Bots/cfxdm/)
 extension provides many bots to re-shape inflight data.

##### Row Based Re-shaping

Following are some of the bots that can do row based re-shaping of inflight data:

| Bot | Description |
| --- | --- |
| [@dm:empty](/Bots/cfxdm/#bot-dmempty) | Creates an empty dataframe.  <br>If used as Sink bot, it empties the previous dataframe |
| [@dm:addrow](/Bots/cfxdm/#bot-dmaddrow) | Adds a new row with specified columns and fixed values |
| [@dm:head](/Bots/cfxdm/#bot-dmhead) | Keep first n rows of the dataframe and discard the rest |
| [@dm:tail](/Bots/cfxdm/#bot-dmtail) | Keep last n rows of the dataframe and discard the rest |
| [@dm:sample](/Bots/cfxdm/#bot-dmsample) | Randomly select rows from input.  <br>Can be used to select subset of rows or replicate rows randomly to create more rows |
| [@dm:sort](/Bots/cfxdm/#bot-dmsort) | Sort rows in ascending or descending order using specified column values |
| [@dm:concat](/Bots/cfxdm/#bot-dmconcat) | Loads one or more [saved datasets](#datasets)<br>, concatenates them and returns a single dataframe |
| [@dm:dedup](/Bots/cfxdm/#bot-dmdedup) | Deduplicates data by using specified column values |
| [@dm:dropnull](/Bots/cfxdm/#bot-dmdropnul) | Drop rows if specified column have null values |
| [@dm:explode](/Bots/cfxdm/#bot-dmexplode) | From a specified column value, split it using a seperator,  <br>replicate the splitted value into multiple rows.  <br>It keeps rest of the columns in-tact |
| [@dm:implode](/Bots/cfxdm/#bot-dmimplode) | Merge values from different rows into single value for that column |
| [@dm:explode-json](/Bots/cfxdm/#bot-dmexplode-json) | From a specified column value, split it as if it a JSON dict or list  <br>replicate the splitted value into multiple rows.  <br>It keeps rest of the columns in-tact |
| [\*dm:filter](/Bots/cfxdm/#bot-dmfilter) | Applies a CFXQL filter on input dataframe and returns rows that matches the filter |
| [\*dm:time-filter](/Bots/cfxdm/#bot-dmtime-filter) | Filter rows using one of the timestamp based column for a specific time range |
| [@#dm:filter-using-dict](/Bots/cfxdm/#bot-dmfilter-using-dict) | Applies a CFXQL filters specified in separate dictionary (saved dataset) and returns rows that matches the filters |

##### Column Based Re-shaping

Following are some of the bots that can do column based re-shaping of inflight data:

| Bot | Description |
| --- | --- |
| [@dm:map](/Bots/cfxdm/#bot-dmmap) | Map values from one column to another, using optional mapping function and arguments |
| [@dm:map-multi-proc](/Bots/cfxdm/#bot-dmmap-multi-proc) | Same as @dm:map, but uses all available CPU core to do parallel processing |
| [@dm:eval](/Bots/cfxdm/#bot-dmeval) | Map values using evaluate function. Specify one of more column = 'expression' pairs |
| [@dm:eval-multi-proc](/Bots/cfxdm/#bot-dmeval-multi-proc) | Same as @dm:eval, but uses all available CPU core to do parallel processing |
| [@dm:add-missing-columns](/Bots/cfxdm/#bot-dmadd-missing-columns) | Add columns to dataframe if they are not found. |
| [@dm:drop-null-columns](/Bots/cfxdm/#bot-dmdrop-null-columns) | Drop specified columns if they have certain percentage of null values |
| [@dm:fixcolumns](/Bots/cfxdm/#bot-dmfixcolumns) | Fix column names such that they contain only allowed characters |
| [@dm:mergecolumns](/Bots/cfxdm/#bot-dmmergecolumns) | Merge columns using 'include' regex and/or 'exclude' regex into a 'to' column |
| [@dm:rename-columns](/Bots/cfxdm/#bot-dmrename-columns) | Rename specified column names using new\_column\_name = 'old\_column\_name' format |
| [@dm:selectcolumns](/Bots/cfxdm/#bot-dmselectcolumns) | Select columns using 'include' regex and/or 'exclude' regex |
| [@dm:transpose](/Bots/cfxdm/#bot-dmtranspose) | Transposes columns to rows |

* * *

### 2.3 Data Extraction

Following bots can be used to extract data from unstructured logs & events

| Bot | Description |
| --- | --- |
| [@dm:eval](/Bots/cfxdm/#bot-dmeval) | Simple parsing & spitting by a word can be accomplished using this bot |
| [@dm:eval-multi-proc](/Bots/cfxdm/#bot-dmeval-multi-proc) | Simple parsing & spitting by a word can be accomplished using this bot |
| [@dm:extract](/Bots/cfxdm/#bot-dmextract) | Extract data using [Python Named Capturing Groups](https://docs.python.org/3/howto/regex.html#non-capturing-and-named-groups)<br> in Regular Expressions |
| [@dm:grok](/Bots/cfxdm/#bot-dmgrok) | Extract using Grok Patterns. [RDA Supported Grok Patterns](/reference_guides/grok_patterns/) |
| [@dm:grok-multi-proc](/Bots/cfxdm/#bot-dmgrok-multi-proc) | Extract using Grok Patterns. [RDA Supported Grok Patterns](/reference_guides/grok_patterns/)<br>. Uses multiple processes to accomplish parallel processing of data |

Example Pipeline snippets for Grok Parsing


```
@dm:empty         --> @dm:addrow             raw = "<85>Mar 21 03:22:17 cfx-rda-worker-vm01 sshd[414991]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.101.101  user=macaw"         --> @dm:grok              column = 'raw' &              pattern = "%{SYSLOGLINE}"
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=grok_2)

Output for the above example

| Column | Value |
| --- | --- |
| logsource | cfx-rda-worker-vm01 |
| priority |     |
| facility |     |
| timestamp | Mar 21 03:22:17 |
| program | sshd |
| message | pam\_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.101.101 user=macaw |
| pid | 414991 |
| timestamp8601 |     |
| meta\_grok\_message |     |

* * *

### 2.4 Data Enrichment

Following bots can be used to enrich inflight data with other datasets:

| Bot | Description |
| --- | --- |
| [@dm:enrich](/Bots/cfxdm/#bot-dmenrich) | Enrich the input dataframe using a saved dictionary dataset |
| [@dm:enrich-using-ip-cidr](/Bots/cfxdm/#bot-dmeval-multi-proc) | Enrich the input dataframe using a saved dictionary dataset.  <br>Match IP address in input dataframe with CIDRs specified in the dictionary |
| [@dm:enrich-using-ip-cidr-multi-proc](/Bots/cfxdm/#bot-dmenrich-using-ip-cidr-multi-proc) | Same as @dm:enrich-using-ip-cidr, but uses all available processors |
| [@dm:enrich-using-rule-dict](/Bots/cfxdm/#bot-dmenrich-using-rule-dict) | Enrich using rule based dictionary which contains 'rule' column |
| [@dm:dns-ip-to-name](/Bots/cfxdm/#bot-dmdns-ip-to-name) | Perform reverse DNS lookup to map IP Addresses to Hostnames on specified columns |
| [@dm:dns-name-to-ip](/Bots/cfxdm/#bot-dmdns-name-to-ip) | Perform DNS lookup to map Hostnames to IP Addresses on specified columns |

#### Enrichment using Geo Location Mapping

If the data contains IP Addresses (IPv4 or IPV6), following bot can be used to enrich with geographical location information:

| Bot | Description |
| --- | --- |
| [@geomap:lookup](/Bots/geomap/#bot-geomaplookup) | Enrich the input dataframe using Geo IP mapping |


```
@dm:empty     --> @dm:addrow             ip= "104.28.124.67"     --> @dm:addrow             ip = "178.197.234.26"     --> @geomap:lookup             ipaddress_column = "ip"
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=geomap_1)

Output for the above example

| Column | Value |
| --- | --- |
| geo\_accuracy\_radius | 1000.0 |
| geo\_autonomous\_system\_number | 13335.0 |
| geo\_autonomous\_system\_organization | CLOUDFLARENET |
| geo\_city\_name | Fremont |
| geo\_continent\_code |     |
| geo\_continent\_name | North America |
| geo\_country\_iso\_code | US  |
| geo\_country\_name | United States |
| geo\_is\_in\_european\_union | 0   |
| geo\_is\_satellite\_provider | 0   |
| geo\_latitude | 37.562 |
| geo\_locale\_code | en  |
| geo\_longitude | \-122.0 |
| geo\_metro\_code | 807.0 |
| geo\_network | 104.28.0.0/15 |
| geo\_postal\_code | 94536 |
| geo\_status | found |
| geo\_subdivision\_1\_iso\_code | CA  |
| geo\_subdivision\_1\_name | California |
| geo\_subdivision\_2\_iso\_code |     |
| geo\_subdivision\_2\_name |     |
| geo\_time\_zone | America/Los\_Angeles |
| ip  | 104.28.124.67 |

#### Enrichment using NLP Techniques

If the data contains natural language text, following NLP techniques can be used to enrich the data:

*   Keyword Extraction
*   Named Entity Recognition
*   Summarization
*   Sentiment Analysis

Refer to [Natural Language Processing (NLP) in RDA](https://bot-docs.cloudfabrix.io/beginners_guide/ml/#section_1)
 for details on how to accomplish this in RDA.

* * *

  

### 2.5 Data Integrity

RDA Fabric provides several ways to ensure integrity of the data moving through the fabric.

Following is a brief summary of different ways RDA Pipelines can check for data integrity and possibly take action:

| Integrity Check Type | Description |
| --- | --- |
| Using Checksum | Using bots [@dm:add-checksum](/Bots/cfxdm/#bot-dmadd-checksum)<br> and [@dm:verify-checksum](/Bots/cfxdm/#bot-dmverify-checksum)<br>, it can be ensured that data has not been tampered between an origin and destination. |
| Basic Column Checks | Using bot [@dm:check-columns](/Bots/cfxdm/#bot-dmcheck-columns)<br> pipeline can look for existence of specific columns and take action on the data. If the intent is to cleanup the data based on amount of nulls in the data, bots [@dm:drop-null-columns](/Bots/cfxdm/#bot-dmdrop-null-columns)<br>, [@dm:dropnull](/Bots/cfxdm/#bot-dmdropnull)<br>, [@dm:fixnull](/Bots/cfxdm/#bot-dmfixnull)<br>, [@dm:fixnull-regex](/Bots/cfxdm/#bot-dmfixnull-regex)<br> can be used. |
| Validing Against Schema | RDA can use [JSON Schema](https://json-schema.org/understanding-json-schema/)<br> to validate any data moving through the fabric. Bot [@dm:validate-data](/Bots/cfxdm/#bot-dmvalidate-data)<br> validates any incoming data against the specified schema.  <br>  <br>Optionally, RDA Datasets can be bound to a specific JSON Schema, and RDA validates the model everytime dataset is saved or updated. |
| Validating Using Rules Dictionary | Bot [@dm:check-integrity](/Bots/cfxdm/#bot-dmcheck-integrity)<br> uses rules dictionary to validate the data and take an action. Each rule would typically specify expected data types for certain set of columns, nulls allowed or not, range of values allowed for numericals, regex patterns for string data types.  <br>  <br>Bot [@dm:filter-using-dict](/Bots/cfxdm/#bot-dmfilter-using-dict)<br> can be used to drop specific rows based on criteria.  <br>  <br>Bot [@dm:enrich-using-rule-dict](/Bots/cfxdm/#bot-dmenrich-using-rule-dict)<br> can be used to check for very complex data types, relationships and tag each row for further action. |

* * *

### 2.6 Data Masking

RDA provides couple of ways to mask the data. First one using [@dm:mask](/Bots/cfxdm/#mask)
.

Example pipeline

|     |     |
| --- | --- |
| 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br>
<br>
<br>
<br>
<br>
 | `@dm:empty     --> @dm:addrow             phone_number = "925-555-5565" &             ssn = "123-56-8008" &             email = "john.doe@acme.com"     ## mask phone number except last 3 digits     --> @dm:mask             columns = "phone_number" & pos = -3 & char = "*"     ## mask SSN except last 4 digits     --> @dm:mask             columns = "ssn" & pos = -4 & char = "*"     ## mask email except first 3 characters     --> @dm:mask             columns = "email" & pos = 3 & char = "*"` |

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=mask_1)

Output for the pipeline would be:

| Column | Value |
| --- | --- |
| email | `joh**************` |
| phone\_number | `*********565` |
| ssn | `*******8008` |

Certain types of masking can also be done using [@dm:eval](/Bots/cfxdm/#eval)
. Eval allows more complex types of masking. For example, let us say we want to keep first 3 digits of phone number and last 3 digits intact, we can do this way:


```
@dm:empty     --> @dm:addrow             phone_number = "925-555-5565" &             ssn = "123-56-8008" &             email = "john.doe@acme.com"     --> @dm:eval             ssn = "'*****'+ssn.split('-')[-1]" &             phone_number = "phone_number[:3]+'*-***-*'+phone_number[-3:]" &             email = "'***'+email.split('@')[0][-5:]+'@xxxxx.yyy'"
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=mask_2)

Output for this pipeline would be

| Column | Value |
| --- | --- |
| email | `***n.doe@xxxxx.yyy` |
| phone\_number | `925*-***-*565` |
| ssn | `*****8008` |

* * *

### 2.7 Data Aggregations

RDA [cfxdm](/Bots/cfxdm/)
 exention provides many bots that can be used for data aggregations.

##### Computing Time Series Data Histograms

Historgrams convert timeseries data such as logs & metrics into 'events per time-interval'. Let us use [sample-servicenow-incidents](/Datasets/#dataset-sample-servicenow-incidents)
 dataset and use Service Now incidents as our input dataset. Let us how count how many tickets been opened by month since Jan 1, 2020. Let

Code Snippet: Histogram

Following snippet does:

*   Download data from a URL
*   Filter the data to retain incidents opened since Jan 1, 2020. We will just retain `sys_created_on` column for this purpose
*   Use [@dm:hist](/Bots/cfxdm/#bot-cfxdmhist)
     bot to compite histogram
*   Change the timestamp format for `sys_created_on` to show year & month only.

|     |     |
| --- | --- |
| 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br>
<br>
<br>
 | `@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-servicenow-incidents.csv'     --> *dm:filter             sys_created_on after '2020-01-01 00:00:00'             GET sys_created_on     --> @dm:hist             timestamp = "sys_created_on" &             interval = "30d"     --> @dm:change-time-format             columns = "sys_created_on" &             from_format = "ns" &             to_format = "%Y-%m"` |

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=histogram_1)

Output:

| sys\_created\_on | count |
| --- | --- |
| 2020-06 | 1   |
| 2020-07 | 0   |
| 2020-08 | 0   |
| 2020-09 | 0   |
| 2020-10 | 0   |
| 2020-11 | 16  |
| 2020-12 | 15  |
| 2021-01 | 0   |
| 2021-02 | 9   |

##### Computing Time Series Data Histograms with GroupBy

Instead of counting number of tickets opened by month, let us count number tickets opened by month but grouped by `priority` of the incident. We will use the bot [@dm:hist-groupby](/Bots/cfxdm/#bot-cfxdmhist-groupby)

Code Snippet: Histogram with GroupBy

|     |     |
| --- | --- |
| 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br>
<br>
<br>
<br>
<br>
 | `@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-servicenow-incidents.csv'     --> *dm:filter             sys_created_on after '2020-01-01 00:00:00'             GET sys_created_on, priority     --> @dm:hist-groupby             timestamp = "sys_created_on" &             interval = "30d" &             groupby = "priority" &              align = "no"     --> @dm:change-time-format             columns = "sys_created_on" &             from_format = "ns" &             to_format = "%Y-%m"` |

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=histogram_2)

Outpuut:

| sys\_created\_on | count | priority |
| --- | --- | --- |
| 2020-11 | 10  | 1 - Critical |
| 2020-12 | 0   | 1 - Critical |
| 2021-01 | 5   | 1 - Critical |
| 2020-11 | 3   | 2 - High |
| 2020-12 | 0   | 2 - High |
| 2021-01 | 1   | 2 - High |
| 2020-11 | 4   | 3 - Moderate |
| 2020-12 | 0   | 3 - Moderate |
| 2021-01 | 2   | 3 - Moderate |
| 2020-12 | 2   | 4 - Low |
| 2020-06 | 1   | 5 - Planning |
| 2020-07 | 0   | 5 - Planning |
| 2020-08 | 0   | 5 - Planning |
| 2020-09 | 0   | 5 - Planning |
| 2020-10 | 0   | 5 - Planning |
| 2020-11 | 3   | 5 - Planning |
| 2020-12 | 9   | 5 - Planning |
| 2021-01 | 0   | 5 - Planning |
| 2021-02 | 1   | 5 - Planning |

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!