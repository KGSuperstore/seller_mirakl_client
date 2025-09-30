from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.a02_response_200_updated_specific_billing_informations_corporate_information import (
        A02Response200UpdatedSpecificBillingInformationsCorporateInformation,
    )
    from ..models.a02_response_200_updated_specific_billing_informations_fiscal_information import (
        A02Response200UpdatedSpecificBillingInformationsFiscalInformation,
    )
    from ..models.a02_response_200_updated_specific_billing_informations_fiscal_representative import (
        A02Response200UpdatedSpecificBillingInformationsFiscalRepresentative,
    )
    from ..models.a02_response_200_updated_specific_billing_informations_personal_information import (
        A02Response200UpdatedSpecificBillingInformationsPersonalInformation,
    )
    from ..models.a02_response_200_updated_specific_billing_informations_registration_address import (
        A02Response200UpdatedSpecificBillingInformationsRegistrationAddress,
    )


T = TypeVar("T", bound="A02Response200UpdatedSpecificBillingInformations")


@_attrs_define
class A02Response200UpdatedSpecificBillingInformations:
    """
    Attributes:
        corporate_information (Union[Unset, A02Response200UpdatedSpecificBillingInformationsCorporateInformation]):
        fiscal_information (Union[Unset, A02Response200UpdatedSpecificBillingInformationsFiscalInformation]):
        fiscal_representative (Union[Unset, A02Response200UpdatedSpecificBillingInformationsFiscalRepresentative]):
        id (Union[Unset, str]): The unique identifier of the specific billing information.
        personal_information (Union[Unset, A02Response200UpdatedSpecificBillingInformationsPersonalInformation]):
        registration_address (Union[Unset, A02Response200UpdatedSpecificBillingInformationsRegistrationAddress]):
    """

    corporate_information: Union[Unset, "A02Response200UpdatedSpecificBillingInformationsCorporateInformation"] = UNSET
    fiscal_information: Union[Unset, "A02Response200UpdatedSpecificBillingInformationsFiscalInformation"] = UNSET
    fiscal_representative: Union[Unset, "A02Response200UpdatedSpecificBillingInformationsFiscalRepresentative"] = UNSET
    id: Union[Unset, str] = UNSET
    personal_information: Union[Unset, "A02Response200UpdatedSpecificBillingInformationsPersonalInformation"] = UNSET
    registration_address: Union[Unset, "A02Response200UpdatedSpecificBillingInformationsRegistrationAddress"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        corporate_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.corporate_information, Unset):
            corporate_information = self.corporate_information.to_dict()

        fiscal_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fiscal_information, Unset):
            fiscal_information = self.fiscal_information.to_dict()

        fiscal_representative: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fiscal_representative, Unset):
            fiscal_representative = self.fiscal_representative.to_dict()

        id = self.id

        personal_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.personal_information, Unset):
            personal_information = self.personal_information.to_dict()

        registration_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.registration_address, Unset):
            registration_address = self.registration_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if corporate_information is not UNSET:
            field_dict["corporate_information"] = corporate_information
        if fiscal_information is not UNSET:
            field_dict["fiscal_information"] = fiscal_information
        if fiscal_representative is not UNSET:
            field_dict["fiscal_representative"] = fiscal_representative
        if id is not UNSET:
            field_dict["id"] = id
        if personal_information is not UNSET:
            field_dict["personal_information"] = personal_information
        if registration_address is not UNSET:
            field_dict["registration_address"] = registration_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.a02_response_200_updated_specific_billing_informations_corporate_information import (
            A02Response200UpdatedSpecificBillingInformationsCorporateInformation,
        )
        from ..models.a02_response_200_updated_specific_billing_informations_fiscal_information import (
            A02Response200UpdatedSpecificBillingInformationsFiscalInformation,
        )
        from ..models.a02_response_200_updated_specific_billing_informations_fiscal_representative import (
            A02Response200UpdatedSpecificBillingInformationsFiscalRepresentative,
        )
        from ..models.a02_response_200_updated_specific_billing_informations_personal_information import (
            A02Response200UpdatedSpecificBillingInformationsPersonalInformation,
        )
        from ..models.a02_response_200_updated_specific_billing_informations_registration_address import (
            A02Response200UpdatedSpecificBillingInformationsRegistrationAddress,
        )

        d = dict(src_dict)
        _corporate_information = d.pop("corporate_information", UNSET)
        corporate_information: Union[Unset, A02Response200UpdatedSpecificBillingInformationsCorporateInformation]
        if isinstance(_corporate_information, Unset):
            corporate_information = UNSET
        else:
            corporate_information = A02Response200UpdatedSpecificBillingInformationsCorporateInformation.from_dict(
                _corporate_information
            )

        _fiscal_information = d.pop("fiscal_information", UNSET)
        fiscal_information: Union[Unset, A02Response200UpdatedSpecificBillingInformationsFiscalInformation]
        if isinstance(_fiscal_information, Unset):
            fiscal_information = UNSET
        else:
            fiscal_information = A02Response200UpdatedSpecificBillingInformationsFiscalInformation.from_dict(
                _fiscal_information
            )

        _fiscal_representative = d.pop("fiscal_representative", UNSET)
        fiscal_representative: Union[Unset, A02Response200UpdatedSpecificBillingInformationsFiscalRepresentative]
        if isinstance(_fiscal_representative, Unset):
            fiscal_representative = UNSET
        else:
            fiscal_representative = A02Response200UpdatedSpecificBillingInformationsFiscalRepresentative.from_dict(
                _fiscal_representative
            )

        id = d.pop("id", UNSET)

        _personal_information = d.pop("personal_information", UNSET)
        personal_information: Union[Unset, A02Response200UpdatedSpecificBillingInformationsPersonalInformation]
        if isinstance(_personal_information, Unset):
            personal_information = UNSET
        else:
            personal_information = A02Response200UpdatedSpecificBillingInformationsPersonalInformation.from_dict(
                _personal_information
            )

        _registration_address = d.pop("registration_address", UNSET)
        registration_address: Union[Unset, A02Response200UpdatedSpecificBillingInformationsRegistrationAddress]
        if isinstance(_registration_address, Unset):
            registration_address = UNSET
        else:
            registration_address = A02Response200UpdatedSpecificBillingInformationsRegistrationAddress.from_dict(
                _registration_address
            )

        a02_response_200_updated_specific_billing_informations = cls(
            corporate_information=corporate_information,
            fiscal_information=fiscal_information,
            fiscal_representative=fiscal_representative,
            id=id,
            personal_information=personal_information,
            registration_address=registration_address,
        )

        a02_response_200_updated_specific_billing_informations.additional_properties = d
        return a02_response_200_updated_specific_billing_informations

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
