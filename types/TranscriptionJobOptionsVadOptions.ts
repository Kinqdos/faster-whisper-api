export type TranscriptionJobOptionsVadOptions = {
    threshold?: number // float
    neg_threshold?: number // float
    min_speech_duration_ms?: number // int
    max_speech_duration_s?: number // float
    min_silence_duration_ms?: number // int
    speech_pad_ms?: number // int
}