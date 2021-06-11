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


class FeatureDistributionResponse(object):
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
        'distribution': 'FeatureDistribution',
        'feature': 'str',
        'interaction': 'FeatureInteraction',
        'total_instances': 'int',
        'type': 'str'
    }

    attribute_map = {
        'distribution': 'distribution',
        'feature': 'feature',
        'interaction': 'interaction',
        'total_instances': 'total_instances',
        'type': 'type'
    }

    def __init__(self, distribution=None, feature=None, interaction=None, total_instances=None, type=None):  # noqa: E501
        """FeatureDistributionResponse - a model defined in Swagger"""  # noqa: E501

        self._distribution = None
        self._feature = None
        self._interaction = None
        self._total_instances = None
        self._type = None
        self.discriminator = None

        if distribution is not None:
            self.distribution = distribution
        if feature is not None:
            self.feature = feature
        if interaction is not None:
            self.interaction = interaction
        if total_instances is not None:
            self.total_instances = total_instances
        if type is not None:
            self.type = type

    @property
    def distribution(self):
        """Gets the distribution of this FeatureDistributionResponse.  # noqa: E501


        :return: The distribution of this FeatureDistributionResponse.  # noqa: E501
        :rtype: FeatureDistribution
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this FeatureDistributionResponse.


        :param distribution: The distribution of this FeatureDistributionResponse.  # noqa: E501
        :type: FeatureDistribution
        """

        self._distribution = distribution

    @property
    def feature(self):
        """Gets the feature of this FeatureDistributionResponse.  # noqa: E501

        FeatureName refers to the name of feature as per the model predictions schema  # noqa: E501

        :return: The feature of this FeatureDistributionResponse.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this FeatureDistributionResponse.

        FeatureName refers to the name of feature as per the model predictions schema  # noqa: E501

        :param feature: The feature of this FeatureDistributionResponse.  # noqa: E501
        :type: str
        """

        self._feature = feature

    @property
    def interaction(self):
        """Gets the interaction of this FeatureDistributionResponse.  # noqa: E501


        :return: The interaction of this FeatureDistributionResponse.  # noqa: E501
        :rtype: FeatureInteraction
        """
        return self._interaction

    @interaction.setter
    def interaction(self, interaction):
        """Sets the interaction of this FeatureDistributionResponse.


        :param interaction: The interaction of this FeatureDistributionResponse.  # noqa: E501
        :type: FeatureInteraction
        """

        self._interaction = interaction

    @property
    def total_instances(self):
        """Gets the total_instances of this FeatureDistributionResponse.  # noqa: E501

        TotalInstances represents the total prediction over which the distribution is computed  # noqa: E501

        :return: The total_instances of this FeatureDistributionResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_instances

    @total_instances.setter
    def total_instances(self, total_instances):
        """Sets the total_instances of this FeatureDistributionResponse.

        TotalInstances represents the total prediction over which the distribution is computed  # noqa: E501

        :param total_instances: The total_instances of this FeatureDistributionResponse.  # noqa: E501
        :type: int
        """

        self._total_instances = total_instances

    @property
    def type(self):
        """Gets the type of this FeatureDistributionResponse.  # noqa: E501

        FeatureType refers to the type of feature as per the model predictions schema  # noqa: E501

        :return: The type of this FeatureDistributionResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FeatureDistributionResponse.

        FeatureType refers to the type of feature as per the model predictions schema  # noqa: E501

        :param type: The type of this FeatureDistributionResponse.  # noqa: E501
        :type: str
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
        if issubclass(FeatureDistributionResponse, dict):
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
        if not isinstance(other, FeatureDistributionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
