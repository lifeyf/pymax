
fn  startup = (
pypath = pathConfig.removePathLeaf(getThisScriptFilename()) + "\SuperDo.py"
python.ExecuteFile pypath
)

startup()