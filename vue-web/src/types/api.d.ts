// types/api.d.ts
export class ApiResponse<T = any> extends AxiosResponse{
  code: number
  data: T
  message: string
}

class ApiError extends Error {
  constructor(
    message: string,
    public code: number,
    public details?: Record<string, unknown>
  ) {
    super(message)
    Object.setPrototypeOf(this, ApiError.prototype)
  }
}

// 业务特定错误码（与后端对齐）
enum ErrorCode {
  Success = 200,
  InvalidToken = 401,
  NotFound = 404,
  ServerError = 500
}
