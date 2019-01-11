"""
Entity module

This file is autogenerated from api specifications
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import super

from mbed_cloud.sdk.common.entity import Entity
from mbed_cloud.sdk.common import fields
from mbed_cloud.sdk import enums


class SubtenantUserInvitation(Entity):
    """Represents the `SubtenantUserInvitation` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "account_id",
        "created_at",
        "email",
        "expiration",
        "id",
        "updated_at",
        "user_id",
    ]

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {}

    def __init__(
        self,
        _client=None,
        account_id=None,
        created_at=None,
        email=None,
        expiration=None,
        id=None,
        updated_at=None,
        user_id=None,
    ):
        """Creates a local `SubtenantUserInvitation` instance

        :param account_id: The UUID of the account the user is invited to.
        :type account_id: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param email: Email address of the invited user.
        :type email: str
        :param expiration: Invitation expiration as UTC time RFC3339.
        :type expiration: datetime
        :param id: The UUID of the invitation.
        :type id: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param user_id: The UUID of the invited user.
        :type user_id: str
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._created_at = fields.DateTimeField(value=created_at)
        self._email = fields.StringField(value=email)
        self._expiration = fields.DateTimeField(value=expiration)
        self._id = fields.StringField(value=id)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._user_id = fields.StringField(value=user_id)

    @property
    def account_id(self):
        """The UUID of the account the user is invited to.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """

        return self._account_id.value

    @account_id.setter
    def account_id(self, value):
        """Set value of `account_id`

        :param value: value to set
        :type value: str
        """

        self._account_id.set(value)

    @property
    def created_at(self):
        """Creation UTC time RFC3339.
        
        api example: '2018-02-13T09:35:20Z'
        
        :rtype: datetime
        """

        return self._created_at.value

    @created_at.setter
    def created_at(self, value):
        """Set value of `created_at`

        :param value: value to set
        :type value: datetime
        """

        self._created_at.set(value)

    @property
    def email(self):
        """Email address of the invited user.
        
        api example: 'friend@arm.com'
        
        :rtype: str
        """

        return self._email.value

    @email.setter
    def email(self, value):
        """Set value of `email`

        :param value: value to set
        :type value: str
        """

        self._email.set(value)

    @property
    def expiration(self):
        """Invitation expiration as UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._expiration.value

    @expiration.setter
    def expiration(self, value):
        """Set value of `expiration`

        :param value: value to set
        :type value: datetime
        """

        self._expiration.set(value)

    @property
    def id(self):
        """The UUID of the invitation.
        
        api example: '01619571e2e89242ac12000600000000'
        
        :rtype: str
        """

        return self._id.value

    @id.setter
    def id(self, value):
        """Set value of `id`

        :param value: value to set
        :type value: str
        """

        self._id.set(value)

    @property
    def updated_at(self):
        """Last update UTC time RFC3339.
        
        api example: '2018-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._updated_at.value

    @updated_at.setter
    def updated_at(self, value):
        """Set value of `updated_at`

        :param value: value to set
        :type value: datetime
        """

        self._updated_at.set(value)

    @property
    def user_id(self):
        """The UUID of the invited user.
        
        api example: '01619571e2e90242ac12000600000000'
        
        :rtype: str
        """

        return self._user_id.value

    @user_id.setter
    def user_id(self, value):
        """Set value of `user_id`

        :param value: value to set
        :type value: str
        """

        self._user_id.set(value)

    def create(self):
        """Create a user invitation.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account-id}/user-invitations
        
        :rtype: SubtenantUserInvitation
        """

        return self._client.call_api(
            method="post",
            path="/v3/accounts/{account-id}/user-invitations",
            body_params={"email": self._email.to_api()},
            path_params={"account-id": self._account_id.to_api()},
            unpack=self,
        )

    def delete(self):
        """Delete a user invitation.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account-id}/user-invitations/{invitation-id}
        
        :rtype: SubtenantUserInvitation
        """

        return self._client.call_api(
            method="delete",
            path="/v3/accounts/{account-id}/user-invitations/{invitation-id}",
            path_params={
                "account-id": self._account_id.to_api(),
                "invitation-id": self._id.to_api(),
            },
            unpack=self,
        )

    def get(self):
        """Details of a user invitation.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/accounts/{account-id}/user-invitations/{invitation-id}
        
        :rtype: SubtenantUserInvitation
        """

        return self._client.call_api(
            method="get",
            path="/v3/accounts/{account-id}/user-invitations/{invitation-id}",
            path_params={
                "account-id": self._account_id.to_api(),
                "invitation-id": self._id.to_api(),
            },
            unpack=self,
        )