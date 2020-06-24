%global pypi_name nbconvert

Name:           python-%{pypi_name}
Version:        5.6.1
Release:        3%{?dist}
Summary:        Converting Jupyter Notebooks

License:        BSD and MIT
URL:            http://jupyter.org
Source0:        %pypi_source

# Compatibility with Inkscape 1.0rc1+
# https://github.com/jupyter/nbconvert/pull/1247
Patch1:         inkscape-1.0rc1.patch

# Python 3.9 compatibility
Patch2:         https://github.com/jupyter/nbconvert/commit/d9a893bf60.patch
Patch3:         https://github.com/jupyter/nbconvert/commit/f072d782dd.patch

BuildArch:      noarch

BuildRequires:  python3-pandocfilters
BuildRequires:  python3-setuptools
BuildRequires:  python3-testpath
BuildRequires:  python3-devel


%bcond_without doc
%bcond_without check

%if %{with doc}
BuildRequires:  python3-entrypoints
BuildRequires:  python3-ipython
BuildRequires:  python3-ipython-sphinx
BuildRequires:  python3-nbformat
BuildRequires:  python3-nbsphinx
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-github-alt
BuildRequires:  pandoc
%endif

%if %{with check}
BuildRequires:  python3-bleach
BuildRequires:  python3-entrypoints
BuildRequires:  python3-defusedxml
BuildRequires:  python3-ipykernel
#BuildRequires:  python3-ipywidgets -- not yet packaged
BuildRequires:  python3-jinja2
BuildRequires:  python3-jupyter-core
BuildRequires:  python3-mock
BuildRequires:  python3-mistune
BuildRequires:  python3-nbformat
BuildRequires:  python3-nose
#BuildRequires:  python3-pebble -- not yet packaged
BuildRequires:  python3-pytest
#BuildRequires:  texlive-xetex -- those are failing for now
BuildRequires:  inkscape
BuildRequires:  pandoc
%endif


%description
The nbconvert tool, jupyter nbconvert, converts notebooks to various other 
formats via Jinja templates. The nbconvert tool allows you to convert an 
.ipynb notebook file into various static formats including HTML, LaTeX, 
PDF, Reveal JS, Markdown (md), ReStructured Text (rst) and executable script.

%package -n     python3-%{pypi_name}
Summary:        Converting Jupyter Notebooks
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       %{py3_dist setuptools}
Recommends:     inkscape
Recommends:     pandoc

%description -n python3-%{pypi_name}

The nbconvert tool, jupyter nbconvert, converts notebooks to various other 
formats via Jinja templates. The nbconvert tool allows you to convert an 
.ipynb notebook file into various static formats including HTML, LaTeX, 
PDF, Reveal JS, Markdown (md), ReStructured Text (rst) and executable script.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for nbconvert
%description -n python-%{pypi_name}-doc
Documentation for nbconvert

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%if %{with doc}
export PYTHONPATH=$(pwd)
sphinx-build-3 docs/source html
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

# fix permissions and shebangs
pathfix.py -pni %{__python3} %{buildroot}%{python3_sitelib}/%{pypi_name}/nbconvertapp.py
chmod 755 %{buildroot}%{python3_sitelib}/%{pypi_name}/nbconvertapp.py

%if %{with check}
%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
# https://github.com/jupyter/nbconvert/issues/815
# https://github.com/jupyter/nbconvert/issues/928
# test_markdown2rst - our pandoc is too new
# test_minimal_version - our pandoc is too new
# test_pandoc_available - our pandoc is too new
# test_run_notebooks, test_widgets - needs ipywidgets
# nbconvert/preprocessors/tests/test_execute.py needs pebble
%{__python3} -m pytest -v -k "not test_markdown2rst and not test_minimal_version and not test_pandoc_available and not test_run_notebooks and not test_widgets" --ignore nbconvert/preprocessors/tests/test_execute.py
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc docs/README.md
%{_bindir}/jupyter-nbconvert
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python3_sitelib}/%{pypi_name}/

%if %{with doc}
%files -n python-%{pypi_name}-doc
%doc html
%endif

%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 5.6.1-3
- Rebuilt for Python 3.9

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 5.6.1-2
- Bootstrap for Python 3.9

* Mon May 04 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.6.1-1
- Update to 5.6.1

* Sun May 03 2020 Miro Hrončok <mhroncok@redhat.com> - 5.6.0-4
- Recommend Inkscape for SVG to PDF conversion (#1830647)
- Fix compatibility with Inkscape 1.0rc1
- Recommend Pandoc for format conversions

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Miro Hrončok <mhroncok@redhat.com> - 5.6.0-2
- Correct the BR of python3-jupyter-core

* Mon Sep 02 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.6.0-1
- Update to 5.6.0

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-4
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-3
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0

* Sun Feb 10 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.4.1-1
- Update to 5.4.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Miro Hrončok <mhroncok@redhat.com> - 5.4.0-1
- Update to 5.4.0

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 5.3.1-11
- Remove Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Miro Hrončok <mhroncok@redhat.com> - 5.3.1-9
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.3.1-8
- Bootstrap for Python 3.7

* Mon Mar 19 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.3.1-7
- Remove pandoc as requires. Only pandocfilters is needed

* Mon Mar 19 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.3.1-6
- Add jupyter-client and defusedxml as requires

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.3.1-4
- Add python-mistune, python-bleach and pandoc as dependencies

* Wed Jan 03 2018 Lumír Balhar <lbalhar@redhat.com> - 5.3.1-3
- Fix directory ownership in python subpackages

* Wed Dec 27 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.3.1-2
- license file renamed to LICENSE (from copying.md)

* Wed Dec 27 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.3.1-1
- Update to 5.3.1

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 5.2.1-5
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Oct 02 2017 Mukundan Ragavan <nonamedotc@gmail.com> - 5.2.1-4
- Fix requires (added pandocfilters and testpath)

* Fri Sep 01 2017 Miro Hrončok <mhroncok@redhat.com> - 5.2.1-3
- Move executables from py2 to py3 (#1410332)
- Add BRs to make the docs build

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-6
- Rebuild for Python 3.6

* Thu Nov 03 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.0-5
- Python dep chain fixed
- Fixes bug#1391124

* Wed Nov 02 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.0-4
- Fix pulling entire python{2,3} stack as deps
- Fixes bug#1391124

* Sun Oct 02 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.0-3
- Fix issues pointed out by rpmlint
- Fix license field

* Thu Aug 11 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.0-2
- Fix build errors

* Thu Aug 11 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 4.2.0-1
- Initial package.
