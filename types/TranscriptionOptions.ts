export type TranscriptionOptions = {
  beam_size: number // int
  best_of: number // int
  patience: number // float
  length_penalty: number // float
  repetition_penalty: number // float
  no_repeat_ngram_size: number // int
  log_prob_threshold?: number // float
  no_speech_threshold?: number // float
  compression_ratio_threshold?: number // float
  condition_on_previous_text: boolean
  prompt_reset_on_temperature: number // float
  temperatures: number[] // float[]
  initial_prompt?: string | number[]
  prefix?: string
  suppress_blank: boolean
  suppress_tokens?: number[] // int[]
  without_timestamps: boolean
  max_initial_timestamp: number // float
  word_timestamps: boolean
  prepend_punctuations: string
  append_punctuations: string
  multilingual: boolean
  max_new_tokens?: number // int
  clip_timestamps: string | number[] // float[]
  hallucination_silence_threshold?: number // float
  hotwords?: string
}