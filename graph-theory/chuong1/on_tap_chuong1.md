# Ôn tập Chương 1: Các khái niệm cơ bản (LTDT 2026)

## Phần A. Công thức cần thuộc

| # | Công thức | Ghi chú |
|---|---|---|
| 1 | $\sum_{v\in V}\deg(v) = 2m$ | Định lý bắt tay, đúng cho cả đơn/đa/giả đồ thị (khuyên tính 2) |
| 2 | Số đỉnh bậc lẻ luôn **chẵn** | Hệ quả của (1) |
| 3 | $\sum \deg^+(v) = \sum \deg^-(v) = \lvert A\rvert$ | Đồ thị có hướng |
| 4 | $\deg(v) = \deg^+(v) + \deg^-(v)$ | Có hướng, khuyên tính 1 cho mỗi bên |
| 5 | $\deg(v) \ge \lvert N(v)\rvert$ | Bằng nhau khi là đơn đồ thị |
| 6 | $\kappa(G) \le \lambda(G) \le \delta(G) = \min \deg(v)$ | Đồ thị liên thông, không đầy đủ, $n\ge3$ |
| 7 | $0\le\kappa(G)\le n-1$, $\kappa(G)=n-1 \iff G=K_n$ | Tương tự cho $\lambda$ |

### Số cạnh các đồ thị đặc biệt (theo quy ước **slide**)

| Đồ thị | Số đỉnh | Bậc mỗi đỉnh | Số cạnh |
|---|---|---|---|
| $K_n$ (đầy đủ) | $n$ | $n-1$ | $\dfrac{n(n-1)}{2}$ |
| $k$-chính quy | $n$ | $k$ | $\dfrac{nk}{2}$ |
| $C_n$ (chu trình) | $n$ | $2$ | $n$ |
| $W_n$ (bánh xe, $n>3$) | $n$ (gồm tâm) | tâm: $n-1$, vành: $3$ | $2(n-1)$ |
| $K_{x,y}$ (2 phía đầy đủ) | $x+y$ | $V_1$: $y$, $V_2$: $x$ | $xy$ |

> ⚠️ **Bẫy quy ước $W_n$**: Slide định nghĩa $W_n$ có **tổng n đỉnh** ($C_{n-1}$ + 1 tâm) → $2(n-1)$ cạnh. **Rosen** định nghĩa $W_n$ = $C_n$ + 1 tâm, tức **n+1 đỉnh** → $2n$ cạnh. Đi thi theo slide của thầy, nhưng đọc Rosen thì nhớ lệch 1.

---

## Phần B. Tóm tắt khái niệm

**Phân loại đồ thị** (slide 24)

| Loại | Có hướng? | Cạnh bội? | Khuyên? |
|---|---|---|---|
| Đơn đồ thị vô hướng | | | |
| Đa đồ thị vô hướng | | ✓ | |
| Giả đồ thị vô hướng | | ✓ | ✓ |
| Đơn đồ thị có hướng | ✓ | | |
| Đa đồ thị có hướng | ✓ | ✓ | |

Không ghi gì thêm thì "đồ thị" = **vô hướng** (có thể đơn hoặc đa).

**Đỉnh & cạnh**
- Kề nhau (adjacent): 2 đỉnh có cạnh nối. $N(v)$ = tập đỉnh kề $v$.
- Liên thuộc (incident): cạnh $e$ nối $v_i, v_j$.
- Đỉnh treo: $\deg = 1$. Đỉnh cô lập: $\deg = 0$.
- Đồ thị nền: bỏ hướng các cung của đồ thị có hướng.

**Đồ thị con**
- Con $G_1 \subseteq G_2$: $V_1\subseteq V_2$, $E_1\subseteq E_2$.
- Con bao trùm (spanning): $V_1 = V_2$, $E_1\subseteq E_2$ (giữ đủ đỉnh).

**Đường đi, chu trình** (thuật ngữ khác nhau giữa tài liệu)

| Rosen | Tài liệu khác | Ý nghĩa |
|---|---|---|
| path | walk | dãy cạnh nối tiếp |
| circuit | closed walk | đỉnh đầu = đỉnh cuối |
| simple path | trail | không lặp **CẠNH** |
| (không có tên riêng) | path | không lặp **ĐỈNH** |

Slide theo Rosen: "đường đi đơn" = không lặp cạnh (được lặp đỉnh).

**Liên thông**
- Liên thông: mọi cặp đỉnh có đường đi.
- Thành phần liên thông: đồ thị con liên thông **tối đại**.
- Đỉnh cắt (khớp): bỏ đỉnh + cạnh liên thuộc → tăng số TPLT.
- Cạnh cắt (cầu): bỏ cạnh (giữ đỉnh) → tăng số TPLT.
- Không tách rời (nonseparable): không có đỉnh cắt.
- $\kappa(G)$: số đỉnh tối thiểu cần bỏ để G mất liên thông hoặc còn 1 đỉnh.
- $\lambda(G)$: số cạnh tối thiểu cần bỏ để G mất liên thông.
- Liên thông đỉnh mức k: $\kappa(G)\ge k$.

**Có hướng**
- Liên thông mạnh: mọi $u\ne v$ có đường $u\to v$ **và** $v\to u$.
- Liên thông yếu: đồ thị nền liên thông.
- Liên thông một phần (unilateral): xem lưu ý bên dưới.

### Mấy chỗ slide cần để ý
1. **Slide 70, liên thông một phần**: slide viết "tồn tại $v_k$ đi đến được cả $v_i$ và $v_j$". Định nghĩa chuẩn (Rosen, hầu hết giáo trình) là: với mọi cặp $u\ne v$, có đường $u\to v$ **hoặc** $v\to u$. Hai định nghĩa này **không tương đương**. Nên hỏi lại thầy dùng cái nào khi thi.
2. **Slide 16** ghi $E \ne \varnothing$, nhưng slide 38 lại có "0-regular graph" (không cạnh), slide 27 có đỉnh cô lập. Tức là quy ước $E\ne\varnothing$ không được áp chặt, đừng lấn cấn.
3. Định lý bắt tay chỉ là **điều kiện cần**: tổng bậc chẵn chưa chắc dựng được **đơn** đồ thị. Vd dãy 3, 3, 1, 1 (tổng 8 chẵn): 4 đỉnh mà có 2 đỉnh bậc 3 thì cả 2 phải kề mọi đỉnh còn lại, nên 2 đỉnh "bậc 1" thực ra có bậc 2, mâu thuẫn. (Đa đồ thị thì vẫn dựng được.)

---

## Phần C. Lời giải bài tập

### Bài 1.1. Số cạnh của đồ thị n đỉnh, mỗi đỉnh bậc k

**Công thức:** $\sum \deg(v) = 2m$

| Dữ kiện | Giá trị |
|---|---|
| Số đỉnh | $n$ |
| Bậc mỗi đỉnh | $k$ |
| Tổng bậc | $nk$ |

**Giải:**
1. Tổng bậc $= \underbrace{k + k + \dots + k}_{n} = nk$.
2. Bắt tay: $nk = 2m$.
3. $m = \dfrac{nk}{2}$. Điều kiện tồn tại: $nk$ chẵn.

$$\boxed{m = \dfrac{nk}{2}}$$

---

### Bài 1.2. Số cạnh khi biết bậc $d_1, \dots, d_n$

**Công thức:** $\sum \deg(v) = 2m$

**Giải:** Tổng bậc $= d_1 + d_2 + \dots + d_n = 2m$.

$$\boxed{m = \dfrac{1}{2}\sum_{i=1}^{n} d_i}$$

---

### Bài 1.3. Dãy bậc nào vi phạm định lý bắt tay?

**Công thức:** tổng bậc phải chẵn (⇔ số đỉnh bậc lẻ là chẵn).

| Câu | Dãy bậc | Tổng | Số đỉnh bậc lẻ | Kết luận |
|---|---|---|---|---|
| a | 3, 3, 3, 3, 2 | 14 | 4 | OK |
| b | 1, 2, 3, 4, 5 | **15** | **3** | **Vi phạm** |
| c | 0, 1, 2, 2, 3 | 8 | 2 | OK |
| d | 1, 1, 1, 1 | 4 | 4 | OK |

**Giải:** Chỉ câu b có tổng lẻ (15), không thể bằng $2m$.

Bonus (không bắt buộc): a, c, d đều dựng được thành **đơn** đồ thị thật:
- a: Havel–Hakimi: bỏ 1 đỉnh bậc 3, trừ 1 cho 3 đỉnh kế tiếp → 2, 2, 2, 2 = $C_4$ ✓.
- c: đỉnh bậc 3 kề 3 đỉnh còn lại (trừ đỉnh cô lập), thêm 1 cạnh giữa 2 đỉnh bậc 2 ✓.
- d: 2 cạnh rời nhau ✓.

$$\boxed{\text{Câu b}}$$

---

### Bài 1.4. Có đơn đồ thị 15 đỉnh, mỗi đỉnh bậc 5?

**Công thức:** $\sum \deg(v) = 2m$

| Dữ kiện | Giá trị |
|---|---|
| $n$ | 15 |
| $k$ | 5 |
| $nk$ | 75 (lẻ) |

**Giải:**
1. Tổng bậc $= 15 \times 5 = 75$.
2. Nếu tồn tại thì $75 = 2m$ → $m = 37{,}5$ không nguyên. Vô lý.
3. (Cách khác: 15 đỉnh đều bậc lẻ → số đỉnh bậc lẻ = 15 lẻ, trái hệ quả.)

$$\boxed{\text{Không tồn tại}}$$

---

### Bài 1.5. n đội, n+1 trận ⇒ có đội đá ≥ 3 trận

**Công thức:** bắt tay + phản chứng.

| Mô hình | |
|---|---|
| Đỉnh | $n$ đội |
| Cạnh | $n+1$ trận (đa đồ thị, vì 2 đội có thể gặp nhau nhiều lần) |
| $\deg(v)$ | số trận đội $v$ đã đá |

**Giải:**
1. Bắt tay: $\sum \deg(v) = 2(n+1) = 2n + 2$.
2. Giả sử mọi đội đá $\le 2$ trận: $\sum \deg(v) \le 2n$.
3. Suy ra $2n + 2 \le 2n$ → $2 \le 0$, vô lý.
4. Vậy tồn tại đội có $\deg(v) \ge 3$.

(Đây chính là nguyên lý Dirichlet: $2n+2$ "lượt đá" chia cho $n$ đội thì có đội nhận $\ge \lceil (2n+2)/n \rceil \ge 3$.)

$$\boxed{\exists\, v: \deg(v)\ge 3}$$

---

### Bài 1.6. Số cạnh của $K_n$

**Công thức:** $m = \dfrac{nk}{2}$ với $k = n-1$, hoặc đếm cặp $\binom{n}{2}$.

| | |
|---|---|
| Bậc mỗi đỉnh | $n-1$ |
| Số cặp đỉnh | $\binom{n}{2}$ |

**Giải:** Mỗi cặp đỉnh có đúng 1 cạnh → $m = \binom{n}{2}$. Kiểm lại bằng bắt tay: $n(n-1) = 2m$ ✓.
Ví dụ: $K_6$ có 15 cạnh, $K_{12}$ có 66 cạnh (khớp bảng slide 37).

$$\boxed{m = \dfrac{n(n-1)}{2}}$$

---

### Bài 1.7. Số cạnh của $C_n$

**Giải:** $C_n$ là đồ thị 2-chính quy → $m = \dfrac{2n}{2} = n$. (Hoặc đếm trực tiếp: $\langle v_1,v_2\rangle,\dots,\langle v_n,v_1\rangle$ có $n$ cạnh.)

$$\boxed{m = n}$$

---

### Bài 1.8. Số cạnh của $W_n$ (n đỉnh, theo slide)

| Phần | Số cạnh |
|---|---|
| Vành $C_{n-1}$ | $n-1$ |
| Nan hoa (tâm nối $n-1$ đỉnh) | $n-1$ |

**Giải:** $m = (n-1) + (n-1) = 2(n-1)$.
Kiểm bắt tay: tâm bậc $n-1$, $n-1$ đỉnh vành bậc 3 → tổng $= (n-1) + 3(n-1) = 4(n-1) = 2m$ ✓.
Ví dụ: $W_4 = K_4$ có 6 cạnh ✓.

$$\boxed{m = 2(n-1)}$$

(Theo Rosen, $W_n$ có $n+1$ đỉnh → $2n$ cạnh.)

---

### Bài 1.9. Số cạnh của $K_{x,y}$

**Giải:** Mỗi đỉnh trong $V_1$ ($x$ đỉnh) kề với cả $y$ đỉnh của $V_2$ → $m = xy$.
Trả lời luôn câu hỏi slide 42: đỉnh thuộc $V_1$ có bậc $y$, đỉnh thuộc $V_2$ có bậc $x$.
Kiểm bắt tay: $xy + yx = 2xy = 2m$ ✓.

$$\boxed{m = xy}$$

---

### Bài 1.10. Vẽ đơn đồ thị đặc biệt bằng Python

File: [`bai_1_10_ve_do_thi.py`](bai_1_10_ve_do_thi.py), kết quả mẫu: [`do_thi_dac_biet.png`](do_thi_dac_biet.png).

```bash
pip install networkx matplotlib
python bai_1_10_ve_do_thi.py --n 6 --k 3 --x 3 --y 4
```

Vẽ $K_n$, $C_n$, $W_n$, $K_{x,y}$, đồ thị $k$-chính quy, tiêu đề mỗi hình in luôn $|V|, |E|$ để tự đối chiếu với bài 1.1, 1.6 đến 1.9. Nếu $nk$ lẻ (như $n=5, k=3$) script báo không tồn tại, đúng bài 1.4.

Ghi chú: `nx.wheel_graph(n)` của networkx dùng tổng $n$ đỉnh, khớp slide (không khớp Rosen).

---

### Bài 1.11. Rosen §10.1

Mình không có sẵn sách nên không chép đề được. Gửi ảnh/đề các câu cần làm vào thread là giải tiếp.
