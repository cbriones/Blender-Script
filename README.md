# Windows Instructions
## batch rendering of a WRL sequence

1. Put the **WRL** files, **serpentina.blend** and **script.py** on c:\temp\render

1. Execute the following command using PowerShell or Command Prompt.

    `blender -b serpentina.blend -P script.py`

The process sequentially generates one PNG image for each WRL file found on c:\temp\render
