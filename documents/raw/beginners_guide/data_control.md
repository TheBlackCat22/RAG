 



Artifacts to Control Data in RDA Fabric
=======================================

| Artifact Type | Description |
| --- | --- |
| [Formatting Templates](#foormatting_templates) | RDAF uses [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)<br> Templating Engine to format data. |
| [Credentials](#credentials) | Credentials to various systems / integrations are stored securely in RDA Fabric Vault |
| [Bookmarks](#bookmarks) | RDA Fabric uses Bookmarks as a way to remember how far each data stream has been read. |
| [Pipelines](#pipelines) | Pipelines are low code lines of text to manage data. |
| [Service Blueprints](#blueprints) | Service Blueprints help manage lifecycle of one more pipelines, and related artifacts, collectively as a single service. |

* * *

1\. Formatting Templates
------------------------

RDAF uses [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
 Templating Engine to format data to make it suitable for REST Endpoints, HTML Reports sent via email, and many other formats as needed by various integration endpoints.

**Storage Location**

> RDAF Object Storage

**Related Bots**

*   [@dm:apply-template-by-row](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#apply-template-by-row)
    
*   [@dm:apply-template-all-rows](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#apply-template-all-rows)
    

**Related RDA Client CLI Commands**

`[](#__codelineno-0-1) rdac fmt-template: -h`

[Example Output](#__tabbed_1_1)

`[](#__codelineno-1-1) Formatting Templates management commands [](#__codelineno-1-2) [](#__codelineno-1-3) Following are valid sub-commands for fmt-template: [](#__codelineno-1-4) list                      List Formatting Templates [](#__codelineno-1-5) get                       Get Formatting Template [](#__codelineno-1-6) delete                    Delete Formatting Template`

**Managing through RDA Portal**

*   In RDA Portal, Click **Home Menu** -> **Configuration** -> **Rda Administration** -> **Formatting Templates**

[![Formatting Templates](https://bot-docs.cloudfabrix.io/images/guide/formatting_templates.png)](/images/guide/formatting_templates.png)

**Managing through RDA Studio**

*   Both RDA Studio & RDA Fabric share this artifact
*   In RDA Studio, Select Task 'Formatting Templates: Edit'

[![Studio Format](https://bot-docs.cloudfabrix.io/images/guide/studio_fmt1.png)](/images/guide/studio_fmt1.png)

**Examples**

*   [Example Formatting Templates](https://bot-docs.cloudfabrix.io/Formatting-Templates/)
    

* * *

2\. Credentials
---------------

Credentials to various systems / integrations are stored securely in RDA Fabric Vault, encrypted using [Fernet](https://github.com/fernet/spec/blob/master/Spec.md)
 that uses 256 bit key. RDAF also uses a unique salt for each encryption.

**Storage Location**

*   In RDA Fabric / RDA Portal: RDAF Object Storage
*   In Studio: Stores locally inside container or on mounted volume.
*   RDA Fabric & Studio **DO NOT** share credentials. Each one must be configured separately.

**Related RDA Client CLI Commands**

`[](#__codelineno-2-1) rdac secret -h`

[Example Output](#__tabbed_2_1)

`[](#__codelineno-3-1) Credentials (Secrets) management commands [](#__codelineno-3-2) [](#__codelineno-3-3) Following are valid sub-commands for secret: [](#__codelineno-3-4)   types                     List of all available secret types [](#__codelineno-3-5)   add                       Add a new secret to the vault [](#__codelineno-3-6)   delete                    Delete a secret from the vault [](#__codelineno-3-7)   list                      List names and types of all secrets in vault`

[See RDA CLI Guide for installation instructions](/beginners_guide/rdac/)

**Managing through RDA Portal**

*   In RDA Portal, Click **Home Menu** -> **Configuration** -> **Rda Integrations** -> **Credentials**

[![Credentials](https://bot-docs.cloudfabrix.io/images/guide/credentials.png)](/images/guide/credentials.png)

**Managing through RDA Studio**

*   RDA Studio & RDA Fabric **DO NOT** share this artifact
*   In RDA Studio, Select Task 'Administration: Manage Bot Sources'

[![Studio Botadmin](https://bot-docs.cloudfabrix.io/images/guide/studio_botadmin.png)](/images/guide/studio_botadmin.png)

* * *

3\. Bookmarks
-------------

RDA Fabric uses Bookmarks as a way to remember how far each data stream has been read. It ensures that future data polls / pulls continue with rest of the data after the bookmarked point. Bookmarks typically stores timestamps or document IDs. Bookmarks are only managed via bots.

**Storage Location**

> **RDAF Object Storage**

**Related Bots**

*   [@c:bookmark-loop](https://bot-docs.cloudfabrix.io/Bots/control/#bot-cbookmark-loop)
    
*   [@dm:bookmark-list](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#bot-dmbookmark-list)
    
*   [@dm:load-bookmark](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#bot-dmload-bookmark)
    
*   [@dm:save-bookmark](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#bot-dmsave-bookmark)
    
*   [@dm:query-persistent-stream-from-bookmark](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#bot-dmquery-persistent-stream-from-bookmark)
    

* * *

4\. Pipelines
-------------

In RDA, Pipelines are low code lines of text to manage data. Each pipeline is usually built using a series of **Bots** and **Parameters** to control the behavior of that bot.

**Storage Location** \* In RDA Fabric / RDA Portal: RDAF Object Storage \* In Studio: Stores locally inside docker container or on a mounted volume. \* RDA Fabric & Studio **DO NOT** share pipelines. Using RDA Studio, Pipelines can be **published** to push pipelines to RDA Fabric.

**Related Bots**

*   [@exec:run-pipeline](https://bot-docs.cloudfabrix.io/Bots/exec/#run-pipeline)
    
*   [@exec:run-pipeline-by-row](https://bot-docs.cloudfabrix.io/Bots/exec/#run-pipeline-by-row)
    
*   [@exec:run-pipeline-multi-proc](https://bot-docs.cloudfabrix.io/Bots/exec/#run-pipeline-multi-proc)
    
*   [@exec:run-pipeline-by-row-multi-proc](https://bot-docs.cloudfabrix.io/Bots/exec/#run-pipeline-by-row-multi-proc)
    

**Related RDA Client CLI Commands**

  `[](#__codelineno-4-1)   pipeline-delete           Delete pipeline by name and version [](#__codelineno-4-2)   pipeline-get              Get pipeline by name and version [](#__codelineno-4-3)   pipeline-get-versions     Get versions for the pipeline [](#__codelineno-4-4)   pipeline-list             List published pipelines [](#__codelineno-4-5)   pipeline-publish          Publish the pipeline on a worker pod [](#__codelineno-4-6)   pipeline-published-run    Run a published pipeline on a worker pod [](#__codelineno-4-7)   pipeline-convert-to-json  Convert all pipelines in folder from yaml to json [](#__codelineno-4-8)   run                       Run a pipeline on a worker pod [](#__codelineno-4-9)   run-get-output            Run a pipeline on a worker pod, wait for completion and get output [](#__codelineno-4-10)   watch-logs                Start watching logs produced by the pipelines [](#__codelineno-4-11)   watch-traces              Start watching traces produced by the pipelines`

[See RDA CLI Guide for installation instructions](/beginners_guide/rdac/)

**Managing through RDA Portal**

*   Go to **Home Menu** -> Click **Configuration** -> **Rda Administration** -> Click **Pipelines** -> **Published Pipelines**
    
*   Typically pipelines are developed, debugged & verified in RDA Studio and then published to RDA Fabric for execution.
    
*   Following is an example view of RDA Pipeline Builder.
    

[![Portal Pipeline Builder](https://bot-docs.cloudfabrix.io/images/guide/portal_pipeline_builder1.png)](/images/guide/portal_pipeline_builder1.png)

**Managing through RDA Studio**

*   RDA Studio & RDA Fabric **DO NOT** share this artifact
*   In RDA Studio, Select Task 'Pipelines: Add a New Pipeline' or 'Pipelines: Edit a Pipeline'

[![Studio Pipeline Edit](https://bot-docs.cloudfabrix.io/images/guide/studio_pipeline_edit.png)](/images/guide/studio_pipeline_edit.png)

[![Studio Pipeline Run](https://bot-docs.cloudfabrix.io/images/guide/studio_pipeline_run.png)](/images/guide/studio_pipeline_run.png)

**Examples**

*   [Example Pipelines](https://bot-docs.cloudfabrix.io/#explore-example-pipelines)
    

* * *

5\. Service Blueprints
----------------------

Service Blueprints help manage life cycle of one more pipelines, and related artifacts, collectively as a single service.

Service Blueprints are created in YAML format.

**Storage Location**

*   In RDA Fabric / RDA Portal: RDAF Object Storage
*   Not supported in RDA Studio.

**Related RDA Client CLI Commands**

    `[](#__codelineno-5-1)     deployment-activity       List recent deployment activities [](#__codelineno-5-2)     deployment-add            Add a new Deployment to the repository.  [](#__codelineno-5-3)                               Deployment specification must be in valid YML format [](#__codelineno-5-4)     deployment-audit-report   Display Audit report for a given deployment ID [](#__codelineno-5-5)     deployment-delete         Delete an existing deployment from repository [](#__codelineno-5-6)     deployment-dependencies   List all artifact dependencies used by the deployment [](#__codelineno-5-7)     deployment-disable        Disable an existing deployment if it is not already disabled [](#__codelineno-5-8)     deployment-enable         Enable an existing deployment if it is not already enabled [](#__codelineno-5-9)     deployment-map            Print service map information in JSON format for the given deployment [](#__codelineno-5-10)     deployment-status         Display status of all deployments [](#__codelineno-5-11)     deployment-svcs-status    List current status of all service pipelines in a deployment`

[See RDA CLI Guide for installation instructions](/beginners_guide/rdac/)

> **Note**: The term `deployment` in CLI commands refers to Service Blueprints.

**Managing through RDA Portal**

*   Go to **Home Menu** -> Click **Configuration** -> **Rda Administration** -> **Service Blueprints** -> **Add**
    
*   **cfxCloud** offers a set of pre-built Service Blueprints. In **Home** screen, Click `Add +` action next to Services, to import pre-built blueprints.
    

[![Add Servicebp](https://bot-docs.cloudfabrix.io/images/guide/add_servicebp.png)](/images/guide/add_servicebp.png)

**Managing through RDA Studio**

*   Not supported

**Examples**

> See [Beginner's Guide: Deploying service blueprint in RDA Portal](/beginners_guide/#14-deploying-service-blueprint-in-rda-portal)
>  for an example.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!