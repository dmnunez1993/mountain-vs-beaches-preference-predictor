declare const ENV_API_ENDPOINT: string | undefined;

declare const ENV_API_URL_SAME_ADDR: string | undefined;
declare const ENV_API_URL_SAME_ADDR_PORT: string | undefined;

export const API_URL_SAME_ADDR = ENV_API_URL_SAME_ADDR
  ? ENV_API_URL_SAME_ADDR === "true"
  : false;
export const API_URL_SAME_ADDR_PORT =
  ENV_API_URL_SAME_ADDR_PORT !== undefined
    ? parseInt(ENV_API_URL_SAME_ADDR_PORT)
    : 8000;

export const API_ENDPOINT =
  ENV_API_ENDPOINT !== undefined ? ENV_API_ENDPOINT : "http://localhost:8000";
