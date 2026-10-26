<!-- vlc-disable: all -->

# Hospitality, Aviation, & Travel Glossary (`design-os-vietnamese`)

This glossary provides standardized Vietnamese terminology for hotels, luxury resorts, commercial aviation, Fine Dining / F&B culinary copy, and outbound/inbound tourism.
The first table is parsed by `validate_copy.py` at runtime; every row acts as a linting rule firing `CAL001` with the declared severity.

## 1. Machine-Readable Hospitality, Aviation, & Culinary Terms

<!-- machine-readable: glossary -->

| EN | ❌ Wrong or stale | ✅ Correct | Severity |
|---|---|---|---|
| check-in | `nhận buồng phòng` | `nhận phòng` | error |
| check-out | `trả buồng phòng` | `trả phòng` | error |
| front desk / reception | `bàn tiếp tân` | `quầy lễ tân` | warn |
| housekeeping | `người lau dọn phòng` | `bộ phận buồng phòng` | error |
| concierge | `người phục vụ hỗ trợ` | `bộ phận trợ giúp đặc biệt / Concierge` | warn |
| bellman | `người mang vác hành lý` | `nhân viên hành lý / Bellman` | warn |
| room service | `dịch vụ phòng ốc` | `dịch vụ ẩm thực tại phòng` | warn |
| complimentary breakfast | `bữa sáng miễn trừ` | `bữa sáng miễn phí / bữa sáng bao gồm` | error |
| early check-in | `nhận phòng sớm trước hạn` | `nhận phòng sớm` | warn |
| late check-out | `trả phòng trễ giờ` | `trả phòng muộn` | warn |
| no-show | `không xuất hiện tại chỗ` | `khách vắng mặt không báo trước (No-show)` | warn |
| overbooking | `đặt phòng vượt quá sức` | `đặt phòng vượt tải (Overbooking)` | warn |
| cancellation policy | `chính sách hủy bỏ phòng` | `chính sách hoàn hủy` | error |
| surcharge | `khoản tính thêm phí` | `phụ thu` | error |
| minibar | `tủ lạnh nhỏ rượu` | `quầy bar mini trong phòng` | warn |
| amenity | `sự tiện nghi phòng` | `tiện ích phòng / vật phẩm tiện ích` | error |
| rollaway bed / extra bed | `giường lăn thêm` | `giường phụ (Extra bed)` | warn |
| turn down service | `dịch vụ gập chăn màn` | `dịch vụ dọn phòng buổi tối (Turn-down service)` | warn |
| sea view | `quang cảnh biển khơi` | `hướng biển` | warn |
| city view | `quang cảnh thành thị` | `hướng thành phố` | warn |
| garden view | `quang cảnh vườn tược` | `hướng vườn` | warn |
| boarding pass | `thẻ lên máy bay tàu bay` | `thẻ lên tàu bay` | error |
| baggage allowance | `sự cho phép hành lý` | `tiêu chuẩn hành lý miễn cước` | error |
| carry-on baggage | `hành lý xách trên tay` | `hành lý xách tay` | error |
| checked baggage | `hành lý kiểm tra kỹ` | `hành lý ký gửi` | error |
| excess baggage | `hành lý dư thừa thãi` | `hành lý quá cước` | error |
| flight attendant | `người phục vụ chuyến bay` | `tiếp viên hàng không` | error |
| flight delay | `sự chậm trễ chuyến` | `chậm chuyến` | error |
| cancelled flight | `chuyến bay bị tiêu hủy` | `chuyến bay bị hủy` | error |
| rebooking | `đặt lại chỗ ngồi máy bay` | `đổi chuyến bay / chuyển chuyến` | error |
| refund (ticket) | `trả lại tiền vé máy bay` | `hoàn vé` | error |
| departure gate | `cổng vào tàu bay` | `cửa ra tàu bay / cửa khởi hành` | error |
| boarding time | `thời gian lên tàu bay đón` | `giờ lên tàu bay` | error |
| departure time | `thời gian cất cánh đi` | `giờ khởi hành` | error |
| arrival time | `thời gian hạ cánh đến` | `giờ đến dự kiến` | error |
| runway | `đường chạy cất hạ cánh` | `đường băng` | warn |
| transit | `quá cảnh chuyển máy bay` | `quá cảnh / nối chuyến` | warn |
| layover | `thời gian dừng chờ bay` | `thời gian quá cảnh / dừng nghỉ` | warn |
| fine dining | `ăn uống tinh tế cao cấp` | `ẩm thực cao cấp (Fine Dining)` | warn |
| tasting menu | `thực đơn nếm thử món` | `thực đơn chọn lọc của bếp trưởng (Tasting Menu)` | warn |
| à la carte | `gọi món theo thực đơn rời` | `thực đơn gọi món (À la carte)` | warn |
| set menu | `thực đơn thiết lập sẵn` | `thực đơn theo set` | warn |
| appetizer | `món ăn khai mạc bữa` | `món khai vị` | error |
| main course | `món ăn chính yếu` | `món chính` | error |
| dessert | `món ăn tráng miệng sau` | `món tráng miệng` | error |
| wine pairing | `ghép nối rượu vang` | `kết hợp rượu vang (Wine pairing)` | warn |
| sommelier | `người phục vụ rượu vang` | `chuyên gia rượu vang (Sommelier)` | warn |
| dress code | `quy chuẩn ăn mặc quần áo` | `quy định trang phục` | warn |
| service charge | `phí tổn phục vụ ăn` | `phí phục vụ` | error |
| corkage fee | `phí khui nút chai rượu` | `phí phục vụ đồ uống mang vào (Corkage fee)` | warn |
| dietary requirement | `yêu cầu ăn kiêng đặc biệt` | `yêu cầu khẩu vị / chế độ ăn uống riêng` | warn |
| tour itinerary | `bản hành trình chuyến đi` | `lịch trình du lịch` | warn |
| guided tour | `chuyến đi có hướng dẫn viên đi kèm` | `tour có hướng dẫn viên` | warn |
| tour operator | `đơn vị vận hành tour lữ hành` | `doanh nghiệp lữ hành` | error |
| sightseeing | `ngắm cảnh tham quan du lịch` | `tham quan ngắm cảnh` | warn |
| package tour | `chuyến du lịch trọn gói toàn bộ` | `tour trọn gói` | error |
| visa on arrival | `thị thực tại chỗ đến` | `thị thực tại cửa khẩu` | error |
| customs clearance | `sự thông quan hải quan` | `thủ tục thông quan hải quan` | warn |
| peak season | `mùa du lịch cao điểm nhất` | `mùa cao điểm` | warn |
| low season | `mùa du lịch thấp điểm vắng` | `mùa thấp điểm` | warn |
