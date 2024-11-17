# Example: Filter files from one folder to a separate folder

To get started, clone this repository and

```
cd filePipeline
```

Create a virtual environment with

```
python -m venv venv
```

Once complete, run

```
pip install -r requirements.txt
```

## Modify file_pipeline.py

In [example_file_pipeline.py](example_file_pipeline.py),replace `SRC_DIR`, with the directory that you would like to watch, and `DEST_DIR` with the folder that you would like filtered files to move to.

My filtering rule is to use regex on the file name, but a more complicated filtering rule could be used. Replace `"PATTERN TO MATCH.*pdf$"` with whatever regex rule you'd like.

## Modify launchagent.plist

In [example_launchagent.plist](example_launchagent.plist), replace `SRC_DIR` and `DEST_DIR` with the same names as you used before. Additionally, specify your `PYTHONPATH` to your `venv` folder.

specify your output and error paths in `StandardOutPath` and `StandardErrorPath` for debugging.

Finally, move your `.plist` file to the `~/Library/LaunchAgents` folder by running

```
mv example_launchagent.plist ~/Library/LaunchAgents
```

## Running the launchagent

```
launchctl bootstrap user/$(id -u) ~/Library/LaunchAgents/example_launchagent.plist
```
