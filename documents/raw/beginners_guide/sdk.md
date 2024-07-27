 



Developing RDA Bots
===================

1\. Prerequisites
-----------------

Developer must have following environments:

1.  Linux OS or MacOS
2.  Python 3 Runtime environment
3.  Docker Installed on the development system
4.  Install `rdac.py` as per instructions from [this page](https://bot-docs.cloudfabrix.io/beginners_guide/rdac/#1-installing-rda-command-line-tool)
    

Bots can be developed in many programming languages. Bot implementation to RDAF interaction happens through language neutral messaging built on [Protcol Buffers](https://developers.google.com/protocol-buffers)
.

Following is support matrix and road map:

| Language | Runtime Version | Availability |
| --- | --- | --- |
| Python | 3.7 | Available Now |
| Python | 3.9, 3.10 | Available Now |
| [Go](https://go.dev/) | 1.18.3 | Available Now |
| Java |     | August 2022 |

If you are looking for additional languages or runtime versions, or want some help during development, Join our [Slack Community](https://join.slack.com/t/rda-community/shared_invite/zt-z47qg2zk-LWujNwi6t7UzvVMcM_jBxQ)
 and let us know.

2\. Bot Definition File
-----------------------

Bots are defined in YAML format. Following is a simple example Bot Package definition file. Going forward, this file will be referred to as `bots.yml`

| bots.yml |     |
| --- | --- |
| [1](#__codelineno-0-1)<br> [2](#__codelineno-0-2)<br> [3](#__codelineno-0-3)<br> [4](#__codelineno-0-4)<br> [5](#__codelineno-0-5)<br> [6](#__codelineno-0-6)<br> [7](#__codelineno-0-7)<br> [8](#__codelineno-0-8)<br> [9](#__codelineno-0-9)<br>[10](#__codelineno-0-10)<br>[11](#__codelineno-0-11)<br>[12](#__codelineno-0-12)<br>[13](#__codelineno-0-13)<br>[14](#__codelineno-0-14)<br>[15](#__codelineno-0-15)<br>[16](#__codelineno-0-16)<br>[17](#__codelineno-0-17)<br>[18](#__codelineno-0-18)<br>[19](#__codelineno-0-19)<br>[20](#__codelineno-0-20)<br>[21](#__codelineno-0-21)<br>[22](#__codelineno-0-22)<br>[23](#__codelineno-0-23)<br>[24](#__codelineno-0-24)<br>[25](#__codelineno-0-25)<br>[26](#__codelineno-0-26)<br>[27](#__codelineno-0-27)<br>[28](#__codelineno-0-28)<br>[29](#__codelineno-0-29)<br>[30](#__codelineno-0-30)<br>[31](#__codelineno-0-31)<br>[32](#__codelineno-0-32)<br>[33](#__codelineno-0-33)<br>[34](#__codelineno-0-34)<br>[35](#__codelineno-0-35)<br>[36](#__codelineno-0-36)<br>[37](#__codelineno-0-37)<br>[38](#__codelineno-0-38)<br>[39](#__codelineno-0-39)<br>[40](#__codelineno-0-40)<br>[41](#__codelineno-0-41) | `extension:   namespace: acme   type: demo1   version: 22.6.6.2   description: Example RDA Bot Package for demonstration   default_name: demo   publisher: ACME Inc   support_email: info@acme.com   config_template: null   implementation:     code: myfile.MyDemoBotPackage runtime:   type: python3.7   packages:     - pandas==1.4.3 bots:   - name: get-data     description:       This bot performs simple get on a URL and loads the data into an output       column     bot_type: source     model_type: api     model_parameters:       - name: url         description: URL from which to load the raw data         type: text         mandatory: true       - name: output_column         description: Column name in the output         type: text         mandatory: false         default: output   - name: post-data     description: This bot performs POST of entire input data frame.     bot_type: sink     model_type: api     model_parameters:       - name: url         description: URL from which to load the raw data         type: text         mandatory: true` |

**`bots.yml`** file has three major sections: `extension`, `runtime`(Optional) and `bots`.

### 2.1 `extension` Section in `bots.yml`

`extension` section is mandatory. Following are the parameters in `extension` section:

| Parameter | Mandatory | Description |
| --- | --- | --- |
| `namespace` | Yes | Namespace should identify developer's company or project uniquely. Namespace must be all lowercase characters may contain digits. If you wish to publish the developed bot packages to RDA Marketplace, CloudFabrix would issue a certificate which can be used to `sign` the bot package to identify the origin of the package. |
| `type` | Yes | `type` parameter identifies name of the package and must be unique within the specified namespace. Must be all lowercase letters and may contain digits. |
| `version` | Yes | Version of the Bot Package. RDA uses date based versioning convention. Date based convention format is `YY.MM.DD`. If the package was changed on June 10th 2022, version would be `22.6.10`. Any versioning format is accepted. RDA determines latest version by sorting alphabetically. |
| `description` | Yes | Descriptive details about the Bot Package. |
| `default_name` |     | A name to be used as prefix for the bot name. At the time of deploying bot package, user can choose any unique name. |
| `publisher` | Yes | Name of the company or developer. |
| `support_email` |     | Email address to contact for any support related to this Bot Package |
| `repo_url` |     | Git or any other publicly accessible URL which may provide additional information for the Bot Package, issue tracking and additional documentation |
| `implementation` | Yes (if runtime is python) | This parameter must be a simple object with one parameter: `code`. The `code` parameter must specify the main python file which contains Bot implementations. All the implementation files must be inside the directory `code` which must be at the level as `bots.yml` This field is ignored if runtime is not python. |
| `config_template` |     | Configuration template for the bot package. This is required only if certain credentials are required for this package to work.  <br>For Example if the bot package pulls data from a certain service using APIs, and if that service needs credentials, format of the credentials must be defined in this object. See below for more details on `config_template` |

### 2.2 `config_template` Details

Let us assume, the Bot Package needs to connect to a specific server & port. Let us say, the server expects authentication for APIs.

Configuration template will look something like below:

| config\_template |     |
| --- | --- |
| [1](#__codelineno-1-1)<br> [2](#__codelineno-1-2)<br> [3](#__codelineno-1-3)<br> [4](#__codelineno-1-4)<br> [5](#__codelineno-1-5)<br> [6](#__codelineno-1-6)<br> [7](#__codelineno-1-7)<br> [8](#__codelineno-1-8)<br> [9](#__codelineno-1-9)<br>[10](#__codelineno-1-10)<br>[11](#__codelineno-1-11)<br>[12](#__codelineno-1-12)<br>[13](#__codelineno-1-13)<br>[14](#__codelineno-1-14)<br>[15](#__codelineno-1-15)<br>[16](#__codelineno-1-16) | `config_template:   hostname:   port: 8060   api_token:   timeout: 60   verify: False   $secure: ["api_token"]   $mapping:     verify: boolean_field   $mandatory: ["hostname", "api_token"]   $labels:     hostname: Host     port: Port     api_token: API Token     verify: Verify SSL Certificate     timeout: "Timeout (sec)"` |

In this template, parameters expected from user are `hostname`, `port`, `api_token`, `timeout`, `verify`. All the parameters that start with `$` are special purpose tags that define behavior or attach metadata.

*   `$secure`: All the parameters listed under this tag are encrypted when stored. Also, user input would be masked.
*   `$mandatory`: All parameters listed under this tag must have a valid value.
*   `$labels`: This tag is object which provides parameter name to display label. If such a mapping is not specified, parameter name is used as label.

### 2.3 `runtime` section in `bots.yml`

`runtime` section in `bots.yml` is an optional section that is used to specify the languange and other runtime environment specific to this extension.

|     |     |
| --- | --- |
| [1](#__codelineno-2-1)<br>[2](#__codelineno-2-2)<br>[3](#__codelineno-2-3)<br>[4](#__codelineno-2-4) | `runtime:   type: python3.9   packages:     - pandas==1.4.3` |

| Parameter | Mandatory | Description |
| --- | --- | --- |
| `type` | optional | Language and version in which bot extension runs on. Currently supported values are `python3.7`, `python3.9`, `python3.10` and `go1.18`, Default is `python3.7` |
| `packages` | optional | Any python packages required to be installed for bot extension to run successfully. All the packages should be pegged to a version using ==. Applicable only if runtime type is pythonxxx. Ignored for other runtimes. |

### 2.4 `bots` section in `bots.yml`

`bots` section is mandatory. Bots must be a list of objects. At least one bot is required. Each bot object will have following parameters.

|     |     |
| --- | --- |
| [1](#__codelineno-3-1)<br> [2](#__codelineno-3-2)<br> [3](#__codelineno-3-3)<br> [4](#__codelineno-3-4)<br> [5](#__codelineno-3-5)<br> [6](#__codelineno-3-6)<br> [7](#__codelineno-3-7)<br> [8](#__codelineno-3-8)<br> [9](#__codelineno-3-9)<br>[10](#__codelineno-3-10)<br>[11](#__codelineno-3-11)<br>[12](#__codelineno-3-12)<br>[13](#__codelineno-3-13)<br>[14](#__codelineno-3-14)<br>[15](#__codelineno-3-15)<br>[16](#__codelineno-3-16) | `bots:   - name: get-data     description:       This bot performs simple get on a URL and loads the data into an output       column     bot_type: source     model_type: api     model_parameters:       - name: url         description: URL from which to load the raw data         type: text         mandatory: true       - name: output_column         description: Column name in the output         type: text         mandatory: true` |

| Parameter | Mandatory | Description |
| --- | --- | --- |
| `name` | yes | Name of the bot. Must be unique within the bot package. Must be all lowercase. Must start with a letter and may contain hyphens and digits. |
| `description` | Yes | Description of the bot |
| `bot_type` | Yes | Valid values for bot `source`, `source-any`, `sink`, `sink-updates`.  <br>  <br>`source`: Bot outputs data. Can only be used at the beginning of a Pipeline Block.  <br>`source-any`: Bot outputs data. Can be used at any position in the pipeline. Does not consume input data.  <br>`sink`: Bot consumes data but does not modify it.  <br>`sink-updates`: Bot consumes input data and produces updated data |
| `model_type` | Yes | Only allowed value for this parameter is `api`. Future versions of Bot Package Development Kits will support additional types |
| `model_parameters` |     | `model_parameters` is a list of objects. Each object must contain following parameters  <br>  <br>`name`: Parameter name. Recommended to use letters, digits and underscore.  <br>`description`: Description for the parameter  <br>`type`: Valid values are `text` or `datetime`. Future versions of Bot Package Development Kit will support additional data types and enums.  <br>`mandatory`: Must be `true` or `false`. Declares whether the specified by `name` is mandatory |

3\. Bot Implementation Code
---------------------------

### 3.1 Bot Implementation Code (Python)

Following a simple working example code that works with `bots.yml` specified above.

| code/myfile.py |     |
| --- | --- |
| [1](#__codelineno-4-1)<br> [2](#__codelineno-4-2)<br> [3](#__codelineno-4-3)<br> [4](#__codelineno-4-4)<br> [5](#__codelineno-4-5)<br> [6](#__codelineno-4-6)<br> [7](#__codelineno-4-7)<br> [8](#__codelineno-4-8)<br> [9](#__codelineno-4-9)<br>[10](#__codelineno-4-10)<br>[11](#__codelineno-4-11)<br>[12](#__codelineno-4-12)<br>[13](#__codelineno-4-13)<br>[14](#__codelineno-4-14)<br>[15](#__codelineno-4-15)<br>[16](#__codelineno-4-16)<br>[17](#__codelineno-4-17)<br>[18](#__codelineno-4-18)<br>[19](#__codelineno-4-19)<br>[20](#__codelineno-4-20)<br>[21](#__codelineno-4-21)<br>[22](#__codelineno-4-22)<br>[23](#__codelineno-4-23)<br>[24](#__codelineno-4-24)<br>[25](#__codelineno-4-25)<br>[26](#__codelineno-4-26)<br>[27](#__codelineno-4-27)<br>[28](#__codelineno-4-28)<br>[29](#__codelineno-4-29)<br>[30](#__codelineno-4-30)<br>[31](#__codelineno-4-31)<br>[32](#__codelineno-4-32)<br>[33](#__codelineno-4-33)<br>[34](#__codelineno-4-34)<br>[35](#__codelineno-4-35)<br>[36](#__codelineno-4-36)<br>[37](#__codelineno-4-37)<br>[38](#__codelineno-4-38)<br>[39](#__codelineno-4-39)<br>[40](#__codelineno-4-40)<br>[41](#__codelineno-4-41)<br>[42](#__codelineno-4-42)<br>[43](#__codelineno-4-43)<br>[44](#__codelineno-4-44)<br>[45](#__codelineno-4-45)<br>[46](#__codelineno-4-46)<br>[47](#__codelineno-4-47)<br>[48](#__codelineno-4-48)<br>[49](#__codelineno-4-49)<br>[50](#__codelineno-4-50)<br>[51](#__codelineno-4-51)<br>[52](#__codelineno-4-52)<br>[53](#__codelineno-4-53)<br>[54](#__codelineno-4-54)<br>[55](#__codelineno-4-55)<br>[56](#__codelineno-4-56)<br>[57](#__codelineno-4-57)<br>[58](#__codelineno-4-58)<br>[59](#__codelineno-4-59) | `import requests import logging logger = logging.getLogger(__name__) class MyDemoBotPackage(object):     def __init__(self, **kwargs):         # kwargs will contain a reference to config object         # config object may also contain credentials provided by the user (if any)         self.__config = kwargs.get("config")         logger.info("Initializing my demo bot package")     def shutdown(self):         # Shutdown hook may be called before shutting down the bot code.         # any cleanup can be performed.         logger.info("Shutdown hook called")     # for bot get-data, expected method name for implementation is bot_get_data     def bot_get_data(self, **kwargs):         query_params = kwargs.get("query_params", {})         url = query_params.get("url")         output_column = query_params.get("output_column") or "output"         response = requests.get(url, timeout=10.0)         if not response.ok:             response.raise_for_status()         data = response.text         # Output can be Pandas Dataframe or list of objects         result = [             {                 output_column: data             }         ]         return result     # for bot post-data, expected method name for implementation is bot_post_data     def bot_post_data(self, **kwargs):         query_params = kwargs.get("query_params", {})         url = query_params.get("url")         # Input data is an array of objects         input_data = kwargs.get("input_data")         response = requests.post(url, json=input_data, timeout=10.0)         if not response.ok:             response.raise_for_status()         # Since this is s Sink bot, it does not produce any updated output.         # Output of this bot is ignored.         return None` |

### 3.2 Bot Implementation Code (Go Lang)

The bot implementation in golang needs to conform to the following structure:

1.  The extension implementation code needs to be placed in `code/rda` directory relative to `bots.yml` file.
2.  Place a `go.mod` file in this directory and add any dependent packages in this file (optional) If the dependant packages are not included in this file, they are automatically installed during build time.
3.  Create a file (ex. extension.go) in the directory and make sure it is declared as `pacakge rda`
4.  This file should have the following functions implemented.

`[](#__codelineno-5-1) package rda [](#__codelineno-5-2) type Extension struct { [](#__codelineno-5-3)     Config  map[string]interface{} [](#__codelineno-5-4)     ExtInfo map[string]interface{} [](#__codelineno-5-5) } [](#__codelineno-5-6) func NewExtension(extInfo map[string]interface{}, config map[string]interface{}) Extension { [](#__codelineno-5-7)   // This function should instantiate Extension struct and return it. [](#__codelineno-5-8) } [](#__codelineno-5-9) func (p Extension) ShutdownHook() { [](#__codelineno-5-10)     // Any code that needs to be executed when the extension is being shutdown [](#__codelineno-5-11) } [](#__codelineno-5-12) func (p Extension) ExecuteBot(botName string, botDef map[string]interface{}, args map[string]interface{}) (*[]map[string]interface{}, error) { [](#__codelineno-5-13)   // This is the main function that executes a bot. botName is passed as an argument so that this function can switch based on botName [](#__codelineno-5-14) }`

Following is a sample code for golang:

`[](#__codelineno-6-1) package rda [](#__codelineno-6-2) [](#__codelineno-6-3) import ( [](#__codelineno-6-4)     "errors" [](#__codelineno-6-5)     "fmt" [](#__codelineno-6-6)     "io/ioutil" [](#__codelineno-6-7)     "net/http" [](#__codelineno-6-8)     "runtime" [](#__codelineno-6-9)     "runtime/debug" [](#__codelineno-6-10) [](#__codelineno-6-11)     "github.com/sirikothe/gotextfsm" [](#__codelineno-6-12) ) [](#__codelineno-6-13) [](#__codelineno-6-14) type Extension struct { [](#__codelineno-6-15)     Config  map[string]interface{} [](#__codelineno-6-16)     ExtInfo map[string]interface{} [](#__codelineno-6-17) } [](#__codelineno-6-18) [](#__codelineno-6-19) func NewExtension(extInfo map[string]interface{}, config map[string]interface{}) Extension { [](#__codelineno-6-20)     return *(new(Extension)) [](#__codelineno-6-21) } [](#__codelineno-6-22) [](#__codelineno-6-23) func (p Extension) ShutdownHook() { [](#__codelineno-6-24)     fmt.Printf("Shutfown Hook Called") [](#__codelineno-6-25) } [](#__codelineno-6-26) func (p Extension) parseTextFsm(botDef map[string]interface{}, args map[string]interface{}) (*[]map[string]interface{}, error) { [](#__codelineno-6-27)     queryParams := args["query_params"].(map[string]interface{}) [](#__codelineno-6-28)     inputColumn := "" [](#__codelineno-6-29)     if queryParams["input_column"] != nil { [](#__codelineno-6-30)         inputColumn = queryParams["input_column"].(string) [](#__codelineno-6-31)     } [](#__codelineno-6-32)     url := "" [](#__codelineno-6-33)     if queryParams["url"] == nil { [](#__codelineno-6-34)         return nil, errors.New("url is not passed as a param to the bot") [](#__codelineno-6-35)     } [](#__codelineno-6-36)     url = queryParams["url"].(string) [](#__codelineno-6-37)     if args["input_data"] == nil { [](#__codelineno-6-38)         return nil, errors.New("input_data is not passed to the bot") [](#__codelineno-6-39)     } [](#__codelineno-6-40)     resp, err := http.Get(url) [](#__codelineno-6-41)     if err != nil { [](#__codelineno-6-42)         return nil, err [](#__codelineno-6-43)     } [](#__codelineno-6-44)     if resp.StatusCode != http.StatusOK { [](#__codelineno-6-45)         return nil, errors.New(fmt.Sprintf("Error while getting %s. Status: %d\n", url, resp.StatusCode)) [](#__codelineno-6-46)     } [](#__codelineno-6-47) [](#__codelineno-6-48)     body, err := ioutil.ReadAll(resp.Body) [](#__codelineno-6-49)     if err != nil { [](#__codelineno-6-50)         return nil, err [](#__codelineno-6-51)     } [](#__codelineno-6-52)     template := string(body) [](#__codelineno-6-53)     fsm := gotextfsm.TextFSM{} [](#__codelineno-6-54)     err = fsm.ParseString(template) [](#__codelineno-6-55)     if err != nil { [](#__codelineno-6-56)         return nil, err [](#__codelineno-6-57)     } [](#__codelineno-6-58)     parser := gotextfsm.ParserOutput{} [](#__codelineno-6-59)     inputData := args["input_data"].([]map[string]interface{}) [](#__codelineno-6-60)     var output []map[string]interface{} [](#__codelineno-6-61)     for i := 0; i < len(inputData); i++ { [](#__codelineno-6-62)         row := inputData[i] [](#__codelineno-6-63)         if row[inputColumn] != nil { [](#__codelineno-6-64)             input := row[inputColumn].(string) [](#__codelineno-6-65)             err = parser.ParseTextString(input, fsm, true) [](#__codelineno-6-66)             if err != nil { [](#__codelineno-6-67)                 return nil, err [](#__codelineno-6-68)             } [](#__codelineno-6-69)             output = append(output, parser.Dict...) [](#__codelineno-6-70)         } [](#__codelineno-6-71) [](#__codelineno-6-72)     } [](#__codelineno-6-73)     return &output, nil [](#__codelineno-6-74) } [](#__codelineno-6-75) func (p Extension) getVersions(botDef map[string]interface{}, args map[string]interface{}) (*[]map[string]interface{}, error) { [](#__codelineno-6-76)     bi, ok := debug.ReadBuildInfo() [](#__codelineno-6-77)     if !ok { [](#__codelineno-6-78)         return nil, errors.New("Failed to read build info") [](#__codelineno-6-79)     } [](#__codelineno-6-80)     var output []map[string]interface{} [](#__codelineno-6-81)     output = append(output, map[string]interface{}{"path": "go", "version": runtime.Version()}) [](#__codelineno-6-82)     for _, dep := range bi.Deps { [](#__codelineno-6-83)         output = append(output, map[string]interface{}{"path": dep.Path, "version": dep.Version}) [](#__codelineno-6-84)     } [](#__codelineno-6-85)     return &output, nil [](#__codelineno-6-86) } [](#__codelineno-6-87) func (p Extension) ExecuteBot(botName string, botDef map[string]interface{}, args map[string]interface{}) (*[]map[string]interface{}, error) { [](#__codelineno-6-88)     switch botName { [](#__codelineno-6-89)     case "parse": [](#__codelineno-6-90)         return p.parseTextFsm(botDef, args) [](#__codelineno-6-91)     case "get-versions": [](#__codelineno-6-92)         return p.getVersions(botDef, args) [](#__codelineno-6-93)     default: [](#__codelineno-6-94)         return nil, errors.New(fmt.Sprintf("Unknown bot %s. Don't know how to execute", botName)) [](#__codelineno-6-95)     } [](#__codelineno-6-96) }`

4\. Building and Publishing First Bot Package
---------------------------------------------

Make sure to place `bots.yml` and `myfile.py` in the following directory structure:

Let us assume you have your bot package source code in `~/rda_bots/myfirst_bot/`

`[](#__codelineno-7-1) ~/rda_bots/myfirst_bot/ [](#__codelineno-7-2)                       bots.yml [](#__codelineno-7-3)                       code/ [](#__codelineno-7-4)                            myfile.py`

Make sure to [**Install `rdac.py`**](https://bot-docs.cloudfabrix.io/beginners_guide/rdac/#1-installing-rda-command-line-tool)

### 4.1 Build and Deploy Bot Package

Change directory

`[](#__codelineno-8-1) cd ~/rda_bots/myfirst_bot/`

Do Build:

`[](#__codelineno-9-1) rdac.py bot-package-build --file ./bots.yml`

If no errors occur, push the package and code to RDA Fabric:

`[](#__codelineno-10-1) rdac.py bot-package-add --file ./bots.yml --push`

Verify that package is added to RDA Fabric:

`[](#__codelineno-11-1) rdac.py bot-package-list`

Output should be similar to following:

`[](#__codelineno-12-1) Name               Version    Description                                Has Dist    Publisher    Saved Time [](#__codelineno-12-2) -----------------  ---------  -----------------------------------------  ----------  -----------  -------------------------- [](#__codelineno-12-3) botpkg_acme_demo1  22.6.6.2   Example RDA Bot Package for demonstration  Yes         ACME Inc     2022-06-01T20:42:09.551631`

If bot package is not needed, use `rdac.py bot-package-delete` to delete it from RDA Fabric.

### 4.2 Add Credentials to Vault

Once Bot Package has beed deployed, we need to add necessary credentials to RDA Fabric Vault.

Verify that \`botpkg\_acme\_demo\`\` is a valid Secret Type in RDAF:

`[](#__codelineno-13-1) rdac.py secret-types | grep botpkg`

Output should be like this:

`[](#__codelineno-14-1) | botpkg_acme_demo1     | Example RDA Bot Package for demonstration`

Now add credentials to vault:

`[](#__codelineno-15-1) rdac.py secret-add --type botpkg_acme_demo1`

This command will prompt for inputs. Name of the credential is mandatory and must be unique within RDAF deployment. Name must be all lowercase with optional hyphens. If the Bot Package has any additional credential requirement such as `username` and `password`, they should defined in `config_template` ([Section 2.2](#22-config_template-details)
).

`[](#__codelineno-16-1) Configure Integration: Example RDA Bot Package for demonstration [](#__codelineno-16-2) [](#__codelineno-16-3) Name*: demo [](#__codelineno-16-4) Add to Default Site Profile: no`

Verify that secret has been added to vault using `rdac.py secret-list | grep botpkg`

### 4.3 Test the Bots with a Pipeline

To test the first bot `get-data` in this package, we can use following simple pipeline:

|     |     |
| --- | --- |
| [1](#__codelineno-17-1)<br>[2](#__codelineno-17-2)<br>[3](#__codelineno-17-3) | `@demo:get-data     url = 'https://bot-docs.cloudfabrix.io/data/ft/ft-a04-News-Template-HTML' &     output_column = "output"` |

Save the above pipeline snippet as `test_pipeline_1.rda`

Run the pipeline:

`[](#__codelineno-18-1) rdac.py run-get-output --pipeline test_pipeline_1.rda --vault --attr debug=demo1`

Note

\_ If you omit `--pipeline test_pipeline_1.rda` option, above command will prompt for pipeline. You can copy paste the pipeline contents and type `.` in a new line. \_ `--vault` option instructs the Pipeline execution tool to fetch any required credentials from the Vault. \* `--attr debug=demo1` attaches an attribute called `debug` with value \`demo\`\`. This will help is while observing logs or traces for this test.

Output should be similar to:

[Example Output](#__tabbed_1_1)

``[](#__codelineno-19-1) Created Job: {} 2788d2bec2f84004b070c7761e3ee05b [](#__codelineno-19-2) Running: [](#__codelineno-19-3) Running: [](#__codelineno-19-4) Completed: [](#__codelineno-19-5) Completed the job in 3.2 seconds [](#__codelineno-19-6) Purging output for jobid: 2788d2bec2f84004b070c7761e3ee05b [](#__codelineno-19-7) Output has 1 rows, 1 columns [](#__codelineno-19-8) [](#__codelineno-19-9)     +----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ [](#__codelineno-19-10)     |    | output                                                                                                                                                                                        | [](#__codelineno-19-11)     |----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| [](#__codelineno-19-12)     |  0 | <p><h3>News that doesn't make you Snooze. <i>Generated by CloudFabrix RDA Bots</i></h3><ul>{%for row in rows%}<li><a href='{{ row.link }}'>{{ row.title }}</a></li>{% endfor %}</li></ul></p> | [](#__codelineno-19-13)     +----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ [](#__codelineno-19-14)     ``` [](#__codelineno-19-15) [](#__codelineno-19-16) === "Example Traces" [](#__codelineno-19-17) ` Host Pipeline JobID Seq Status Bot Dataframe Error Message ec5289f08e52 test_pipeline_20220610_171948 2788d2be 0 in-progress @demo:get-data 0x0 ec5289f08e52 test_pipeline_20220610_171948 2788d2be 1 in-progress 1x1 ec5289f08e52 test_pipeline_20220610_171948 2788d2be 2 completed 1x1 ec5289f08e52 test_pipeline_20220610_171948 2788d2be 3 trace 0x0 Saving output ` [](#__codelineno-19-18) [](#__codelineno-19-19) !!! note [](#__codelineno-19-20) Traces can be observed using `rdac.py watch-traces --attr debug=demo1` [](#__codelineno-19-21) This command keeps running until it is stopped using ++ctrl+c++``

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!