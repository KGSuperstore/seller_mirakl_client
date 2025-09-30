from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.a01_response_200_specific_billing_informations_corporate_information import (
        A01Response200SpecificBillingInformationsCorporateInformation,
    )
    from ..models.a01_response_200_specific_billing_informations_fiscal_information import (
        A01Response200SpecificBillingInformationsFiscalInformation,
    )
    from ..models.a01_response_200_specific_billing_informations_fiscal_representative import (
        A01Response200SpecificBillingInformationsFiscalRepresentative,
    )
    from ..models.a01_response_200_specific_billing_informations_personal_information import (
        A01Response200SpecificBillingInformationsPersonalInformation,
    )
    from ..models.a01_response_200_specific_billing_informations_registration_address import (
        A01Response200SpecificBillingInformationsRegistrationAddress,
    )


T = TypeVar("T", bound="A01Response200SpecificBillingInformations")


@_attrs_define
class A01Response200SpecificBillingInformations:
    """
    Attributes:
        corporate_information (Union[Unset, A01Response200SpecificBillingInformationsCorporateInformation]):
        fiscal_information (Union[Unset, A01Response200SpecificBillingInformationsFiscalInformation]):
        fiscal_representative (Union[Unset, A01Response200SpecificBillingInformationsFiscalRepresentative]):
        id (Union[Unset, str]): The unique identifier of the specific billing information.
        personal_information (Union[Unset, A01Response200SpecificBillingInformationsPersonalInformation]):
        registration_address (Union[Unset, A01Response200SpecificBillingInformationsRegistrationAddress]):
    """

    corporate_information: Union[Unset, "A01Response200SpecificBillingInformationsCorporateInformation"] = UNSET
    fiscal_information: Union[Unset, "A01Response200SpecificBillingInformationsFiscalInformation"] = UNSET
    fiscal_representative: Union[Unset, "A01Response200SpecificBillingInformationsFiscalRepresentative"] = UNSET
    id: Union[Unset, str] = UNSET
    personal_information: Union[Unset, "A01Response200SpecificBillingInformationsPersonalInformation"] = UNSET
    registration_address: Union[Unset, "A01Response200SpecificBillingInformationsRegistrationAddress"] = UNSET
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
        from ..models.a01_response_200_specific_billing_informations_corporate_information import (
            A01Response200SpecificBillingInformationsCorporateInformation,
        )
        from ..models.a01_response_200_specific_billing_informations_fiscal_information import (
            A01Response200SpecificBillingInformationsFiscalInformation,
        )
        from ..models.a01_response_200_specific_billing_informations_fiscal_representative import (
            A01Response200SpecificBillingInformationsFiscalRepresentative,
        )
        from ..models.a01_response_200_specific_billing_informations_personal_information import (
            A01Response200SpecificBillingInformationsPersonalInformation,
        )
        from ..models.a01_response_200_specific_billing_informations_registration_address import (
            A01Response200SpecificBillingInformationsRegistrationAddress,
        )

        d = dict(src_dict)
        _corporate_information = d.pop("corporate_information", UNSET)
        corporate_information: Union[Unset, A01Response200SpecificBillingInformationsCorporateInformation]
        if isinstance(_corporate_information, Unset):
            corporate_information = UNSET
        else:
            corporate_information = A01Response200SpecificBillingInformationsCorporateInformation.from_dict(
                _corporate_information
            )

        _fiscal_information = d.pop("fiscal_information", UNSET)
        fiscal_information: Union[Unset, A01Response200SpecificBillingInformationsFiscalInformation]
        if isinstance(_fiscal_information, Unset):
            fiscal_information = UNSET
        else:
            fiscal_information = A01Response200SpecificBillingInformationsFiscalInformation.from_dict(
                _fiscal_information
            )

        _fiscal_representative = d.pop("fiscal_representative", UNSET)
        fiscal_representative: Union[Unset, A01Response200SpecificBillingInformationsFiscalRepresentative]
        if isinstance(_fiscal_representative, Unset):
            fiscal_representative = UNSET
        else:
            fiscal_representative = A01Response200SpecificBillingInformationsFiscalRepresentative.from_dict(
                _fiscal_representative
            )

        id = d.pop("id", UNSET)

        _personal_information = d.pop("personal_information", UNSET)
        personal_information: Union[Unset, A01Response200SpecificBillingInformationsPersonalInformation]
        if isinstance(_personal_information, Unset):
            personal_information = UNSET
        else:
            personal_information = A01Response200SpecificBillingInformationsPersonalInformation.from_dict(
                _personal_information
            )

        _registration_address = d.pop("registration_address", UNSET)
        registration_address: Union[Unset, A01Response200SpecificBillingInformationsRegistrationAddress]
        if isinstance(_registration_address, Unset):
            registration_address = UNSET
        else:
            registration_address = A01Response200SpecificBillingInformationsRegistrationAddress.from_dict(
                _registration_address
            )

        a01_response_200_specific_billing_informations = cls(
            corporate_information=corporate_information,
            fiscal_information=fiscal_information,
            fiscal_representative=fiscal_representative,
            id=id,
            personal_information=personal_information,
            registration_address=registration_address,
        )

        a01_response_200_specific_billing_informations.additional_properties = d
        return a01_response_200_specific_billing_informations

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
