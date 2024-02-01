import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;

public class Main {

    private static BufferedReader br;
    private static PrintWriter pw;

    public static void main(String[] args) throws Exception {
        Main.br = new BufferedReader(new InputStreamReader(System.in));
        Main.pw = new PrintWriter(System.out);
        final Main main = new Main();
        main.input();
        main.solve();
        main.print();
        pw.flush();
    }

    private int n;
    private List<List<Integer>> adj;
    private int[] parent;

    public void input() throws Exception {
        StringTokenizer st;

        this.n = Integer.parseInt(Main.br.readLine().trim());
        this.adj = new ArrayList<>(n + 1);
        for (int i = 0; i <= n; i++) {
            this.adj.add(new ArrayList<>());
        }
        this.parent = new int[n + 1];

        for (int i = 1, a, b; i != n; i++) {
            st = new StringTokenizer(Main.br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            this.adj.get(a).add(b);
            this.adj.get(b).add(a);
        }
    }

    public void solve() {
        this.parent[1] = 1;
        dfs(1);
    }

    public void print() {
        for (int i = 2; i <= n; i++) {
            Main.pw.println(this.parent[i]);
        }
    }

    private void dfs(final int src) {
        for (final int dest : this.adj.get(src)) {
            if (this.parent[dest] == 0) {
                this.parent[dest] = src;
                dfs(dest);
            }
        }
    }
}