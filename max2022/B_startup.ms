if isProperty python "execute" then (
    python.execute ("def _python_startup():\n"+
    "   try:\n" +
    "       import Bmain\n" +
    "   except ImportError:\n" +
    "       print('Import Error!')\n" +
    "       return\n" +
    "   Bmain.B_main()\n" +
    "_python_startup()\n" +
    "del _python_startup\n")
)
