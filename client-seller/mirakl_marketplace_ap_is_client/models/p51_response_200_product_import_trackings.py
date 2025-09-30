import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.p51_response_200_product_import_trackings_conversion_options import (
        P51Response200ProductImportTrackingsConversionOptions,
    )
    from ..models.p51_response_200_product_import_trackings_integration_details import (
        P51Response200ProductImportTrackingsIntegrationDetails,
    )


T = TypeVar("T", bound="P51Response200ProductImportTrackings")


@_attrs_define
class P51Response200ProductImportTrackings:
    """
    Attributes:
        conversion_options (Union[Unset, P51Response200ProductImportTrackingsConversionOptions]):
        conversion_type (Union[Unset, str]): Type of conversion applied on products
        date_created (Union[Unset, datetime.datetime]): Import creation date
        has_error_report (Union[Unset, bool]): Returns true if error report is available. Value is filled when the
            import is completed
        has_new_product_report (Union[Unset, bool]): Returns true if new product report is available. Value is filled
            when the import is completed
        has_transformation_error_report (Union[Unset, bool]): Returns true if transformation error report is available.
            Value is filled when the import is completed
        has_transformed_file (Union[Unset, bool]): Returns true if transformed file is available. Value is filled when
            the import is completed
        import_id (Union[Unset, int]): Import identifier
        import_status (Union[Unset, str]): Import status
        integration_details (Union[Unset, P51Response200ProductImportTrackingsIntegrationDetails]):
        reason_status (Union[Unset, str]): A message explaining the reason of the import status, if relevant
        shop_id (Union[Unset, int]): Shop identifier
        transform_lines_in_error (Union[Unset, int]): Total count of transformed lines in error
        transform_lines_in_success (Union[Unset, int]): Total count of transformed lines in success
        transform_lines_read (Union[Unset, int]): Total count of transformed lines read
        transform_lines_with_warning (Union[Unset, int]): Total count of transformed lines with warning
    """

    conversion_options: Union[Unset, "P51Response200ProductImportTrackingsConversionOptions"] = UNSET
    conversion_type: Union[Unset, str] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    has_error_report: Union[Unset, bool] = UNSET
    has_new_product_report: Union[Unset, bool] = UNSET
    has_transformation_error_report: Union[Unset, bool] = UNSET
    has_transformed_file: Union[Unset, bool] = UNSET
    import_id: Union[Unset, int] = UNSET
    import_status: Union[Unset, str] = UNSET
    integration_details: Union[Unset, "P51Response200ProductImportTrackingsIntegrationDetails"] = UNSET
    reason_status: Union[Unset, str] = UNSET
    shop_id: Union[Unset, int] = UNSET
    transform_lines_in_error: Union[Unset, int] = UNSET
    transform_lines_in_success: Union[Unset, int] = UNSET
    transform_lines_read: Union[Unset, int] = UNSET
    transform_lines_with_warning: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversion_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conversion_options, Unset):
            conversion_options = self.conversion_options.to_dict()

        conversion_type = self.conversion_type

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        has_error_report = self.has_error_report

        has_new_product_report = self.has_new_product_report

        has_transformation_error_report = self.has_transformation_error_report

        has_transformed_file = self.has_transformed_file

        import_id = self.import_id

        import_status = self.import_status

        integration_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.integration_details, Unset):
            integration_details = self.integration_details.to_dict()

        reason_status = self.reason_status

        shop_id = self.shop_id

        transform_lines_in_error = self.transform_lines_in_error

        transform_lines_in_success = self.transform_lines_in_success

        transform_lines_read = self.transform_lines_read

        transform_lines_with_warning = self.transform_lines_with_warning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversion_options is not UNSET:
            field_dict["conversion_options"] = conversion_options
        if conversion_type is not UNSET:
            field_dict["conversion_type"] = conversion_type
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if has_error_report is not UNSET:
            field_dict["has_error_report"] = has_error_report
        if has_new_product_report is not UNSET:
            field_dict["has_new_product_report"] = has_new_product_report
        if has_transformation_error_report is not UNSET:
            field_dict["has_transformation_error_report"] = has_transformation_error_report
        if has_transformed_file is not UNSET:
            field_dict["has_transformed_file"] = has_transformed_file
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if import_status is not UNSET:
            field_dict["import_status"] = import_status
        if integration_details is not UNSET:
            field_dict["integration_details"] = integration_details
        if reason_status is not UNSET:
            field_dict["reason_status"] = reason_status
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if transform_lines_in_error is not UNSET:
            field_dict["transform_lines_in_error"] = transform_lines_in_error
        if transform_lines_in_success is not UNSET:
            field_dict["transform_lines_in_success"] = transform_lines_in_success
        if transform_lines_read is not UNSET:
            field_dict["transform_lines_read"] = transform_lines_read
        if transform_lines_with_warning is not UNSET:
            field_dict["transform_lines_with_warning"] = transform_lines_with_warning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.p51_response_200_product_import_trackings_conversion_options import (
            P51Response200ProductImportTrackingsConversionOptions,
        )
        from ..models.p51_response_200_product_import_trackings_integration_details import (
            P51Response200ProductImportTrackingsIntegrationDetails,
        )

        d = dict(src_dict)
        _conversion_options = d.pop("conversion_options", UNSET)
        conversion_options: Union[Unset, P51Response200ProductImportTrackingsConversionOptions]
        if isinstance(_conversion_options, Unset):
            conversion_options = UNSET
        else:
            conversion_options = P51Response200ProductImportTrackingsConversionOptions.from_dict(_conversion_options)

        conversion_type = d.pop("conversion_type", UNSET)

        _date_created = d.pop("date_created", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        has_error_report = d.pop("has_error_report", UNSET)

        has_new_product_report = d.pop("has_new_product_report", UNSET)

        has_transformation_error_report = d.pop("has_transformation_error_report", UNSET)

        has_transformed_file = d.pop("has_transformed_file", UNSET)

        import_id = d.pop("import_id", UNSET)

        import_status = d.pop("import_status", UNSET)

        _integration_details = d.pop("integration_details", UNSET)
        integration_details: Union[Unset, P51Response200ProductImportTrackingsIntegrationDetails]
        if isinstance(_integration_details, Unset):
            integration_details = UNSET
        else:
            integration_details = P51Response200ProductImportTrackingsIntegrationDetails.from_dict(_integration_details)

        reason_status = d.pop("reason_status", UNSET)

        shop_id = d.pop("shop_id", UNSET)

        transform_lines_in_error = d.pop("transform_lines_in_error", UNSET)

        transform_lines_in_success = d.pop("transform_lines_in_success", UNSET)

        transform_lines_read = d.pop("transform_lines_read", UNSET)

        transform_lines_with_warning = d.pop("transform_lines_with_warning", UNSET)

        p51_response_200_product_import_trackings = cls(
            conversion_options=conversion_options,
            conversion_type=conversion_type,
            date_created=date_created,
            has_error_report=has_error_report,
            has_new_product_report=has_new_product_report,
            has_transformation_error_report=has_transformation_error_report,
            has_transformed_file=has_transformed_file,
            import_id=import_id,
            import_status=import_status,
            integration_details=integration_details,
            reason_status=reason_status,
            shop_id=shop_id,
            transform_lines_in_error=transform_lines_in_error,
            transform_lines_in_success=transform_lines_in_success,
            transform_lines_read=transform_lines_read,
            transform_lines_with_warning=transform_lines_with_warning,
        )

        p51_response_200_product_import_trackings.additional_properties = d
        return p51_response_200_product_import_trackings

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
