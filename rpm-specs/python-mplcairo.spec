%global srcname mplcairo

Name:           python-%{srcname}
Version:        0.3
Release:        2%{?dist}
Summary:        A (new) cairo backend for Matplotlib

License:        MIT
URL:            https://github.com/matplotlib/mplcairo
Source0:        %pypi_source

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
BuildRequires:  texlive-cm

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

%{__python3} -c 'import mplcairo.base'

MPLBACKEND=module://mplcairo.base %{__python3} - <<EOF
import matplotlib.pyplot as plt
print(plt.get_backend())
fig, ax = plt.subplots()
fig.savefig("/dev/null", format="png")
EOF

# 50 is upstream recommended tolerance since results won't match MPL exactly.
%{__python3} run-mpl-test-suite.py --tolerance=50 -m 'not network' -v -n auto


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}.pth
%{python3_sitearch}/%{srcname}-%{version}-py*.egg-info


%changelog
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
