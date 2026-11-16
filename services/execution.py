"""M3 Theo dõi WIP, truy xuất và M4 Thu thập dữ liệu công đoạn."""
from db.database import fetch_one, query_df, transaction
from services import planning as P
from services.common import now_str


def stations_in_order(ma_san_pham):
    return list(query_df("SELECT ma_tram FROM quy_trinh WHERE ma_san_pham = ? ORDER BY thu_tu",
                         (ma_san_pham,))["ma_tram"])


def next_station(ma_lsx):
    """Trạm kế tiếp lệnh phải đi qua (None nếu đã qua hết)."""
    lsx = fetch_one("SELECT ma_san_pham FROM lenh_san_xuat WHERE ma_lsx = ?", (ma_lsx,))
    done = set(query_df("SELECT ma_tram FROM nhat_ky_cong_doan WHERE ma_lsx = ? AND thoi_diem_ket_thuc IS NOT NULL",
                        (ma_lsx,))["ma_tram"])
    for s in stations_in_order(lsx["ma_san_pham"]):
        if s not in done:
            return s
    return None


def input_quantity(ma_lsx, ma_tram):
    """Số lượng vào trạm = số đạt của trạm trước; trạm đầu = số lượng kế hoạch."""
    lsx = fetch_one("SELECT ma_san_pham, so_luong_ke_hoach FROM lenh_san_xuat WHERE ma_lsx = ?", (ma_lsx,))
    route = stations_in_order(lsx["ma_san_pham"])
    i = route.index(ma_tram)
    if i == 0:
        return lsx["so_luong_ke_hoach"]
    prev = fetch_one("SELECT so_luong_dat FROM nhat_ky_cong_doan WHERE ma_lsx = ? AND ma_tram = ?"
                     " AND thoi_diem_ket_thuc IS NOT NULL", (ma_lsx, route[i - 1]))
    return prev["so_luong_dat"] if prev else 0


def issue_material(ma_lsx, ts, conn):
    """Xuất vật tư theo BOM, lấy lô nhập trước xuất trước (FIFO). Trả về mã lô nguyên liệu chính."""
    # TODO Buổi 4: viết hàm issue_material theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 4: issue_material")


def start_operation(ma_lsx, ma_tram, ts=None, ma_nv=None):
    """Công nhân báo bắt đầu công đoạn. Kiểm tra trạng thái lệnh và thứ tự trạm."""
    # TODO Buổi 4: viết hàm start_operation theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 4: start_operation")


def finish_operation(log_id, so_dat, so_loi, ts=None):
    """Báo kết thúc công đoạn; trạm cuối thì cập nhật kết quả lệnh và chuyển Hoàn thành."""
    # TODO Buổi 4: viết hàm finish_operation theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 4: finish_operation")


def wip_status():
    """Bảng WIP: lệnh đang sản xuất, trạm hiện tại, số trạm đã qua."""
    # TODO Buổi 4: viết hàm wip_status theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 4: wip_status")


def trace_order(ma_lsx):
    """Hồ sơ phả hệ của một lệnh: công đoạn, lô vật tư, kiểm tra, dừng máy."""
    # TODO Buổi 4: viết hàm trace_order theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 4: trace_order")


def trace_lot(ma_lo):
    """Truy xuất ngược: lô vật tư đã dùng cho những lệnh, đơn hàng, khách hàng nào."""
    # TODO Buổi 4: viết hàm trace_lot theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 4: trace_lot")
