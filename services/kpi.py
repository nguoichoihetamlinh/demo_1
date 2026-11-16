"""M7 Báo cáo KPI và xuất báo cáo về ERP."""
from db.database import fetch_one, query_df
from services import planning as P
from services.common import minutes_between, to_dt


def order_results():
    """Mỗi lệnh đã xong: thời điểm bắt đầu T1, kết thúc T5, lead time, đúng hạn hay không."""
    # TODO Buổi 5: viết hàm order_results theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 5: order_results")


def kpi_summary():
    """Các chỉ số tổng hợp cho dashboard."""
    # TODO Buổi 5: viết hàm kpi_summary theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 5: kpi_summary")


def export_erp_report(path):
    """Xuất báo cáo sản lượng, tiêu hao về ERP giả lập (CSV UTF-8)."""
    # TODO Buổi 5: viết hàm export_erp_report theo danh mục hàm (Bước 5, mục 4).
    raise NotImplementedError("TODO Buổi 5: export_erp_report")
