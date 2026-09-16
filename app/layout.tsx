import type { Metadata } from "next";
import "./globals.css";
export const dynamic = "force-static";
const faviconPath = process.env.GITHUB_PAGES_BUILD === "1" ? "/kmislem/favicon.svg" : "/favicon.svg";
export const metadata:Metadata={title:"Kadastro İşlem Rehberi",description:"Mevzuatı arama, işlem adımları ve kontrol asistanı",icons:{icon:faviconPath,shortcut:faviconPath}};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="tr" suppressHydrationWarning><body>{children}</body></html>}
