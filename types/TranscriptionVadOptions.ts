export type TranscriptionVadOptions = {
    /**
     * Speech threshold.
     * Probabilities ABOVE this value are considered SPEECH.
     * Default: 0.5
     */
    threshold: number; // float

    /**
     * Silence threshold for determining end of speech.
     * Optional.
     */
    neg_threshold?: number; // float

    /**
     * Speech chunks shorter than this (in ms) are discarded.
     * Default: 0
     */
    min_speech_duration_ms: number; // int

    /**
     * Maximum duration of speech chunks (in seconds).
     * Default: Infinity
     */
    max_speech_duration_s: number; // float

    /**
     * Wait this long (in ms) after end of speech before separating.
     * Default: 2000
     */
    min_silence_duration_ms: number; // int

    /**
     * Pad this many ms on each side of final speech chunks.
     * Default: 400
     */
    speech_pad_ms: number; // int
};
