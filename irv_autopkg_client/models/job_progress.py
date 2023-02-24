from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobProgress")


@attr.s(auto_attribs=True)
class JobProgress:
    """Specifics about the progress of an individual Processors Job

    Attributes:
        percent_complete (Union[Unset, int]):
        current_task (Union[Unset, str]):
    """

    percent_complete: Union[Unset, int] = 0
    current_task: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percent_complete = self.percent_complete
        current_task = self.current_task

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percent_complete is not UNSET:
            field_dict["percent_complete"] = percent_complete
        if current_task is not UNSET:
            field_dict["current_task"] = current_task

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        percent_complete = d.pop("percent_complete", UNSET)

        current_task = d.pop("current_task", UNSET)

        job_progress = cls(
            percent_complete=percent_complete,
            current_task=current_task,
        )

        job_progress.additional_properties = d
        return job_progress

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
