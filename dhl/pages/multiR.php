<?php 
  include_once "../utility/packed_library.php";

  use Google\Cloud\Core\ServiceBuilder;

  $gcloud = new ServiceBuilder([
      'keyFilePath' => '../../../gjson.json',
      'projectId' => 'supple-folder-256709'
  ]);

  $storage = $gcloud->storage();

  $bucket = $storage->bucket('real-bucket-dhl');
  $json = Null;
  if(!$bucket){
    #show no bucket not exist
  } else {
    $option = [];
    $option["prefix"] = "single_date_path";
    // $option["delimeter"] = "";
    $object = $bucket->objects($option);
    if(!$object) {
      #show file no exist\
      // print_r($object);
    } else {


      $selectionList = [];
      foreach ($object as $key => $value) {
        # code...

        // print($value->downloadAsString());
        // print "<pre>";

        // print_r($value->name());
        $string = $value->name();

        $fileName = explode("/", $string);
        $label = $fileName[1] . "/" . $fileName[2];
        $fileName = explode(".", end($fileName));
        // print_r("</br>");
        // print_r($a); 
        if($fileName[0] == "input") {
          continue;
        }
        // $selectionList[$a[1]] = $a[1];
        $selectionList[$string] = $label;
        // print_r($value->identity());
        // print "</pre>";

        // print("DELIMETER HERE !");
      }
      // print_r($selectionList);

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
<?php include_once "template/header.php"; ?>

<body>
      <div class="wrapper">
        <div class="sidebar" data-image="../assets/img/sidebar-5.jpg">
<?php include_once "template/sidebar.php"; ?>
        </div>

<div class="main-panel">
<?php include_once "template/nav.php"; ?>
  <div class="content">

  <div style="margin:20px 0 25px 0;">
   <div class="form-group">
    <form action="route.php" method="post" id="form1" name="form1">
      <label for="select-response-date">select with date/session</label>
      <select id="select-response-date" name="fileName" class="form-control" form="form1">
        <?php foreach($selectionList as $key => $value): ?>
          <<?= "option value = ". $key ?>> <?= $value ?> </option>
        <?php endforeach; ?> 
      </select>
      <input type="hidden" value="singe-date" name="mode">
      <input type="submit" value="Submit">

    </form>
</div>



</div>

<?php include_once "template/footer.php"; ?>
</div>

  </body>
  <script type="text/javascript">
    $("#select-response-date").change(function (e){
      val = $(this).val();
      // $.post( "route.php", {mode : "singe-date", fileName: val} );
    });
  </script>