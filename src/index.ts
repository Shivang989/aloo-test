import http from "http";

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ ok: true, runtime: "TypeScript on HF", node: process.version }));
});

server.listen(3000, "127.0.0.1", () => {
  console.log("TS_BACKEND_READY on 127.0.0.1:3000");
});
