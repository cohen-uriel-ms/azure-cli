# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network service-endpoint policy-definition create",
)
class Create(AAZCommand):
    """Create a service endpoint policy definition.

    :example: Create a service endpoint policy definition.
        az network service-endpoint policy-definition create -g MyResourceGroup --policy-name MyPolicy -n MyPolicyDefinition --service Microsoft.Storage --description "Test Def" --service-resources MyServiceResources
    """

    _aaz_info = {
        "version": "2021-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/serviceendpointpolicies/{}/serviceendpointpolicydefinitions/{}", "2021-08-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the service endpoint policy definition.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.policy_name = AAZStrArg(
            options=["--policy-name"],
            help="Name of the service endpoint policy.",
            required=True,
            id_part="name",
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            help="Description of the policy definition.",
        )
        _args_schema.service = AAZStrArg(
            options=["--service"],
            help="Service name the policy definition applies to.  Values from: `az network service-endpoint list`.",
        )
        _args_schema.service_resources = AAZListArg(
            options=["--service-resources"],
            help="Space-separated list of service resources the definition applies to.",
        )

        service_resources = cls._args_schema.service_resources
        service_resources.Element = AAZStrArg()

        # define Arg Group "ServiceEndpointPolicyDefinitions"
        return cls._args_schema

    def _execute_operations(self):
        yield self.ServiceEndpointPolicyDefinitionsCreateOrUpdate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ServiceEndpointPolicyDefinitionsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceEndpointPolicyDefinitionName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceEndpointPolicyName", self.ctx.args.policy_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-08-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("service", AAZStrType, ".service")
                properties.set_prop("serviceResources", AAZListType, ".service_resources")

            service_resources = _builder.get(".properties.serviceResources")
            if service_resources is not None:
                service_resources.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.id = AAZStrType()
            _schema_on_200_201.name = AAZStrType()
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.type = AAZStrType()

            properties = cls._schema_on_200_201.properties
            properties.description = AAZStrType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.service = AAZStrType()
            properties.service_resources = AAZListType(
                serialized_name="serviceResources",
            )

            service_resources = cls._schema_on_200_201.properties.service_resources
            service_resources.Element = AAZStrType()

            return cls._schema_on_200_201


__all__ = ["Create"]
