"""Bài 1.10 - Vẽ các đơn đồ thị đặc biệt (Chương 1, LTDT).

Cài đặt:  pip install networkx matplotlib
Chạy:     python bai_1_10_ve_do_thi.py --n 6 --k 3 --x 3 --y 4
"""
import argparse

import matplotlib.pyplot as plt
import networkx as nx


def wheel_slide(n):
    """W_n theo slide: TỔNG n đỉnh = C_{n-1} + 1 đỉnh trung tâm (n > 3).
    Lưu ý: nx.wheel_graph(n) cũng dùng n đỉnh tổng, khớp với slide.
    (Rosen thì W_n có n+1 đỉnh!)"""
    return nx.wheel_graph(n)


def build_graphs(n, k, x, y):
    graphs = {
        f"K_{n} (đầy đủ)": (nx.complete_graph(n), "circular"),
        f"C_{n} (chu trình)": (nx.cycle_graph(n), "circular"),
        f"W_{n} (bánh xe)": (wheel_slide(n), "wheel"),
        f"K_{{{x},{y}}} (2 phía đầy đủ)": (nx.complete_bipartite_graph(x, y), "bipartite"),
    }
    # k-regular cần n*k chẵn và k < n (định lý bắt tay)
    if n * k % 2 == 0 and k < n:
        graphs[f"{k}-regular, {n} đỉnh"] = (nx.random_regular_graph(k, n, seed=1), "circular")
    else:
        print(f"[!] Không tồn tại đơn đồ thị {k}-chính quy {n} đỉnh (n*k lẻ hoặc k >= n)")
    return graphs


def layout(G, kind, x):
    if kind == "bipartite":
        return nx.bipartite_layout(G, range(x))
    if kind == "wheel":
        pos = nx.circular_layout(range(1, G.number_of_nodes()))
        pos[0] = (0, 0)  # đỉnh trung tâm
        return pos
    return nx.circular_layout(G)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=6)
    p.add_argument("--k", type=int, default=3)
    p.add_argument("--x", type=int, default=3)
    p.add_argument("--y", type=int, default=4)
    p.add_argument("--out", default="do_thi_dac_biet.png")
    a = p.parse_args()

    graphs = build_graphs(a.n, a.k, a.x, a.y)
    fig, axes = plt.subplots(1, len(graphs), figsize=(4 * len(graphs), 4))
    for ax, (name, (G, kind)) in zip(axes, graphs.items()):
        colors = ["tab:orange" if kind == "bipartite" and v < a.x else "tab:blue" for v in G]
        nx.draw(G, layout(G, kind, a.x), ax=ax, node_color=colors, node_size=250, with_labels=True,
                font_color="white", font_size=8)
        ax.set_title(f"{name}\n|V|={G.number_of_nodes()}, |E|={G.number_of_edges()}")
    plt.tight_layout()
    plt.savefig(a.out, dpi=120)
    print("Đã lưu", a.out)


if __name__ == "__main__":
    main()
