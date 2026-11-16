"""M1 Dữ liệu nền: kiểm tra tính hợp lệ và tồn kho."""
import pandas as pd

from db.database import query_df


def get_stock():
    """Tồn kho hiện tại của từng vật tư = tổng so_luong_con các lô; đánh dấu dưới mức tối thiểu."""
    # TODO Buổi 2: viết hàm get_stock theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 2: get_stock")


def validate_master_data():
    """Kiểm tra logic nghiệp vụ mà khóa ngoại không bắt được. Trả về DataFrame các vấn đề."""
    # TODO Buổi 2: viết hàm validate_master_data theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 2: validate_master_data")
