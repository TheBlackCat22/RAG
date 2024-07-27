 



Schedule Pipelines within Service Blueprints
============================================

**Scheduled Pipelines Section (`scheduled_pipelines`)**

Instead of having **Service Pipeline** that always run, the user can have the pipelines to run on a schedule basis.

Here is a sample blueprint with scheduled pipeline definitions. It has the following scheduled pipeline definitions:

*   `sample-scheduled-pipeline-1`: Executes once a day at a certain time
*   `sample-scheduled-pipeline-3`: Executes every 30 minutes
*   `sample-scheduled-pipeline-3`: Incorrect schedule

|     |     |
| --- | --- |
| [1](#__codelineno-0-1)<br> [2](#__codelineno-0-2)<br> [3](#__codelineno-0-3)<br> [4](#__codelineno-0-4)<br> [5](#__codelineno-0-5)<br> [6](#__codelineno-0-6)<br> [7](#__codelineno-0-7)<br> [8](#__codelineno-0-8)<br> [9](#__codelineno-0-9)<br>[10](#__codelineno-0-10)<br>[11](#__codelineno-0-11)<br>[12](#__codelineno-0-12)<br>[13](#__codelineno-0-13)<br>[14](#__codelineno-0-14)<br>[15](#__codelineno-0-15)<br>[16](#__codelineno-0-16)<br>[17](#__codelineno-0-17)<br>[18](#__codelineno-0-18)<br>[19](#__codelineno-0-19)<br>[20](#__codelineno-0-20)<br>[21](#__codelineno-0-21)<br>[22](#__codelineno-0-22)<br>[23](#__codelineno-0-23)<br>[24](#__codelineno-0-24)<br>[25](#__codelineno-0-25)<br>[26](#__codelineno-0-26) | `name: Sample Scheduled Blueprint id: sample scheduled blueprint category: sample type: Service provider: CloudFabrix Software, Inc. scheduled_pipelines:     -   name: sample-scheduled-pipeline-1         label: Sample scheduled pipeline 1         version: '*'         site: rda.*         cron_expression: 0 12 * * *         site_type: regex     -   name: sample-scheduled-pipeline-2         label: Sample scheduled pipeline 2         version: '*'         site: rda.*         cron_expression: '*/30 * * * *'         site_type: regex         max_execution_mins: 5     -   name: sample-scheduled-pipeline-3         label: Sample scheduled pipeline 3         version: '*'         site: rda.*         cron_expression: '* 25 * * *'         site_type: regex enabled: true` |

Scheduled Pipeline parameters:

*   `name`: Name of the Pipeline
*   `label`: Label for the Pipeline
*   `version`: Version of the pipeline to use. `*` implies any latest version of the pipeline.
*   `site_type`: Valid values are `regex` or `name`. If set to `regex`, the **site** parameter is interpreted as a regular expression. If set to `name`, the **site** parameter is interpreted as an exact name of the site. Default is `regex`
*   `site`: Either name of pattern identifying the Site for the RDA Worker(s). RDAF uses prefix `cfx-` for all workers hosted in cfxCloud.
*   `cron_expression`: Cron schedule expression. You can use `https://crontab.guru/` to come up with cron expression.
*   `max_execution_mins`: Optional field. This can be used to evict the scheduled pipeline that runs longer than expected.
*   `initialize_timeout_seconds`: Evict the job if it's stuck in Initialization for longer than the value specified. Default is 30 and that would be the minimum value we allow.
*   `restart_count_on_failure`: Number of times to retry on failure. Default value is 0. This is applicable when the job fails or gets stuck in Initialization state as well

  

Understanding **scheduled pipeline** within service blueprint details dashboard

When you drill down into **Details** of the blueprint, it would look something like this:

> ![Portal](https://bot-docs.cloudfabrix.io/images/guide/portal_bp_scheduled_audit_warning.png)
> 
> **STATUS** Tab:
> 
> *   Audit Report: Shows list of audit checks performed and their status. If any of the scheduled pipelines has an **invalid** cron expression, it will show up as a warning. Refer to the picture above.

  

> **SCHEDULED** Tab:
> 
> This tab shows current status of all `scheduled pipelines` in the blueprint. The screenshot below shows the scheduled pipeline information, related jobs etc..
> 
> ![Portal](https://bot-docs.cloudfabrix.io/images/guide/portal_bp_scheduled_tab.png)

  

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!