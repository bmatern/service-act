# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class AlleleCall(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, hla: List[str]=None, gfe: str=None, version: str=None):
        """
        AlleleCall - a model defined in Swagger

        :param hla: The hla of this AlleleCall.
        :type hla: List[str]
        :param gfe: The gfe of this AlleleCall.
        :type gfe: str
        :param version: The version of this AlleleCall.
        :type version: str
        """
        self.swagger_types = {
            'hla': List[str],
            'gfe': str,
            'version': str
        }

        self.attribute_map = {
            'hla': 'hla',
            'gfe': 'gfe',
            'version': 'version'
        }

        self._hla = hla
        self._gfe = gfe
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'AlleleCall':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AlleleCall of this AlleleCall.
        :rtype: AlleleCall
        """
        return deserialize_model(dikt, cls)

    @property
    def hla(self) -> List[str]:
        """
        Gets the hla of this AlleleCall.

        :return: The hla of this AlleleCall.
        :rtype: List[str]
        """
        return self._hla

    @hla.setter
    def hla(self, hla: List[str]):
        """
        Sets the hla of this AlleleCall.

        :param hla: The hla of this AlleleCall.
        :type hla: List[str]
        """

        self._hla = hla

    @property
    def gfe(self) -> str:
        """
        Gets the gfe of this AlleleCall.

        :return: The gfe of this AlleleCall.
        :rtype: str
        """
        return self._gfe

    @gfe.setter
    def gfe(self, gfe: str):
        """
        Sets the gfe of this AlleleCall.

        :param gfe: The gfe of this AlleleCall.
        :type gfe: str
        """

        self._gfe = gfe

    @property
    def version(self) -> str:
        """
        Gets the version of this AlleleCall.

        :return: The version of this AlleleCall.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """
        Sets the version of this AlleleCall.

        :param version: The version of this AlleleCall.
        :type version: str
        """

        self._version = version

