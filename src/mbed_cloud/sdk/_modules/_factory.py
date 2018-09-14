"""
Factory module

This file is autogenerated from api specifications
"""

# Python 2 compatibility
from __future__ import unicode_literals
from builtins import str  # noqa
from builtins import object


class InstanceFactory:
    """Creates instances of Entities with a client mixed in"""

    def __init__(self, client):
        """InstanceFactory takes a client to attach to the models it creates"""
        self._client = client

    def api_key(
        self,
        created_at=None,
        creation_time=None,
        group_ids=None,
        id=None,
        key=None,
        last_login_time=None,
        name=None,
        owner=None,
        status=None,
        updated_at=None,
    ):
        """Creates a local `ApiKey` instance, binding the client

        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: The timestamp of the API key creation in the storage, in
            milliseconds.
        :type creation_time: int
        :param group_ids: A list of group IDs this API key belongs to.
        :type group_ids: list
        :param id: The UUID of the API key.
        :type id: str
        :param key: The API key.
        :type key: str
        :param last_login_time: The timestamp of the latest API key usage, in milliseconds.
        :type last_login_time: int
        :param name: The display name for the API key.
        :type name: str
        :param owner: The owner of this API key, who is the creator by default.
        :type owner: str
        :param status: The status of the API key.
        :type status: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        
        :rtype: mbed_cloud.sdk.entities.ApiKey
        """
        from mbed_cloud.sdk.entities import ApiKey

        return ApiKey(
            _client=self._client,
            created_at=created_at,
            creation_time=creation_time,
            group_ids=group_ids,
            id=id,
            key=key,
            last_login_time=last_login_time,
            name=name,
            owner=owner,
            status=status,
            updated_at=updated_at,
        )

    def login_history(self, date=None, ip_address=None, success=None, user_agent=None):
        """Creates a local `LoginHistory` instance, binding the client

        :param date: UTC time RFC3339 for this login attempt.
        :type date: datetime
        :param ip_address: IP address of the client.
        :type ip_address: str
        :param success: Flag indicating whether login attempt was successful or not.
        :type success: bool
        :param user_agent: User Agent header from the login request.
        :type user_agent: str
        
        :rtype: mbed_cloud.sdk.entities.LoginHistory
        """
        from mbed_cloud.sdk.entities import LoginHistory

        return LoginHistory(
            _client=self._client,
            date=date,
            ip_address=ip_address,
            success=success,
            user_agent=user_agent,
        )

    def my_account(
        self,
        address_line1=None,
        address_line2=None,
        aliases=None,
        city=None,
        company=None,
        contact=None,
        contract_number=None,
        country=None,
        created_at=None,
        custom_fields=None,
        customer_number=None,
        display_name=None,
        email=None,
        end_market=None,
        expiration_warning_threshold=None,
        id=None,
        idle_timeout=None,
        limits=None,
        mfa_status=None,
        notification_emails=None,
        parent_id=None,
        password_policy=None,
        phone_number=None,
        policies=None,
        postal_code=None,
        reason=None,
        reference_note=None,
        sales_contact=None,
        state=None,
        status=None,
        sub_accounts=None,
        template_id=None,
        tier=None,
        updated_at=None,
        upgraded_at=None,
    ):
        """Creates a local `MyAccount` instance, binding the client

        :param address_line1: Postal address line 1.
        :type address_line1: str
        :param address_line2: Postal address line 2.
        :type address_line2: str
        :param aliases: An array of aliases.
        :type aliases: list
        :param city: The city part of the postal address.
        :type city: str
        :param company: The name of the company.
        :type company: str
        :param contact: The name of the contact person for this account.
        :type contact: str
        :param contract_number: Contract number of the customer.
        :type contract_number: str
        :param country: The country part of the postal address.
        :type country: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param custom_fields: Account's custom properties as key-value pairs.
        :type custom_fields: dict
        :param customer_number: Customer number of the customer.
        :type customer_number: str
        :param display_name: The display name for the account.
        :type display_name: str
        :param email: The company email address for this account.
        :type email: str
        :param end_market: Account end market.
        :type end_market: str
        :param expiration_warning_threshold: Indicates how many days (1-180) before account expiration a
            notification email should be sent.
        :type expiration_warning_threshold: str
        :param id: Account ID.
        :type id: str
        :param idle_timeout: The reference token expiration time in minutes for this account.
        :type idle_timeout: str
        :param limits: List of limits as key-value pairs if requested.
        :type limits: dict
        :param mfa_status: The enforcement status of the multi-factor authentication, either
            'enforced' or 'optional'.
        :type mfa_status: str
        :param notification_emails: A list of notification email addresses.
        :type notification_emails: list
        :param parent_id: The ID of the parent account, if it has any.
        :type parent_id: str
        :param password_policy: 
        :type password_policy: dict
        :param phone_number: The phone number of a representative of the company.
        :type phone_number: str
        :param policies: List of policies if requested.
        :type policies: list
        :param postal_code: The postal code part of the postal address.
        :type postal_code: str
        :param reason: A reason note for updating the status of the account
        :type reason: str
        :param reference_note: A reference note for updating the status of the account
        :type reference_note: str
        :param sales_contact: Email address of the sales contact.
        :type sales_contact: str
        :param state: The state part of the postal address.
        :type state: str
        :param status: The status of the account.
        :type status: str
        :param sub_accounts: List of sub accounts. Not available for developer users.
        :type sub_accounts: list
        :param template_id: Account template ID.
        :type template_id: str
        :param tier: The tier level of the account; '0': free tier, '1': commercial
            account, '2': partner tier. Other values are reserved for the
            future.
        :type tier: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param upgraded_at: Time when upgraded to commercial account in UTC format RFC3339.
        :type upgraded_at: datetime
        
        :rtype: mbed_cloud.sdk.entities.MyAccount
        """
        from mbed_cloud.sdk.entities import MyAccount

        return MyAccount(
            _client=self._client,
            address_line1=address_line1,
            address_line2=address_line2,
            aliases=aliases,
            city=city,
            company=company,
            contact=contact,
            contract_number=contract_number,
            country=country,
            created_at=created_at,
            custom_fields=custom_fields,
            customer_number=customer_number,
            display_name=display_name,
            email=email,
            end_market=end_market,
            expiration_warning_threshold=expiration_warning_threshold,
            id=id,
            idle_timeout=idle_timeout,
            limits=limits,
            mfa_status=mfa_status,
            notification_emails=notification_emails,
            parent_id=parent_id,
            password_policy=password_policy,
            phone_number=phone_number,
            policies=policies,
            postal_code=postal_code,
            reason=reason,
            reference_note=reference_note,
            sales_contact=sales_contact,
            state=state,
            status=status,
            sub_accounts=sub_accounts,
            template_id=template_id,
            tier=tier,
            updated_at=updated_at,
            upgraded_at=upgraded_at,
        )

    def password_policy(self, minimum_length=None):
        """Creates a local `PasswordPolicy` instance, binding the client

        :param minimum_length: Minimum length for the password. A number between 8 and 512.
        :type minimum_length: str
        
        :rtype: mbed_cloud.sdk.entities.PasswordPolicy
        """
        from mbed_cloud.sdk.entities import PasswordPolicy

        return PasswordPolicy(_client=self._client, minimum_length=minimum_length)

    def policy_group(
        self,
        account_id=None,
        apikey_count=None,
        created_at=None,
        id=None,
        name=None,
        updated_at=None,
        user_count=None,
    ):
        """Creates a local `PolicyGroup` instance, binding the client

        :param account_id: The UUID of the account this group belongs to.
        :type account_id: str
        :param apikey_count: The number of API keys in this group.
        :type apikey_count: int
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param id: The UUID of the group.
        :type id: str
        :param name: The name of the group.
        :type name: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param user_count: The number of users in this group.
        :type user_count: int
        
        :rtype: mbed_cloud.sdk.entities.PolicyGroup
        """
        from mbed_cloud.sdk.entities import PolicyGroup

        return PolicyGroup(
            _client=self._client,
            account_id=account_id,
            apikey_count=apikey_count,
            created_at=created_at,
            id=id,
            name=name,
            updated_at=updated_at,
            user_count=user_count,
        )

    def subtenant_account(
        self,
        address_line1=None,
        address_line2=None,
        admin_email=None,
        admin_full_name=None,
        admin_id=None,
        admin_key=None,
        admin_name=None,
        admin_password=None,
        aliases=None,
        city=None,
        company=None,
        contact=None,
        contract_number=None,
        country=None,
        created_at=None,
        custom_fields=None,
        customer_number=None,
        display_name=None,
        email=None,
        end_market=None,
        expiration_warning_threshold=None,
        id=None,
        idle_timeout=None,
        limits=None,
        mfa_status=None,
        notification_emails=None,
        parent_id=None,
        password_policy=None,
        phone_number=None,
        policies=None,
        postal_code=None,
        reason=None,
        reference_note=None,
        sales_contact=None,
        state=None,
        status=None,
        sub_accounts=None,
        template_id=None,
        tier=None,
        updated_at=None,
        upgraded_at=None,
    ):
        """Creates a local `SubtenantAccount` instance, binding the client

        :param address_line1: Postal address line 1.
        :type address_line1: str
        :param address_line2: Postal address line 2.
        :type address_line2: str
        :param admin_email: The email address of the account admin, not longer than 254
            characters.
        :type admin_email: str
        :param admin_full_name: The full name of the admin user to be created.
        :type admin_full_name: str
        :param admin_id: The ID of the admin user created.
        :type admin_id: str
        :param admin_key: The admin API key created for the account.
        :type admin_key: str
        :param admin_name: The username of the admin user to be created, containing
            alphanumerical letters and -,._@+= characters. It must be at least
            4 but not more than 30 character long.
        :type admin_name: str
        :param admin_password: The password when creating a new user. It will be generated when
            not present in the request.
        :type admin_password: str
        :param aliases: An array of aliases.
        :type aliases: list
        :param city: The city part of the postal address.
        :type city: str
        :param company: The name of the company.
        :type company: str
        :param contact: The name of the contact person for this account.
        :type contact: str
        :param contract_number: Contract number of the customer.
        :type contract_number: str
        :param country: The country part of the postal address.
        :type country: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param custom_fields: Account's custom properties as key-value pairs.
        :type custom_fields: dict
        :param customer_number: Customer number of the customer.
        :type customer_number: str
        :param display_name: The display name for the account.
        :type display_name: str
        :param email: The company email address for this account.
        :type email: str
        :param end_market: Account end market.
        :type end_market: str
        :param expiration_warning_threshold: Indicates how many days (1-180) before account expiration a
            notification email should be sent.
        :type expiration_warning_threshold: str
        :param id: Account ID.
        :type id: str
        :param idle_timeout: The reference token expiration time in minutes for this account.
        :type idle_timeout: str
        :param limits: List of limits as key-value pairs if requested.
        :type limits: dict
        :param mfa_status: The enforcement status of the multi-factor authentication, either
            'enforced' or 'optional'.
        :type mfa_status: str
        :param notification_emails: A list of notification email addresses.
        :type notification_emails: list
        :param parent_id: The ID of the parent account, if it has any.
        :type parent_id: str
        :param password_policy: 
        :type password_policy: dict
        :param phone_number: The phone number of a representative of the company.
        :type phone_number: str
        :param policies: List of policies if requested.
        :type policies: list
        :param postal_code: The postal code part of the postal address.
        :type postal_code: str
        :param reason: A reason note for updating the status of the account
        :type reason: str
        :param reference_note: A reference note for updating the status of the account
        :type reference_note: str
        :param sales_contact: Email address of the sales contact.
        :type sales_contact: str
        :param state: The state part of the postal address.
        :type state: str
        :param status: The status of the account.
        :type status: str
        :param sub_accounts: List of sub accounts. Not available for developer users.
        :type sub_accounts: list
        :param template_id: Account template ID.
        :type template_id: str
        :param tier: The tier level of the account; '0': free tier, '1': commercial
            account, '2': partner tier. Other values are reserved for the
            future.
        :type tier: str
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param upgraded_at: Time when upgraded to commercial account in UTC format RFC3339.
        :type upgraded_at: datetime
        
        :rtype: mbed_cloud.sdk.entities.SubtenantAccount
        """
        from mbed_cloud.sdk.entities import SubtenantAccount

        return SubtenantAccount(
            _client=self._client,
            address_line1=address_line1,
            address_line2=address_line2,
            admin_email=admin_email,
            admin_full_name=admin_full_name,
            admin_id=admin_id,
            admin_key=admin_key,
            admin_name=admin_name,
            admin_password=admin_password,
            aliases=aliases,
            city=city,
            company=company,
            contact=contact,
            contract_number=contract_number,
            country=country,
            created_at=created_at,
            custom_fields=custom_fields,
            customer_number=customer_number,
            display_name=display_name,
            email=email,
            end_market=end_market,
            expiration_warning_threshold=expiration_warning_threshold,
            id=id,
            idle_timeout=idle_timeout,
            limits=limits,
            mfa_status=mfa_status,
            notification_emails=notification_emails,
            parent_id=parent_id,
            password_policy=password_policy,
            phone_number=phone_number,
            policies=policies,
            postal_code=postal_code,
            reason=reason,
            reference_note=reference_note,
            sales_contact=sales_contact,
            state=state,
            status=status,
            sub_accounts=sub_accounts,
            template_id=template_id,
            tier=tier,
            updated_at=updated_at,
            upgraded_at=upgraded_at,
        )

    def user(
        self,
        account_id=None,
        address=None,
        created_at=None,
        creation_time=None,
        email=None,
        email_verified=None,
        full_name=None,
        group_ids=None,
        id=None,
        last_login_time=None,
        login_history=None,
        marketing_accepted=None,
        password=None,
        password_changed_time=None,
        phone_number=None,
        status=None,
        terms_accepted=None,
        two_factor_authentication=None,
        updated_at=None,
        username=None,
    ):
        """Creates a local `User` instance, binding the client

        :param account_id: The UUID of the account.
        :type account_id: str
        :param address: Address.
        :type address: str
        :param created_at: Creation UTC time RFC3339.
        :type created_at: datetime
        :param creation_time: A timestamp of the user creation in the storage, in milliseconds.
        :type creation_time: int
        :param email: The email address.
        :type email: str
        :param email_verified: A flag indicating whether the user's email address has been
            verified or not.
        :type email_verified: bool
        :param full_name: The full name of the user.
        :type full_name: str
        :param group_ids: A list of IDs of the groups this user belongs to.
        :type group_ids: list
        :param id: The UUID of the user.
        :type id: str
        :param last_login_time: A timestamp of the latest login of the user, in milliseconds.
        :type last_login_time: int
        :param login_history: Timestamps, succeedings, IP addresses and user agent information
            of the last five logins of the user, with timestamps in RFC3339
            format.
        :type login_history: list
        :param marketing_accepted: A flag indicating that receiving marketing information has been
            accepted.
        :type marketing_accepted: bool
        :param password: The password when creating a new user. It will be generated when
            not present in the request.
        :type password: str
        :param password_changed_time: A timestamp of the latest change of the user password, in
            milliseconds.
        :type password_changed_time: int
        :param phone_number: Phone number.
        :type phone_number: str
        :param status: The status of the user. ENROLLING state indicates that the user is
            in the middle of the enrollment process. INVITED means that the
            user has not accepted the invitation request. RESET means that the
            password must be changed immediately. INACTIVE users are locked
            out and not permitted to use the system.
        :type status: str
        :param terms_accepted: A flag indicating that the General Terms and Conditions has been
            accepted.
        :type terms_accepted: bool
        :param two_factor_authentication: A flag indicating whether 2-factor authentication (TOTP) has been
            enabled.
        :type two_factor_authentication: bool
        :param updated_at: Last update UTC time RFC3339.
        :type updated_at: datetime
        :param username: A username containing alphanumerical letters and -,._@+=
            characters.
        :type username: str
        
        :rtype: mbed_cloud.sdk.entities.User
        """
        from mbed_cloud.sdk.entities import User

        return User(
            _client=self._client,
            account_id=account_id,
            address=address,
            created_at=created_at,
            creation_time=creation_time,
            email=email,
            email_verified=email_verified,
            full_name=full_name,
            group_ids=group_ids,
            id=id,
            last_login_time=last_login_time,
            login_history=login_history,
            marketing_accepted=marketing_accepted,
            password=password,
            password_changed_time=password_changed_time,
            phone_number=phone_number,
            status=status,
            terms_accepted=terms_accepted,
            two_factor_authentication=two_factor_authentication,
            updated_at=updated_at,
            username=username,
        )
