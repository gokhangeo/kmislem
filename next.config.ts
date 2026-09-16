import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  ...(process.env.GITHUB_PAGES_BUILD === "1"
    ? { output: "export" as const, assetPrefix: "/kmislem/", trailingSlash: true }
    : {}),
};

export default nextConfig;
