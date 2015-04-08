import pytest
import break_me as br


with pytest.raises(NameError):
    br.name_break()

