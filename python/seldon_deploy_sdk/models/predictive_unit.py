# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PredictiveUnit(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'children': 'list[PredictiveUnit]',
        'endpoint': 'Endpoint',
        'env_secret_ref_name': 'str',
        'implementation': 'PredictiveUnitImplementation',
        'logger': 'Logger',
        'methods': 'list[PredictiveUnitMethod]',
        'model_uri': 'str',
        'name': 'str',
        'parameters': 'list[Parameter]',
        'service_account_name': 'str',
        'storage_initializer_image': 'str',
        'type': 'PredictiveUnitType'
    }

    attribute_map = {
        'children': 'children',
        'endpoint': 'endpoint',
        'env_secret_ref_name': 'envSecretRefName',
        'implementation': 'implementation',
        'logger': 'logger',
        'methods': 'methods',
        'model_uri': 'modelUri',
        'name': 'name',
        'parameters': 'parameters',
        'service_account_name': 'serviceAccountName',
        'storage_initializer_image': 'storageInitializerImage',
        'type': 'type'
    }

    def __init__(self, children=None, endpoint=None, env_secret_ref_name=None, implementation=None, logger=None, methods=None, model_uri=None, name=None, parameters=None, service_account_name=None, storage_initializer_image=None, type=None):  # noqa: E501
        """PredictiveUnit - a model defined in Swagger"""  # noqa: E501

        self._children = None
        self._endpoint = None
        self._env_secret_ref_name = None
        self._implementation = None
        self._logger = None
        self._methods = None
        self._model_uri = None
        self._name = None
        self._parameters = None
        self._service_account_name = None
        self._storage_initializer_image = None
        self._type = None
        self.discriminator = None

        if children is not None:
            self.children = children
        if endpoint is not None:
            self.endpoint = endpoint
        if env_secret_ref_name is not None:
            self.env_secret_ref_name = env_secret_ref_name
        if implementation is not None:
            self.implementation = implementation
        if logger is not None:
            self.logger = logger
        if methods is not None:
            self.methods = methods
        if model_uri is not None:
            self.model_uri = model_uri
        if name is not None:
            self.name = name
        if parameters is not None:
            self.parameters = parameters
        if service_account_name is not None:
            self.service_account_name = service_account_name
        if storage_initializer_image is not None:
            self.storage_initializer_image = storage_initializer_image
        if type is not None:
            self.type = type

    @property
    def children(self):
        """Gets the children of this PredictiveUnit.  # noqa: E501


        :return: The children of this PredictiveUnit.  # noqa: E501
        :rtype: list[PredictiveUnit]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this PredictiveUnit.


        :param children: The children of this PredictiveUnit.  # noqa: E501
        :type: list[PredictiveUnit]
        """

        self._children = children

    @property
    def endpoint(self):
        """Gets the endpoint of this PredictiveUnit.  # noqa: E501


        :return: The endpoint of this PredictiveUnit.  # noqa: E501
        :rtype: Endpoint
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this PredictiveUnit.


        :param endpoint: The endpoint of this PredictiveUnit.  # noqa: E501
        :type: Endpoint
        """

        self._endpoint = endpoint

    @property
    def env_secret_ref_name(self):
        """Gets the env_secret_ref_name of this PredictiveUnit.  # noqa: E501


        :return: The env_secret_ref_name of this PredictiveUnit.  # noqa: E501
        :rtype: str
        """
        return self._env_secret_ref_name

    @env_secret_ref_name.setter
    def env_secret_ref_name(self, env_secret_ref_name):
        """Sets the env_secret_ref_name of this PredictiveUnit.


        :param env_secret_ref_name: The env_secret_ref_name of this PredictiveUnit.  # noqa: E501
        :type: str
        """

        self._env_secret_ref_name = env_secret_ref_name

    @property
    def implementation(self):
        """Gets the implementation of this PredictiveUnit.  # noqa: E501


        :return: The implementation of this PredictiveUnit.  # noqa: E501
        :rtype: PredictiveUnitImplementation
        """
        return self._implementation

    @implementation.setter
    def implementation(self, implementation):
        """Sets the implementation of this PredictiveUnit.


        :param implementation: The implementation of this PredictiveUnit.  # noqa: E501
        :type: PredictiveUnitImplementation
        """

        self._implementation = implementation

    @property
    def logger(self):
        """Gets the logger of this PredictiveUnit.  # noqa: E501


        :return: The logger of this PredictiveUnit.  # noqa: E501
        :rtype: Logger
        """
        return self._logger

    @logger.setter
    def logger(self, logger):
        """Sets the logger of this PredictiveUnit.


        :param logger: The logger of this PredictiveUnit.  # noqa: E501
        :type: Logger
        """

        self._logger = logger

    @property
    def methods(self):
        """Gets the methods of this PredictiveUnit.  # noqa: E501


        :return: The methods of this PredictiveUnit.  # noqa: E501
        :rtype: list[PredictiveUnitMethod]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this PredictiveUnit.


        :param methods: The methods of this PredictiveUnit.  # noqa: E501
        :type: list[PredictiveUnitMethod]
        """

        self._methods = methods

    @property
    def model_uri(self):
        """Gets the model_uri of this PredictiveUnit.  # noqa: E501


        :return: The model_uri of this PredictiveUnit.  # noqa: E501
        :rtype: str
        """
        return self._model_uri

    @model_uri.setter
    def model_uri(self, model_uri):
        """Sets the model_uri of this PredictiveUnit.


        :param model_uri: The model_uri of this PredictiveUnit.  # noqa: E501
        :type: str
        """

        self._model_uri = model_uri

    @property
    def name(self):
        """Gets the name of this PredictiveUnit.  # noqa: E501


        :return: The name of this PredictiveUnit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PredictiveUnit.


        :param name: The name of this PredictiveUnit.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this PredictiveUnit.  # noqa: E501


        :return: The parameters of this PredictiveUnit.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this PredictiveUnit.


        :param parameters: The parameters of this PredictiveUnit.  # noqa: E501
        :type: list[Parameter]
        """

        self._parameters = parameters

    @property
    def service_account_name(self):
        """Gets the service_account_name of this PredictiveUnit.  # noqa: E501


        :return: The service_account_name of this PredictiveUnit.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this PredictiveUnit.


        :param service_account_name: The service_account_name of this PredictiveUnit.  # noqa: E501
        :type: str
        """

        self._service_account_name = service_account_name

    @property
    def storage_initializer_image(self):
        """Gets the storage_initializer_image of this PredictiveUnit.  # noqa: E501


        :return: The storage_initializer_image of this PredictiveUnit.  # noqa: E501
        :rtype: str
        """
        return self._storage_initializer_image

    @storage_initializer_image.setter
    def storage_initializer_image(self, storage_initializer_image):
        """Sets the storage_initializer_image of this PredictiveUnit.


        :param storage_initializer_image: The storage_initializer_image of this PredictiveUnit.  # noqa: E501
        :type: str
        """

        self._storage_initializer_image = storage_initializer_image

    @property
    def type(self):
        """Gets the type of this PredictiveUnit.  # noqa: E501


        :return: The type of this PredictiveUnit.  # noqa: E501
        :rtype: PredictiveUnitType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PredictiveUnit.


        :param type: The type of this PredictiveUnit.  # noqa: E501
        :type: PredictiveUnitType
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PredictiveUnit, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PredictiveUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
