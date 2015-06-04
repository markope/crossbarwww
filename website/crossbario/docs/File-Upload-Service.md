## Introduction

> The *File Uploader* feature is available starting with Crossbar **0.11.1**.

The *HTTP Publisher* is a service that allows clients to submit PubSub events via HTTP/POST requests.
Crossbar will receive the event data via the request and forward the event via standard WAMP to any connected subscribers in real-time.

![](/static/img/docs/crossbar_http_publish.png)
## Try it

Clone the [Crossbar.io examples repository](https://github.com/crossbario/crossbarexamples), and go to the `file_upload_node` subdirectory.

Now start Crossbar:

```console
crossbar start
```

and open [http://localhost:8089](http://localhost:8089) in your browser. Open the JavaScript console to see file upload progress events when uploading files.


## Configuration

The *File Uploader* is configured on a path of a Web transport - here is part of a Crossbar configuration:

```javascript
{
   "workers": [
      {
         "type": "router",
         ...
         "transports": [
            {
               "type": "web",
               ...
               "paths": {
                  ...
                 "upload": {
                           "type": "fileupload",
                           "form_fields": {
                              "file_id": "resumableIdentifier",
                              "file_name": "resumableFilename",
                              "mime_type": "resumableType",
                              "total_size": "resumableTotalSize",
                              "chunk_number": "resumableChunkNumber",
                              "chunk_size": "resumableChunkSize",
                              "total_chunks": "resumableTotalChunks",
                              "content": "file",
                              "progress_uri": "progress_uri"
                           },
                           "directory": "../web_upload",
                           "temp_directory": "../temp",
                           "file_permissions": "0644",
                           "max_file_size": 209715200,
                           "file_types": [".csv", ".txt"],
                           "progress_realm": "myrealm"
                        }
            }
         ]
      }
   ]
}
```

The service dictionary has the following parameters:

option | description
---|---
**`type`** | MUST be `"fileupload"` (*required*)
**`form_fields`** | Contains the form field mapping between client POST request and backend (*required*)
**`directory`** | The folder for completely uploaded files relative to the .crossbar folder in your crossbar node. (*required*)
**`temp_directory`** | A folder to hold incomplete uploads. Each incomplete upload will be a subfolder containing the uploaded file chunks.  (*required*)
**`file_permissions`** | The file access permissions to use for the completely uploaded files. (chmod octal code)
**`max_file_size`** | The maximally allowed file size in bytes to upload. Refers to the file not to the chunks of the file. 
**`file_types`** | A JSON Array of permitted file extension strings including the dots. 
**`progress_realm`** | The realm inside which progress events may be published. (*required when progress_uri is set in the form_fields dictionary*)

The `form_fields` dictionary contains the form field names that the client uses to upload files. It has the following configuration parameters (**all required**):

 "file_id": "resumableIdentifier",
                              "file_name": "myFilename",
                              "mime_type": "my"Type",
                              "total_size": "myTotalSize",
                              "chunk_number": "myChunkNumber",
                              "chunk_size": "myChunkSize",
                              "total_chunks": "myTotalChunks",
                              "content": "myfile",
                              "progress_uri": "myprogress_uri"

option | description
---|---
**`file_id`** | The name of the field identifying the file. Two files with the same file_id are considered to be the same.
**`file_name`** | The name of the field containing the file name. (The file name is not used for anything in the backend).
**`mime_type`** | Not used but .
**`total_size`** | The name of the field to hold the integer representing the size of the file in bytes.
**`chunk_number`** | The name of the field to hold the chunk number of the current fiel chunk.
**`chunk_size`** | The name of the field holding the overall chunk size. (Currently not used in the backend)
**`total_chunks`** | The name of the field holding the total number of chunks for the file to be transfered. Needs to be POSTed with every chunk.
**`content`** | The name of the field containing the file content.
**`progress_uri`** | The name of the field containing the URI to publish upload related events to. Publish will be restricted to the globaly configured `progress_realm`. 


In the example above the file name is passsed to the backend in a POST multipart formdata field with name="myFilename") 

```html
<input ... myFilename="test.csv" myprogress_uri="my.upload.progress.uri" ... />
```

## Resumable Uploads

To implement resumable uploads crossbar file upload functionality provides a GET response on the same path. The response will either be with 

* `Status 200` which indicates that the file or chunk of file is already pressent in the backend. 
* A response with any other Status means the file/chunk is not yet present in the backend and should be uploaded.

With this service the upload client can check for existence of the chunk in the backend prior to POSTing the chunk. This effectively implements resumable uploads.

The GET response needs to have the same arguments as the POST request above.



