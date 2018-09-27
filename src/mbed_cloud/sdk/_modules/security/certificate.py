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


class Certificate(Entity):
    """Represents the `Certificate` entity in Mbed Cloud"""

    # all fields available on this entity
    _fieldnames = [
        "account_id",
        "certificate",
        "certificate_type",
        "created_at",
        "description",
        "developer_certificate",
        "developer_private_key",
        "device_execution_mode",
        "enrollment_mode",
        "id",
        "issuer",
        "name",
        "owner_id",
        "security_file_content",
        "service",
        "status",
        "subject",
        "updated_at",
        "validity",
    ]

    # common renames used when mapping {<API spec>: <SDK>}
    _renames = {"cert-id": "id"}

    def __init__(
        self,
        _client=None,
        account_id=None,
        certificate=None,
        certificate_type=None,
        created_at=None,
        description=None,
        developer_certificate=None,
        developer_private_key=None,
        enrollment_mode=None,
        id=None,
        issuer=None,
        name=None,
        owner_id=None,
        security_file_content=None,
        status=None,
        subject=None,
        updated_at=None,
        validity=None,
    ):
        """Creates a local `Certificate` instance

        :param account_id: The UUID of the account.
        :type account_id: str
        :param certificate: X509.v3 trusted certificate in PEM format.
        :type certificate: str
        :param certificate_type: The type of the certificate.
        :type certificate_type: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param description: Human readable description of this certificate.
        :type description: str
        :param developer_certificate: PEM format X.509 developer certificate.
        :type developer_certificate: str
        :param developer_private_key: PEM format developer private key associated to the certificate.
        :type developer_private_key: str
        :param enrollment_mode: If true, signature is not required. Default value false.
        :type enrollment_mode: bool
        :param id: Entity ID.
        :type id: str
        :param issuer: Issuer of the certificate.
        :type issuer: str
        :param name: Certificate name.
        :type name: str
        :param owner_id: The UUID of the owner.
        :type owner_id: str
        :param security_file_content: Content of the security.c file that will be flashed into the
            device to provide the security credentials
        :type security_file_content: str
        :param status: Status of the certificate.
        :type status: str
        :param subject: Subject of the certificate.
        :type subject: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param validity: Expiration time in UTC formatted as RFC3339.
        :type validity: datetime
        """

        super().__init__(_client=_client)

        # inline imports for avoiding circular references and bulk imports

        # fields
        self._account_id = fields.StringField(value=account_id)
        self._certificate = fields.StringField(value=certificate)
        self._certificate_type = fields.StringField(
            value=certificate_type, enum=enums.CertificateCertificateTypeEnum
        )
        self._created_at = fields.DateTimeField(value=created_at)
        self._description = fields.StringField(value=description)
        self._developer_certificate = fields.StringField(value=developer_certificate)
        self._developer_private_key = fields.StringField(value=developer_private_key)
        self._device_execution_mode = fields.IntegerField(value=None)
        self._enrollment_mode = fields.BooleanField(value=enrollment_mode)
        self._id = fields.StringField(value=id)
        self._issuer = fields.StringField(value=issuer)
        self._name = fields.StringField(value=name)
        self._owner_id = fields.StringField(value=owner_id)
        self._security_file_content = fields.StringField(value=security_file_content)
        self._service = fields.StringField(
            value=None, enum=enums.CertificateServiceEnum
        )
        self._status = fields.StringField(
            value=status, enum=enums.CertificateStatusEnum
        )
        self._subject = fields.StringField(value=subject)
        self._updated_at = fields.DateTimeField(value=updated_at)
        self._validity = fields.DateTimeField(value=validity)

    @property
    def account_id(self):
        """The UUID of the account.
        
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
    def certificate(self):
        """X509.v3 trusted certificate in PEM format.
        
        api example: '-----BEGIN CERTIFICATE----- ... -----END CERTIFICATE-----'
        
        :rtype: str
        """

        return self._certificate.value

    @certificate.setter
    def certificate(self, value):
        """Set value of `certificate`

        :param value: value to set
        :type value: str
        """

        self._certificate.set(value)

    @property
    def certificate_type(self):
        """The type of the certificate.
        
        api example: 'DEVELOPER'
        
        :rtype: str
        """

        from mbed_cloud.sdk.common._custom_methods import certificate_type_getter

        return certificate_type_getter(self=self, field=self._certificate_type)

    @certificate_type.setter
    def certificate_type(self, value):
        """Set value of `certificate_type`

        :param value: value to set
        :type value: str
        """

        from mbed_cloud.sdk.common._custom_methods import certificate_type_setter

        return certificate_type_setter(
            self=self, field=self._certificate_type, value=value
        )

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
    def description(self):
        """Human readable description of this certificate.
        
        api example: 'Certificate created by me.'
        
        :rtype: str
        """

        return self._description.value

    @description.setter
    def description(self, value):
        """Set value of `description`

        :param value: value to set
        :type value: str
        """

        self._description.set(value)

    @property
    def developer_certificate(self):
        """PEM format X.509 developer certificate.
        
        :rtype: str
        """

        return self._developer_certificate.value

    @developer_certificate.setter
    def developer_certificate(self, value):
        """Set value of `developer_certificate`

        :param value: value to set
        :type value: str
        """

        self._developer_certificate.set(value)

    @property
    def developer_private_key(self):
        """PEM format developer private key associated to the certificate.
        
        :rtype: str
        """

        return self._developer_private_key.value

    @developer_private_key.setter
    def developer_private_key(self, value):
        """Set value of `developer_private_key`

        :param value: value to set
        :type value: str
        """

        self._developer_private_key.set(value)

    @property
    def device_execution_mode(self):
        """Device execution mode where 1 means a developer certificate.
        
        api example: 1
        
        :rtype: int
        """

        return self._device_execution_mode.value

    @device_execution_mode.setter
    def device_execution_mode(self, value):
        """Set value of `device_execution_mode`

        :param value: value to set
        :type value: int
        """

        self._device_execution_mode.set(value)

    @property
    def enrollment_mode(self):
        """If true, signature is not required. Default value false.
        
        :rtype: bool
        """

        return self._enrollment_mode.value

    @enrollment_mode.setter
    def enrollment_mode(self, value):
        """Set value of `enrollment_mode`

        :param value: value to set
        :type value: bool
        """

        self._enrollment_mode.set(value)

    @property
    def id(self):
        """Entity ID.
        
        api example: '01619571d01d0242ac12000600000000'
        
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
    def issuer(self):
        """Issuer of the certificate.
        
        api example: 'CN=issuer'
        
        :rtype: str
        """

        return self._issuer.value

    @issuer.setter
    def issuer(self, value):
        """Set value of `issuer`

        :param value: value to set
        :type value: str
        """

        self._issuer.set(value)

    @property
    def name(self):
        """Certificate name.
        
        api example: 'My certificate'
        
        :rtype: str
        """

        return self._name.value

    @name.setter
    def name(self, value):
        """Set value of `name`

        :param value: value to set
        :type value: str
        """

        self._name.set(value)

    @property
    def owner_id(self):
        """The UUID of the owner.
        
        api example: '01619571dad80242ac12000600000000'
        
        :rtype: str
        """

        return self._owner_id.value

    @owner_id.setter
    def owner_id(self, value):
        """Set value of `owner_id`

        :param value: value to set
        :type value: str
        """

        self._owner_id.set(value)

    @property
    def security_file_content(self):
        """Content of the security.c file that will be flashed into the device to provide
        the security credentials
        
        :rtype: str
        """

        return self._security_file_content.value

    @security_file_content.setter
    def security_file_content(self, value):
        """Set value of `security_file_content`

        :param value: value to set
        :type value: str
        """

        self._security_file_content.set(value)

    @property
    def service(self):
        """Service name where the certificate is to be used.
        
        :rtype: str
        """

        return self._service.value

    @service.setter
    def service(self, value):
        """Set value of `service`

        :param value: value to set
        :type value: str
        """

        self._service.set(value)

    @property
    def status(self):
        """Status of the certificate.
        
        api example: 'ACTIVE'
        
        :rtype: str
        """

        return self._status.value

    @status.setter
    def status(self, value):
        """Set value of `status`

        :param value: value to set
        :type value: str
        """

        self._status.set(value)

    @property
    def subject(self):
        """Subject of the certificate.
        
        api example: 'CN=subject'
        
        :rtype: str
        """

        return self._subject.value

    @subject.setter
    def subject(self, value):
        """Set value of `subject`

        :param value: value to set
        :type value: str
        """

        self._subject.set(value)

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
    def validity(self):
        """Expiration time in UTC formatted as RFC3339.
        
        api example: '2038-02-14T15:24:14Z'
        
        :rtype: datetime
        """

        return self._validity.value

    @validity.setter
    def validity(self, value):
        """Set value of `validity`

        :param value: value to set
        :type value: datetime
        """

        self._validity.set(value)

    def create_developer(self, authorization):
        """Create a new developer certificate to connect to the bootstrap server.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/developer-certificates
        
        :param authorization: Bearer {Access Token}.
        :type authorization: str
        
        :rtype: Certificate
        """

        return self._client.call_api(
            method="post",
            path="/v3/developer-certificates",
            header_params={"Authorization": fields.StringField(authorization).to_api()},
            None_params={},
            body_params={
                "description": self._description.to_api(),
                "name": self._name.to_api(),
            },
            unpack=self,
        )

    def create_standard(self, signature=None):
        """Upload a new trusted certificate.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/trusted-certificates
        
        :param signature: DEPRECATED: Base64 encoded signature of the account ID signed by the
            certificate to be uploaded. The signature must be hashed with SHA256.
        :type signature: str
        
        :rtype: Certificate
        """

        return self._client.call_api(
            method="post",
            path="/v3/trusted-certificates",
            body_params={
                "certificate": self._certificate.to_api(),
                "description": self._description.to_api(),
                "enrollment_mode": self._enrollment_mode.to_api(),
                "name": self._name.to_api(),
                "": self._service.to_api(),
                "signature": fields.StringField(signature).to_api(),
                "status": self._status.to_api(),
            },
            None_params={},
            unpack=self,
        )

    def delete(self):
        """Delete a trusted certificate by ID.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/trusted-certificates/{cert-id}
        
        :rtype: Certificate
        """

        return self._client.call_api(
            method="delete",
            path="/v3/trusted-certificates/{cert-id}",
            None_params={},
            path_params={"cert-id": self._id.to_api()},
            unpack=self,
        )

    def get_developer(self, authorization, developercertificateid):
        """Fetch an existing developer certificate to connect to the bootstrap server.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/developer-certificates/{developerCertificateId}
        
        :param authorization: Bearer {Access Token}.
        :type authorization: str
        
        :param developercertificateid: A unique identifier for the developer certificate.
        :type developercertificateid: str
        
        :rtype: Certificate
        """

        return self._client.call_api(
            method="get",
            path="/v3/developer-certificates/{developerCertificateId}",
            header_params={"Authorization": fields.StringField(authorization).to_api()},
            None_params={},
            path_params={
                "developerCertificateId": fields.StringField(
                    developercertificateid
                ).to_api()
            },
            unpack=self,
        )

    def get_standard(self):
        """Get trusted certificate by ID.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/trusted-certificates/{cert-id}
        
        :rtype: Certificate
        """

        return self._client.call_api(
            method="get",
            path="/v3/trusted-certificates/{cert-id}",
            None_params={},
            path_params={"cert-id": self._id.to_api()},
            body_params={"": self._service.to_api()},
            unpack=self,
        )

    def list(
        self,
        after=None,
        device_execution_mode__eq=None,
        device_execution_mode__neq=None,
        enrollment_mode__eq=None,
        expire__eq=None,
        include=None,
        issuer__like=None,
        limit=50,
        name__eq=None,
        order="ASC",
        service__eq=None,
        subject__like=None,
    ):
        """Get all trusted certificates.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/trusted-certificates
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param device_execution_mode__eq: Device execution mode, as 1 for developer certificates or as another
            natural integer value
        :type device_execution_mode__eq: int
        
        :param device_execution_mode__neq: Device execution mode not equals filter
        :type device_execution_mode__neq: int
        
        :param enrollment_mode__eq: Enrollment mode filter
        :type enrollment_mode__eq: bool
        
        :param expire__eq: Expire filter in days
        :type expire__eq: int
        
        :param include: Comma separated additional data to return. Currently supported:
            total_count
        :type include: str
        
        :param issuer__like: Issuer filter. Finds all matches where the filter value is a case
            insensitive substring of the result. Example: issuer__like=cn=iss
            matches CN=issuer.
        :type issuer__like: str
        
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: int
        
        :param name__eq: Filter for certificate name
        :type name__eq: str
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :param service__eq: Service filter, either lwm2m or bootstrap
        :type service__eq: str
        
        :param subject__like: Subject filter. Finds all matches where the filter value is a case
            insensitive substring of the result. Example: subject__like=cn=su
            matches CN=subject.
        :type subject__like: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        from mbed_cloud.sdk.common._custom_methods import paginate
        from mbed_cloud.sdk.entities import Certificate

        return paginate(
            self=self,
            foreign_key=Certificate,
            after=after,
            device_execution_mode__eq=device_execution_mode__eq,
            device_execution_mode__neq=device_execution_mode__neq,
            enrollment_mode__eq=enrollment_mode__eq,
            expire__eq=expire__eq,
            include=include,
            issuer__like=issuer__like,
            limit=limit,
            name__eq=name__eq,
            order=order,
            service__eq=service__eq,
            subject__like=subject__like,
            wraps=self._paginate_list,
        )

    def _paginate_list(
        self,
        after=None,
        device_execution_mode__eq=None,
        device_execution_mode__neq=None,
        enrollment_mode__eq=None,
        expire__eq=None,
        include=None,
        issuer__like=None,
        limit=50,
        name__eq=None,
        order="ASC",
        service__eq=None,
        subject__like=None,
    ):
        """Get all trusted certificates.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/trusted-certificates
        
        :param after: The entity ID to fetch after the given one.
        :type after: str
        
        :param device_execution_mode__eq: Device execution mode, as 1 for developer certificates or as another
            natural integer value
        :type device_execution_mode__eq: int
        
        :param device_execution_mode__neq: Device execution mode not equals filter
        :type device_execution_mode__neq: int
        
        :param enrollment_mode__eq: Enrollment mode filter
        :type enrollment_mode__eq: bool
        
        :param expire__eq: Expire filter in days
        :type expire__eq: int
        
        :param include: Comma separated additional data to return. Currently supported:
            total_count
        :type include: str
        
        :param issuer__like: Issuer filter. Finds all matches where the filter value is a case
            insensitive substring of the result. Example: issuer__like=cn=iss
            matches CN=issuer.
        :type issuer__like: str
        
        :param limit: The number of results to return (2-1000), default is 50.
        :type limit: int
        
        :param name__eq: Filter for certificate name
        :type name__eq: str
        
        :param order: The order of the records based on creation time, ASC or DESC; by
            default ASC
        :type order: str
        
        :param service__eq: Service filter, either lwm2m or bootstrap
        :type service__eq: str
        
        :param subject__like: Subject filter. Finds all matches where the filter value is a case
            insensitive substring of the result. Example: subject__like=cn=su
            matches CN=subject.
        :type subject__like: str
        
        :rtype: mbed_cloud.pagination.PaginatedResponse
        """

        return self._client.call_api(
            method="get",
            path="/v3/trusted-certificates",
            query_params={
                "after": fields.StringField(after).to_api(),
                "device_execution_mode__eq": fields.IntegerField(
                    device_execution_mode__eq
                ).to_api(),
                "device_execution_mode__neq": fields.IntegerField(
                    device_execution_mode__neq
                ).to_api(),
                "enrollment_mode__eq": fields.BooleanField(
                    enrollment_mode__eq
                ).to_api(),
                "expire__eq": fields.IntegerField(expire__eq).to_api(),
                "include": fields.StringField(include).to_api(),
                "issuer__like": fields.StringField(issuer__like).to_api(),
                "limit": fields.IntegerField(limit).to_api(),
                "name__eq": fields.StringField(name__eq).to_api(),
                "order": fields.StringField(
                    order, enum=enums.CertificateOrderEnum
                ).to_api(),
                "service__eq": fields.StringField(service__eq).to_api(),
                "subject__like": fields.StringField(subject__like).to_api(),
            },
            None_params={},
            unpack=False,
        )

    def update(self, signature=None):
        """Update trusted certificate.

        api documentation:
        https://os.mbed.com/search/?q=service+apis+/v3/trusted-certificates/{cert-id}
        
        :param signature: DEPRECATED: Base64 encoded signature of the account ID signed by the
            certificate to be uploaded. The signature must be hashed with SHA256.
        :type signature: str
        
        :rtype: Certificate
        """

        return self._client.call_api(
            method="put",
            path="/v3/trusted-certificates/{cert-id}",
            body_params={
                "certificate": self._certificate.to_api(),
                "description": self._description.to_api(),
                "enrollment_mode": self._enrollment_mode.to_api(),
                "name": self._name.to_api(),
                "": self._service.to_api(),
                "signature": fields.StringField(signature).to_api(),
                "status": self._status.to_api(),
            },
            None_params={},
            path_params={"cert-id": self._id.to_api()},
            unpack=self,
        )
