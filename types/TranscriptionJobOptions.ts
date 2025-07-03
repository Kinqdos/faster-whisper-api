import {TranscriptionJobOptionsVadOptions} from "./TranscriptionJobOptionsVadOptions";

export type TranscriptionJobOptions = {
  language?: string
  task?: string
  log_progress?: boolean
  beam_size?: number // int
  best_of?: number // int
  patience?: number // float
  length_penalty?: number // float
  repetition_penalty?: number // float
  no_repeat_ngram_size?: number // int
  temperature?: number | number[] // float or float[]
  compression_ratio_threshold?: number // float
  log_prob_threshold?: number // float
  no_speech_threshold?: number // float
  condition_on_previous_text?: boolean
  prompt_reset_on_temperature?: number // float
  initial_prompt?: string | number[]
  prefix?: string
  suppress_blank?: boolean
  suppress_tokens?: number[] // int[]
  without_timestamps?: boolean
  max_initial_timestamp?: number // float
  word_timestamps?: boolean
  prepend_punctuations?: string
  append_punctuations?: string
  multilingual?: boolean
  vad_filter?: boolean
  vad_parameters?: Record<string, any> | TranscriptionJobOptionsVadOptions
  max_new_tokens?: number // int
  chunk_length?: number // int
  clip_timestamps?: string | number[] // float[]
  hallucination_silence_threshold?: number // float
  hotwords?: string
  language_detection_threshold?: number // float
  language_detection_segments?: number // int
}