import {TranscriptionJobOptions} from "./TranscriptionJobOptions";
import {TranscriptionJobState} from "./TranscriptionJobState";
import {TranscriptionJobResult} from "./TranscriptionJobResult";

export type TranscriptionJob = {
    id: string
    options: TranscriptionJobOptions | null

    state: TranscriptionJobState
    error: string | null

    result: TranscriptionJobResult | null
    progress: number
    finished_at: number
}