# coding: utf-8

"""
    Platform Operations Rest API

    The Platform Operations REST API can be leveraged to customize the Platform Operator experience of managing infrastructure and applications for the Apprenda Platform. This allows some of the functionality of the Platform's System Operations Center (SOC) to be accomplished through a variety of means such as custom-built UX or command-line interfaces.   For more information about the abilities of Platform Operators, see our documentation on the [SOC](/current/SOC).   ##Authentication   Before making a request, you must be authenticated. Learn how to [get authenticated](/restapi/platformops/v1/authentication).   ##Making a Request   ###Prerequisites   * Installed Platform of version 6.5.1 or later (Note that most endpoints are only available in version 6.7.0 and later)    * Authentication token   * If SOC authorization is enabled on your Platform, you must be assigned as an active Platform Operator   ###Request URL   All requests must use **https**.   The URL for every request you make is the Cloud URI of your Platform followed by \"/soc\" and the path structure of the endpoint. For example, if your Cloud URI is apps.apprenda.harp and you want to get the Add-ons for your Platform, the request URI will be **apps.apprenda.harp/soc/api/v1/addons**.   For more information, see our documentation on [using API resources](/restapi/platformops/v1/using-resources) and [finding your Cloud URI](/current/clouduri).   ###Request Headers   Your authenication token must be passed in the header of all requests using the key **ApprendaSessionToken** (not case sensitive).  

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ClusterReportCardSection(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, begindate=None, endate=None, iscanceled=None, messages=None, description=None):
        """
        ClusterReportCardSection - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'begindate': 'datetime',
            'endate': 'datetime',
            'iscanceled': 'bool',
            'messages': 'list[ClusterReportCardMessage]',
            'description': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'begindate': 'begindate',
            'endate': 'endate',
            'iscanceled': 'iscanceled',
            'messages': 'messages',
            'description': 'description'
        }

        self._name = name
        self._begindate = begindate
        self._endate = endate
        self._iscanceled = iscanceled
        self._messages = messages
        self._description = description

    @property
    def name(self):
        """
        Gets the name of this ClusterReportCardSection.

        :return: The name of this ClusterReportCardSection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ClusterReportCardSection.

        :param name: The name of this ClusterReportCardSection.
        :type: str
        """

        self._name = name

    @property
    def begindate(self):
        """
        Gets the begindate of this ClusterReportCardSection.

        :return: The begindate of this ClusterReportCardSection.
        :rtype: datetime
        """
        return self._begindate

    @begindate.setter
    def begindate(self, begindate):
        """
        Sets the begindate of this ClusterReportCardSection.

        :param begindate: The begindate of this ClusterReportCardSection.
        :type: datetime
        """

        self._begindate = begindate

    @property
    def endate(self):
        """
        Gets the endate of this ClusterReportCardSection.

        :return: The endate of this ClusterReportCardSection.
        :rtype: datetime
        """
        return self._endate

    @endate.setter
    def endate(self, endate):
        """
        Sets the endate of this ClusterReportCardSection.

        :param endate: The endate of this ClusterReportCardSection.
        :type: datetime
        """

        self._endate = endate

    @property
    def iscanceled(self):
        """
        Gets the iscanceled of this ClusterReportCardSection.

        :return: The iscanceled of this ClusterReportCardSection.
        :rtype: bool
        """
        return self._iscanceled

    @iscanceled.setter
    def iscanceled(self, iscanceled):
        """
        Sets the iscanceled of this ClusterReportCardSection.

        :param iscanceled: The iscanceled of this ClusterReportCardSection.
        :type: bool
        """

        self._iscanceled = iscanceled

    @property
    def messages(self):
        """
        Gets the messages of this ClusterReportCardSection.

        :return: The messages of this ClusterReportCardSection.
        :rtype: list[ClusterReportCardMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this ClusterReportCardSection.

        :param messages: The messages of this ClusterReportCardSection.
        :type: list[ClusterReportCardMessage]
        """

        self._messages = messages

    @property
    def description(self):
        """
        Gets the description of this ClusterReportCardSection.

        :return: The description of this ClusterReportCardSection.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ClusterReportCardSection.

        :param description: The description of this ClusterReportCardSection.
        :type: str
        """

        self._description = description

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ClusterReportCardSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
