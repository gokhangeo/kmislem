import type { Metadata } from "next";
import "./globals.css";
export const metadata:Metadata={title:"Kadastro İşlem Rehberi",description:"Mevzuatı arama, işlem adımları ve kontrol asistanı",icons:{icon:"/favicon.svg",shortcut:"/favicon.svg"}};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="tr" suppressHydrationWarning><body>{children}</body></html>}
