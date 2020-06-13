<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/translate/v3/translation_service.proto

namespace Google\Cloud\Translate\V3;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * The batch translation request.
 *
 * Generated from protobuf message <code>google.cloud.translation.v3.BatchTranslateTextRequest</code>
 */
class BatchTranslateTextRequest extends \Google\Protobuf\Internal\Message
{
    /**
     * Required. Location to make a call. Must refer to a caller's project.
     * Format: `projects/{project-number-or-id}/locations/{location-id}`.
     * The `global` location is not supported for batch translation.
     * Only AutoML Translation models or glossaries within the same region (have
     * the same location-id) can be used, otherwise an INVALID_ARGUMENT (400)
     * error is returned.
     *
     * Generated from protobuf field <code>string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = {</code>
     */
    private $parent = '';
    /**
     * Required. Source language code.
     *
     * Generated from protobuf field <code>string source_language_code = 2 [(.google.api.field_behavior) = REQUIRED];</code>
     */
    private $source_language_code = '';
    /**
     * Required. Specify up to 10 language codes here.
     *
     * Generated from protobuf field <code>repeated string target_language_codes = 3 [(.google.api.field_behavior) = REQUIRED];</code>
     */
    private $target_language_codes;
    /**
     * Optional. The models to use for translation. Map's key is target language
     * code. Map's value is model name. Value can be a built-in general model,
     * or an AutoML Translation model.
     * The value format depends on model type:
     * - AutoML Translation models:
     *   `projects/{project-number-or-id}/locations/{location-id}/models/{model-id}`
     * - General (built-in) models:
     *   `projects/{project-number-or-id}/locations/{location-id}/models/general/nmt`,
     *   `projects/{project-number-or-id}/locations/{location-id}/models/general/base`
     * If the map is empty or a specific model is
     * not requested for a language pair, then default google model (nmt) is used.
     *
     * Generated from protobuf field <code>map<string, string> models = 4 [(.google.api.field_behavior) = OPTIONAL];</code>
     */
    private $models;
    /**
     * Required. Input configurations.
     * The total number of files matched should be <= 1000.
     * The total content size should be <= 100M Unicode codepoints.
     * The files must use UTF-8 encoding.
     *
     * Generated from protobuf field <code>repeated .google.cloud.translation.v3.InputConfig input_configs = 5 [(.google.api.field_behavior) = REQUIRED];</code>
     */
    private $input_configs;
    /**
     * Required. Output configuration.
     * If 2 input configs match to the same file (that is, same input path),
     * we don't generate output for duplicate inputs.
     *
     * Generated from protobuf field <code>.google.cloud.translation.v3.OutputConfig output_config = 6 [(.google.api.field_behavior) = REQUIRED];</code>
     */
    private $output_config = null;
    /**
     * Optional. Glossaries to be applied for translation.
     * It's keyed by target language code.
     *
     * Generated from protobuf field <code>map<string, .google.cloud.translation.v3.TranslateTextGlossaryConfig> glossaries = 7 [(.google.api.field_behavior) = OPTIONAL];</code>
     */
    private $glossaries;
    /**
     * Optional. The labels with user-defined metadata for the request.
     * Label keys and values can be no longer than 63 characters
     * (Unicode codepoints), can only contain lowercase letters, numeric
     * characters, underscores and dashes. International characters are allowed.
     * Label values are optional. Label keys must start with a letter.
     * See https://cloud.google.com/translate/docs/labels for more information.
     *
     * Generated from protobuf field <code>map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];</code>
     */
    private $labels;

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type string $parent
     *           Required. Location to make a call. Must refer to a caller's project.
     *           Format: `projects/{project-number-or-id}/locations/{location-id}`.
     *           The `global` location is not supported for batch translation.
     *           Only AutoML Translation models or glossaries within the same region (have
     *           the same location-id) can be used, otherwise an INVALID_ARGUMENT (400)
     *           error is returned.
     *     @type string $source_language_code
     *           Required. Source language code.
     *     @type string[]|\Google\Protobuf\Internal\RepeatedField $target_language_codes
     *           Required. Specify up to 10 language codes here.
     *     @type array|\Google\Protobuf\Internal\MapField $models
     *           Optional. The models to use for translation. Map's key is target language
     *           code. Map's value is model name. Value can be a built-in general model,
     *           or an AutoML Translation model.
     *           The value format depends on model type:
     *           - AutoML Translation models:
     *             `projects/{project-number-or-id}/locations/{location-id}/models/{model-id}`
     *           - General (built-in) models:
     *             `projects/{project-number-or-id}/locations/{location-id}/models/general/nmt`,
     *             `projects/{project-number-or-id}/locations/{location-id}/models/general/base`
     *           If the map is empty or a specific model is
     *           not requested for a language pair, then default google model (nmt) is used.
     *     @type \Google\Cloud\Translate\V3\InputConfig[]|\Google\Protobuf\Internal\RepeatedField $input_configs
     *           Required. Input configurations.
     *           The total number of files matched should be <= 1000.
     *           The total content size should be <= 100M Unicode codepoints.
     *           The files must use UTF-8 encoding.
     *     @type \Google\Cloud\Translate\V3\OutputConfig $output_config
     *           Required. Output configuration.
     *           If 2 input configs match to the same file (that is, same input path),
     *           we don't generate output for duplicate inputs.
     *     @type array|\Google\Protobuf\Internal\MapField $glossaries
     *           Optional. Glossaries to be applied for translation.
     *           It's keyed by target language code.
     *     @type array|\Google\Protobuf\Internal\MapField $labels
     *           Optional. The labels with user-defined metadata for the request.
     *           Label keys and values can be no longer than 63 characters
     *           (Unicode codepoints), can only contain lowercase letters, numeric
     *           characters, underscores and dashes. International characters are allowed.
     *           Label values are optional. Label keys must start with a letter.
     *           See https://cloud.google.com/translate/docs/labels for more information.
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Google\Cloud\Translate\V3\TranslationService::initOnce();
        parent::__construct($data);
    }

    /**
     * Required. Location to make a call. Must refer to a caller's project.
     * Format: `projects/{project-number-or-id}/locations/{location-id}`.
     * The `global` location is not supported for batch translation.
     * Only AutoML Translation models or glossaries within the same region (have
     * the same location-id) can be used, otherwise an INVALID_ARGUMENT (400)
     * error is returned.
     *
     * Generated from protobuf field <code>string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = {</code>
     * @return string
     */
    public function getParent()
    {
        return $this->parent;
    }

    /**
     * Required. Location to make a call. Must refer to a caller's project.
     * Format: `projects/{project-number-or-id}/locations/{location-id}`.
     * The `global` location is not supported for batch translation.
     * Only AutoML Translation models or glossaries within the same region (have
     * the same location-id) can be used, otherwise an INVALID_ARGUMENT (400)
     * error is returned.
     *
     * Generated from protobuf field <code>string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = {</code>
     * @param string $var
     * @return $this
     */
    public function setParent($var)
    {
        GPBUtil::checkString($var, True);
        $this->parent = $var;

        return $this;
    }

    /**
     * Required. Source language code.
     *
     * Generated from protobuf field <code>string source_language_code = 2 [(.google.api.field_behavior) = REQUIRED];</code>
     * @return string
     */
    public function getSourceLanguageCode()
    {
        return $this->source_language_code;
    }

    /**
     * Required. Source language code.
     *
     * Generated from protobuf field <code>string source_language_code = 2 [(.google.api.field_behavior) = REQUIRED];</code>
     * @param string $var
     * @return $this
     */
    public function setSourceLanguageCode($var)
    {
        GPBUtil::checkString($var, True);
        $this->source_language_code = $var;

        return $this;
    }

    /**
     * Required. Specify up to 10 language codes here.
     *
     * Generated from protobuf field <code>repeated string target_language_codes = 3 [(.google.api.field_behavior) = REQUIRED];</code>
     * @return \Google\Protobuf\Internal\RepeatedField
     */
    public function getTargetLanguageCodes()
    {
        return $this->target_language_codes;
    }

    /**
     * Required. Specify up to 10 language codes here.
     *
     * Generated from protobuf field <code>repeated string target_language_codes = 3 [(.google.api.field_behavior) = REQUIRED];</code>
     * @param string[]|\Google\Protobuf\Internal\RepeatedField $var
     * @return $this
     */
    public function setTargetLanguageCodes($var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::STRING);
        $this->target_language_codes = $arr;

        return $this;
    }

    /**
     * Optional. The models to use for translation. Map's key is target language
     * code. Map's value is model name. Value can be a built-in general model,
     * or an AutoML Translation model.
     * The value format depends on model type:
     * - AutoML Translation models:
     *   `projects/{project-number-or-id}/locations/{location-id}/models/{model-id}`
     * - General (built-in) models:
     *   `projects/{project-number-or-id}/locations/{location-id}/models/general/nmt`,
     *   `projects/{project-number-or-id}/locations/{location-id}/models/general/base`
     * If the map is empty or a specific model is
     * not requested for a language pair, then default google model (nmt) is used.
     *
     * Generated from protobuf field <code>map<string, string> models = 4 [(.google.api.field_behavior) = OPTIONAL];</code>
     * @return \Google\Protobuf\Internal\MapField
     */
    public function getModels()
    {
        return $this->models;
    }

    /**
     * Optional. The models to use for translation. Map's key is target language
     * code. Map's value is model name. Value can be a built-in general model,
     * or an AutoML Translation model.
     * The value format depends on model type:
     * - AutoML Translation models:
     *   `projects/{project-number-or-id}/locations/{location-id}/models/{model-id}`
     * - General (built-in) models:
     *   `projects/{project-number-or-id}/locations/{location-id}/models/general/nmt`,
     *   `projects/{project-number-or-id}/locations/{location-id}/models/general/base`
     * If the map is empty or a specific model is
     * not requested for a language pair, then default google model (nmt) is used.
     *
     * Generated from protobuf field <code>map<string, string> models = 4 [(.google.api.field_behavior) = OPTIONAL];</code>
     * @param array|\Google\Protobuf\Internal\MapField $var
     * @return $this
     */
    public function setModels($var)
    {
        $arr = GPBUtil::checkMapField($var, \Google\Protobuf\Internal\GPBType::STRING, \Google\Protobuf\Internal\GPBType::STRING);
        $this->models = $arr;

        return $this;
    }

    /**
     * Required. Input configurations.
     * The total number of files matched should be <= 1000.
     * The total content size should be <= 100M Unicode codepoints.
     * The files must use UTF-8 encoding.
     *
     * Generated from protobuf field <code>repeated .google.cloud.translation.v3.InputConfig input_configs = 5 [(.google.api.field_behavior) = REQUIRED];</code>
     * @return \Google\Protobuf\Internal\RepeatedField
     */
    public function getInputConfigs()
    {
        return $this->input_configs;
    }

    /**
     * Required. Input configurations.
     * The total number of files matched should be <= 1000.
     * The total content size should be <= 100M Unicode codepoints.
     * The files must use UTF-8 encoding.
     *
     * Generated from protobuf field <code>repeated .google.cloud.translation.v3.InputConfig input_configs = 5 [(.google.api.field_behavior) = REQUIRED];</code>
     * @param \Google\Cloud\Translate\V3\InputConfig[]|\Google\Protobuf\Internal\RepeatedField $var
     * @return $this
     */
    public function setInputConfigs($var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::MESSAGE, \Google\Cloud\Translate\V3\InputConfig::class);
        $this->input_configs = $arr;

        return $this;
    }

    /**
     * Required. Output configuration.
     * If 2 input configs match to the same file (that is, same input path),
     * we don't generate output for duplicate inputs.
     *
     * Generated from protobuf field <code>.google.cloud.translation.v3.OutputConfig output_config = 6 [(.google.api.field_behavior) = REQUIRED];</code>
     * @return \Google\Cloud\Translate\V3\OutputConfig
     */
    public function getOutputConfig()
    {
        return $this->output_config;
    }

    /**
     * Required. Output configuration.
     * If 2 input configs match to the same file (that is, same input path),
     * we don't generate output for duplicate inputs.
     *
     * Generated from protobuf field <code>.google.cloud.translation.v3.OutputConfig output_config = 6 [(.google.api.field_behavior) = REQUIRED];</code>
     * @param \Google\Cloud\Translate\V3\OutputConfig $var
     * @return $this
     */
    public function setOutputConfig($var)
    {
        GPBUtil::checkMessage($var, \Google\Cloud\Translate\V3\OutputConfig::class);
        $this->output_config = $var;

        return $this;
    }

    /**
     * Optional. Glossaries to be applied for translation.
     * It's keyed by target language code.
     *
     * Generated from protobuf field <code>map<string, .google.cloud.translation.v3.TranslateTextGlossaryConfig> glossaries = 7 [(.google.api.field_behavior) = OPTIONAL];</code>
     * @return \Google\Protobuf\Internal\MapField
     */
    public function getGlossaries()
    {
        return $this->glossaries;
    }

    /**
     * Optional. Glossaries to be applied for translation.
     * It's keyed by target language code.
     *
     * Generated from protobuf field <code>map<string, .google.cloud.translation.v3.TranslateTextGlossaryConfig> glossaries = 7 [(.google.api.field_behavior) = OPTIONAL];</code>
     * @param array|\Google\Protobuf\Internal\MapField $var
     * @return $this
     */
    public function setGlossaries($var)
    {
        $arr = GPBUtil::checkMapField($var, \Google\Protobuf\Internal\GPBType::STRING, \Google\Protobuf\Internal\GPBType::MESSAGE, \Google\Cloud\Translate\V3\TranslateTextGlossaryConfig::class);
        $this->glossaries = $arr;

        return $this;
    }

    /**
     * Optional. The labels with user-defined metadata for the request.
     * Label keys and values can be no longer than 63 characters
     * (Unicode codepoints), can only contain lowercase letters, numeric
     * characters, underscores and dashes. International characters are allowed.
     * Label values are optional. Label keys must start with a letter.
     * See https://cloud.google.com/translate/docs/labels for more information.
     *
     * Generated from protobuf field <code>map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];</code>
     * @return \Google\Protobuf\Internal\MapField
     */
    public function getLabels()
    {
        return $this->labels;
    }

    /**
     * Optional. The labels with user-defined metadata for the request.
     * Label keys and values can be no longer than 63 characters
     * (Unicode codepoints), can only contain lowercase letters, numeric
     * characters, underscores and dashes. International characters are allowed.
     * Label values are optional. Label keys must start with a letter.
     * See https://cloud.google.com/translate/docs/labels for more information.
     *
     * Generated from protobuf field <code>map<string, string> labels = 9 [(.google.api.field_behavior) = OPTIONAL];</code>
     * @param array|\Google\Protobuf\Internal\MapField $var
     * @return $this
     */
    public function setLabels($var)
    {
        $arr = GPBUtil::checkMapField($var, \Google\Protobuf\Internal\GPBType::STRING, \Google\Protobuf\Internal\GPBType::STRING);
        $this->labels = $arr;

        return $this;
    }

}

