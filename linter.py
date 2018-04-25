from SublimeLinter.lint import Linter, WARNING  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class Kotlin(Linter):
    cmd = 'ktlint ${file}'
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    tempfile_suffix = '-'
    default_type = WARNING
    defaults = {
        'selector': 'source.Kotlin'
    }
