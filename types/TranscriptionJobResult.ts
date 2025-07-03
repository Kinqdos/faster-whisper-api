import {TranscriptionInfo} from "./TranscriptionInfo";
import {TranscriptionSegment} from "./TranscriptionSegment";

export type TranscriptionJobResult = {
    info: TranscriptionInfo
    segements: Array<TranscriptionSegment>
}