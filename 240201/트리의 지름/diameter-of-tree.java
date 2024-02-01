import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;

public class Main {

    private static final BufferedReader br = new BufferedReader(
        new InputStreamReader(System.in)
    );
    private static final PrintWriter pw = new PrintWriter(System.out);

    public static void main(String[] args) throws Exception {
        final Main mn = new Main();
        mn.input();
        mn.solve();
        Main.pw.flush();
    }

    private int n;
    private List<List<int[]>> adj;
    private int[] dists;
    private int[] stack;

    public void input() throws Exception {
        StringTokenizer st;

        this.n = Integer.parseInt(br.readLine().trim());
        this.adj = new ArrayList<>(this.n + 1);
        for (int i = 0; i <= n; i++) {
            this.adj.add(new ArrayList<>());
        }
        for (int i = 1, a, b, c; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            this.adj.get(a).add(new int[] {b, c});
            this.adj.get(b).add(new int[] {a, c});
        }
        this.dists = new int[this.n + 1];
        this.stack = new int[this.n];
    }

    public void solve() {
        search(1);
        int u = 1;
        for (int i = 2; i <= n; i++) {
            if (this.dists[i] > this.dists[u]) {
                u = i;
            }
        }
        search(u);
        u = 1;
        for (int i = 2; i <= n; i++) {
            if (this.dists[i] > this.dists[u]) {
                u = i;
            }
        }
        Main.pw.print(this.dists[u] - 1);
    }
    
    private void search(final int src) {
        for (int i = 1; i <= this.n; i++) {
            this.dists[i] = 0;
        }
        this.dists[src] = 1;
        int top = 0;
        this.stack[0] = src;
        while (top != -1) {
            final int u = stack[top--];
            final int du = this.dists[u];
            for (final int[] vw : adj.get(u)) {
                if (this.dists[vw[0]] == 0) {
                    this.dists[vw[0]] = du + vw[1];
                    this.stack[++top] = vw[0];
                }
            }
        }
    }
}