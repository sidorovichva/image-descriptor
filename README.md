The service accepts link to an image online and returns description of the image in english.

Currently works with two transformers: 
  Salesforce/blip-image-captioning-base
  nlpconnect/vit-gpt2-image-captioning

API: 
  Describes an image
  path: /image/describe 
  RequestParams: 
    path: a link to an image
    transformer_name: a name of the transformer to use (default is blip)
  returns: a dictionary {link -> description}

  Describes images from test set
  path: /image/test 
  RequestParams: 
    transformer_name: a name of the transformer to use (default is blip)
  returns: a list of dictionaries {link -> description}


Installed locally download model files at first use and than works with the local model
