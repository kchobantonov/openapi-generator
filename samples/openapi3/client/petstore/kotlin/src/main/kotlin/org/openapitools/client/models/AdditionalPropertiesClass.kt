/**
* OpenAPI Petstore
* This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
*
* The version of the OpenAPI document: 1.0.0
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
package org.openapitools.client.models


import com.squareup.moshi.Json
/**
 * 
 * @param mapProperty 
 * @param mapOfMapProperty 
 */
data class AdditionalPropertiesClass (
    @Json(name = "map_property")
    val mapProperty: kotlin.collections.Map<kotlin.String, kotlin.String>? = null,
    @Json(name = "map_of_map_property")
    val mapOfMapProperty: kotlin.collections.Map<kotlin.String, kotlin.collections.Map<kotlin.String, kotlin.String>>? = null
) {

}

