 



Guide to CFXQL: Robotic Data Automation's Query Language
========================================================

CFXQL is a _SQL_ like data query language. RDA Low-Code developers use CFXQL to convey their intent of what each bot should do with the data. CFXQL helps RDA Low-Code developers to consistently interact with hundreds of different data sources and destinations in a unified manner.

RDA Bot Types
-------------

Before we get into the details of CFXQL, let us take look at the types of RDA Bots and how they use CFXQL:

> | Bot Type | Bot Name Prefix | Description |
> | --- | --- | --- |
> | Source Filtering Bots | `#` | Bots starting with `#` in the name are considered source filtering bots.  <br>They accept [Full CFXQL](#fullcfxql)<br> and translate into a Query or API call that is sent to the remote data source (such as a Database).  <br>This helps to filter the data at the source itself.  <br>  <br>For example [#splunkv2:search-index](/Bots/splunk_v2/#search-index)<br> is a source filtering bot. |
> | Destination Filtering Bots | `*` | Bots starting with `*` in the name are considered destination filtering bots.  <br>They accept [Full CFXQL](#fullcfxql)<br> and filter the data that is already in memory, or the data source does not provide a flexible query mechanism.  <br>  <br>For example [\*dm:filter](/Bots/cfxdm/#filter)<br> is a destination filtering bot.  <br>It filters the data that is already in the pipeline. |
> | API Bots | `@` | Bots starting with `@` in the name are the API Based bots.  <br>They accept a simple [Restricted CFXQL](#restrictedcfxql)<br> and extract API parameters from the query  <br>The API parameters for each bot control the behavior of that bot.  <br>  <br>For example [@watson:summarize](/Bots/ibm_watson/#summarize)<br> is an API based bot.  <br>It sends the input data to IBM Watson and API parameters specified in CFXQL control the bot's behavior. |

Full CFXQL
----------

Full CFXQL supports several _SQL_ like operators.

Below is a simple example of CFXQL Query:

    `[](#__codelineno-0-1)     device_category is 'SWITCH' and  [](#__codelineno-0-2)         ( severity is not in [ 'INFO', 'DEBUG' ] or status != 'CLOSED' ) [](#__codelineno-0-3)     GET [](#__codelineno-0-4)         device_category, severity, status as 'Incident Status'`

Full CFXQL has two parts: Query and Result Format

**Query**

> *   Query can be any of the operations with a combination of **AND** **OR** logical groupings.
> *   If the query is `*` it means match all. Equivalent to `SELECT *` in SQL
> *   All column names MUST be only made up of letters, digits and underscore(\_). If the name has other characters, it can be escaped using backquote characters: `` `Column with Spaces` == 'value' ``

**Result Format**

> *   Optionally Result format can be specified to select subset of columns from the query response.
> *   Result format uses `GET` (keyword, case insensitive) to seperate Query and Result Format.
> *   Example Result formats
>     
>     > *   ``* GET ColumnA, ColumnB, `Column-C` as 'Column C'``
>     > *   `* GET columnA as 'A', columnB as 'B'`
>     

#### Equality Operators

| Operator | Description and Examples |
| --- | --- |
| **\=** | Compares if the left side column value is equal to right side constant or column value.  <br>  <br>`device = '10.10.10.1'`  <br>`device == '10.10.10.1'`  <br>`device is equal to '10.10.10.1'`  <br>`device is '10.10.10.1'`  <br>`device equals '10.10.10.1'`  <br>`port == 80` |
| **!=** | Compares if the left side column value is not equals to right side constant or column value.  <br>  <br>`device != "10.10.10.1"`  <br>`device is not equal to '10.10.10.1'`  <br>`device is not '10.10.10.1'`  <br>`device not equals '10.10.10.1'` |

#### Numerical Operators

| Operator | Description and Examples |
| --- | --- |
| **\>** | Compares if the left side numerical column value is greater to right side numerical constant or column value.  <br>  <br>`port > 80`  <br>`port is greater than 80`  <br>`port gt 80` |
| **\>=** | Compares if the left side numerical column value is greater or equal to right side numerical constant or column value.  <br>  <br>`port >= 80`  <br>`port is greater than or equal to 80`  <br>`port gte 80` |
| **<** | Compares if the left side numerical column value is less than right side numerical constant or column value.  <br>  <br>`port > 80`  <br>`port is greater than 80`  <br>`port lt 80` |
| **<=** | Compares if the left side numerical column value is less than or equal to right side numerical constant or column value.  <br>  <br>`port <= 80`  <br>`port is less than or equal to 80`  <br>`port lte 80` |

#### String Operators

| Operator | Description and Examples |
| --- | --- |
| **~** | Contains operator.  <br>  <br>`device ~ '10.10'`  <br>`device contains '10.10'`  <br>`device has '10.10'` |
| **!~** | Does not contain operator.  <br>  <br>`device !~ '10.10'`  <br>`device does not contains '10.10'`  <br>`device not contains '10.10'` |
| **?** | Regex match operator.  <br>  <br>`device ? '^10.*'`  <br>`device matches '^10.*'` |
| **!?** | Regex does not match operator.  <br>  <br>`device !? '^10.*'`  <br>`device does not match '^10.*'` |
| **^~** | Starts-with operator.  <br>  <br>`device ^~ '10'`  <br>`device starts with '10.'` |
| **!^~** | Not-starts-with operator.  <br>  <br>`device !^~ '10'`  <br>`device does not start with '10.'` |
| **~$** | Ends-with operator.  <br>  <br>`device ~$ '.1'`  <br>`device ends with '.1'` |
| **!~$** | Not-ends-with operator.  <br>  <br>`device !~$ '10'`  <br>`device does not end with '.1'` |

#### List Operators

| Operator | Description and Examples |
| --- | --- |
| **in** | List IN operator.  <br>  <br>`device in ['10.10.10.1', '10.10.10.2']`  <br>`device in '10.10.10.1', '10.10.10.2'`  <br>`port in 80, 443`  <br>`port is in [ 80, 443 ]`  <br>`port is one of [ 80, 443 ]`  <br>`port is among [ 80, 443 ]`  <br>`port is any of [ 80, 443 ]` |
| **not in** | List NOT IN operator.  <br>  <br>`device not in ['10.10.10.1', '10.10.10.2']`  <br>`device not-in '10.10.10.1', '10.10.10.2'`  <br>`port not in 80, 443`  <br>`port is not in [ 80, 443 ]`  <br>`port is not one of [ 80, 443 ]`  <br>`port is not among [ 80, 443 ]` |

#### Unary Operators for NULL Value Checks

| Operator | Description and Examples |
| --- | --- |
| **null** | Checks if the value is NULL or empty.  <br>  <br>`device is null`  <br>`device is none`  <br>`device is empty` |
| **not null** | Checks if the value is not NULL or not empty.  <br>  <br>`device is not null`  <br>`device notnull`  <br>`device is not none` |

#### Time Operators

| Operator | Description and Examples |
| --- | --- |
| **before** | Operator to test if given timestamp column is less than an absolute or relative timestamp.  <br>  <br>`timestamp is before 'Jan 1, 2022 10am'`  <br>`timestamp is before -10 days`  <br>`timestamp is before -15 minutes`  <br>`timestamp is before this month` |
| **after** | Operator to test if given timestamp column is greater than an absolute or relative timestamp.  <br>  <br>`timestamp is after 'Jan 1, 2022 10am'`  <br>`timestamp after -10 days`  <br>`timestamp after -15 minutes`  <br>`expiry_date is after this month` |
| **during** | Operator to test if given timestamp column is between two absolute or relative timestamps.  <br>  <br>`resolved_date is during 'Jan 1, 2022 10am' to 'Jan 5, 2022 10am'`  <br>`resolved_date is during today`  <br>`resolved_date is during this year` |
| **not during** | Operator to test if given timestamp column is not between two absolute or relative timestamps.  <br>  <br>`resolved_date is not during 'Jan 1, 2022 10am' to 'Jan 5, 2022 10am'`  <br>`resolved_date notduring this month`  <br>`resolved_date is not during this CY2022` |

#### Logical Operators

Logical Operators **AND** and **OR** can be nested using parenthesis.

| Operator | Description and Examples |
| --- | --- |
| **AND** | Logical AND Operator  <br>  <br>`timestamp is before 'Jan 1, 2022 10am' AND status is 'OK'`  <br>`device is '10.10.10.10' & status is not 'ok'`  <br>`A != B & C = 20` |
| **OR** | Logical OR Operator  <br>  <br>`timestamp is before 'Jan 1, 2022 10am' OR status is 'OK'`  <br>`device is '10.10.10.10' or status is not 'ok'`  <br>`(device is '10.10.10.10' ) or (status is not 'ok')`  <br>`A != B \| C == 20` |

Restricted CFXQL
----------------

Restricted CFXQL supports only `=` operator and `AND` logical operator. Does not support 'Result Format'

Below are simple examples of restricted CFXQL Query:

    `[](#__codelineno-1-1)     device_category is 'SWITCH' and severity = 'INFO'`

    `[](#__codelineno-2-1)     device_category = 'SWITCH' &  [](#__codelineno-2-2)     severity = 'INFO' & [](#__codelineno-2-3)     status = 200`

#### Equality Operators

| Operator | Description and Examples |
| --- | --- |
| **\=** | Compares if the left side column value is equals to right side constant or column value.  <br>  <br>`device = '10.10.10.1'`  <br>`device == '10.10.10.1'`  <br>`device is equal to '10.10.10.1'`  <br>`device is '10.10.10.1'`  <br>`device equals '10.10.10.1'`  <br>`port = 80` |

#### Logical Operators

| Operator | Description and Examples |
| --- | --- |
| **AND** | Logical AND Operator  <br>  <br>`device = '10.10.10.1' AND status is 'OK'`  <br>`device is '10.10.10.10' & status = 'ok'`  <br>`A = 100 & C = 20` |

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!