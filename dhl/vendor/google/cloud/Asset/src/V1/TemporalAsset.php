<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/asset/v1/assets.proto

namespace Google\Cloud\Asset\V1;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * An asset in Google Cloud and its temporal metadata, including the time window
 * when it was observed and its status during that window.
 *
 * Generated from protobuf message <code>google.cloud.asset.v1.TemporalAsset</code>
 */
class TemporalAsset extends \Google\Protobuf\Internal\Message
{
    /**
     * The time window when the asset data and state was observed.
     *
     * Generated from protobuf field <code>.google.cloud.asset.v1.TimeWindow window = 1;</code>
     */
    private $window = null;
    /**
     * Whether the asset has been deleted or not.
     *
     * Generated from protobuf field <code>bool deleted = 2;</code>
     */
    private $deleted = false;
    /**
     * An asset in Google Cloud.
     *
     * Generated from protobuf field <code>.google.cloud.asset.v1.Asset asset = 3;</code>
     */
    private $asset = null;

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type \Google\Cloud\Asset\V1\TimeWindow $window
     *           The time window when the asset data and state was observed.
     *     @type bool $deleted
     *           Whether the asset has been deleted or not.
     *     @type \Google\Cloud\Asset\V1\Asset $asset
     *           An asset in Google Cloud.
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Google\Cloud\Asset\V1\Assets::initOnce();
        parent::__construct($data);
    }

    /**
     * The time window when the asset data and state was observed.
     *
     * Generated from protobuf field <code>.google.cloud.asset.v1.TimeWindow window = 1;</code>
     * @return \Google\Cloud\Asset\V1\TimeWindow
     */
    public function getWindow()
    {
        return $this->window;
    }

    /**
     * The time window when the asset data and state was observed.
     *
     * Generated from protobuf field <code>.google.cloud.asset.v1.TimeWindow window = 1;</code>
     * @param \Google\Cloud\Asset\V1\TimeWindow $var
     * @return $this
     */
    public function setWindow($var)
    {
        GPBUtil::checkMessage($var, \Google\Cloud\Asset\V1\TimeWindow::class);
        $this->window = $var;

        return $this;
    }

    /**
     * Whether the asset has been deleted or not.
     *
     * Generated from protobuf field <code>bool deleted = 2;</code>
     * @return bool
     */
    public function getDeleted()
    {
        return $this->deleted;
    }

    /**
     * Whether the asset has been deleted or not.
     *
     * Generated from protobuf field <code>bool deleted = 2;</code>
     * @param bool $var
     * @return $this
     */
    public function setDeleted($var)
    {
        GPBUtil::checkBool($var);
        $this->deleted = $var;

        return $this;
    }

    /**
     * An asset in Google Cloud.
     *
     * Generated from protobuf field <code>.google.cloud.asset.v1.Asset asset = 3;</code>
     * @return \Google\Cloud\Asset\V1\Asset
     */
    public function getAsset()
    {
        return $this->asset;
    }

    /**
     * An asset in Google Cloud.
     *
     * Generated from protobuf field <code>.google.cloud.asset.v1.Asset asset = 3;</code>
     * @param \Google\Cloud\Asset\V1\Asset $var
     * @return $this
     */
    public function setAsset($var)
    {
        GPBUtil::checkMessage($var, \Google\Cloud\Asset\V1\Asset::class);
        $this->asset = $var;

        return $this;
    }

}
