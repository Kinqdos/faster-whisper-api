import {TranscriptionVadOptions} from "./TranscriptionVadOptions";
import {TranscriptionOptions} from "./TranscriptionOptions";

export type TranscriptionInfo = {
    language: string
    language_probability: number // float
    duration: number // float
    duration_after_vad: number // float
    all_language_probs?: [string, number][] // Tuple[str, float][]
    transcription_options: TranscriptionOptions
    vad_options: TranscriptionVadOptions
}