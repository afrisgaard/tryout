import narwhals as nw
from narwhals.typing import IntoFrameT


def main():
    print("Hello from tryout!")

    def some_func(df_in: IntoFrameT) -> IntoFrameT:
        """Some random func"""
        df = nw.from_native(df_in)
        return df.to_native()


if __name__ == "__main__":
    main()
