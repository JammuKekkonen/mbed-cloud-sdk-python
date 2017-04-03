# coding: utf-8

"""
    Connect Statistics API

    mbed Cloud Connect Statistics API provides statistics about other cloud services through defined counters.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AccountApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def v3_metrics_get(self, include, start, end, period, interval, authorization, **kwargs):
        """
        Provides account-specific statistics for other cloud services.
        This REST API is used to get account-specific statistics.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_metrics_get(include, start, end, period, interval, authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str include: A comma-separated list of requested metrics. Supported values are:  - `transactions` - `bootstraps_successful` - `bootstraps_failed` - `bootstraps_pending` - `device_server_rest_api_success` - `device_server_rest_api_error`  (required)
        :param str start: UTC time/year/date in RFC3339 format. Fetch the data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207. The parameter is not mandatory, if the period is specified.  (required)
        :param str end: UTC time/year/date in RFC3339 format. Fetch the data with timestamp less than this value.Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207.The parameter is not mandatory, if the period is specified.  (required)
        :param str period: Period. Fetch the data for the period in days, weeks or hours. Sample values: 2h, 3w, 4d. The parameter is not mandatory, if the start and end time are specified.  (required)
        :param str interval: Group data by this interval in days, weeks or hours. Sample values: 2h, 3w, 4d.  (required)
        :param str authorization: Bearer {Access Token}. A valid API Gateway access token. The token is validated and the associated account identifier is used to retrieve account-specific statistics.  (required)
        :return: SuccessfulResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v3_metrics_get_with_http_info(include, start, end, period, interval, authorization, **kwargs)
        else:
            (data) = self.v3_metrics_get_with_http_info(include, start, end, period, interval, authorization, **kwargs)
            return data

    def v3_metrics_get_with_http_info(self, include, start, end, period, interval, authorization, **kwargs):
        """
        Provides account-specific statistics for other cloud services.
        This REST API is used to get account-specific statistics.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v3_metrics_get_with_http_info(include, start, end, period, interval, authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str include: A comma-separated list of requested metrics. Supported values are:  - `transactions` - `bootstraps_successful` - `bootstraps_failed` - `bootstraps_pending` - `device_server_rest_api_success` - `device_server_rest_api_error`  (required)
        :param str start: UTC time/year/date in RFC3339 format. Fetch the data with timestamp greater than or equal to this value. Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207. The parameter is not mandatory, if the period is specified.  (required)
        :param str end: UTC time/year/date in RFC3339 format. Fetch the data with timestamp less than this value.Sample values: 20170207T092056990Z/2017-02-07T09:20:56.990Z/2017/20170207.The parameter is not mandatory, if the period is specified.  (required)
        :param str period: Period. Fetch the data for the period in days, weeks or hours. Sample values: 2h, 3w, 4d. The parameter is not mandatory, if the start and end time are specified.  (required)
        :param str interval: Group data by this interval in days, weeks or hours. Sample values: 2h, 3w, 4d.  (required)
        :param str authorization: Bearer {Access Token}. A valid API Gateway access token. The token is validated and the associated account identifier is used to retrieve account-specific statistics.  (required)
        :return: SuccessfulResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include', 'start', 'end', 'period', 'interval', 'authorization']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_metrics_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'include' is set
        if ('include' not in params) or (params['include'] is None):
            raise ValueError("Missing the required parameter `include` when calling `v3_metrics_get`")
        # verify the required parameter 'start' is set
        if ('start' not in params) or (params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `v3_metrics_get`")
        # verify the required parameter 'end' is set
        if ('end' not in params) or (params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `v3_metrics_get`")
        # verify the required parameter 'period' is set
        if ('period' not in params) or (params['period'] is None):
            raise ValueError("Missing the required parameter `period` when calling `v3_metrics_get`")
        # verify the required parameter 'interval' is set
        if ('interval' not in params) or (params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `v3_metrics_get`")
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `v3_metrics_get`")


        collection_formats = {}

        resource_path = '/v3/metrics'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']
        if 'start' in params:
            query_params['start'] = params['start']
        if 'end' in params:
            query_params['end'] = params['end']
        if 'period' in params:
            query_params['period'] = params['period']
        if 'interval' in params:
            query_params['interval'] = params['interval']

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SuccessfulResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)