# Enabled by default
# If the package needs to download data for the test which cannot be done in
# koji, these can be disabled in koji by using `bcond_with` instead, but the
# tests must be validated in mock with network enabled like so:
# mock -r fedora-rawhide-x86_64 rebuild <srpm> --enable-network --rpmbuild-opts="--with tests"
%bcond_without tests

# Enabled by default
%bcond_without docs

%global pypi_name pylatex
%global fancy_name PyLaTeX

%global _description %{expand:
PyLaTeX is a Python library for creating and compiling LaTeX files or snippets.
The goal of this library is being an easy but extensible interface between
Python and LaTeX.}

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Library for creating LaTeX files and snippets

# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
License:        MIT
URL:            https://jeltef.github.io/PyLaTeX/
Source0:        https://github.com/JelteF/%{fancy_name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description %_description

%{?python_enable_dependency_generator}

%package -n python3-%{pypi_name}
Summary:        %{summary}
# Not picked up by dep generator
Requires:       %{py3_dist matplotlib}
Requires:       %{py3_dist quantities}
Requires:       %{py3_dist numpy}
# Will also pull a lot of texlive, but that cannot be helpeb
Requires:       /usr/bin/latexmk
Requires:       /usr/bin/pdflatex
# From `ag Package`
Requires:       tex(alltt.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(longtable.sty)
Requires:       tex(ltablex.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(microtype.sty)
Requires:       tex(multirow.sty)
Requires:       tex(parskip.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tabu.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       texlive

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
# Explicit requirements for tests
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist quantities}
# https://fedoraproject.org/wiki/Features/TeXLive
BuildRequires:  tex(alltt.sty)
BuildRequires:  tex(amsmath.sty)
BuildRequires:  tex(booktabs.sty)
BuildRequires:  tex(cleveref.sty)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(lmodern.sty)
BuildRequires:  tex(lastpage.sty)
BuildRequires:  tex(longtable.sty)
BuildRequires:  tex(ltablex.sty)
BuildRequires:  tex(mdframed.sty)
BuildRequires:  tex(microtype.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(parskip.sty)
BuildRequires:  tex(pgfplots.sty)
BuildRequires:  tex(ragged2e.sty)
BuildRequires:  tex(subcaption.sty)
BuildRequires:  tex(siunitx.sty)
BuildRequires:  tex(tabularx.sty)
BuildRequires:  tex(tabu.sty)
BuildRequires:  tex(textcomp.sty)
BuildRequires:  tex(textpos.sty)
BuildRequires:  tex(tikz.sty)
BuildRequires:  tex(xcolor.sty)
BuildRequires:  texlive
%endif

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%if %{with docs}
%package doc
Summary:        %{summary}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist ordered-set}
BuildRequires:  %{py3_dist sphinx_rtd_theme}

%description doc
Documentation for %{name}.
%endif

%prep
%autosetup -n %{fancy_name}-%{version}
rm -rf %{fancy_name}.egg-info

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

make -C docs SPHINXBUILD=sphinx-build-3 html
pushd docs/build/html
    # Remove unneeded dot files
    rm -frv .doctrees
    rm -frv .buildinfo
    # Correct end of line
    sed -i 's/\r$//' _static/favicons/browserconfig.xml
    # convert to utf8
    iconv -f iso8859-1 -t utf-8 objects.inv > objects.inv.conv && mv -f objects.inv.conv objects.inv
    sed -i 's/\r$//' objects.inv
popd

%install
%py3_install


%check
%if %{with tests}
# Run tests
nosetests-3 tests/*

# Test examples
pushd examples
for f in *.py; do
    PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} $f
done
popd
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{fancy_name}-%{version}-py3.?.egg-info
%{python3_sitelib}/%{pypi_name}

%if %{with docs}
%files doc
%license LICENSE
%doc docs/build/html examples
%endif

%changelog
* Thu Oct 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.0-1
- Update to new release

* Sat Aug 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.4-1
- Update to new release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.3-2
- Explicitly BR setuptools

* Sun Jun 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.3-1
- Update to 1.3.3

* Mon Jun 15 2020 Victor Tejada Yau <victortyau@gmail.com> 1.3.2-1
- Update to 1.3.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.1-1
- Update to 1.3.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.0-1
- Minor tweaks as per review comments
- https://bugzilla.redhat.com/show_bug.cgi?id=1721409
- Improve description macro

* Mon Jun 17 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.0-1
- Initial rpm build
