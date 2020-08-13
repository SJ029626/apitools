"""Generated client library for servicemanagement version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from samples.servicemanagement_sample.servicemanagement_v1 import servicemanagement_v1_messages as messages


class ServicemanagementV1(base_api.BaseApiClient):
  """Generated client library for service servicemanagement version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://servicemanagement.googleapis.com/'
  MTLS_BASE_URL = u''

  _PACKAGE = u'servicemanagement'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/service.management']
  _VERSION = u'v1'
  _CLIENT_ID = None
  _CLIENT_SECRET = None
  _USER_AGENT = None
  _CLIENT_CLASS_NAME = u'ServicemanagementV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new servicemanagement handle."""
    url = url or self.BASE_URL
    super(ServicemanagementV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.operations = self.OperationsService(self)
    self.services_accessPolicy = self.ServicesAccessPolicyService(self)
    self.services_configs = self.ServicesConfigsService(self)
    self.services_customerSettings = self.ServicesCustomerSettingsService(self)
    self.services_projectSettings = self.ServicesProjectSettingsService(self)
    self.services = self.ServicesService(self)
    self.v1 = self.V1Service(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(ServicemanagementV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (ServicemanagementOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'servicemanagement.operations.get',
        ordered_params=[u'operationsId'],
        path_params=[u'operationsId'],
        query_params=[],
        relative_path=u'v1/operations/{operationsId}',
        request_field='',
        request_type_name=u'ServicemanagementOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ServicesAccessPolicyService(base_api.BaseApiService):
    """Service class for the services_accessPolicy resource."""

    _NAME = u'services_accessPolicy'

    def __init__(self, client):
      super(ServicemanagementV1.ServicesAccessPolicyService, self).__init__(client)
      self._upload_configs = {
          }

    def Query(self, request, global_params=None):
      r"""Method to query the accessibility of a service and any associated.
visibility labels for a specified user.

Members of the producer project may call this method and specify any user.

Any user may call this method, but must specify their own email address.
In this case the method will return NOT_FOUND if the user has no access to
the service.

      Args:
        request: (ServicemanagementServicesAccessPolicyQueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (QueryUserAccessResponse) The response message.
      """
      config = self.GetMethodConfig('Query')
      return self._RunMethod(
          config, request, global_params=global_params)

    Query.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'servicemanagement.services.accessPolicy.query',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[u'userEmail'],
        relative_path=u'v1/services/{serviceName}/accessPolicy:query',
        request_field='',
        request_type_name=u'ServicemanagementServicesAccessPolicyQueryRequest',
        response_type_name=u'QueryUserAccessResponse',
        supports_download=False,
    )

  class ServicesConfigsService(base_api.BaseApiService):
    """Service class for the services_configs resource."""

    _NAME = u'services_configs'

    def __init__(self, client):
      super(ServicemanagementV1.ServicesConfigsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new service config (version) for a managed service. This method.
only stores the service config, but does not apply the service config to
any backend services.

      Args:
        request: (ServicemanagementServicesConfigsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Service) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'servicemanagement.services.configs.create',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[],
        relative_path=u'v1/services/{serviceName}/configs',
        request_field=u'service',
        request_type_name=u'ServicemanagementServicesConfigsCreateRequest',
        response_type_name=u'Service',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a service config (version) for a managed service. If `config_id` is.
not specified, the latest service config will be returned.

      Args:
        request: (ServicemanagementServicesConfigsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Service) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'servicemanagement.services.configs.get',
        ordered_params=[u'serviceName', u'configId'],
        path_params=[u'configId', u'serviceName'],
        query_params=[],
        relative_path=u'v1/services/{serviceName}/configs/{configId}',
        request_field='',
        request_type_name=u'ServicemanagementServicesConfigsGetRequest',
        response_type_name=u'Service',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists the history of the service config for a managed service,.
from the newest to the oldest.

      Args:
        request: (ServicemanagementServicesConfigsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListServiceConfigsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'servicemanagement.services.configs.list',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1/services/{serviceName}/configs',
        request_field='',
        request_type_name=u'ServicemanagementServicesConfigsListRequest',
        response_type_name=u'ListServiceConfigsResponse',
        supports_download=False,
    )

    def Submit(self, request, global_params=None):
      r"""Creates a new service config (version) for a managed service based on.
user-supplied configuration sources files (for example: OpenAPI
Specification). This method stores the source configurations as well as the
generated service config. It does NOT apply the service config to any
backend services.

Operation<response: SubmitConfigSourceResponse>

      Args:
        request: (ServicemanagementServicesConfigsSubmitRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Submit')
      return self._RunMethod(
          config, request, global_params=global_params)

    Submit.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'servicemanagement.services.configs.submit',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[],
        relative_path=u'v1/services/{serviceName}/configs:submit',
        request_field=u'submitConfigSourceRequest',
        request_type_name=u'ServicemanagementServicesConfigsSubmitRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ServicesCustomerSettingsService(base_api.BaseApiService):
    """Service class for the services_customerSettings resource."""

    _NAME = u'services_customerSettings'

    def __init__(self, client):
      super(ServicemanagementV1.ServicesCustomerSettingsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Retrieves the settings that control the specified customer's usage of the.
service.

      Args:
        request: (ServicemanagementServicesCustomerSettingsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CustomerSettings) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'servicemanagement.services.customerSettings.get',
        ordered_params=[u'serviceName', u'customerId'],
        path_params=[u'customerId', u'serviceName'],
        query_params=[u'expand', u'view'],
        relative_path=u'v1/services/{serviceName}/customerSettings/{customerId}',
        request_field='',
        request_type_name=u'ServicemanagementServicesCustomerSettingsGetRequest',
        response_type_name=u'CustomerSettings',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates specified subset of the settings that control the specified.
customer's usage of the service.  Attempts to update a field not
controlled by the caller will result in an access denied error.

Operation<response: CustomerSettings>

      Args:
        request: (ServicemanagementServicesCustomerSettingsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'servicemanagement.services.customerSettings.patch',
        ordered_params=[u'serviceName', u'customerId'],
        path_params=[u'customerId', u'serviceName'],
        query_params=[u'updateMask'],
        relative_path=u'v1/services/{serviceName}/customerSettings/{customerId}',
        request_field=u'customerSettings',
        request_type_name=u'ServicemanagementServicesCustomerSettingsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ServicesProjectSettingsService(base_api.BaseApiService):
    """Service class for the services_projectSettings resource."""

    _NAME = u'services_projectSettings'

    def __init__(self, client):
      super(ServicemanagementV1.ServicesProjectSettingsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Retrieves the settings that control the specified consumer project's usage.
of the service.

      Args:
        request: (ServicemanagementServicesProjectSettingsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ProjectSettings) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'servicemanagement.services.projectSettings.get',
        ordered_params=[u'serviceName', u'consumerProjectId'],
        path_params=[u'consumerProjectId', u'serviceName'],
        query_params=[u'expand', u'view'],
        relative_path=u'v1/services/{serviceName}/projectSettings/{consumerProjectId}',
        request_field='',
        request_type_name=u'ServicemanagementServicesProjectSettingsGetRequest',
        response_type_name=u'ProjectSettings',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates specified subset of the settings that control the specified.
consumer project's usage of the service.  Attempts to update a field not
controlled by the caller will result in an access denied error.

Operation<response: ProjectSettings>

      Args:
        request: (ServicemanagementServicesProjectSettingsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'servicemanagement.services.projectSettings.patch',
        ordered_params=[u'serviceName', u'consumerProjectId'],
        path_params=[u'consumerProjectId', u'serviceName'],
        query_params=[u'updateMask'],
        relative_path=u'v1/services/{serviceName}/projectSettings/{consumerProjectId}',
        request_field=u'projectSettings',
        request_type_name=u'ServicemanagementServicesProjectSettingsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""NOTE: Currently unsupported.  Use PatchProjectSettings instead.

Updates the settings that control the specified consumer project's usage
of the service.  Attempts to update a field not controlled by the caller
will result in an access denied error.

Operation<response: ProjectSettings>

      Args:
        request: (ProjectSettings) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'servicemanagement.services.projectSettings.update',
        ordered_params=[u'serviceName', u'consumerProjectId'],
        path_params=[u'consumerProjectId', u'serviceName'],
        query_params=[],
        relative_path=u'v1/services/{serviceName}/projectSettings/{consumerProjectId}',
        request_field='<request>',
        request_type_name=u'ProjectSettings',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ServicesService(base_api.BaseApiService):
    """Service class for the services resource."""

    _NAME = u'services'

    def __init__(self, client):
      super(ServicemanagementV1.ServicesService, self).__init__(client)
      self._upload_configs = {
          }

    def ConvertConfig(self, request, global_params=None):
      r"""DEPRECATED. `SubmitConfigSource` with `validate_only=true` will provide.
config conversion moving forward.

Converts an API specification (e.g. Swagger spec) to an
equivalent `google.api.Service`.

      Args:
        request: (ConvertConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ConvertConfigResponse) The response message.
      """
      config = self.GetMethodConfig('ConvertConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    ConvertConfig.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'servicemanagement.services.convertConfig',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1/services:convertConfig',
        request_field='<request>',
        request_type_name=u'ConvertConfigRequest',
        response_type_name=u'ConvertConfigResponse',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Creates a new managed service.

Operation<response: ManagedService>

      Args:
        request: (ManagedService) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'servicemanagement.services.create',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1/services',
        request_field='<request>',
        request_type_name=u'ManagedService',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a managed service.

Operation<response: google.protobuf.Empty>

      Args:
        request: (ServicemanagementServicesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'servicemanagement.services.delete',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[],
        relative_path=u'v1/services/{serviceName}',
        request_field='',
        request_type_name=u'ServicemanagementServicesDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Disable(self, request, global_params=None):
      r"""Disable a managed service for a project.
Google Service Management will only disable the managed service even if
there are other services depend on the managed service.

Operation<response: DisableServiceResponse>

      Args:
        request: (ServicemanagementServicesDisableRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Disable')
      return self._RunMethod(
          config, request, global_params=global_params)

    Disable.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'servicemanagement.services.disable',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[],
        relative_path=u'v1/services/{serviceName}:disable',
        request_field=u'disableServiceRequest',
        request_type_name=u'ServicemanagementServicesDisableRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Enable(self, request, global_params=None):
      r"""Enable a managed service for a project with default setting.
If the managed service has dependencies, they will be enabled as well.

Operation<response: EnableServiceResponse>

      Args:
        request: (ServicemanagementServicesEnableRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Enable')
      return self._RunMethod(
          config, request, global_params=global_params)

    Enable.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'servicemanagement.services.enable',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[],
        relative_path=u'v1/services/{serviceName}:enable',
        request_field=u'enableServiceRequest',
        request_type_name=u'ServicemanagementServicesEnableRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a managed service. If the `consumer_project_id` is specified,.
the project's settings for the specified service are also returned.

      Args:
        request: (ServicemanagementServicesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedService) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'servicemanagement.services.get',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[u'consumerProjectId', u'expand', u'view'],
        relative_path=u'v1/services/{serviceName}',
        request_field='',
        request_type_name=u'ServicemanagementServicesGetRequest',
        response_type_name=u'ManagedService',
        supports_download=False,
    )

    def GetAccessPolicy(self, request, global_params=None):
      r"""Producer method to retrieve current policy.

      Args:
        request: (ServicemanagementServicesGetAccessPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServiceAccessPolicy) The response message.
      """
      config = self.GetMethodConfig('GetAccessPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetAccessPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'servicemanagement.services.getAccessPolicy',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[],
        relative_path=u'v1/services/{serviceName}/accessPolicy',
        request_field='',
        request_type_name=u'ServicemanagementServicesGetAccessPolicyRequest',
        response_type_name=u'ServiceAccessPolicy',
        supports_download=False,
    )

    def GetConfig(self, request, global_params=None):
      r"""Gets a service config (version) for a managed service. If `config_id` is.
not specified, the latest service config will be returned.

      Args:
        request: (ServicemanagementServicesGetConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Service) The response message.
      """
      config = self.GetMethodConfig('GetConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetConfig.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'servicemanagement.services.getConfig',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[u'configId'],
        relative_path=u'v1/services/{serviceName}/config',
        request_field='',
        request_type_name=u'ServicemanagementServicesGetConfigRequest',
        response_type_name=u'Service',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all managed services. If the `consumer_project_id` is specified,.
the project's settings for the specified service are also returned.

      Args:
        request: (ServicemanagementServicesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListServicesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'servicemanagement.services.list',
        ordered_params=[],
        path_params=[],
        query_params=[u'category', u'consumerProjectId', u'expand', u'pageSize', u'pageToken', u'producerProjectId'],
        relative_path=u'v1/services',
        request_field='',
        request_type_name=u'ServicemanagementServicesListRequest',
        response_type_name=u'ListServicesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the specified subset of the configuration. If the specified service.
does not exists the patch operation fails.

Operation<response: ManagedService>

      Args:
        request: (ServicemanagementServicesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'servicemanagement.services.patch',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[u'updateMask'],
        relative_path=u'v1/services/{serviceName}',
        request_field=u'managedService',
        request_type_name=u'ServicemanagementServicesPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def PatchConfig(self, request, global_params=None):
      r"""Updates the specified subset of the service resource. Equivalent to.
calling `PatchService` with only the `service_config` field updated.

Operation<response: google.api.Service>

      Args:
        request: (ServicemanagementServicesPatchConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('PatchConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    PatchConfig.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'servicemanagement.services.patchConfig',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[u'updateMask'],
        relative_path=u'v1/services/{serviceName}/config',
        request_field=u'service',
        request_type_name=u'ServicemanagementServicesPatchConfigRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates the configuration of a service.  If the specified service does not.
already exist, then it is created.

Operation<response: ManagedService>

      Args:
        request: (ServicemanagementServicesUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'servicemanagement.services.update',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[u'updateMask'],
        relative_path=u'v1/services/{serviceName}',
        request_field=u'managedService',
        request_type_name=u'ServicemanagementServicesUpdateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def UpdateAccessPolicy(self, request, global_params=None):
      r"""Producer method to update the current policy.  This method will return an.
error if the policy is too large (more than 50 entries across all lists).

      Args:
        request: (ServiceAccessPolicy) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServiceAccessPolicy) The response message.
      """
      config = self.GetMethodConfig('UpdateAccessPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateAccessPolicy.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'servicemanagement.services.updateAccessPolicy',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[],
        relative_path=u'v1/services/{serviceName}/accessPolicy',
        request_field='<request>',
        request_type_name=u'ServiceAccessPolicy',
        response_type_name=u'ServiceAccessPolicy',
        supports_download=False,
    )

    def UpdateConfig(self, request, global_params=None):
      r"""Updates the specified subset of the service resource. Equivalent to.
calling `UpdateService` with only the `service_config` field updated.

Operation<response: google.api.Service>

      Args:
        request: (ServicemanagementServicesUpdateConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('UpdateConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpdateConfig.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'servicemanagement.services.updateConfig',
        ordered_params=[u'serviceName'],
        path_params=[u'serviceName'],
        query_params=[u'updateMask'],
        relative_path=u'v1/services/{serviceName}/config',
        request_field=u'service',
        request_type_name=u'ServicemanagementServicesUpdateConfigRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class V1Service(base_api.BaseApiService):
    """Service class for the v1 resource."""

    _NAME = u'v1'

    def __init__(self, client):
      super(ServicemanagementV1.V1Service, self).__init__(client)
      self._upload_configs = {
          }

    def ConvertConfig(self, request, global_params=None):
      r"""DEPRECATED. `SubmitConfigSource` with `validate_only=true` will provide.
config conversion moving forward.

Converts an API specification (e.g. Swagger spec) to an
equivalent `google.api.Service`.

      Args:
        request: (ConvertConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ConvertConfigResponse) The response message.
      """
      config = self.GetMethodConfig('ConvertConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    ConvertConfig.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'servicemanagement.convertConfig',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1:convertConfig',
        request_field='<request>',
        request_type_name=u'ConvertConfigRequest',
        response_type_name=u'ConvertConfigResponse',
        supports_download=False,
    )
