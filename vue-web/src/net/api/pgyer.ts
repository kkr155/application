import request from '@/net/utils/request.js'
import type { ApiResponse } from '@/types/api'

export interface Config {
  config_id: number
  name: string
  apikey: string
  appkey: String
}
