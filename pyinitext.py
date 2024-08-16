import base64
import logging
from argparse import ArgumentParser


class InitExt:
    def __init__(
            self,
            file: str
    ):
        self.data = open(file, "rb").read()

    @staticmethod
    def _substring_indices(
            content: bytes | str,
            sub: bytes | str
    ) -> list[int]:
        start, indices = 0, []
        while (start := content.find(sub, start)) != -1:
            indices.append(start)
            start += 1
        return indices

    def extract(self) -> list[str]:
        indices = InitExt._substring_indices(self.data, b'pssh')
        for i in indices:
            size = int.from_bytes(self.data[i - 4:i], "big")
            yield base64.b64encode(
                self.data[i - 4:i - 4 + size]
            ).decode()


if __name__ == '__main__':
    parser = ArgumentParser(
        prog="init file PSSH extractor",
        description="Author: github.com/DevLARLEY"
    )
    parser.add_argument(
        "--file",
        type=str,
        help="A path to a local init file",
        required=True
    )

    args = parser.parse_args()
    logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.INFO)

    initExt = InitExt(
        file=args.file
    )
    for pssh in initExt.extract():
        logging.info(pssh)
