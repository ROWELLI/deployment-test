/// <reference types="vite/client" />
interface ImportMetaEnv {
    readonly VITE_API_URL: string;
    // 여기에 env에서 설정한 변수 추가하기
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}
