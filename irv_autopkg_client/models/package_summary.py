from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PackageSummary")


@attr.s(auto_attribs=True)
class PackageSummary:
    """Summary information about a top-level package (which is formed from a boundary)

    Attributes:
        boundary_name (str):
        uri (str):
    """

    boundary_name: str
    uri: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        boundary_name = self.boundary_name
        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "boundary_name": boundary_name,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        boundary_name = d.pop("boundary_name")

        uri = d.pop("uri")

        package_summary = cls(
            boundary_name=boundary_name,
            uri=uri,
        )

        package_summary.additional_properties = d
        return package_summary

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
