<?php 
  require '../vendor/autoload.php';
  use Google\Cloud\Core\ServiceBuilder;

  $gcloud = new ServiceBuilder([
      'keyFilePath' => 'gjson.json',
      'projectId' => 'supple-folder-256709'
  ]);

  $storage = $gcloud->storage();

  
  $mode = "";
  $session = "a";
  $date = "a";
  $routeID = "a";
  $fileName = "";

  $bucket = $storage->bucket('real-bucket-dhl/');
  $json = Null;
  if(!$bucket){
    #show no bucket not exist
  } else {
    $option = [];
    $option["prefix"] = "/files/february/" . "20200201";
    // $option["delimeter"] = "";
    $object = $bucket->objects($option);
    if(!$object) {
      #show file no exist\
      print_r($object);
    } else {


      foreach ($object as $key => $value) {
        # code...

        print($value->downloadAsString());
        print("DELIMETER HERE !");
      }

      // print_r($object);
      // $json = $object->downloadAsString();
    }
  }

  // $blob = $bucket.get_blob("testing1.json ");

  // $file = $storage->objects->get($bucket, $object, ['alt' => 'media']);


  // $a = $bucket->file_get_contents("https://storage.googleapis.com/" . "testing1.json");

  // $json_data_bytes = $blob.download_as_string();
  // print_r($json);

?>