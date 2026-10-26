<!-- vlc-disable: all -->

# Survey & Research Design in Vietnamese (`vietnamese-tech-writing`)

In product user research (UXR) and customer feedback surveys, poorly formulated Vietnamese questions rarely read as grammatically broken. Instead, they produce **systematically corrupted quantitative data**—inflating customer satisfaction metrics and blinding product teams to usability failures.

---

## 1. Acquiescence Bias & The Agree/Disagree Trap (`PROD002`)

### The Psychometric Hazard
Acquiescence bias is the tendency of survey respondents to agree with assertions presented to them regardless of their true experience. In psychometric research (Jon A. Krosnick et al.), agree/disagree question structures artificially inflate agreement by **10 to 15 percentage points**.

In Vietnam, this effect is magnified by cultural politeness norms (*"tính hòa hiếu"*) and a societal reluctance to bluntly contradict an interviewer or a formally presented corporate statement.

### The Defect in Action
```
❌ FATALLY BIASED QUESTION:
"Bạn có đồng ý rằng giao diện ứng dụng rất dễ sử dụng không?"
( ) Rất đồng ý    ( ) Đồng ý    ( ) Không đồng ý    ( ) Rất không đồng ý

Result: 78% of respondents select "Đồng ý" or "Rất đồng ý" due to suggestion priming
and acquiescence bias, despite actual high drop-off rates on the checkout flow.
```

### The Rule
**Never use Agree/Disagree scales (`Đồng ý / Không đồng ý`) in user research or product feedback.**
Instead, measure the latent psychological construct directly using an **Item-Specific Construct Scale**.

---

## 2. Item-Specific Construct Scales in Vietnamese

An item-specific scale asks directly about the attribute being evaluated, anchoring both endpoints to the specific spectrum of that property.

### A. Ease of Use (Customer Effort Score — CES)
```
✅ ITEM-SPECIFIC SCALE:
"Mức độ dễ dàng khi hoàn thành thủ tục thanh toán trên ứng dụng?"
( ) Rất khó khăn
( ) Khó khăn
( ) Bình thường
( ) Dễ dàng
( ) Rất dễ dàng
```

### B. Satisfaction (Customer Satisfaction — CSAT)
```
✅ ITEM-SPECIFIC SCALE:
"Mức độ hài lòng của bạn đối với tính năng lập báo cáo tự động?"
( ) Rất không hài lòng
( ) Không hài lòng
( ) Tạm chấp nhận
( ) Hài lòng
( ) Rất hài lòng
```

### C. Frequency of Use
```
✅ ITEM-SPECIFIC SCALE:
"Tần suất bạn sử dụng tính năng xuất dữ liệu Excel?"
( ) Chưa bao giờ
( ) Hiếm khi (vài tháng một lần)
( ) Thỉnh thoảng (vài tuần một lần)
( ) Thường xuyên (hàng tuần)
( ) Rất thường xuyên (hàng ngày)
```

### D. Importance / Prioritization
```
✅ ITEM-SPECIFIC SCALE:
"Mức độ quan trọng của tính năng bảo mật hai lớp (2FA) đối với bạn?"
( ) Hoàn toàn không quan trọng
( ) Ít quan trọng
( ) Quan trọng ở mức trung bình
( ) Rất quan trọng
( ) Tối quan trọng (bắt buộc phải có)
```

---

## 3. Net Promoter Score (NPS) Preservation

NPS measures customer loyalty on an internationally benchmarked **0 to 10 scale**. A frequent defect in translated Vietnamese surveys is collapsing this scale into a binary question or a 1–5 scale.

### The Canonical Vietnamese NPS Question
```
"Trên thang điểm từ 0 đến 10, khả năng bạn sẽ giới thiệu sản phẩm DESIGN:OS
cho đồng nghiệp hoặc đối tác trong ngành là bao nhiêu?"

[0] [1] [2] [3] [4] [5] [6]  |  [7] [8]  |  [9] [10]
(Hoàn toàn không có khả năng)                (Chắc chắn sẽ giới thiệu)
         ↓                                ↓                 ↓
  Detractors (0 - 6)             Passives (7 - 8)    Promoters (9 - 10)
```

- **Rule 1: Never change the 11-point range (0–10).** Collapsing to 1–5 or Yes/No destroys comparability against international benchmarks.
- **Rule 2: Anchor both polar extremes.** Always label 0 as *"Hoàn toàn không có khả năng"* and 10 as *"Chắc chắn sẽ giới thiệu"*.

---

## 4. Avoiding Double-Barreled Questions in Vietnamese

A double-barreled question (*câu hỏi kép*) asks about two distinct properties simultaneously, making the answer impossible to interpret:
- ❌ *"Tính năng này có nhanh và tiện lợi không?"* (If the user found it fast but inconvenient, they cannot accurately answer).
- ✅ Split into two independent questions:
  1. *"Đánh giá tốc độ phản hồi của hệ thống:"* (Rất chậm → Rất nhanh)
  2. *"Đánh giá mức độ tiện lợi trong thao tác:"* (Rất bất tiện → Rất tiện lợi)

---

## 5. Summary Matrix of Psychometric Scale Anchors

| Measurement Metric | Left Anchor (1) | Midpoint (3) | Right Anchor (5) |
|---|---|---|---|
| **Dễ dàng (CES)** | `Rất khó khăn` | `Bình thường` | `Rất dễ dàng` |
| **Hài lòng (CSAT)** | `Rất không hài lòng` | `Bình thường` | `Rất hài lòng` |
| **Hữu ích (Utility)**| `Hoàn toàn không hữu ích`| `Hữu ích một phần` | `Vô cùng hữu ích` |
| **Tốc độ (Speed)** | `Rất chậm chạp` | `Chấp nhận được` | `Rất nhanh chóng` |
| **Rõ ràng (Clarity)**| `Rất mơ hồ / khó hiểu` | `Khá rõ ràng` | `Rất rõ ràng / dễ hiểu`|
