import {TranscriptionWord} from "./TranscriptionWord";

export type TranscriptionSegment = {
    id: number // int
    seek: number // int
    start: number // float
    end: number // float
    text: string
    tokens: number[] // int[]
    avg_logprob: number // float
    compression_ratio: number // float
    no_speech_prob: number // float
    words?: TranscriptionWord[]
    temperature?: number // float
}