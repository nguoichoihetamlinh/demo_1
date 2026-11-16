"""M2 Lệnh sản xuất và điều độ."""
import pandas as pd

from db.database import fetch_one, query_df, transaction
from services.common import (due_in_work_minutes, now_str, to_dt, to_str,
                             work_minutes_to_dt)

# ---------- Vòng đời trạng thái lệnh (Bước 3, mục 4.1) ----------
MOI_TAO, DA_LAP_LICH, DA_PHAT_LENH = "Mới tạo", "Đã lập lịch", "Đã phát lệnh"
DANG_SX, TAM_DUNG, HOAN_THANH, DA_DONG, DA_HUY = (
    "Đang sản xuất", "Tạm dừng", "Hoàn thành", "Đã đóng", "Đã hủy")

TRANSITIONS = {
    MOI_TAO: {DA_LAP_LICH, DA_HUY},
    DA_LAP_LICH: {DA_PHAT_LENH, DA_HUY, DA_LAP_LICH},   # được lập lịch lại
    DA_PHAT_LENH: {DANG_SX},
    DANG_SX: {TAM_DUNG, HOAN_THANH},
    TAM_DUNG: {DANG_SX},
    HOAN_THANH: {DA_DONG},
    DA_DONG: set(),
    DA_HUY: set(),
}
RULES = {"FIFO": "Đến trước làm trước (ngày đặt)",
         "EDD": "Hạn giao sớm nhất trước",
         "SPT": "Thời gian gia công ngắn nhất trước"}


def can_transition(cur, new):
    return new in TRANSITIONS.get(cur, set())


def change_status(ma_lsx, new, ts=None, conn=None):
    """Đổi trạng thái lệnh, chặn chuyển trạng thái không hợp lệ, ghi lịch sử."""
    # TODO Buổi 3: viết hàm change_status theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 3: change_status")


def new_order_code(day, conn):
    """Sinh mã LSX-yyMMdd-xx kế tiếp cho ngày day."""
    prefix = f"LSX-{to_dt(day):%y%m%d}-"
    n = conn.execute("SELECT COUNT(*) FROM lenh_san_xuat WHERE ma_lsx LIKE ?", (prefix + "%",)).fetchone()[0]
    return f"{prefix}{n + 1:02d}"


def create_work_order(ma_dh, ts=None):
    """Tạo lệnh sản xuất từ một đơn hàng 'mới'. Trả về mã lệnh."""
    # TODO Buổi 3: viết hàm create_work_order theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 3: create_work_order")


def get_routing(ma_san_pham):
    return query_df("SELECT * FROM quy_trinh WHERE ma_san_pham = ? ORDER BY thu_tu", (ma_san_pham,))


def material_requirements(ma_lsx):
    """Nhu cầu vật tư của lệnh = định mức x (1 + hao hụt) x số lượng; so với tồn kho."""
    # TODO Buổi 3: viết hàm material_requirements theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 3: material_requirements")


def schedule_orders(rule, start_day, orders=None):
    """Lập lịch flow shop 5 trạm, chuyển cả lô giữa các trạm.

    rule: FIFO | EDD | SPT. orders: DataFrame lệnh cần xếp (mặc định: lệnh Mới tạo/Đã lập lịch).
    Trả về (plan, summary): plan = mỗi lệnh x mỗi trạm có bat_dau/ket_thuc;
    summary = mỗi lệnh có thời điểm hoàn thành, hạn giao, số phút trễ.
    """
    # TODO Buổi 3: viết hàm schedule_orders theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 3: schedule_orders")


def compare_rules(start_day):
    """So sánh 3 quy tắc: makespan, tổng phút trễ, số lệnh trễ."""
    # TODO Buổi 3: viết hàm compare_rules theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 3: compare_rules")


def save_schedule(plan):
    """Ghi thứ tự ưu tiên và thời gian kế hoạch vào lệnh, chuyển sang Đã lập lịch."""
    # TODO Buổi 3: viết hàm save_schedule theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 3: save_schedule")


def eligible_workers(ma_tram, ma_ca=None):
    sql = """SELECT n.ma_nv, n.ho_ten, n.ma_ca, k.muc_thanh_thao FROM nhan_vien n
             JOIN ky_nang k ON k.ma_nv = n.ma_nv WHERE k.ma_tram = ? AND n.vai_tro = 'công nhân'"""
    params = [ma_tram]
    if ma_ca:
        sql += " AND n.ma_ca = ?"
        params.append(ma_ca)
    return query_df(sql + " ORDER BY k.muc_thanh_thao DESC, n.ma_nv", tuple(params))


def assign_worker(ma_lsx, ma_tram, ma_nv, ma_ca, ngay):
    """Phân công công nhân cho một công đoạn; chặn người không có kỹ năng ở trạm đó."""
    # TODO Buổi 3: viết hàm assign_worker theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 3: assign_worker")


def auto_assign(ma_lsx, ma_ca, ngay):
    """Gán cho mỗi trạm công nhân thành thạo nhất trong ca."""
    # TODO Buổi 3: viết hàm auto_assign theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 3: auto_assign")


def release_order(ma_lsx, ts=None):
    """Phát lệnh xuống trạm: đủ vật tư và đủ phân công 5 trạm mới được phát."""
    # TODO Buổi 3: viết hàm release_order theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 3: release_order")
