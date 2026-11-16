"""M6 Thiết bị, dừng máy và OEE."""
import pandas as pd

from db.database import execute, query_df
from services.common import minutes_between, to_dt


def record_downtime(ma_tb, bat_dau, ket_thuc, ma_nguyen_nhan, ma_lsx=None, ghi_chu=None):
    # TODO Buổi 4: viết hàm record_downtime theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 4: record_downtime")


def downtime_summary():
    """Tổng phút dừng theo trạm và nguyên nhân."""
    # TODO Buổi 5: viết hàm downtime_summary theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 5: downtime_summary")


def _overlap(a0, a1, b0, b1):
    s, e = max(to_dt(a0), to_dt(b0)), min(to_dt(a1), to_dt(b1))
    return max(0.0, (e - s).total_seconds() / 60)


def calc_oee(ma_tram, tu, den):
    """OEE = A x P x Q của một trạm trong khoảng [tu, den].

    Thời gian kế hoạch = (den - tu) trừ bảo trì định kỳ (nhóm 'kế hoạch').
    A: trừ dừng máy ảnh hưởng 'khả dụng'. P: thời gian chuẩn x sản lượng / thời gian chạy.
    Q: số đạt / tổng số sản xuất.
    """
    # TODO Buổi 5: viết hàm calc_oee theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 5: calc_oee")


def oee_all(tu, den):
    stations = query_df("SELECT ma_tram FROM tram ORDER BY thu_tu_tren_day_chuyen")["ma_tram"]
    return pd.DataFrame([calc_oee(s, tu, den) for s in stations])


def production_window():
    """Khoảng thời gian từ lúc trạm đầu bắt đầu đến lúc công đoạn cuối kết thúc (mặc định để tính OEE)."""
    r = query_df("SELECT MIN(thoi_diem_bat_dau) a, MAX(thoi_diem_ket_thuc) b FROM nhat_ky_cong_doan")
    return (r.a[0], r.b[0]) if r.a[0] else (None, None)
