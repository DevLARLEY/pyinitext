# pyinitext
init file PSSH extractor

# Usage
```ruby
usage: init file PSSH extractor [-h] --file FILE

Author: github.com/DevLARLEY

options:
  -h, --help   show this help message and exit
  --file FILE  A path to a local init file
```

# Preview
```ruby
python initext.py --file init_example.mp4
[INFO]: AAAAOHBzc2gAAAAA7e+LqXnWSs6jyCfc1R0h7QAAABgSEBU+lzefx0GHndy6mCNQRLZIscaJmwY=
[INFO]: AAAFonBzc2gAAAAAmgTweZhAQoarkuZb4IhflQAABYKCBQAAAgABALoC//48AFcAUgBNAEgARQBBAEQARQBSACAAeABtAGwAbgBzAD0AIgBoAHQAdABwADoALwAvAHMAYwBoAGUAbQBhAHMALgBtAGkAYwByAG8AcwBvAGYAdAAuAGMAbwBtAC8ARABSAE0ALwAyADAAMAA3AC8AMAAzAC8AUABsAGEAeQBSAGUAYQBkAHkASABlAGEAZABlAHIAIgAgAHYAZQByAHMAaQBvAG4APQAiADQALgAzAC4AMAAuADAAIgA+AA0ACgAgACAAPABEAEEAVABBAD4ADQAKACAAIAAgACAAPABQAFIATwBUAEUAQwBUAEkATgBGAE8APgANAAoAIAAgACAAIAAgACAAPABLAEkARABTAD4ADQAKACAAIAAgACAAIAAgACAAIAA8AEsASQBEACAAQQBMAEcASQBEAD0AIgBBAEUAUwBDAEIAQwAiACAAVgBBAEwAVQBFAD0AIgBqADgANABHAE4ARwA3AHoASQA0AFgAbQB6AGsASABrADIAawBBAHgAdgB3AD0APQAiAD4ADQAKACAAIAAgACAAIAAgACAAIAA8AC8ASwBJAEQAPgANAAoAIAAgACAAIAAgACAAPAAvAEsASQBEAFMAPgANAAoAIAAgACAAIAA8AC8AUABSAE8AVABFAEMAVABJAE4ARgBPAD4ADQAKACAAIAAgACAAPABMAEEAXwBVAFIATAA+AGgAdAB0AHAAcwA6AC8ALwBsAGkAYwBlAG4AcwBlAC4AcABhAGwAbAB5AGMAbwBuAC4AYwBvAG0ALwByAGkALwBsAGkAYwBlAG4AcwBlAE0AYQBuAGEAZwBlAHIALgBkAG8APAAvAEwAQQBfAFUAUgBMAD4ADQAKACAAIAA8AC8ARABBAFQAQQA+AA0ACgA8AC8AVwBSAE0ASABFAEEARABFAFIAPgABALoC//48AFcAUgBNAEgARQBBAEQARQBSACAAeABtAGwAbgBzAD0AIgBoAHQAdABwADoALwAvAHMAYwBoAGUAbQBhAHMALgBtAGkAYwByAG8AcwBvAGYAdAAuAGMAbwBtAC8ARABSAE0ALwAyADAAMAA3AC8AMAAzAC8AUABsAGEAeQBSAGUAYQBkAHkASABlAGEAZABlAHIAIgAgAHYAZQByAHMAaQBvAG4APQAiADQALgAzAC4AMAAuADAAIgA+AA0ACgAgACAAPABEAEEAVABBAD4ADQAKACAAIAAgACAAPABQAFIATwBUAEUAQwBUAEkATgBGAE8APgANAAoAIAAgACAAIAAgACAAPABLAEkARABTAD4ADQAKACAAIAAgACAAIAAgACAAIAA8AEsASQBEACAAQQBMAEcASQBEAD0AIgBBAEUAUwBDAEIAQwAiACAAVgBBAEwAVQBFAD0AIgB5ADMAQgBzAFYASQBCAEsAUQBZACsAVQBEAGoAMQB6ADkAaQBWAGgAMgBnAD0APQAiAD4ADQAKACAAIAAgACAAIAAgACAAIAA8AC8ASwBJAEQAPgANAAoAIAAgACAAIAAgACAAPAAvAEsASQBEAFMAPgANAAoAIAAgACAAIAA8AC8AUABSAE8AVABFAEMAVABJAE4ARgBPAD4ADQAKACAAIAAgACAAPABMAEEAXwBVAFIATAA+AGgAdAB0AHAAcwA6AC8ALwBsAGkAYwBlAG4AcwBlAC4AcABhAGwAbAB5AGMAbwBuAC4AYwBvAG0ALwByAGkALwBsAGkAYwBlAG4AcwBlAE0AYQBuAGEAZwBlAHIALgBkAG8APAAvAEwAQQBfAFUAUgBMAD4ADQAKACAAIAA8AC8ARABBAFQAQQA+AA0ACgA8AC8AVwBSAE0ASABFAEEARABFAFIAPgA=
[INFO]: AAAIaHBzc2gAAAAAmgTweZhAQoarkuZb4IhflQAACEhICAAAAwABALgCPABXAFIATQBIAEUAQQBEAEUAUgAgAHgAbQBsAG4AcwA9ACIAaAB0AHQAcAA6AC8ALwBzAGMAaABlAG0AYQBzAC4AbQBpAGMAcgBvAHMAbwBmAHQALgBjAG8AbQAvAEQAUgBNAC8AMgAwADAANwAvADAAMwAvAFAAbABhAHkAUgBlAGEAZAB5AEgAZQBhAGQAZQByACIAIAB2AGUAcgBzAGkAbwBuAD0AIgA0AC4AMwAuADAALgAwACIAPgANAAoAIAAgADwARABBAFQAQQA+AA0ACgAgACAAIAAgADwAUABSAE8AVABFAEMAVABJAE4ARgBPAD4ADQAKACAAIAAgACAAIAAgADwASwBJAEQAUwA+AA0ACgAgACAAIAAgACAAIAAgACAAPABLAEkARAAgAEEATABHAEkARAA9ACIAQQBFAFMAQwBCAEMAIgAgAFYAQQBMAFUARQA9ACIAagA4ADQARwBOAEcANwB6AEkANABYAG0AegBrAEgAawAyAGsAQQB4AHYAdwA9AD0AIgA+AA0ACgAgACAAIAAgACAAIAAgACAAPAAvAEsASQBEAD4ADQAKACAAIAAgACAAIAAgADwALwBLAEkARABTAD4ADQAKACAAIAAgACAAPAAvAFAAUgBPAFQARQBDAFQASQBOAEYATwA+AA0ACgAgACAAIAAgADwATABBAF8AVQBSAEwAPgBoAHQAdABwAHMAOgAvAC8AbABpAGMAZQBuAHMAZQAuAHAAYQBsAGwAeQBjAG8AbgAuAGMAbwBtAC8AcgBpAC8AbABpAGMAZQBuAHMAZQBNAGEAbgBhAGcAZQByAC4AZABvADwALwBMAEEAXwBVAFIATAA+AA0ACgAgACAAPAAvAEQAQQBUAEEAPgANAAoAPAAvAFcAUgBNAEgARQBBAEQARQBSAD4AAQC4AjwAVwBSAE0ASABFAEEARABFAFIAIAB4AG0AbABuAHMAPQAiAGgAdAB0AHAAOgAvAC8AcwBjAGgAZQBtAGEAcwAuAG0AaQBjAHIAbwBzAG8AZgB0AC4AYwBvAG0ALwBEAFIATQAvADIAMAAwADcALwAwADMALwBQAGwAYQB5AFIAZQBhAGQAeQBIAGUAYQBkAGUAcgAiACAAdgBlAHIAcwBpAG8AbgA9ACIANAAuADMALgAwAC4AMAAiAD4ADQAKACAAIAA8AEQAQQBUAEEAPgANAAoAIAAgACAAIAA8AFAAUgBPAFQARQBDAFQASQBOAEYATwA+AA0ACgAgACAAIAAgACAAIAA8AEsASQBEAFMAPgANAAoAIAAgACAAIAAgACAAIAAgADwASwBJAEQAIABBAEwARwBJAEQAPQAiAEEARQBTAEMAQgBDACIAIABWAEEATABVAEUAPQAiAHkAMwBCAHMAVgBJAEIASwBRAFkAKwBVAEQAagAxAHoAOQBpAFYAaAAyAGcAPQA9ACIAPgANAAoAIAAgACAAIAAgACAAIAAgADwALwBLAEkARAA+AA0ACgAgACAAIAAgACAAIAA8AC8ASwBJAEQAUwA+AA0ACgAgACAAIAAgADwALwBQAFIATwBUAEUAQwBUAEkATgBGAE8APgANAAoAIAAgACAAIAA8AEwAQQBfAFUAUgBMAD4AaAB0AHQAcABzADoALwAvAGwAaQBjAGUAbgBzAGUALgBwAGEAbABsAHkAYwBvAG4ALgBjAG8AbQAvAHIAaQAvAGwAaQBjAGUAbgBzAGUATQBhAG4AYQBnAGUAcgAuAGQAbwA8AC8ATABBAF8AVQBSAEwAPgANAAoAIAAgADwALwBEAEEAVABBAD4ADQAKADwALwBXAFIATQBIAEUAQQBEAEUAUgA+AAEAxgI8AFcAUgBNAEgARQBBAEQARQBSACAAeABtAGwAbgBzAD0AIgBoAHQAdABwADoALwAvAHMAYwBoAGUAbQBhAHMALgBtAGkAYwByAG8AcwBvAGYAdAAuAGMAbwBtAC8ARABSAE0ALwAyADAAMAA3AC8AMAAzAC8AUABsAGEAeQBSAGUAYQBkAHkASABlAGEAZABlAHIAIgAgAHYAZQByAHMAaQBvAG4APQAiADQALgAzAC4AMAAuADAAIgA+ACAAPABEAEEAVABBAD4AIAA8AFAAUgBPAFQARQBDAFQASQBOAEYATwA+ACAAPABLAEkARABTAD4AIAA8AEsASQBEACAAQQBMAEcASQBEAD0AIgBBAEUAUwBDAEIAQwAiACAAVgBBAEwAVQBFAD0AIgBqADgANABHAE4ARwA3AHoASQA0AFgAbQB6AGsASABrADIAawBBAHgAdgB3AD0APQAiAD4AIAA8AC8ASwBJAEQAPgAgADwASwBJAEQAIABBAEwARwBJAEQAPQAiAEEARQBTAEMAQgBDACIAIABWAEEATABVAEUAPQAiAHkAMwBCAHMAVgBJAEIASwBRAFkAKwBVAEQAagAxAHoAOQBpAFYAaAAyAGcAPQA9ACIAPgAgADwALwBLAEkARAA+ACAAPAAvAEsASQBEAFMAPgAgADwALwBQAFIATwBUAEUAQwBUAEkATgBGAE8APgAgADwATABBAF8AVQBSAEwAPgBoAHQAdABwAHMAOgAvAC8AbABpAGMAZQBuAHMAZQAuAHAAYQBsAGwAeQBjAG8AbgAuAGMAbwBtAC8AcgBpAC8AbABpAGMAZQBuAHMAZQBNAGEAbgBhAGcAZQByAC4AZABvADwALwBMAEEAXwBVAFIATAA+ACAAPAAvAEQAQQBUAEEAPgAgADwALwBXAFIATQBIAEUAQQBEAEUAUgA+AA==
```
