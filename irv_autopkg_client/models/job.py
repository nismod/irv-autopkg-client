from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """
    Attributes:
        boundary_name (str):
        processors (List[str]):
    """

    boundary_name: str
    processors: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        boundary_name = self.boundary_name
        processors = self.processors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "boundary_name": boundary_name,
                "processors": processors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        boundary_name = d.pop("boundary_name")

        processors = cast(List[str], d.pop("processors"))

        job = cls(
            boundary_name=boundary_name,
            processors=processors,
        )

        job.additional_properties = d
        return job

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
