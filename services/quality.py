"""M5 Quản lý chất lượng."""
from db.database import execute, query_df
from services.common import now_str


def record_inspection(ma_lsx, ma_tram, so_mau, so_dat, ma_loi=None, so_luong_loi=0, ma_nv_qc=None, ts=None):
    """Ghi kết quả kiểm tra; số đạt + số lỗi không vượt số mẫu; có lỗi thì bắt buộc mã lỗi."""
    # TODO Buổi 4: viết hàm record_inspection theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 4: record_inspection")


def pareto_defects():
    """Pareto lỗi: số lượng theo mã lỗi, sắp giảm dần, kèm tỷ lệ tích lũy."""
    # TODO Buổi 4: viết hàm pareto_defects theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 4: pareto_defects")


def defect_rate_by_station():
    """Tỷ lệ lỗi theo trạm = số lỗi / (số đạt + số lỗi) từ nhật ký công đoạn."""
    # TODO Buổi 4: viết hàm defect_rate_by_station theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 4: defect_rate_by_station")


def quality_alerts(threshold=0.05):
    """Trạm có tỷ lệ lỗi vượt ngưỡng (mặc định 5%, Bước 3 mục 5.5)."""
    # TODO Buổi 4: viết hàm quality_alerts theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 4: quality_alerts")
