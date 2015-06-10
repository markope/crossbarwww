## Introduction

> The *File Uploader* feature is available starting with Crossbar.io **0.11.0**.

The **File Upload Service** allows uploading of files to a directory on the Crossbar.io node via (chunked) HTTP/POSTs. E.g. modern browsers [support](http://caniuse.com/#feat=fileapi) the [HTML5 File API](http://www.w3.org/TR/FileAPI/) which allows users to select files from their local system to be uploaded by the browser. This service can handle big files (GBs) and when combined with [Resumable.js](http://www.resumablejs.com/) features:

* upload one or multiple files
* chunked uploading
* select or drag & drop to upload
* resuming uploads
* progress indication via WAMP PubSub events


## Try it

We have a [complete example](https://github.com/crossbario/crossbarexamples/tree/master/fileupload) in the [Crossbar.io examples repository](https://github.com/crossbario/crossbarexamples) repository.

Clone the repo, change to the example folder `fileupload` and start Crossbar.io:

```console
crossbar start
```

Open [http://localhost:8080](http://localhost:8080) in your browser. Open the JavaScript console to see file upload progress events when uploading files. Then either click **Select files to upload** or drop files to **Drop files here to upload**. The uploaded files will appear within the `uploaded` subdirectory in the example folder.


## Configuration

The *File Uploader* is configured on a path of a Web transport - here is part of a Crossbar configuration:

```javascript
{
   "workers": [{
      "type": "router",
      ...
      "transports": [{
         "type": "web",
         ...
         "paths": {
            ...
            "upload": {
               "type": "upload",
               "realm": "realm1",
               "role": "anonymous",
               "directory": "../uploaded",
               "temp_directory": "../temp",
               "form_fields": {
                  "file_name": "resumableFilename",
                  "mime_type": "resumableType",
                  "total_size": "resumableTotalSize",
                  "chunk_number": "resumableChunkNumber",
                  "chunk_size": "resumableChunkSize",
                  "total_chunks": "resumableTotalChunks",
                  "content": "file",
                  "on_progress": "on_progress",
                  "session": "session"
               },
               "options": {
                  "max_file_size": 209715200,
                  "file_permissions": "0644",
                  "file_types": [".csv", ".txt", ".pdf", ".img"]
               }
            }
         }
      }]
   }]
}
```

The service dictionary has the following parameters:

option | description
---|---
**`type`** | MUST be `"fileupload"` (*required*)
**`form_fields`** | Contains the form field mapping between client POST request and backend (*required*)
**`directory`** | The folder for completely uploaded files relative to the .crossbar folder in your crossbar node. (*required*)
**`temp_directory`** | A folder to hold incomplete uploads. Each incomplete upload will be a subfolder containing the uploaded file chunks. (*required*)
**`file_permissions`** | The file access permissions to use for the completely uploaded files. (chmod octal code)
**`max_file_size`** | The maximally allowed file size in bytes to upload. Refers to the file not to the chunks of the file.
**`file_types`** | A JSON Array of permitted file extension strings including the dots.
**`progress_realm`** | The realm inside which progress events may be published. (*required when progress_uri is set in the form_fields dictionary*)

The `form_fields` dictionary contains the form field names that the client uses to upload files. It has the following configuration parameters (**all required**):

```javascript
"form_fields": {
   "file_name": "resumableFilename",
   "mime_type": "resumableType",
   "total_size": "resumableTotalSize",
   "chunk_number": "resumableChunkNumber",
   "chunk_size": "resumableChunkSize",
   "total_chunks": "resumableTotalChunks",
   "content": "file",
   "on_progress": "on_progress"
}
```

option | description
---|---
**`file_name`** | The name of the form field containing the file name. (The file name is not used for anything in the backend). (*required*)
**`mime_type`** | The name of the form field to hold the MIME type of the uploaded file. (*required*)
**`total_size`** | The name of the form field to hold the integer representing the size of the file in bytes. (*required*)
**`chunk_number`** | The name of the form field to hold the chunk number of the current file chunk. (*required*)
**`chunk_size`** | The name of the form field holding the chunk size. (*required*)
**`total_chunks`** | The name of the form field holding the total number of chunks for the file to be transfered. Needs to be POSTed with every chunk. (*required*)
**`content`** | The name of the form field containing the file content. (*required*)
**`progress_uri`** | The name of the form field containing the URI to publish upload related events to. Publish will be restricted to the globaly configured `progress_realm`.


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
