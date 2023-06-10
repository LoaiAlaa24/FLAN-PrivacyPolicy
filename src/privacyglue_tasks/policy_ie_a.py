#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import cast

import datasets

from ..utils.task_utils import policy_ie_file_mapping

LABELS = [
    "Other",
    "Data Collection Usage",
    "Data Security Protection",
    "Data Sharing Disclosure",
    "Data Storage Retention Deletion",
]


def load_policy_ie_a(directory: str) -> datasets.DatasetDict:
    # initialize DatasetDict object
    combined = datasets.DatasetDict()\
    
    data_files=policy_ie_file_mapping(directory, "seq.in")

    # load tokens which are common for all sub-tasks
    tokens = datasets.load_dataset(
        "text", data_files=policy_ie_file_mapping(directory, "seq.in")
    )

    # since this is task A, only load labels
    labels = datasets.load_dataset(
        "text", data_files=policy_ie_file_mapping(directory, "label")
    ).rename_column("text", "label")
    
    
    # collect information about label
    label_info = datasets.ClassLabel(names=LABELS)

    # mypy-related specification to sub-type
    tokens = cast(datasets.DatasetDict, tokens)
    labels = cast(datasets.DatasetDict, labels)

    # zip together data
    for split in ["train", "validation", "test"]:        
        dataset = datasets.concatenate_datasets([tokens[split], labels[split]], axis=1)
        dataset.features["label"] = label_info
        combined[split] = dataset

    return combined


# def replace_labels(dataset):
#     # Replace text with prompt template logic
#     # You can use string formatting or any other method to generate the prompt template
    
#     return template
