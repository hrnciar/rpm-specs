%global srcname mplcairo

Name:           python-%{srcname}
Version:        0.3
Release:        4%{?dist}
Summary:        A (new) cairo backend for Matplotlib

License:        MIT
URL:            https://github.com/matplotlib/mplcairo
Source0:        %pypi_source
Patch0001:      https://github.com/matplotlib/mplcairo/commit/d2a95cad1f605c45d55d4a8aa64a546d2b96c93f.patch

BuildRequires:  gcc-c++

%description
This is a new, essentially complete implementation of a cairo backend for
Matplotlib. It can be used in combination with a Qt5, GTK3, Tk, wx, or macOS
UI, or noninteractively (i.e., to save figure to various file formats).
Noteworthy points include:
  - Improved accuracy (e.g., with marker positioning, quad meshes, and text
    kerning).
  - Support for a wider variety of font formats, such as otf and pfb, for vector
    (PDF, PS, SVG) backends (Matplotlib's Agg backend also supports such fonts).
  - Optional support for complex text layout (right-to-left languages, etc.)
    using Raqm.
  - Support for embedding URLs in PDF (but not SVG) output.
  - Support for multi-page output both for PDF and PS (Matplotlib only supports
    multi-page PDF).
  - Support for custom blend modes (see `examples/operators.py`).


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  cairo-devel >= 1.15.4
BuildRequires:  freetype-devel
BuildRequires:  libraqm-devel >= 0.7.0
BuildRequires:  python3-devel
BuildRequires:  python3dist(matplotlib) >= 2.2
BuildRequires:  python3-matplotlib-test-data >= 2.2
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pybind11) >= 2.5
BuildRequires:  python3dist(pycairo) >= 1.16
BuildRequires:  python3dist(pytest) >= 3.2.2
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(sphinx)

# LaTeX dependencies for tests, copied from python-matplotlib.
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-tex-bin
BuildRequires:  texlive-xetex-bin
# Search for documentclass and add the classes here.
BuildRequires:  tex(article.cls)
BuildRequires:  tex(minimal.cls)
# Search for inputenc and add any encodings used with it.
BuildRequires:  tex(utf8.def)
BuildRequires:  tex(utf8x.def)
# Found with: rg -Io 'usepackage(\[.+\])?\{.+\}' lib | rg -o '\{.+\}' | sort -u
# and then removing duplicates in one line, etc.
BuildRequires:  tex(avant.sty)
BuildRequires:  tex(bm.sty)
BuildRequires:  tex(chancery.sty)
BuildRequires:  tex(charter.sty)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(courier.sty)
BuildRequires:  tex(euler.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(fontspec.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(helvet.sty)
BuildRequires:  tex(import.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(mathpazo.sty)
BuildRequires:  tex(mathptmx.sty)
BuildRequires:  tex(pgf.sty)
BuildRequires:  tex(preview.sty)
BuildRequires:  tex(psfrag.sty)
BuildRequires:  tex(sfmath.sty)
BuildRequires:  tex(textcomp.sty)
BuildRequires:  tex(txfonts.sty)
BuildRequires:  tex(type1cm.sty)
BuildRequires:  tex(type1ec.sty)
BuildRequires:  tex(unicode-math.sty)
# See BakomaFonts._fontmap in lib/matplotlib/mathtext.py
BuildRequires:  tex(cmb10.tfm)
BuildRequires:  tex(cmex10.tfm)
BuildRequires:  tex(cmmi10.tfm)
BuildRequires:  tex(cmr10.tfm)
BuildRequires:  tex(cmss10.tfm)
BuildRequires:  tex(cmsy10.tfm)
BuildRequires:  tex(cmtt10.tfm)

Requires:       cairo >= 1.15.4
Requires:       libraqm >= 0.7.0

%description -n python3-%{srcname}
This is a new, essentially complete implementation of a cairo backend for
Matplotlib. It can be used in combination with a Qt5, GTK3, Tk, wx, or macOS
UI, or noninteractively (i.e., to save figure to various file formats).
Noteworthy points include:
  - Improved accuracy (e.g., with marker positioning, quad meshes, and text
    kerning).
  - Support for a wider variety of font formats, such as otf and pfb, for vector
    (PDF, PS, SVG) backends (Matplotlib's Agg backend also supports such fonts).
  - Optional support for complex text layout (right-to-left languages, etc.)
    using Raqm.
  - Support for embedding URLs in PDF (but not SVG) output.
  - Support for multi-page output both for PDF and PS (Matplotlib only supports
    multi-page PDF).
  - Support for custom blend modes (see `examples/operators.py`).


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info and vendoring
rm -rf %{srcname}.egg-info vendor


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build


%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install


%check
export PYTHONPATH="%{buildroot}%{python3_sitearch}" PYTHONDONTWRITEBYTECODE=1

%{python3} -c 'import mplcairo.base'

MPLBACKEND=module://mplcairo.base %{python3} - <<EOF
import matplotlib.pyplot as plt
print(plt.get_backend())
fig, ax = plt.subplots()
fig.savefig("/dev/null", format="png")
EOF

# 50 is upstream recommended tolerance since results won't match MPL exactly.
%{python3} run-mpl-test-suite.py --tolerance=50 -m 'not network' -v -n auto


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}.pth
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3-2
- Backport fix for Matplotlib 3.3.0rc1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-2
- Rebuilt for Python 3.9

* Mon May 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1-1
- Update to final release

* Mon Apr 16 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1-0.2.a1
- Remove bundled eggs.
- Add checks and missing Requires.

* Tue Mar 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1-0.1.a1
- Initial package.
