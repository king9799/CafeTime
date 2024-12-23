# # import re
# #
# #
# # def parse_time(t):
# #     """Converts a time string (e.g., '10:30' or '10') to a float representing hours."""
# #     if ':' in t:
# #         h, m = map(int, t.split(':'))
# #         return h + m / 60
# #     return float(t)
# #
# #
# # def calculate_elapsed(start, end):
# #     """Calculates the elapsed time between start and end, accounting for AM/PM transitions."""
# #     start_time = parse_time(start)
# #     end_time = parse_time(end)
# #
# #     # If the end time is earlier than the start time, it spans midnight
# #     if end_time < start_time:
# #         if start_time < 12:
# #             end_time += 12  # Handle AM/PM transition
# #         else:
# #             end_time += 24  # Handle midnight crossing
# #
# #     elapsed = end_time - start_time
# #     print(f"Start: {start}, End: {end}, Elapsed: {elapsed}")
# #     return elapsed
# #
# #
# # def timesheetSum(path):
# #     total_hours = 0.0
# #     with open(path, 'r') as file:
# #         for line in file:
# #             line = line.strip()
# #             print(f"Processing line: {line}")
# #             # Split ranges like "10-11, 11:30-4" into individual intervals
# #             intervals = re.split(r',\s*', line)
# #             for interval in intervals:
# #                 try:
# #                     start, end = map(str.strip, interval.split('-'))
# #                     total_hours += calculate_elapsed(start, end)
# #                 except ValueError:
# #                     print(f"Skipping malformed interval: {interval}")
# #     print(f"Final Total Hours: {total_hours}")
# #     return total_hours
# #
# #
# # # Example usage
# # file_path = "test.txt"  # Update with your actual file path
# # result = timesheetSum(file_path)
# # print(f"Total hours worked: {result}")
# import re
#
#
# def parse_time(time_str):
#     """Parse time in H or H:MM format and convert to float hours."""
#     time_str = str(time_str).strip()
#
#     if ":" in time_str:  # Handle HH:MM format
#         h, m = map(int, time_str.split(":"))
#         return h + m / 60
#     return float(time_str)  # Handle single hour (H format)
#
#
# def convert_to_24hr(start, end):
#     """Converts 12-hour format to 24-hour format, for both start and end times."""
#
#     def convert_single_time(t):
#         h, m = (map(int, t.split(":"))) if ':' in t else (int(t), 0)
#         # Handle AM/PM logic
#         if h == 12:
#             return 0 + (m / 60) if m == 0 else 12 + (m / 60)  # 12 AM -> 0:00 and 12 PM -> 12:00
#         elif h < 12:
#             return h + (m / 60)  # AM case, no change
#         else:
#             return (h - 12) + (m / 60)  # PM case, convert to 24-hour
#
#     return convert_single_time(start), convert_single_time(end)
#
#
# def calculate_elapsed(start, end):
#     """Calculate the time difference in hours between start and end, adjusting for overnight times."""
#     start_time = parse_time(start)
#     end_time = parse_time(end)
#
#     if end_time < start_time:  # If end time is earlier than start time, add 24 hours
#         end_time += 24
#
#     return end_time - start_time
#
#
# def sum_timesheet(path):
#     """Summarizes the total hours worked from the timesheet file."""
#     total_hours = 0.0
#
#     with open(path, 'r') as file:
#         for line in file:
#             line = line.strip()  # Remove leading/trailing whitespace
#             intervals = re.split(r',\s*', line)  # Split on commas, to handle multiple ranges in one line
#
#             for interval in intervals:
#                 try:
#                     start, end = map(str.strip, interval.split('-'))  # Extract start and end time
#
#                     # Check if the time format is a 12-hour format (no ':' sign in times)
#                     if ':' not in start and ':' not in end:
#                         # Handle the 12-hour format time (e.g., "10-1" -> 10 AM to 1 PM)
#                         start, end = map(int, [start, end])  # Convert to integers
#                         start, end = convert_to_24hr(str(start), str(end))  # Convert to 24-hour format
#                     else:
#                         # Handle 24-hour format or already 12-hour format (with ':' sign)
#                         start, end = convert_to_24hr(start, end)  # Convert both to 24-hour format
#
#                     # Calculate and add the elapsed time for this interval
#                     total_hours += calculate_elapsed(start, end)
#
#                 except ValueError:
#                     pass  # If there is an error in the format, skip this interval
#
#     return total_hours
#
#
# # Example usage
# file_path = "test.txt"  # Update with your actual file path
# result = sum_timesheet(file_path)
# print(f"Total hours worked: {result}")


from fpdf import FPDF

# PDF sinfini yaratish (fpdf kutubxonasi bilan)
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, '3 Yoshdagi Bolada Yurak Chastotasi, Sistolik va Minutlik Hajmini Aniqlash', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Sahifa {self.page_no()}', 0, 0, 'C')

# PDF tarkibini yaratish
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

content = """
3 yoshdagi bolada yurak chastotasi, sistolik va minutlik hajmini aniqlash uchun bir necha muhim ma'lumotlarga ega bo'lishimiz kerak:

1. Yurak chastotasi: 3 yoshdagi bolalarda yurak chastotasi odatda 80-120 marta/minut bo'ladi. Bu ma'lumotni bolani tinch holatda o'lchash orqali aniqlash mumkin.

2. Sistolik hajm: Sistolik hajm (SV) yurakning bir urilishida chiqaradigan qon miqdorini anglatadi. Bolalarda sistolik hajmi odatda 30-50 ml atrofida bo'ladi.

3. Minutlik hajm: Minutlik hajm (CO) yurakning bir daqiqada chiqaradigan qon miqdorini anglatadi va quyidagi formuladan foydalanib hisoblanadi:

    CO = HR × SV

Bu yerda:
- HR — yurak chastotasi (marta/minut),
- SV — sistolik hajm (ml).

Masalan, agar bolada yurak chastotasi 100 marta/minut va sistolik hajmi 40 ml bo'lsa, minutlik hajmi quyidagicha hisoblanadi:

    CO = 100 × 40 = 4000 ml/min

Yoki boshqa so'z bilan aytganda, bu 4 litr/minutga teng.

Agar sizda aniq o'lchovlar mavjud bo'lsa, ulardan foydalanib hisoblashni amalga oshirishingiz mumkin.
"""

# Multi-cellni qo'llab-quvvatlash
pdf.set_auto_page_break(auto=True, margin=15)
pdf.multi_cell(0, 10, content)

# PDF faylni saqlash
file_path = "3_yoshdagi_bola_yurak_hisoblari.pdf"
pdf.output(file_path)

file_path
