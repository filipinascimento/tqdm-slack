"""
Enables multiple commonly used features.

Method resolution order:

- `tqdm.autonotebook` without import warnings
- `tqdm.asyncio` on Python3.6+
- `tqdm.std` base class

Usage:
>>> from tqdm.auto import trange, tqdm
>>> for i in trange(10):
...     ...
"""
from .auto_normal import tqdm as tqdm_auto

import os
if("TQDM_SLACK_TOKEN" in os.environ and "TQDM_SLACK_CHANNEL" in os.environ):
    from .contrib.slack import tqdm as tqdm_slack
    from .contrib.slack import trange as trange_slack
    def tqdm (*args, **kwargs):
        return tqdm_slack(*args, **kwargs)
    def trange (*args, **kwargs):
        return trange_slack(*args, **kwargs)
else: 
    from .auto_normal import tqdm, trange

__all__ = ["tqdm", "trange"]
